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
-   [x] RAG retrieval wired into SoundBrainService with graceful fallback

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
during Sprint 4 or the next architecture cleanup cycle.

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

## P2 — Sprint 3 — Core Integration

Status: ✅ Completed

Description

Sprint 3 wired the V1 deterministic and optional AI components into a single
end-to-end flow: Audio → Analysis → Context → Knowledge (RAG) → Reasoning →
Engineering → Report.

Completed

- Added `include_semantic_analysis` to `AnalysisRequest` and passed it through
  to `AudioReviewService`.
- Wired RAG retrieval in `SoundBrainService` with safe query building and
  graceful fallback when Chroma is empty or unavailable.
- Wired LLM reasoning in `SoundBrainService` and rebuilt the final report with
  the LLM-generated `ai_summary` when reasoning succeeds.
- Replaced bare `print()` statements with `logging` in `brain.rag.pipeline`,
  `brain.pipeline.engine`, and `brain/orchestration/executor`.
- Updated `main.py` CLI with `--reasoning`, `--rag`, `--semantic`, `--intent`,
  `--delivery-target`, and `--reference` flags.
- Updated `Orchestrator.analyze` to accept and pass the new flags.
- Added integration and optional-feature tests.

Files

- brain/application/soundbrain_service.py
- brain/application/audio_review_service.py
- brain/orchestration/orchestrator.py
- brain/rag/pipeline.py
- brain/pipeline/engine.py
- brain/orchestration/executor.py
- main.py
- tests/test_soundbrain_service_integration.py (new)
- tests/test_soundbrain_service_rag.py (new)
- tests/test_soundbrain_service_semantic.py (new)
- tests/test_soundbrain_service_reasoning.py (new)

## P2 — Sprint 4 — Reference Intelligence Integration

Status: ✅ Completed

Description

Sprint 4 enhanced the reference comparison path and merged it into the V1
SoundBrainService workflow.

Completed

- Added reference intent fields (`genre`, `mood`, `target`, `focus_areas`) to
  the reference models and `AnalysisRequest`.
- Added multi-reference support to `SoundBrainService.analyze`.
- Added `ReferenceService.compare_files_multiple` and
  `ReferenceEngine.compare_files_multiple`.
- Computed per-reference similarity scores and metric variance across references.
- Added `SegmentDeviation` structure with a thin V1 implementation over the
  global analysis.
- Updated `ReferenceReasoner` to build style-aware prompts and categorize
  decisions as `technical_issue`, `stylistic_difference`, or
  `insufficient_evidence`.
- Updated `main.py` with repeatable `--reference` and reference intent flags.
- Added evaluation fixtures under `tests/assets/reference_eval/`.
- Added reference intelligence tests.

Files

- brain/reference/models.py
- brain/reference/engine.py
- brain/reference/service.py
- brain/reference/reasoner.py
- brain/reference/pipeline.py
- brain/application/soundbrain_service.py
- main.py
- tests/test_reference_intelligence.py (new)
- tests/test_reference_reasoner.py (new)
- tests/test_soundbrain_service.py
- tests/assets/reference_eval/reference_eval_manifest.json (new)

Remaining Notes

- Segment analysis is currently a thin V1 placeholder over the global analysis.
  Full per-window segmentation is future work (P2).
- ReferenceAI uses rule-based reasoning; LLM-backed reference reasoning is future
  work (P2).

## P2 — Sprint 5 — Mix Intelligence

Status: ✅ Completed

Completed

-   [x] Root cause detection, priority engine, processing chain and explanations.
-   [x] Confidence scoring across issues, root causes, and recommendations.
-   [x] Integration into `SoundBrainService` and `main.py`.
-   [x] Tests and CLI validation.

Files

-   brain/audio/mix/
-   brain/audio/engineer/models.py
-   brain/application/soundbrain_service.py
-   brain/report/models.py
-   brain/report/builder.py
-   brain/report/exporter.py
-   main.py
-   tests/test_root_cause.py
-   tests/test_priority_engine.py
-   tests/test_processing_chain.py
-   tests/test_mix_explanation.py

---

## Blockers for Sprint 6 — Plugin Intelligence

-   [ ] Commercial plugin recommendation dataset — P2
-   [ ] Parameter generation for processing chain — P2
-   [ ] Preset export format (VST3/AU) and validation — P2
-   [ ] Real Whisper provider / test — P2 (carry-over)
-   [ ] Real Qwen provider / test — P2 (carry-over)
-   [ ] CUDA validation — P2 (carry-over)

---

## Environment Note — Pytest Temporary Directory on Windows

pytest defaults to `C:\Users\<user>\AppData\Local\Temp\pytest-of-<user>`, which
can raise `PermissionError` on Windows when existing directories are protected.
`pytest.ini` now sets `--basetemp=tmp` so temporary directories are created under
the repository root, making reference pipeline tests reproducible on Windows.

Files

-   pytest.ini
-   tmp/

---

## Environment Note — PyArrow Faulthandler Noise on Windows

When pytest's faulthandler plugin is active, importing ``pyarrow`` (pulled in by
``pandas`` → ``sklearn`` → ``transformers``) prints a non-fatal
``Windows fatal exception: access violation`` traceback during test collection.
The process continues and all tests pass. The noise disappears when running with
``-p no:faulthandler``. This is an environment-level quirk, not a SoundBrain bug.
