from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from .models import MemoryBundle, ProjectProfile, UserProfile


class MemoryLoader:
    """Load a MemoryBundle from YAML files or an inline dictionary."""

    def __init__(self, root: str | Path = "configs/memory") -> None:
        self._root = Path(root)

    def load(self) -> MemoryBundle:
        """Load the default memory bundle from ``root/memory_bundle.yaml``."""
        return self.load_from_path(self._root / "memory_bundle.yaml")

    def load_from_path(self, path: str | Path) -> MemoryBundle:
        """Load a memory bundle from a master YAML file."""
        path = Path(path)
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise TypeError(f"Memory bundle must be a mapping: {path}")
        return self._parse_bundle(data, path.parent)

    def load_from_dict(self, data: dict[str, Any]) -> MemoryBundle:
        """Load a memory bundle from a fully populated dictionary."""
        if not isinstance(data, dict):
            raise TypeError("Memory bundle must be a mapping")
        return self._parse_bundle(data, None)

    def _parse_bundle(
        self,
        data: dict[str, Any],
        base_dir: Path | None,
    ) -> MemoryBundle:
        version = str(data.get("version", "0.0.0"))

        user_profile = self._load_section("user_profile", data, base_dir, default_factory=dict)
        project_profile = self._load_section(
            "project_profile", data, base_dir, default_factory=dict
        )

        return MemoryBundle(
            version=version,
            user_profile=self._parse_user_profile(user_profile),
            project_profile=self._parse_project_profile(project_profile),
        )

    def _load_section(
        self,
        name: str,
        data: dict[str, Any],
        base_dir: Path | None,
        default_factory: Any = None,
    ) -> Any:
        """Resolve a section either inline or from a referenced YAML file."""
        value = data.get(name, default_factory() if default_factory else None)
        if isinstance(value, str) and base_dir is not None:
            section_path = base_dir / value
            if not section_path.exists():
                return {}
            section_data = yaml.safe_load(section_path.read_text(encoding="utf-8"))
            if isinstance(section_data, dict) and name in section_data:
                return section_data[name]
            return section_data
        return value

    def _parse_user_profile(self, data: dict[str, Any]) -> UserProfile:
        return UserProfile(
            user_id=str(data.get("user_id", "default")),
            preferred_loudness_by_platform=dict(data.get("preferred_loudness_by_platform", {})),
            preferred_true_peak_max=data.get("preferred_true_peak_max"),
            preferred_dynamic_range_min=data.get("preferred_dynamic_range_min"),
            preferred_plugin_brands=list(data.get("preferred_plugin_brands", [])),
            preferred_genres=list(data.get("preferred_genres", [])),
            preferred_processing_order=list(data.get("preferred_processing_order", [])),
            preferred_export_targets=list(data.get("preferred_export_targets", [])),
            notes=list(data.get("notes", [])),
        )

    def _parse_project_profile(self, data: dict[str, Any]) -> ProjectProfile:
        return ProjectProfile(
            project_id=str(data.get("project_id", "default")),
            target_platform=data.get("target_platform"),
            genre=data.get("genre"),
            reference_paths=list(data.get("reference_paths", [])),
            delivery_targets=list(data.get("delivery_targets", [])),
            notes=list(data.get("notes", [])),
        )
