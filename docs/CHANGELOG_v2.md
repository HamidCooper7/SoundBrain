
# Changelog

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
