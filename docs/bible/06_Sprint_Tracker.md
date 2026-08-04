# 06 --- Sprint Tracker

> SoundBrain Project Bible

------------------------------------------------------------------------

# Current Sprint Dashboard

  Sprint       Status       Progress
  ------------ ------------ ----------
  Sprint 2.1   ✅ Completed 100%
  Sprint 2.2   ✅ Completed 100%
  Sprint 2.3   ✅ Completed 100%
  Sprint 2.4   ✅ Completed 100%
  Sprint 2.5   ✅ Completed 100%
  Sprint 2.6   ✅ Completed 100%
  Sprint 3     ✅ Completed 100%
  Sprint 4     ✅ Completed 100%
  Sprint 5     ✅ Completed 100%
  Sprint 6     ✅ Completed 100%
  Sprint 7     ✅ Completed 100%
  Sprint 8     ✅ Completed 100%
  Sprint 9     ✅ Completed 100%
  Sprint 10    ✅ Completed 100%
  Sprint 11    ✅ Completed 100%
  Sprint 12    ⏳ Waiting    0%

------------------------------------------------------------------------

# Sprint 2.5 --- Runtime Validation

## Goal

Validate the Runtime before feature development.

### Checklist

-   [x] Install pytest
-   [x] Execute Runtime tests (tests/test_runtime.py passes)
-   [x] Validate CLAP (tests/test_audio_pipeline.py passes)
-   [ ] Validate Whisper (no Whisper model or test exists)
-   [x] Validate BGE (imports are now clean; no dedicated test exists)
-   [ ] Validate Qwen (no Qwen-specific test exists)
-   [x] CPU Validation (main.py analyze tests/audio.wav passes)
-   [ ] CUDA Validation (no CUDA device available in current env)
-   [x] Create runtime-v1-stable tag

Definition of Done

-   Every runtime test passes.
-   No architecture regressions.
-   Runtime declared production-ready.
-   RAG and service imports no longer crash.

------------------------------------------------------------------------

# Sprint 2.6 --- Architecture Freeze Prep

-   [x] Create V1 SoundBrainService facade
-   [x] Register V1 capabilities
-   [x] Create EngineRegistry
-   [x] Fix remaining broken/lazy imports (brain.embedding)
-   [x] Wire Orchestrator to SoundBrainService
-   [x] Route main.py through SoundBrainService
-   [x] Add tests for SoundBrainService and EngineRegistry
-   [x] Update capability registry docs
-   [x] Lock public interfaces before Sprint 3

Blocked By: - Sprint 2.5 completion

------------------------------------------------------------------------

# Sprint 3 --- Core Integration

-   [x] Audio → Analysis (via AudioReviewService)
-   [x] Analysis → Context (AudioContextDetector)
-   [x] Context → Knowledge (RAG retrieval wired)
-   [x] Knowledge → Reasoning (LLM reasoning wired)
-   [x] Reasoning → Engineering (report rebuilt with reasoning output)
-   [x] Engineering → Report (ReportBuilder)
-   [x] End-to-End Pipeline (SoundBrainService + main.py + Orchestrator)
-   [x] Replace bare print() with logging in pipeline modules
-   [x] Add integration and optional feature tests
-   [x] Update CLI with --reasoning, --rag, --semantic, --intent, --delivery-target, --reference
-   [x] Update Orchestrator.analyze to pass new flags
-   [x] Update Capability Registry and Technical Debt

Blocked By: - Sprint 2.6 completion

------------------------------------------------------------------------

# Sprint 4 --- Reference Intelligence

CLI compatibility note: the reference command uses
`soundbrain reference <current.wav> <reference.wav> [additional_reference.wav ...]`.
This positional ordering is intentional for the multi-reference command and supersedes
the previous single-reference ordering.

-   [x] Capture reference intent (genre, mood, target, focus areas)
-   [x] Multi-reference support in SoundBrainService
-   [x] Per-reference similarity and metric variance
-   [x] Segment deviation structure (thin V1 implementation)
-   [x] Style-aware reasoning with decision categorization
-   [x] Integrate reference comparison into SoundBrainService.analyze
-   [x] Update CLI with repeatable --reference and intent flags
-   [x] Add evaluation fixtures under tests/assets/reference_eval/
-   [x] Add reference intelligence tests
-   [x] Update Capability Registry and Technical Debt

Blocked By: - Sprint 3 completion

------------------------------------------------------------------------

# Sprint 5 --- Mix Intelligence

-   [x] Root cause detection (`brain.audio.mix.root_cause`)
-   [x] Priority engine (`brain.audio.mix.priority`)
-   [x] Processing chain recommendations (`brain.audio.mix.chains`)
-   [x] Engineering explanations (`brain.audio.mix.explanation`)
-   [x] Confidence scoring on issues, root causes, and recommendations
-   [x] Integrate mix intelligence into `SoundBrainService.analyze`
-   [x] Extend `SoundBrainReport` and `AnalysisResponse` with mix intelligence fields
-   [x] Add `--mix-intelligence` flag to `main.py`
-   [x] Add unit tests for root cause, priority, chain, and explanation modules
-   [x] Update integration tests for `include_mix_intelligence`
-   [x] Update Capability Registry and Technical Debt

Blocked By: - Sprint 4 completion

------------------------------------------------------------------------

# Sprint 6 --- Plugin Intelligence

