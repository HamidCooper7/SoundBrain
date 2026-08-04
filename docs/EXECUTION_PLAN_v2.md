# SoundBrain Execution Plan

Version: 2.0

Status: Working plan

---

## Purpose

This document turns the V1-to-V5 product roadmap into an incremental
implementation plan for the current repository. It preserves the existing
audio core and prioritizes connecting, validating, and productizing it before
introducing larger research areas.

The status below is a repository snapshot. A component marked **verify** may
already work in the local development environment and needs an explicit
repeatable acceptance test rather than a rewrite.

---

## Current Asset Map

| Domain | Existing assets | Status |
| --- | --- | --- |
| Audio I/O | `AudioIOService`, `AudioData`, SoundFile backend | implemented |
| DSP analysis | Tempo, pitch, key, LUFS, dynamics, stereo, phase, spectral metrics | implemented |
| Audio context | Rules plus semantic classifier and CLAP-backed intelligence | implemented / verify |
| Engineering analysis | Rule engine, issues, recommendations, score and report objects | implemented |
| Reference comparison | Metric comparator, scoring and comparison report models | implemented / verify |
| Mix intelligence | Root-cause analysis, priority engine, processing chain, explanations | implemented / verify |
| Audio embeddings | CLAP provider, registry, factory, runtime cache | implemented / verify |
| Audio memory/search | Vector-backed audio indexing and text/audio retrieval | implemented / verify |
| Knowledge RAG | Loading, splitting, retrieval, reranking and public service | implemented / verify |
| LLM reasoning | Prompt builder, parser, guards and LM Studio provider | implemented / verify |
| Orchestration | State, planner, router, pipeline engine and selected stages | partial integration |
| Reports/export | Structured report builder, validator and JSON/export utilities | implemented / verify |
| Product interface | CLI is the supported V1 surface; API and desktop UI are not yet defined | CLI implemented |

---

## Product Boundary for V1

V1 should be a reliable **professional audio review assistant**, not an
autonomous mixer. A user gives SoundBrain a source track, optional reference
track, engineering intent and delivery target. SoundBrain returns an auditable
report with measurements, context, observations, confidence, evidence and
non-destructive recommendations.

### V1 In Scope

- Analyze a local audio file.
- Compare it against an optional reference track.
- Retrieve relevant engineering knowledge with source references.
- Generate structured, guarded reasoning.
- Build deterministic mix intelligence (root causes, priorities, chain, explanations).
- Export a JSON report and a human-readable report.
- Make every recommendation traceable to measured evidence or retrieved
  knowledge.

### V1 Out of Scope

- Automatic processing of audio.
- DAW or plugin control.
- Mixing/mastering changes without explicit user review.
- Music generation.
- Multi-agent autonomy.

---

## Canonical V1 Workflow

```text
Input request + audio + optional reference + intent
    -> validation and canonical AudioData
    -> deterministic audio analysis
    -> context and semantic understanding
    -> optional reference comparison
    -> engineering-rule evaluation
    -> optional mix intelligence
    -> knowledge retrieval
    -> structured LLM reasoning
    -> validation, confidence and evidence checks
    -> report/export
```

`AudioData`, `AnalysisResult`, `AudioContext`, `EngineerResult`,
`ComparisonResult`, `MixIntelligenceResult`, `ReasoningResult` and
`SoundBrainReport` should be the stable contracts between these stages.
Providers and UI code must not leak into these contracts.

---

## Phase 0: Establish a Reproducible Baseline

**Status:** Completed

**Goal:** make the current working system reproducible without changing its
audio logic.

### Work

1. Add one supported environment definition (`pyproject.toml` or a curated
   root `requirements.txt`) with pinned direct dependencies.
2. Add documented configuration for LM Studio, model names, vector database
   paths and hardware selection. Keep secrets outside Git.
3. Define a supported Python version and an install/run command.
4. Separate source code, sample fixtures, generated reports, local indexes and
   model caches in the repository policy.
5. Finish the documentation migration from legacy names to `_v2` names as one
   intentional Git change.

### Acceptance Criteria

- A clean machine can create an environment and run a deterministic DSP-only
  analysis without downloading or manually locating project files.
- Optional services (LM Studio, CLAP, reranker) fail with an actionable
  message, not an import-time crash.
- A newcomer can identify the supported entry point from the README.

---

## Phase 1: Define the Supported Application Contract

**Status:** Completed

**Goal:** expose the existing core through one stable request/response API.

### Work

1. Define an `AnalysisRequest` contract: source path, optional reference path,
   user question, intent, delivery target and feature flags.
2. Define a `SoundBrainService` facade that returns a single structured result.
3. Make the facade the only supported end-to-end entry point; keep experiments
   and one-off scripts separate.
4. Add an explicit composition root where backends, models, vector stores and
   services are created and injected.
5. Add typed domain errors for invalid audio, unavailable model, unavailable
   knowledge base and invalid report output.

### Acceptance Criteria

- One Python call can run the V1 workflow with deterministic services only.
- Optional services can be substituted with test doubles.
- Callers do not need to import individual analysis, RAG or LLM modules.

---

## Phase 2: Complete and Verify Pipeline Integration

**Status:** Completed

**Goal:** ensure the orchestration state represents the real workflow and no
planned work is silently lost.

### Work

1. Decide whether `orchestration` is the V1 production path or an experimental
   agent path. Do not maintain two competing public pipelines.
2. Register an implementation for every route that can be selected, or make
   unsupported routes explicit failures with capability metadata.
3. Pass `audio`, `reference`, intent and output preferences through the state;
   the current state has room for them but needs a defined contract.
4. Connect audio analysis, context, engineer, comparison, RAG, reasoning and
   reporting stages in the canonical V1 order.
