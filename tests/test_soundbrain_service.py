from __future__ import annotations

from pathlib import Path

import pytest

from brain.application.soundbrain_service import (
    AnalysisRequest,
    SoundBrainService,
)


AUDIO_PATH = Path("tests/audio.wav")


@pytest.mark.skipif(
    not AUDIO_PATH.exists(),
    reason="No test audio file is available",
)
def test_soundbrain_service_analyze():
    request = AnalysisRequest(
        audio_path=AUDIO_PATH,
        intent="test analysis",
        delivery_target="streaming",
    )

    service = SoundBrainService()
    response = service.analyze(request)

    assert response.audio is not None
    assert response.analysis is not None
    assert response.context is not None
    assert response.engineering is not None
    assert response.report is not None
    assert response.comparison is None


def test_soundbrain_service_analyze_missing_audio_gracefully():
    request = AnalysisRequest(
        audio_path="tests/does_not_exist.wav",
    )

    service = SoundBrainService()
    with pytest.raises(Exception):
        service.analyze(request)


def test_soundbrain_service_module_import_does_not_load_torch():
    """Importing the service module must not load torch or transformers."""
    import subprocess
    import sys

    script = (
        "import sys\n"
        "from brain.application.soundbrain_service import AnalysisRequest\n"
        "print('torch' in sys.modules, 'transformers' in sys.modules)\n"
    )

    result = subprocess.run(
        [sys.executable, "-c", script],
        capture_output=True,
        text=True,
        cwd=Path(__file__).resolve().parents[1],
    )

    assert result.returncode == 0, result.stderr
    output = result.stdout.strip()
    assert output == "False False", f"heavy modules loaded: {output}"