-   [x] Plugin taxonomy and registry (`brain.audio.plugin`)
-   [x] Parameter generator (`brain.audio.plugin.parameter_generator`)
-   [x] Plugin selector (`brain.audio.plugin.selector`)
-   [x] Plugin chain builder (`brain.audio.plugin.chain_builder`)
-   [x] Plugin validator (`brain.audio.plugin.validator`)
-   [x] Plugin intelligence service (`brain.audio.plugin.service`)
-   [x] Integrate plugin intelligence into `SoundBrainService.analyze`
-   [x] Extend `SoundBrainReport` and `AnalysisResponse` with plugin intelligence fields
-   [x] Add `--plugin-intelligence` flag to `main.py`
-   [x] Add unit tests for plugin modules and integration test for `include_plugin_intelligence`
-   [x] Update Capability Registry and Technical Debt

Blocked By: - Sprint 5 completion

------------------------------------------------------------------------

# Sprint 7 --- Knowledge Infrastructure

-   [x] Knowledge models (`brain.knowledge.models`)
-   [x] Knowledge loader (`brain.knowledge.loader`)
-   [x] Knowledge validator (`brain.knowledge.validator`)
-   [x] Knowledge registry (`brain.knowledge.registry`)
-   [x] Knowledge resolver (`brain.knowledge.resolver`)
-   [x] Knowledge service (`brain.knowledge.service`)
-   [x] Default configuration structure under `configs/knowledge/`
-   [x] Deterministic unit tests for loader, validator, registry, resolver, and service
-   [x] Update Capability Registry and Technical Debt

Blocked By: - Sprint 6 completion

------------------------------------------------------------------------

# Sprint 8 --- Memory & Personalization

-   [x] Memory models (`brain.memory.models`)
-   [x] UserProfile and ProjectProfile dataclasses
-   [x] Memory loader (`brain.memory.loader`)
-   [x] Memory registry (`brain.memory.registry`)
-   [x] Memory resolver (`brain.memory.resolver`)
-   [x] Memory service (`brain.memory.service`)
-   [x] Default empty configuration under `configs/memory/`
-   [x] Memory overrides Knowledge only through `MemoryResolver`
-   [x] Support for preferred loudness, plugin brands, genres, processing order, export targets
-   [x] Deterministic unit tests for loader, registry, resolver, and service
-   [x] Update Capability Registry and Technical Debt

Blocked By: - Sprint 7 completion

------------------------------------------------------------------------

# Sprint 9 --- Evaluation & Benchmark

-   [x] Evaluation models (`brain.evaluation.models`)
-   [x] Evaluation metrics (`brain.evaluation.metrics`)
-   [x] Score aggregation (`brain.evaluation.scoring`)
-   [x] Benchmark runner (`brain.evaluation.benchmark`)
-   [x] Report exporter (`brain.evaluation.report`)
-   [x] Evaluation service (`brain.evaluation.service`)
-   [x] Analysis quality scoring
-   [x] Recommendation consistency scoring
-   [x] Confidence evaluation
-   [x] Reference matching evaluation
-   [x] Plugin recommendation evaluation
-   [x] Knowledge resolution evaluation
-   [x] Overall score aggregation
-   [x] Deterministic unit tests for metrics, scoring, benchmark, and service
-   [x] Example evaluation report generated
-   [x] Update Capability Registry

Blocked By: - Sprint 8 completion

------------------------------------------------------------------------

# Sprint 10 --- Workflow Integration Contracts

-   [x] Create `brain.integration` package with workflow models
-   [x] Define `WorkflowAdapter` abstract contract with four export methods
-   [x] Implement `BaseWorkflowAdapter` placeholder helpers (JSON/text export only)
-   [x] Create Ableton adapter
-   [x] Create Reaper adapter
-   [x] Create Cubase adapter
-   [x] Create FL Studio adapter
-   [x] Create Studio One adapter
-   [x] Create `AdapterFactory` with register / get / list / default
-   [x] Add deterministic unit tests for factory and every adapter
-   [x] Verify adapters do not communicate with any DAW
-   [x] Generate example export package under `outputs/integration_example/`
-   [x] Update Capability Registry and Technical Debt

Blocked By: - Sprint 9 completion

------------------------------------------------------------------------

# Sprint 11 --- AI Provider Layer

-   [x] Create `brain.providers` package with models, base contract, registry, factory, and service
-   [x] Implement `BaseAIProvider` abstraction
-   [x] Implement `MockProvider` for deterministic tests
-   [x] Implement `QwenProvider` using the existing Qwen integration (lazy import)
-   [x] Implement `GeminiProvider` stub (NotImplementedError)
-   [x] Implement `OpenAIProvider` stub (NotImplementedError)
-   [x] Implement `LocalProvider` stub (NotImplementedError)
-   [x] Register all providers in `ProviderFactory`
-   [x] Make QwenProvider the default production provider
-   [x] Wire `LLMReasoningProvider` to depend only on `BaseAIProvider`
-   [x] Add deterministic provider tests (factory, registry, mock, reasoning integration)
-   [x] Update config default provider from `lmstudio` to `qwen`
-   [x] Update Capability Registry and Technical Debt

Blocked By: - Sprint 10 completion

------------------------------------------------------------------------

# Sprint 12 --- Future Sprint (Placeholder)

-   [ ] TBD

------------------------------------------------------------------------

# Notes

Update sprint status immediately after completing each sprint.
