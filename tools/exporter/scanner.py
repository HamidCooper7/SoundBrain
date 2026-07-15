"""File-system scanning for project exports."""

from __future__ import annotations

from dataclasses import dataclass
from fnmatch import fnmatchcase
import os
from pathlib import Path
from typing import Callable

from .config import ExportConfig
from .utils import is_probably_binary, language_for, read_text_safely


@dataclass(slots=True)
class FileRecord:
    path: Path
    relative_path: Path
    size: int
    language: str
    is_binary: bool
    content: str | None = None
    skipped_reason: str | None = None


def scan_project(
    config: ExportConfig,
    on_progress: Callable[[int], None] | None = None,
) -> list[FileRecord]:
    """Scan eligible files under the configured root in deterministic order."""
    records: list[FileRecord] = []
    output_path = config.output
    scanned_count = 0

    for directory, directory_names, file_names in os.walk(config.root, topdown=True):
        relative_directory = Path(directory).relative_to(config.root)
        directory_names[:] = sorted(
            name
            for name in directory_names
            if not _should_skip_directory(
                relative_directory / name, Path(directory, name), config
            )
        )
        for filename in sorted(file_names, key=str.lower):
            scanned_count += 1
            if on_progress and scanned_count % 1_000 == 0:
                on_progress(scanned_count)

            path = Path(directory, filename)
            if path.resolve() == output_path:
                continue
            relative_path = path.relative_to(config.root)
            if _should_skip_file(relative_path, config):
                continue
            try:
                size = path.stat().st_size
            except OSError:
                continue

            binary = is_probably_binary(path)
            record = FileRecord(path, relative_path, size, language_for(path), binary)
            if not config.include_content:
                record.skipped_reason = "content disabled"
            elif binary:
                record.skipped_reason = "binary file"
            elif size > config.max_file_size:
                record.skipped_reason = f"larger than {config.max_file_size} bytes"
            else:
                record.content = read_text_safely(path)
                if record.content is None:
                    record.skipped_reason = "could not read file"
            records.append(record)
    if on_progress:
        on_progress(scanned_count)
    records.sort(key=lambda record: record.relative_path.as_posix().lower())
    return records


def scan_structure(config: ExportConfig) -> list[tuple[Path, bool]]:
    """Return all allowed directories and files for a complete project tree."""
    entries: list[tuple[Path, bool]] = []
    output_path = config.output
    for directory, directory_names, file_names in os.walk(config.root, topdown=True):
        relative_directory = Path(directory).relative_to(config.root)
        directory_names[:] = sorted(
            name
            for name in directory_names
            if not _should_skip_directory(
                relative_directory / name, Path(directory, name), config
            )
        )
        entries.extend((relative_directory / name, True) for name in directory_names)
        for filename in sorted(file_names, key=str.lower):
            path = Path(directory, filename)
            relative_path = path.relative_to(config.root)
            if path.resolve() == output_path or _should_skip_tree_file(relative_path, config):
                continue
            entries.append((relative_path, False))
    return entries


def _should_skip_directory(relative_path: Path, absolute_path: Path, config: ExportConfig) -> bool:
    return (
        relative_path.name.casefold()
        in {name.casefold() for name in config.excluded_directories}
        or (absolute_path / "pyvenv.cfg").is_file()
        or (not config.include_hidden and relative_path.name.startswith("."))
        or _matches_ignore_pattern(relative_path, config.ignore_patterns, is_directory=True)
    )


def _should_skip_file(relative_path: Path, config: ExportConfig) -> bool:
    if relative_path.name in config.excluded_filenames:
        return True
    if not config.include_hidden and relative_path.name.startswith("."):
        return True
    if _matches_ignore_pattern(relative_path, config.ignore_patterns):
        return True
    return bool(config.extensions and relative_path.suffix.lower() not in config.extensions)


def _should_skip_tree_file(relative_path: Path, config: ExportConfig) -> bool:
    """Tree exports retain all visible files, independent of content filters."""
    return (
        relative_path.name in config.excluded_filenames
        or (not config.include_hidden and relative_path.name.startswith("."))
        or _matches_ignore_pattern(relative_path, config.ignore_patterns)
    )


def _matches_ignore_pattern(
    relative_path: Path,
    patterns: tuple[str, ...],
    *,
    is_directory: bool = False,
) -> bool:
    path = relative_path.as_posix()
    for pattern in patterns:
        normalized = pattern.lstrip("/")
        if normalized.endswith("/"):
            directory_pattern = normalized.rstrip("/")
            if is_directory and (
                fnmatchcase(path, directory_pattern)
                or fnmatchcase(relative_path.name, directory_pattern)
            ):
                return True
        elif fnmatchcase(path, normalized) or fnmatchcase(relative_path.name, normalized):
            return True
    return False
