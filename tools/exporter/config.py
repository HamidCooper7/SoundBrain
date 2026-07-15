"""Configuration models and defaults for the exporter."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


DEFAULT_EXCLUDED_DIRECTORIES = {
    ".git", ".hg", ".idea", ".pytest_cache", ".mypy_cache", ".ruff_cache",
    ".venv", "venv", "env", ".env", ".tox", "__pycache__", "node_modules", "vendor", "dist", "build",
    ".next", ".nuxt", "coverage",
    "exports",
    ".lmstudio", "lmstudio", "LM Studio",
}
DEFAULT_EXCLUDED_FILENAMES = {".DS_Store", "Thumbs.db"}
DEFAULT_MAX_FILE_SIZE = 1_000_000


@dataclass(slots=True)
class ExportConfig:
    root: Path
    output: Path
    include_content: bool = True
    include_hidden: bool = False
    max_file_size: int = DEFAULT_MAX_FILE_SIZE
    extensions: set[str] | None = None
    excluded_directories: set[str] = field(
        default_factory=lambda: set(DEFAULT_EXCLUDED_DIRECTORIES)
    )
    excluded_filenames: set[str] = field(
        default_factory=lambda: set(DEFAULT_EXCLUDED_FILENAMES)
    )
    ignore_patterns: tuple[str, ...] = ()
    tree_depth: int | None = None

    def __post_init__(self) -> None:
        self.root = self.root.resolve()
        self.output = self.output.resolve()
        self.excluded_directories.update(DEFAULT_EXCLUDED_DIRECTORIES)
        self.excluded_filenames.update(DEFAULT_EXCLUDED_FILENAMES)
        if self.extensions:
            self.extensions = {
                extension if extension.startswith(".") else f".{extension}"
                for extension in self.extensions
            }
