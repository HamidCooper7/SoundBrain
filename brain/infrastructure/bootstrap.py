from __future__ import annotations

from brain.infrastructure.application import Application
from brain.infrastructure.container import container

from brain.services.registration import (
    register_services,
)


def create_application() -> Application:

    register_services(
        container.services,
    )

    return Application(container)