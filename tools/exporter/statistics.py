"""Project statistics calculations."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass

from .scanner import FileRecord
from .analyzer import SourceAnalysis


@dataclass(slots=True)
class ProjectStatistics:
    file_count: int
    total_size: int
    binary_count: int
    content_count: int
    by_extension: Counter[str]
    by_language: Counter[str]


def calculate_statistics(records: list[FileRecord]) -> ProjectStatistics:
    return ProjectStatistics(
        file_count=len(records),
        total_size=sum(record.size for record in records),
        binary_count=sum(record.is_binary for record in records),
        content_count=sum(record.content is not None for record in records),
        by_extension=Counter(record.relative_path.suffix.lower() or "[no extension]" for record in records),
        by_language=Counter(record.language for record in records),
    )


def statistics_json(
    records: list[FileRecord], analyses: dict[object, SourceAnalysis], project_name: str, generated_at: str
) -> dict[str, object]:
    return {
        "project": project_name,
        "generated_at": generated_at,
        "files": len(records),
        "python_files": sum(record.relative_path.suffix.lower() == ".py" for record in records),
        "classes": sum(len(item.classes) for item in analyses.values()),
        "functions": sum(len(item.functions) for item in analyses.values()),
        "imports": sum(len(item.imports) for item in analyses.values()),
        "public_api_count": sum(len(item.exports) for item in analyses.values()),
        "lines": sum(item.lines for item in analyses.values()),
        "packages": len({str(path.parent) for path in analyses}),
    }
