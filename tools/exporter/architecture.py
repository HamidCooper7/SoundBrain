"""Directory tree rendering."""

from __future__ import annotations

from pathlib import Path

from .analyzer import SourceAnalysis, build_import_graph, module_for_path
from .scanner import FileRecord


def render_tree(root: Path, records: list[FileRecord], max_depth: int | None = None) -> str:
    """Render a compact tree from exported file paths."""
    entries = [(record.relative_path, False) for record in records]
    return render_structure_tree(root, entries, max_depth)


def render_structure_tree(
    root: Path,
    entries: list[tuple[Path, bool]],
    max_depth: int | None = None,
) -> str:
    """Render a tree including empty directories and non-exported text files."""
    tree: dict[str, dict] = {}
    directories: set[tuple[str, ...]] = set()
    for relative_path, is_directory in entries:
        cursor = tree
        parts = relative_path.parts
        for index, part in enumerate(parts):
            cursor = cursor.setdefault(part, {})
            if is_directory or index < len(parts) - 1:
                directories.add(parts[: index + 1])

    lines = [f"{root.name}/"]
    _append_tree(lines, tree, "", 0, max_depth, (), directories)
    return "\n".join(lines)


def _append_tree(lines: list[str], tree: dict[str, dict], prefix: str, depth: int, max_depth: int | None, parent: tuple[str, ...], directories: set[tuple[str, ...]]) -> None:
    entries = sorted(tree.items(), key=lambda item: (not (parent + (item[0],) in directories), item[0].lower()))
    for index, (name, children) in enumerate(entries):
        is_last = index == len(entries) - 1
        branch = "└── " if is_last else "├── "
        path = parent + (name,)
        suffix = "/" if path in directories else ""
        lines.append(f"{prefix}{branch}{name}{suffix}")
        if children and path in directories:
            if max_depth is not None and depth + 1 >= max_depth:
                lines.append(f"{prefix}{'    ' if is_last else '│   '}└── …")
            else:
                _append_tree(lines, children, prefix + ("    " if is_last else "│   "), depth + 1, max_depth, path, directories)


def architecture_json(analyses: dict[Path, SourceAnalysis]) -> dict[str, dict[str, list[str]]]:
    """Create a package-level architecture manifest."""
    internal, external = build_import_graph(analyses)
    result: dict[str, dict[str, set[str]]] = {}
    for path, analysis in analyses.items():
        module = module_for_path(path)
        parts = module.split(".")
        package = ".".join(parts[:2]) if len(parts) > 1 else module
        entry = result.setdefault(package, {"imports": set(), "exports": set()})
        entry["imports"].update(internal.get(module, []))
        entry["imports"].update(external.get(module, []))
        entry["exports"].update(analysis.exports)
    return {
        package: {key: sorted(values) for key, values in payload.items()}
        for package, payload in sorted(result.items())
    }
