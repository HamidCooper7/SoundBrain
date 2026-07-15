from __future__ import annotations

from brain.infrastructure.config.settings import settings


def load_settings():

    """
    Future entry point.

    Later this function will load:

    - .env
    - JSON
    - YAML

    Currently returns default settings.
    """

    return settings