5. Replace console-only diagnostics in production stages with structured
   logging and request-scoped progress events.
6. Verify compatibility at the LLM service/provider boundary and retain one
   canonical generation interface.

### Acceptance Criteria

- Each selected stage produces a documented state update.
- The pipeline records skipped optional capabilities and their reason.
- A request cannot claim a report or recommendation when the required stages
  did not run.
- Every final report identifies analysis and model/provider versions.

---

## Phase 3: Make Reasoning Auditable

**Status:** Completed

**Goal:** enforce the project principle: observation -> evidence -> reasoning
-> confidence -> recommendation.

### Work

1. Define a strict structured schema for reasoning output.
2. Attach metric names, values and source document/page references to each
   conclusion where applicable.
3. Separate deterministic rule recommendations from LLM explanations.
4. Add confidence sources: measurement validity, classification confidence,
   retrieval quality and model confidence/uncertainty.
5. Add guards for unsupported claims, unsafe automation language and malformed
   structured output.
6. Store the complete decision trace inside the JSON report.

### Acceptance Criteria

- A reviewer can trace every recommendation to one or more facts.
- The system says "insufficient evidence" when the required context is absent.
- LLM unavailability still produces a valid deterministic engineering report.

---

## Phase 4: Reference Intelligence and Mix Intelligence

**Status:** Completed

**Goal:** promote comparison from raw deltas to intent-aware guidance and add
rule-based mix intelligence to the V1 report.

### Work

1. Capture reference intent: genre, playback target, loudness goal and desired
   relationship to the source.
2. Segment comparisons by meaningful time windows rather than relying only on
   one global average (thin V1 implementation).
3. Categorize differences as likely technical issue, deliberate stylistic
   difference or insufficient evidence.
4. Weight comparison metrics using context and psychoacoustic relevance.
5. Build reference-specific prompts from structured comparison evidence.
6. Create a curated reference evaluation set with expected conclusions.
7. Add root-cause detection, priority engine, processing chain recommendation
   and deterministic explanation generation to the V1 report.
8. Surface mix intelligence through `SoundBrainService`, `main.py` and the JSON
   report schema.

### Acceptance Criteria

- The system never labels a numerical difference as an error without context.
- A reference report clearly separates similarities, differences and suggested
  experiments.
- Results are comparable across a fixed evaluation set.
- Mix intelligence is deterministic, tested and degrades gracefully when the
  analysis is inconclusive.

---

## Phase 5: Quality, Evaluation and Release Readiness

**Status:** Next

**Goal:** turn local success into a maintainable release candidate.

### Test Pyramid

| Level | What to test | External dependencies |
| --- | --- | --- |
| Unit | DSP adapters, rules, parsers, validators, models | none |
| Contract | providers, vector store, report/export contracts | controlled fixtures |
| Integration | supported V1 workflow with known audio | local optional services |
| Evaluation | quality of recommendations and references | versioned audio/reference set |
| Smoke | CLI/API and a single real model request | explicitly opt-in |

### Work

1. Retain useful manual scripts but move them to `scripts/` or mark them as
   smoke tests; use assertions for automated regression tests.
2. Add fixtures for mono/stereo, silence, short files, invalid files and known
   metric values.
3. Add one end-to-end deterministic test and one opt-in model-backed smoke
   test.
4. Add formatting, linting, type checking and a minimal CI workflow.
5. Establish report schema versioning and backward-compatible migrations.
6. Add benchmark timing/memory measurements for analysis, embeddings and RAG.

### Acceptance Criteria

- Core tests run without models, network access or a GPU.
- Model-backed tests are clearly labelled and not required for ordinary CI.
- Every release candidate has a recorded quality evaluation set and known
  limitations.

---

## Phase 6: Product Surface

**Status:** Planned

**Goal:** make V1 usable by an audio engineer.

### Recommended Order

1. CLI: `soundbrain analyze`, `compare`, `ask` and `export`.
2. Local API once the CLI contract is stable.
3. Desktop UI once the API has a stable asynchronous job/progress model.

### UX Requirements

- Show what was analyzed and which optional capabilities ran.
- Show evidence and confidence beside every recommendation.
- Require explicit user confirmation before any future action layer.
- Preserve source audio; V1 is analysis-only.

---

## V2 Through V5 Gates

| Version | Start only when | First concrete deliverable |
| --- | --- | --- |
| V2 Perceptual Intelligence | V1 reports are stable and evaluated | masking, translation and loudness-perception models with validation set |
| V3 Autonomous Mixing | V2 recommendations are trustworthy and reversible | proposed processing chain with human approval, no automatic execution |
| V4 Audio Foundation Model | representation and data strategy are proven | evaluated multimodal embedding/retrieval experiment |
| V5 Agent OS | action contracts and safety controls are mature | bounded multi-agent review workflow with audit trail |

---

## Priority Backlog

### Now

1. Phase 5 quality gates and release readiness.
2. Evaluation dataset for reference and mix intelligence recommendations.
3. Report schema versioning and backward-compatible migrations.
4. Baseline packaging and deterministic CI.

### Next

1. Plugin intelligence and actionable parameter recommendations.
2. Structured, evidence-linked reasoning output.
3. API and asynchronous job/progress model.

### Later

1. Psychoacoustics.
2. DAW/plugin integrations.
3. Agent collaboration and autonomous actions.
4. Generation and foundation-model research.

---

## First Implementation Slice

The most valuable first slice is **Analyze One Track**:

1. Validate and load one audio file.
2. Run the existing DSP analysis, context detector and engineering rules.
3. Produce a schema-versioned JSON report without requiring an LLM.
4. Add optional RAG/reasoning enrichment behind a feature flag.
5. Verify the output using one known fixture and one real user track.

This slice proves the product contract, preserves the existing core and gives
every later capability a stable place to connect.
