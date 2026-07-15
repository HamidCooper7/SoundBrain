"""Python source analysis used by architecture and report exports."""

from __future__ import annotations

import ast
from collections import defaultdict
from dataclasses import dataclass, field
from fnmatch import fnmatchcase
from pathlib import Path

from .scanner import FileRecord


@dataclass(slots=True)
class SourceAnalysis:
    classes: list[str] = field(default_factory=list)
    functions: list[str] = field(default_factory=list)
    imports: list[str] = field(default_factory=list)
    exports: list[str] = field(default_factory=list)
    class_details: dict[str, dict[str, str]] = field(default_factory=dict)
    function_details: dict[str, dict[str, object]] = field(default_factory=dict)
    lines: int = 0


def analyze_records(records: list[FileRecord]) -> dict[Path, SourceAnalysis]:
    """Parse readable Python files, retaining partial results for invalid source."""
    analyses: dict[Path, SourceAnalysis] = {}
    for record in records:
        if record.relative_path.suffix.lower() != ".py" or record.content is None:
            continue
        analysis = SourceAnalysis(lines=record.content.count("\n") + bool(record.content))
        try:
            tree = ast.parse(record.content, filename=str(record.relative_path))
        except SyntaxError:
            analyses[record.relative_path] = analysis
            continue
        for node in tree.body:
            if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
                destination = analysis.classes if isinstance(node, ast.ClassDef) else analysis.functions
                destination.append(node.name)
                if not node.name.startswith("_"):
                    analysis.exports.append(node.name)
                    if isinstance(node, ast.ClassDef):
                        analysis.class_details[node.name] = {
                            "docstring": ast.get_docstring(node) or "",
                        }
                    else:
                        analysis.function_details[node.name] = {
                            "type_hints": _function_type_hints(node),
                            "return_type": _annotation_text(node.returns),
                            "docstring": ast.get_docstring(node) or "",
                        }
            elif isinstance(node, ast.Import):
                analysis.imports.extend(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    base_module = "." * node.level + node.module
                    analysis.imports.append(base_module)
                    analysis.imports.extend(f"{base_module}.{alias.name}" for alias in node.names)
                else:
                    analysis.imports.extend("." * node.level + alias.name for alias in node.names)
        analyses[record.relative_path] = analysis
    return analyses


def module_for_path(path: Path) -> str:
    """Return an import-like module name for a Python source path."""
    parts = list(path.with_suffix("").parts)
    if parts[-1] == "__init__":
        parts.pop()
    return ".".join(parts)


def build_import_graph(
    analyses: dict[Path, SourceAnalysis],
) -> tuple[dict[str, list[str]], dict[str, list[str]]]:
    """Return internal and external imports keyed by project module."""
    known_modules = {module_for_path(path) for path in analyses}
    internal: dict[str, list[str]] = {}
    external: dict[str, list[str]] = {}
    for path, analysis in analyses.items():
        module = module_for_path(path)
        local: set[str] = set()
        outside: set[str] = set()
        for imported in analysis.imports:
            resolved = _resolve_import(module, imported)
            if resolved in known_modules or any(name.startswith(f"{resolved}.") for name in known_modules):
                local.add(resolved)
            elif imported:
                outside.add(imported.lstrip(".").split(".")[0])
        internal[module] = sorted(local)
        external[module] = sorted(outside)
    return internal, external


def find_cycles(graph: dict[str, list[str]]) -> list[list[str]]:
    """Find unique directed cycles in an import graph."""
    cycles: list[list[str]] = []
    active: list[str] = []
    visited: set[str] = set()

    def visit(module: str) -> None:
        visited.add(module)
        active.append(module)
        for dependency in graph.get(module, []):
            if dependency == module:
                continue
            if dependency in active:
                start = active.index(dependency)
                cycle = active[start:] + [dependency]
                key = tuple(sorted(cycle[:-1]))
                if not any(tuple(sorted(item[:-1])) == key for item in cycles):
                    cycles.append(cycle)
            elif dependency not in visited:
                visit(dependency)
        active.pop()

    for module in graph:
        if module not in visited:
            visit(module)
    return cycles


def duplicate_symbols(analyses: dict[Path, SourceAnalysis]) -> dict[str, list[str]]:
    locations: dict[str, list[str]] = defaultdict(list)
    for path, analysis in analyses.items():
        for symbol in [*analysis.classes, *analysis.functions]:
            locations[symbol].append(path.as_posix())
    return {
        symbol: files
        for symbol, files in locations.items()
        if len(files) > 1 and not _is_common_symbol(symbol)
    }


def api_manifest(analyses: dict[Path, SourceAnalysis]) -> dict[str, dict[str, list[str]]]:
    """Return a searchable manifest of public Python symbols and imports."""
    return {
        module_for_path(path): {
            "classes": sorted(name for name in analysis.classes if not name.startswith("_")),
            "functions": sorted(name for name in analysis.functions if not name.startswith("_")),
            "imports": sorted(set(analysis.imports)),
            "class_details": dict(sorted(analysis.class_details.items())),
            "function_details": dict(sorted(analysis.function_details.items())),
        }
        for path, analysis in sorted(analyses.items(), key=lambda item: item[0].as_posix())
    }


def _resolve_import(current_module: str, imported: str) -> str:
    if not imported.startswith("."):
        return imported
    dots = len(imported) - len(imported.lstrip("."))
    package = current_module.split(".")[:-1]
    base = package[: max(0, len(package) - dots + 1)]
    suffix = imported.lstrip(".")
    return ".".join([*base, *([suffix] if suffix else [])])


def _is_common_symbol(symbol: str) -> bool:
    return symbol.casefold() in {"main", "__init__", "run"} or fnmatchcase(symbol.casefold(), "test_*")


def _function_type_hints(node: ast.FunctionDef | ast.AsyncFunctionDef) -> dict[str, str]:
    arguments = [*node.args.posonlyargs, *node.args.args, *node.args.kwonlyargs]
    hints = {argument.arg: _annotation_text(argument.annotation) for argument in arguments if argument.annotation}
    if node.args.vararg and node.args.vararg.annotation:
        hints[f"*{node.args.vararg.arg}"] = _annotation_text(node.args.vararg.annotation)
    if node.args.kwarg and node.args.kwarg.annotation:
        hints[f"**{node.args.kwarg.arg}"] = _annotation_text(node.args.kwarg.annotation)
    return hints


def _annotation_text(annotation: ast.expr | None) -> str:
    return ast.unparse(annotation) if annotation else ""
