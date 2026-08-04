# SoundBrain Technical Debt

Version: 0.1.0

Last Updated: 2026-08-04

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

Status: ✅ Completed

Description

Reference Intelligence was integrated into SoundBrainService.analyze via the
``reference_path`` option. Multi-reference support, reference intent
(genre/mood/target/focus), per-reference similarity, metric variance, segment
deviation structure, and style-aware decision categorization are now in place.

Completed

- Added ``ReferenceIntent``, ``SegmentDeviation``, and decision categorization models.
- Extended ``ReferenceComparison`` with references, reference_similarities,
  metric_variance, and segment_deviations.
- Added multi-reference support in ``ReferenceService`` and ``ReferenceEngine``.
- Added thin V1 segment deviation implementation in ``ReferenceService``.
- Updated ``ReferenceReasoner`` to accept intent, build style-aware prompts, and
  categorize decisions as ``technical_issue``, ``stylistic_difference``, or
  ``insufficient_evidence``.
- Integrated ``reference_path`` (single or list) and reference intent fields into
  ``SoundBrainService.analyze``.
- Updated CLI with repeatable ``--reference`` and reference intent flags.
- Added evaluation fixtures under ``tests/assets/reference_eval/``.
- Added ``tests/test_reference_intelligence.py``, ``tests/test_reference_reasoner.py``,
  and reference tests in ``tests/test_soundbrain_service.py``.

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
- tests/assets/reference_eval/reference_eval_manifest.json (new)

Remaining Notes

- Segment analysis is currently a thin V1 placeholder over the global analysis.
  Full per-window segmentation is future work (P2).
- ReferenceAI uses rule-based reasoning; LLM-backed reference reasoning is future
  work (P2).

---

## Mix Intelligence

Status: ✅ Completed

Description

Deterministic mix intelligence now generates root causes, prioritized issues,
a non-destructive processing chain and human-readable explanations for every
V1 analysis.

Completed

- Created `brain.audio.mix` package with `RootCauseAnalyzer`, `PriorityEngine`,
  `ProcessingChainRecommender` and `ExplanationBuilder`.
- Added confidence scoring to `EngineerIssue`, `Recommendation`, `RootCause`,
  `PrioritizedIssue` and `ProcessingStep`.
- Extended `SoundBrainReport` and `AnalysisResponse` with mix intelligence fields.
- Wired `include_mix_intelligence` through `SoundBrainService.analyze`.
- Added `--mix-intelligence` flag to `main.py`.
- Added unit tests and integration test coverage.

Files

- brain/audio/mix/root_cause.py (new)
- brain/audio/mix/priority.py (new)
- brain/audio/mix/chains.py (new)
- brain/audio/mix/explanation.py (new)
- brain/audio/mix/models.py (new)
- brain/audio/mix/__init__.py (new)
- brain/audio/engineer/models.py
- brain/report/models.py
- brain/application/soundbrain_service.py
- main.py
- tests/test_root_cause.py (new)
- tests/test_priority_engine.py (new)
- tests/test_processing_chain.py (new)
- tests/test_mix_explanation.py (new)
- tests/test_soundbrain_service_integration.py

Remaining Notes

- Mix intelligence is deterministic and rule-based. LLM-enriched mix reasoning is
  future work (P2).
- Processing chain suggestions are high-level plugin types only; commercial
  plugin recommendations and parameter generation are future work (Sprint 6).

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

## Sprint 3 — Core Integration

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
- Preserved deterministic report fields (score, issues, recommendations,
  strengths, semantic_labels) during reasoning rebuild.
- Replaced bare `print()` statements with `logging` in `brain.rag.pipeline`,
  `brain.pipeline.engine`, and `brain.orchestration.executor`.
- Updated `main.py` CLI with `--reasoning`, `--rag`, `--semantic`, `--intent`,
  `--delivery-target`, and `--reference` flags.
- Updated `Orchestrator.analyze` to accept and pass the new flags.
- Added integration and optional-feature tests:
  - `tests/test_soundbrain_service_integration.py`
  - `tests/test_soundbrain_service_rag.py`
  - `tests/test_soundbrain_service_semantic.py`
  - `tests/test_soundbrain_service_reasoning.py`

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

---

## Sprint 4 — Reference Intelligence Integration

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

