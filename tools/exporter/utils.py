"""Shared utility functions."""

from __future__ import annotations

from pathlib import Path


LANGUAGES = {
    ".py": "Python", ".js": "JavaScript", ".ts": "TypeScript", ".tsx": "TSX",
    ".jsx": "JSX", ".json": "JSON", ".html": "HTML", ".css": "CSS",
    ".scss": "SCSS", ".md": "Markdown", ".yml": "YAML", ".yaml": "YAML",
    ".toml": "TOML", ".xml": "XML", ".java": "Java", ".c": "C", ".cpp": "C++",
    ".cs": "C#", ".go": "Go", ".rs": "Rust", ".rb": "Ruby", ".php": "PHP",
    ".sh": "Shell", ".sql": "SQL", ".vue": "Vue", ".svelte": "Svelte",
}


def human_size(size: int) -> str:
    """Return a byte count in a compact human-readable form."""
    units = ("B", "KB", "MB", "GB")
    value = float(size)
    for unit in units:
        if value < 1024 or unit == units[-1]:
            return f"{value:.1f} {unit}" if unit != "B" else f"{int(value)} B"
        value /= 1024
    return f"{size} B"


def language_for(path: Path) -> str:
    return LANGUAGES.get(path.suffix.lower(), "Text")


def is_probably_binary(path: Path) -> bool:
    """Detect binary files cheaply, without decoding their entire content."""
    try:
        with path.open("rb") as file:
            sample = file.read(8192)
    except OSError:
        return True
    return b"\x00" in sample


def read_text_safely(path: Path) -> str | None:
    """Read a text file while tolerating uncommon encodings and read failures."""
    for encoding in ("utf-8", "utf-8-sig", "utf-16", "latin-1"):
        try:
            return path.read_text(encoding=encoding)
        except UnicodeError:
            continue
        except OSError:
            return None
    return None


def load_ignore_patterns(path: Path) -> tuple[str, ...]:
    """Load simple .gitignore-style patterns from a UTF-8 text file."""
    if not path.is_file():
        return ()
    try:
        lines = path.read_text(encoding="utf-8-sig").splitlines()
    except (OSError, UnicodeError):
        return ()
    return tuple(
        line.strip().replace("\\", "/")
        for line in lines
        if line.strip() and not line.lstrip().startswith("#")
    )
