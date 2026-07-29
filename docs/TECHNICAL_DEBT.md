# SoundBrain Technical Debt

Version: 0.1.0

Last Updated: 2026-07-28

---

# Overview

This document tracks every architectural debt, missing feature,
refactor and engineering task inside SoundBrain.

Priority:

- P0 = Critical
- P1 = High
- P2 = Medium
- P3 = Low
- Future = Long-term Vision

---

# P0 — Critical

## Runtime Integration

Status: ✅ Completed

Description

Every AI model must be loaded through ModelRuntime.

Completed

- CLAP now reads model name from configuration.
- Qwen now reads model name from configuration.
- BGE Reranker now reads model name from configuration.

Target

ModelRuntime becomes the single entry point for loading AI models.

---

## Remove Hardcoded Paths

Status: ✅ Completed

Updated files

- brain/audio/intelligence/embeddings.py
- brain/llm/qwen.py
- brain/rag/reranker.py

Target

No absolute filesystem path should exist anywhere in the project.

---

## Central Model Configuration

Status: ✅ Completed

Target

Every model is now resolved using ModelRepository and configured through:

- configs/runtime.yaml
- configs/models.yaml
- configs/audio.yaml

---

# P0 — Critical New Items

## Environment Import Crash

Status: ✅ Resolved

Description

Importing sentence_transformers at the same time as chromadb's
EmbeddingFunction Protocol caused a Windows segmentation fault during
module import. This blocked any code path that loaded brain.rag,
brain.services, or RAG-backed tests.

Resolution

- Lazy import of sentence_transformers in brain.rag.reranker.
- Lazy import of get_embedding_model in brain.rag.vectordb.
- Lazy import of langchain_text_splitters in brain.rag.splitter.

Remaining Note

- No dedicated BGE reranker test exists in tests/.
- tests/test_rag_pipeline.py is still blocked because brain.chat does
  not exist and the file is interactive (uses input()).

---

## Broken Audio Pipeline Test Interface

Status: ✅ Completed

Description

tests/test_audio_pipeline.py failed at collection because
AudioEncoder.encode() did not accept a task keyword argument, but
brain/audio/pipeline.py passes task=EmbeddingTask.SEMANTIC_SEARCH.

Resolution

- AudioEncoder.encode(), EmbeddingManager.encode(), and
  CLAPEmbedding.encode_audio() now accept an optional task argument.
- brain/audio/pipeline.py correctly passes the factory keyword.
- CLAPEmbedding now resamples non-48kHz audio and casts inputs to the
  model dtype.

Files

- brain/audio/pipeline.py
- brain/audio/embeddings/encoder.py
- brain/audio/embeddings/manager.py
- brain/audio/embeddings/base.py
- brain/audio/embeddings/clap.py

---

## Missing brain.audio.io.loader Module

Status: ✅ Completed

Description

brain/reference/service.py imports brain.audio.io.loader, which did not
exist. This broke tests/test_reference_pipeline.py at collection.

Resolution

- Created brain/audio/io/loader.py with AudioLoader.
- Created brain/engineering/engine.py with EngineeringEngine because
  ReferenceService also depended on it.

Files

- brain/audio/io/loader.py (new)
- brain/engineering/__init__.py (new)
- brain/engineering/engine.py (new)

---

## Missing brain.chat Module

Status: ✅ Resolved

tests/test_rag_pipeline.py imported brain.chat.chat, which did not exist. The
interactive test file was moved to tests/archive/ and replaced with a
non-interactive test (tests/test_rag_collection.py).

Files

- tests/test_rag_pipeline.py → tests/archive/test_rag_pipeline.py
- tests/test_rag_collection.py (new)

---

## RAG Test File Is Interactive

Status: ✅ Resolved

tests/test_rag_pipeline.py used a while True loop with input() and could not be
executed by pytest. It was archived and replaced with tests/test_rag_collection.py,
which only verifies that RAG modules import without loading models.

Files

- tests/test_rag_pipeline.py → tests/archive/test_rag_pipeline.py
- tests/test_rag_collection.py (new)

---

## Reference AI

Status: In Progress

Tasks

- Improve Prompt Builder
- Improve Formatter
- JSON Output
- Structured Recommendations
- Confidence Score
- Better Engineering Reasoning

---

## Mix Intelligence

Status: Planned

Tasks

- Frequency Balance
- Dynamic Balance
- Stereo Analysis
- Tonal Balance
- Loudness Strategy
- Human Engineering Suggestions

---

## Master Intelligence

Status: Planned

Tasks

- Loudness Optimization
- Streaming Optimization
- Dynamics
- Translation
- Commercial Master Analysis

---

## Knowledge Base

Status: Planned

Sources

- AES
- ITU
- EBU
- Dolby
- Harman
- Spotify
- Apple Music
- Engineering Books

---

# P2

## Memory

- Long-term Memory
- Session Memory
- Audio Memory

---

## Agent Planning

- Task Planner
- Reflection
- Self Critique

---

## RAG Improvements

- Metadata Search
- Hybrid Search
- Audio Retrieval
- Context Compression

---

## Canonical CLAP Provider Consolidation

Status: P2 — Long-term cleanup

Description