---

## P2 — Sprint 5 — Mix Intelligence

Status: ✅ Completed

Description

Sprint 5 delivered deterministic mix intelligence as an optional, flag-gated
stage in the V1 workflow.

Completed

- Root cause detection, priority engine, processing chain and explanations.
- Confidence scoring across issues, root causes, and recommendations.
- Integration into `SoundBrainService` and `main.py`.
- Tests and CLI validation.

Files

- brain/audio/mix/
- brain/audio/engineer/models.py
- brain/application/soundbrain_service.py
- brain/report/models.py
- brain/report/builder.py
- brain/report/exporter.py
- main.py
- tests/test_root_cause.py
- tests/test_priority_engine.py
- tests/test_processing_chain.py
- tests/test_mix_explanation.py

---

## P2 — Sprint 6 — Plugin Intelligence

Status: ✅ Completed

Description

Sprint 6 extended Mix Intelligence with Plugin Intelligence: parameter
recommendations, plugin selection, and validated processing chains. Plugin brands
exist only inside the registry; decision logic is brand-agnostic.

Completed

- Plugin taxonomy and JSON registry (`configs/plugin_registry.json`).
- Parameter generator (`brain.audio.plugin.parameter_generator`) executed before plugin selection.
- Plugin selector (`brain.audio.plugin.selector`) that filters by category, format, and limit.
- Plugin chain builder (`brain.audio.plugin.chain_builder`) that deduplicates categories and limits chain length.
- Plugin validator (`brain.audio.plugin.validator`) that clamps parameter ranges and removes mismatched options.
- Plugin intelligence service (`brain.audio.plugin.service`) orchestrating the pipeline.
- Integration into `SoundBrainService` via `include_plugin_intelligence` flag.
- Extension of `SoundBrainReport` and `AnalysisResponse` with `plugin_intelligence` fields.
- `--plugin-intelligence` CLI flag in `main.py`.
- Unit and integration tests for all plugin modules.

Files

- brain/audio/plugin/
- configs/plugin_registry.json
- brain/application/soundbrain_service.py
- brain/report/models.py
- brain/report/exporter.py
- main.py
- tests/test_plugin_registry.py
- tests/test_plugin_selector.py
- tests/test_plugin_parameter_generator.py
- tests/test_plugin_chain_builder.py
- tests/test_plugin_validator.py
- tests/test_plugin_intelligence_service.py
- tests/test_soundbrain_service_integration.py

Remaining Notes

- Plugin registry is a small hand-curated dataset. Larger commercial datasets are
  future work (P2).
- VST3/AU preset export and validation are future work (Sprint 8+).
- Parameter generation is deterministic; ML-based parameter prediction is future
  work (P2).

---

## P2 — Sprint 7 — Knowledge Infrastructure

Status: ✅ Completed

Description

Sprint 7 introduced the Knowledge Infrastructure layer as a standalone,
optional, read-only data layer. No existing business logic modules were
migrated; this sprint delivered only the models, loader, validator, registry,
resolver, service, and default configuration files.

Completed

- Knowledge models (`brain.knowledge.models`) for engineering rules, genre/platform
  profiles, plugin capabilities, root causes, and best practices.
- Knowledge loader (`brain.knowledge.loader`) for YAML master bundle and inline
  dictionary loading.
- Knowledge validator (`brain.knowledge.validator`) for required keys, version
  checks, and range validation.
- Knowledge registry (`brain.knowledge.registry`) composing loader and validator.
- Knowledge resolver (`brain.knowledge.resolver`) providing defensive query helpers.
- Knowledge service (`brain.knowledge.service`) as lazy-loading facade.
- Default configuration under `configs/knowledge/`.
- Deterministic unit tests for loader, validator, registry, resolver, and service.

Files

- brain/knowledge/
- configs/knowledge/
- tests/test_knowledge_loader.py
- tests/test_knowledge_validator.py
- tests/test_knowledge_registry.py
- tests/test_knowledge_resolver.py
- tests/test_knowledge_service.py

Remaining Notes

- Knowledge layer is isolated; no business logic migration occurred in Sprint 7.
- Future sprints will migrate thresholds and mappings from `RuleEngine`,
  `RootCauseAnalyzer`, `PriorityEngine`, `ProcessingChainRecommender`, and
  `PluginParameterGenerator` into the Knowledge layer.

