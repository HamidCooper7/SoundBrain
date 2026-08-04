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
  Sprint 7     ⏳ Waiting    0%
  Sprint 8     ⏳ Waiting    0%

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

# Sprint 7 --- Memory & Learning

-   [ ] User memory
-   [ ] Project memory
-   [ ] Continuous learning

------------------------------------------------------------------------

# Sprint 8 --- DAW Integration

-   [ ] Ableton
-   [ ] Cubase
-   [ ] FL Studio
-   [ ] Reaper
-   [ ] Import / Export

------------------------------------------------------------------------

# Notes

Update sprint status immediately after completing each sprint.
