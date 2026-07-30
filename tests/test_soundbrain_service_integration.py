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
def test_soundbrain_service_integration_deterministic():
    """End-to-end deterministic flow with default flags."""
    request = AnalysisRequest(
        audio_path=AUDIO_PATH,
        intent="integration test",
        delivery_target="streaming",
    )

    service = SoundBrainService()
    response = service.analyze(request)

    assert response.audio is not None
    assert response.analysis is not None
    assert response.context is not None
    assert response.engineering is not None
    assert response.report is not None

    report = response.report
    assert report.audio_type
    assert report.source_type
    assert isinstance(report.score, float)
    assert isinstance(report.issues, list)
    assert isinstance(report.recommendations, list)
    assert isinstance(report.strengths, list)
    assert response.comparison is None

    # Without reasoning, ai_summary should be the validated intent text.
    assert "Integration test" in report.ai_summary or report.ai_summary == ""


@pytest.mark.skipif(
    not AUDIO_PATH.exists(),
    reason="No test audio file is available",
)
def test_soundbrain_service_integration_with_reference():
    """Deterministic flow with reference comparison."""
    request = AnalysisRequest(
        audio_path=AUDIO_PATH,
        reference_path=AUDIO_PATH,
    )

    service = SoundBrainService()
    response = service.analyze(request)

    assert response.comparison is not None