---

## P2 — Sprint 8 — Memory & Personalization

Status: ✅ Completed

Description

Sprint 8 introduced an isolated Memory layer that stores user and project
preferences. Memory never replaces Knowledge; it only overrides Knowledge values
when an explicit preference exists, and only through `MemoryResolver`.

Completed

- Memory models (`brain.memory.models`) with `UserProfile`, `ProjectProfile`, and
  `MemoryBundle`.
- Memory loader (`brain.memory.loader`) for YAML master bundle and inline
  dictionary loading.
- Memory registry (`brain.memory.registry`) with lightweight validation.
- Memory resolver (`brain.memory.resolver`) that overlays memory preferences on
  top of an optional `KnowledgeResolver`.
- Memory service (`brain.memory.service`) as a lazy-loading facade that can be
  wired to a `KnowledgeService`.
- Default empty configuration under `configs/memory/`.
- Supported preferences: preferred loudness by platform, preferred plugin brands,
  preferred genres, preferred processing order, preferred export targets,
  preferred true peak, preferred dynamic range minimum, and project context.
- Deterministic unit tests for loader, registry, resolver, and service.

Files

- brain/memory/models.py
- brain/memory/loader.py
- brain/memory/registry.py
- brain/memory/resolver.py
- brain/memory/service.py
- brain/memory/__init__.py
- configs/memory/
- tests/test_memory_*.py

Remaining Notes

- Memory is optional and isolated; no business logic module consumes it yet.
- Continuous learning / persistent storage updates are future work (Sprint 10+).

---

## P2 — Sprint 9 — Evaluation & Benchmark

Status: ✅ Completed

Description

Sprint 9 introduced an isolated Evaluation layer that measures the quality and
consistency of SoundBrain outputs without changing business logic.

Completed

- Evaluation models (`brain.evaluation.models`) for metrics, results, and
  benchmark cases.
- Evaluation metrics (`brain.evaluation.metrics`) for:
  - analysis quality
  - recommendation consistency
  - confidence evaluation
  - reference matching
  - plugin recommendation evaluation
  - knowledge resolution evaluation
- Score aggregation (`brain.evaluation.scoring`) with weighted overall score and
  pass/fail threshold.
- Benchmark runner (`brain.evaluation.benchmark`) for multi-case evaluation.
- Report exporter (`brain.evaluation.report`) for JSON output.
- Evaluation service (`brain.evaluation.service`) as a facade consuming existing
  outputs only.
- Deterministic unit tests for metrics, scoring, benchmark, and service.
- Example evaluation report generated at `reports/evaluation_example.json`.

Files

- brain/evaluation/models.py
- brain/evaluation/metrics.py
- brain/evaluation/scoring.py
- brain/evaluation/benchmark.py
- brain/evaluation/report.py
- brain/evaluation/service.py
- brain/evaluation/__init__.py
- tests/test_evaluation_*.py
- reports/evaluation_example.json

Remaining Notes

- Evaluation is optional and isolated; no business logic consumes it yet.
- Future work: integration with CI pipeline, regression thresholds, and golden
  dataset evaluation.

---

## P2 — Sprint 10 — Workflow Integration Contracts

Status: ✅ Completed

Description

Sprint 10 delivered deterministic placeholder workflow integration contracts for five
DAWs: Ableton Live, REAPER, Cubase, FL Studio, and Studio One.

Completed

- Created `brain.integration` package with `WorkflowAdapter`, `BaseWorkflowAdapter`,
  `ExportRequest`, `ExportResult`, `WorkflowSession`, and `DAWCapability` models.
- Implemented five concrete adapters as subclasses of `BaseWorkflowAdapter`.
- Implemented `AdapterFactory` with auto-registration, `get(name)`, `list()`, and `default()`.
- Added deterministic unit tests covering factory registration, every adapter's
  capabilities, all four export methods, empty-request handling, and the no-DAW-call rule.
- Generated example export package under `outputs/integration_example/`.
- Verified no OSC, MIDI, ReaScript, Python Remote API, or filesystem automation is used.

Files

