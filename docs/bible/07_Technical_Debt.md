# 07 --- Technical Debt

> SoundBrain Project Bible

------------------------------------------------------------------------

# Overview

Technical Debt tracks all known unfinished engineering work that should
be resolved before or during future development.

------------------------------------------------------------------------

# Runtime

Status: 🟢 Validation Completed

## Open Items

-   [x] Execute Runtime validation
-   [x] Validate CLAP provider (imports and executes via audio pipeline; no CLAP-specific test exists)
-   [ ] Validate Whisper provider (no Whisper model or test exists)
-   [x] Validate BGE provider (imports are now clean; no dedicated test exists)
-   [ ] Validate Qwen provider (no Qwen-specific test exists)
-   [x] CPU validation (main.py analyze tests/audio.wav passes on CPU)
-   [x] V1 SoundBrainService validation (tests/test_soundbrain_service.py passes)
-   [ ] CUDA validation (no CUDA device available in current env)
-   [ ] Benchmark startup time

------------------------------------------------------------------------

# RAG Integration

Status: 🟢 Clean

## Open Items

-   [x] brain.rag imports without crash
-   [x] brain.services imports without crash
-   [x] tests/test_rag_pipeline.py resolved (archived, replaced by tests/test_rag_collection.py)
-   [x] Replace interactive RAG test with a proper pytest test

------------------------------------------------------------------------

# Audio Pipeline

Status: ✅ Completed

## Open Items

-   [x] AudioEncoder.encode() accepts task argument
-   [x] tests/test_audio_pipeline.py collects and runs without error
-   [x] CLAP embedding handles resampling and dtype

------------------------------------------------------------------------

# Reference Pipeline

Status: ✅ Completed

## Open Items

-   [x] brain.audio.io.loader created
-   [x] brain.engineering created
-   [x] tests/test_reference_pipeline.py passes

------------------------------------------------------------------------

# Rules

Do NOT introduce new technical debt before resolving critical Runtime
validation tasks.

------------------------------------------------------------------------

# Living Notes

Remove items from this document only after they are fully completed.

## P2 — Canonical CLAP Provider Consolidation

Two CLAP providers exist: ``brain.audio.embeddings.clap.CLAPEmbedding`` (canonical)
and ``brain.audio.intelligence.embeddings.CLAPAudioEmbeddingModel`` (legacy). New code
must use the canonical provider. Legacy callers (AudioIntelligenceAnalyzer,
tests/test_intelligence.py) still import the legacy class and should be migrated
during Sprint 3 or the next architecture cleanup cycle.

## P2 — Sprint 2.6 — Platform Finalization

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

## Environment Note — PyArrow Faulthandler Noise on Windows

When pytest's faulthandler plugin is active, importing ``pyarrow`` (pulled in by
``pandas`` → ``sklearn`` → ``transformers``) prints a non-fatal
``Windows fatal exception: access violation`` traceback during test collection.
The process continues and all tests pass. The noise disappears when running with
``-p no:faulthandler``. This is an environment-level quirk, not a SoundBrain bug.
