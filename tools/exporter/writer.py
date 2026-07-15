"""Output writing helpers."""

from __future__ import annotations

from pathlib import Path
import json


def write_text(output: Path, content: str) -> None:
    """Write the export atomically to avoid partial report files."""
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_suffix(output.suffix + ".tmp")
    temporary.write_text(content, encoding="utf-8", newline="\n")
    temporary.replace(output)


def write_json(output: Path, content: object) -> None:
    write_text(output, json.dumps(content, ensure_ascii=False, indent=2) + "\n")
