from .loader import load_settings
from .settings import DEFAULT_SETTINGS

settings = load_settings()

__all__ = [
    "settings",
    "load_settings",
    "DEFAULT_SETTINGS",
]