- brain/integration/__init__.py (new)
- brain/integration/models.py (new)
- brain/integration/base.py (new)
- brain/integration/factory.py (new)
- brain/integration/ableton.py (new)
- brain/integration/reaper.py (new)
- brain/integration/cubase.py (new)
- brain/integration/flstudio.py (new)
- brain/integration/studio_one.py (new)
- tests/test_integration_factory.py (new)
- tests/test_integration_adapters.py (new)
- outputs/integration_example/ (generated)

Remaining Notes

- Adapters currently write placeholder JSON and Markdown files. Real VST3/AU preset
  export and validation are future work (Sprint 11+).
- Actual DAW communication (OSC, MIDI, ReaScript, remote APIs) is explicitly out of
  scope for the contract sprint.

---

## P2 — Sprint 11 — AI Provider Layer

Status: ✅ Completed

Description

Sprint 11 introduced an isolated AI Provider layer that abstracts all LLM interactions
behind a common `BaseAIProvider` interface. The reasoning engine now depends only on
this abstraction, not on a specific provider or manager.

Completed

- Created `brain.providers` package with `BaseAIProvider`, `GenerateRequest`,
  `GenerateResponse`, `ProviderRegistry`, `ProviderFactory`, and `ProviderService`.
- Implemented `MockProvider` for deterministic tests and offline development.
- Implemented `QwenProvider` using the existing `brain.llm.qwen` integration with lazy
  transformers import so the provider package remains lightweight at import time.
- Implemented `GeminiProvider`, `OpenAIProvider`, and `LocalProvider` stubs that raise
  `NotImplementedError` for future backends.
- Registered all providers in `ProviderFactory` with lazy default registration.
- Made `QwenProvider` the default production provider via `ProviderFactory.default()`
  and updated `LLMConfig.provider` default from `lmstudio` to `qwen`.
- Rewired `LLMReasoningProvider` to depend only on `BaseAIProvider` and route calls
  through the standard `GenerateRequest` / `GenerateResponse` contract.
- Added deterministic tests for factory, registry, mock provider, service facade, and
  reasoning integration.
- Verified that `brain.providers` can be imported without loading torch or transformers.

Files

- brain/providers/__init__.py (new)
- brain/providers/models.py (new)
- brain/providers/base.py (new)
- brain/providers/mock.py (new)
- brain/providers/qwen.py (new)
- brain/providers/gemini.py (new)
- brain/providers/openai.py (new)
- brain/providers/local.py (new)
- brain/providers/registry.py (new)
- brain/providers/factory.py (new)
- brain/providers/service.py (new)
- brain/reasoning/engine.py (modified)
- brain/infrastructure/config/models.py (modified)
- tests/test_providers_factory.py (new)
- tests/test_providers_mock.py (new)
- tests/test_providers_reasoning.py (new)

Remaining Notes

- `GeminiProvider`, `OpenAIProvider`, and `LocalProvider` are stubs. Real HTTP client
  integration and local backend support are future work (Sprint 12+).
- Qwen model must be available locally for `QwenProvider.generate()` to succeed; the
  provider layer itself does not download models.

---

## Blockers for Sprint 12

-   [ ] Real HTTP LLM providers (Gemini/OpenAI) — P2
-   [ ] Local inference backend abstraction (llama.cpp/ollama) — P2
-   [ ] Real Qwen model availability / validation test — P2 (carry-over)
-   [ ] Real Whisper provider / test — P2 (carry-over)
-   [ ] CUDA validation — P2 (carry-over)

---

## Environment Note — Pytest Temporary Directory on Windows

pytest defaults to `C:\Users\<user>\AppData\Local\Temp\pytest-of-<user>`, which
can raise `PermissionError` on Windows when existing directories are protected.
`pytest.ini` now sets `--basetemp=tmp` so temporary directories are created under
the repository root, making reference pipeline tests reproducible on Windows.

Files

- pytest.ini
- tmp/ (created by pytest, ignored by Git)

---

## Environment Note — PyArrow Faulthandler Noise on Windows

When pytest's faulthandler plugin is active, importing `pyarrow` (via
`pandas` → `sklearn` → `transformers`) prints a non-fatal
`Windows fatal exception: access violation` traceback during test collection.
All tests still pass and the process continues. Running with
`-p no:faulthandler` suppresses the noise. This is a Windows/pyarrow wheel
quirk, not a SoundBrain bug.

Files

- N/A (environment)

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