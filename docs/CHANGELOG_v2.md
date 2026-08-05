
# Changelog

# [1.0.0-rc1] - 2026-08-05

## Release Candidate — V1 Professional Audio Intelligence

All V1 sprints (2.5 through 12) are complete. SoundBrain is now a production-ready
audio intelligence system with deterministic analysis, optional AI reasoning,
reference comparison, mix intelligence, plugin recommendations, knowledge,
memory, evaluation, workflow integration contracts, and a provider-agnostic AI
layer.

## Hardening

- Made `trust_remote_code` configurable per model entry instead of hardcoded.
- Made `ReportExporter.save_json` atomic via temp file + replace.
- Replaced silent optional-stage failures with explicit `status`/`warnings` in
  `AnalysisResponse` and `SoundBrainReport`.
- Updated `ParameterGenerator` to derive parameters from `ProcessingGoal` fields.
- Resolved default AI provider from configuration instead of hardcoding.
- Made configuration loading fail fast on YAML parse errors.
- Populated `pyproject.toml` dependencies from `requirements.txt`.
- Added `scripts/generate_v1_release_validation.py` and
  `reports/v1_release_validation.json`.

## Validation

- `black --check` and `ruff check` passed on Sprint 12 changed files.
- `compileall brain tests` passed.
- 188 deterministic regression tests passed in ~15 seconds.
- `main.py analyze tests/audio.wav --reasoning` produces a valid report with
  graceful LLM fallback when no local model is available.
- Workflow export, evaluation report, and provider layer verification passed.

## Known Limitations for V1.1

- HTTP LLM providers (Gemini/OpenAI) and local inference backend are stubs.
- Real Qwen/Whisper model availability depends on local environment.
- Reference segmentation is a thin V1 placeholder over global analysis.
- Legacy files still need a repository-wide formatting pass.

---

## Unreleased

- Added Sprint 4 — Reference Intelligence Integration.
  - `ReferenceIntent`, `SegmentDeviation`, and decision categorization models.
  - Multi-reference support in `ReferenceService`, `ReferenceEngine`, and `SoundBrainService`.
  - Per-reference similarity, metric variance, and thin V1 segment deviations.
  - Style-aware `ReferenceReasoner` prompt builder and decision categorization
    (`technical_issue`, `stylistic_difference`, `insufficient_evidence`).
  - `SoundBrainService.analyze` accepts `reference_path` as a single path or list
    and passes reference intent context to the comparison pipeline.
  - CLI `reference` command uses `reference <current.wav> <reference.wav> [...]` and
    writes `reference_report.json` plus `reference_report.md` to its output directory.
  - Added evaluation fixtures under `tests/assets/reference_eval/`.

- The reference CLI command uses `reference <current.wav> <reference.wav> [...]` and
  writes `reference_report.json` plus `reference_report.md` to its output directory.

All notable changes to SoundBrain are documented in this file.

The project follows a continuous architecture-first development process.

---

# [2.0.0] - 2026-07-15

## Vision

- Repositioned SoundBrain as an Audio Intelligence System.
- Defined long-term V1 → V5 roadmap.
- Introduced Audio Intelligence architecture.

## Documentation

Updated:

- README
- VISION
- PHILOSOPHY
- ARCHITECTURE
- AUDIO_ARCHITECTURE
- ROADMAP
- DECISIONS
- ENGINEERING
- DESIGN_PATTERNS
- AUDIO_ADR

## Architecture

Added:

- Perception Layer
- Understanding Layer
- Decision Layer
- Action Layer
- Creation Layer

Introduced:

- Generic Reasoning Engine concept
- Reference Intelligence architecture
- Agent-oriented architecture
- Knowledge Graph integration
- Multimodal Intelligence roadmap

## Audio

Added architectural support for:

- Psychoacoustics
- Reference reasoning
- Audio Memory
- Audio Foundation Models

## AI

Defined future support for:

- Mix Intelligence
- Master Intelligence
- Autonomous Mixing
- Audio Generation
- Voice Generation
- Agent Collaboration

---

# [1.x]

## Core Engine

Completed

- Audio IO
- Audio Analysis
- DSP Metrics
- Engineering Engine
- Semantic Intelligence
- CLAP Embeddings
- Comparison Engine
- Report Generation
- JSON Export
- Validation
- Reasoning Engine
- Prompt System
- Runtime Layer
- Service Layer

---

# Upcoming

## 2.1

- Generic Reasoning Engine
- Reference AI
- Intelligent Comparison

## 2.2

- Mix Intelligence
- Recommendation Engine

## 2.3

- Psychoacoustic Intelligence
- Knowledge Graph

## 2.4

- Agent Operating System

## 3.0

- Autonomous Mixing

## 4.0

- Audio Foundation Model

## 5.0

- Autonomous Audio Intelligence System