Two parallel CLAP implementations exist: ``brain.audio.embeddings.clap.CLAPEmbedding``
(the canonical provider) and ``brain.audio.intelligence.embeddings.CLAPAudioEmbeddingModel``
(the legacy provider). New code should use ``CLAPEmbedding``. Legacy callers
(AudioIntelligenceAnalyzer, tests/test_intelligence.py) still import the legacy
class and should be migrated to the canonical provider during Sprint 3 or the next
architecture cleanup cycle.

Files

- brain/audio/embeddings/clap.py (canonical)
- brain/audio/intelligence/embeddings.py (legacy)
- brain/audio/intelligence/analyzer.py (legacy caller)

---

## Sprint 2.6 — Platform Finalization

Status: ✅ Completed

Description

Sprint 2.6 closed the platform surface before Core Integration (Sprint 3).

Completed

- Created `brain.application.soundbrain_service` with `SoundBrainService` and V1
  `AnalysisRequest` / `AnalysisResponse`.
- Routed `main.py` through `SoundBrainService`.
- Extended `Orchestrator` and `State` to carry a V1 `AnalysisRequest` and
  `AnalysisResponse`.
- Registered V1 capabilities in `brain.runtime.capabilities`.
- Created `brain.runtime.engine_registry` with `audio_review`,
  `reference_comparison`, and `soundbrain` engines.
- Made `brain.embedding` lazy-import `sentence_transformers` to avoid heavy
  module-level imports.
- Added `tests/test_soundbrain_service.py` and `tests/test_engine_registry.py`.

Files

- brain/application/soundbrain_service.py (new)
- brain/runtime/engine_registry.py (new)
- brain/runtime/capabilities.py
- brain/orchestration/orchestrator.py
- brain/orchestration/state.py
- brain/embedding.py
- main.py
- tests/test_soundbrain_service.py (new)
- tests/test_engine_registry.py (new)

---

## Environment Note — PyArrow Faulthandler Noise on Windows

Status: P3 — Environment quirk

Description

When pytest's faulthandler plugin is active, importing ``pyarrow`` (via
``pandas`` → ``sklearn`` → ``transformers``) prints a non-fatal
``Windows fatal exception: access violation`` traceback during test collection.
All tests still pass and the process continues. Running with
``-p no:faulthandler`` suppresses the noise. This is a Windows/pyarrow wheel
quirk, not a SoundBrain bug.

Files

- N/A (environment)

---

## Sprint 2.6 — Platform Finalization

Status: ✅ Completed

Description

Sprint 2.6 closed the platform surface before Core Integration (Sprint 3).

Completed

- Created `brain.application.soundbrain_service` with `SoundBrainService` and V1
  `AnalysisRequest` / `AnalysisResponse`.
- Routed `main.py` through `SoundBrainService`.
- Extended `Orchestrator` and `State` to carry a V1 `AnalysisRequest` and
  `AnalysisResponse`.
- Registered V1 capabilities in `brain.runtime.capabilities`.
- Created `brain.runtime.engine_registry` with `audio_review`,
  `reference_comparison`, and `soundbrain` engines.
- Made `brain.embedding` lazy-import `sentence_transformers` to avoid heavy
  module-level imports.
- Refactored heavy package-level imports in `brain.audio`, `brain.audio.analysis`,
  `brain.audio.context`, `brain.audio.engineer`, `brain.audio.io`, and
  `brain.reference` to use lazy `__getattr__` resolution. This prevents
  importing `torch`/`transformers` when only dataclass models are needed.
- Added `tests/test_soundbrain_service.py` and `tests/test_engine_registry.py`.

Files

- brain/application/soundbrain_service.py (new)
- brain/runtime/engine_registry.py (new)
- brain/runtime/capabilities.py
- brain/orchestration/orchestrator.py
- brain/orchestration/state.py
- brain/embedding.py
- brain/audio/__init__.py
- brain/audio/analysis/__init__.py
- brain/audio/context/__init__.py
- brain/audio/engineer/__init__.py
- brain/audio/io/__init__.py
- brain/reference/__init__.py
- main.py
- tests/test_soundbrain_service.py (new)
- tests/test_engine_registry.py (new)

---

## CLI

Commands

soundbrain analyze

soundbrain compare

soundbrain reference

soundbrain engineer

---

## REST API

Endpoints

/audio/analyze

/audio/reference

/audio/report

/audio/reason

---

# P3

## GUI

Desktop Application

Dashboard

Timeline

Visualizer

Audio Inspector

---

## DAW Integration

Ableton

FL Studio

Cubase

Reaper

Logic

---

## Plugin

VST3

AU

AAX

---

# Future

## Audio Foundation Model

Unified Audio Model

Semantic Understanding

Engineering Understanding

Generation

Editing

Restoration

Automation

---

## Autonomous Audio Intelligence

Target

SoundBrain should evolve into a complete Audio Intelligence System capable of:

- Audio Analysis
- Audio Understanding
- Audio Reasoning
- Audio Memory
- Audio Retrieval
- Audio Generation
- Audio Editing
- Audio Restoration
- DAW Automation
- Mixing
- Mastering
- Voice Interaction

---

# Completed

- Project Architecture
- Runtime Foundation
- Audio Analysis
- Audio Context
- Engineering Rules
- Comparison Engine
- Report Builder
- RAG Foundation
- Documentation
- GitHub Repository
- Clean Repository Structure

---

# Notes

Every Sprint must update this file.

No new feature should be started before reviewing this document.