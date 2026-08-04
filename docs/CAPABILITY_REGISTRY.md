# SoundBrain Capability Registry

Version: 1.0

Status: ACTIVE

---

# Purpose

This document defines every capability supported by SoundBrain.

A capability is a discrete feature that can be discovered, validated, enabled, disabled, tested, and composed into larger workflows.

Capabilities provide the contract between architecture and implementation.

---

# Capability Lifecycle

Planned

↓

Implemented

↓

Verified

↓

Production

↓

Deprecated

↓

Removed

---

# Capability Categories

## Infrastructure

- Runtime
- Configuration
- Dependency Injection
- Logging
- Cache
- Model Repository

---

## Audio

- Audio Loading
- Audio Validation
- Feature Extraction
- DSP Metrics
- Audio Context
- Audio Comparison

---

## AI

- Embeddings
- Semantic Understanding
- Reasoning
- Prompt Building
- Validation

---

## Knowledge

- RAG
- Vector Search
- Knowledge Base
- Knowledge Graph

---

## Reports

- JSON Export
- Human Report
- Validation
- Versioning

---

## Product

- CLI
- API
- Desktop UI

---

# Capability Status

| Capability | Status |
|------------|--------|
| Runtime | Production |
| Audio Loading | Production |
| DSP Analysis | Production |
| Audio Context | Production |
| Engineering Analysis | Production |
| CLAP Embeddings | Verified |
| Reference Comparison | Production |
| RAG Retrieval | Implemented |
| LLM Reasoning | Implemented |
| Report Generation | Production |
| Service Facade | Production |
| Engine Registry | Production |
| Orchestration | Implemented |
| AI Provider Layer | Implemented |
| Audio Intelligence | Production |
| Reference AI | Production |
| Mix Intelligence | Production |
| Plugin Intelligence | Production |
| Knowledge Infrastructure | Implemented |
| Memory & Personalization | Implemented |
| Evaluation & Benchmark | Implemented |
| DAW Integration | Implemented |
| CLI | Production |
| API | Planned |
| Desktop UI | Planned |

---

# Workflow Integration Contracts (Sprint 10)

## Adapters

- Ableton Live
- REAPER
- Steinberg Cubase
- FL Studio
- PreSonus Studio One

## Export Contracts

- `export_analysis` — JSON summary of analysis results
- `export_processing_chain` — JSON + text processing chain notes
- `export_plugin_recommendations` — JSON plugin recommendations with parameters
- `export_report` — JSON + Markdown report export

## Rules

- Adapters are pure contracts in this sprint.
- No OSC, MIDI, ReaScript, Python Remote API, or filesystem automation is performed.
- All exports are deterministic placeholder files written to `output_dir/<adapter_name>/`.
- Brands appear only in registry data, never in decision logic.

---

# AI Provider Layer (Sprint 11)

## Providers

- `BaseAIProvider` — abstract contract for all AI providers
- `MockProvider` — deterministic test provider
- `QwenProvider` — local Qwen LLM provider (default production provider)
- `GeminiProvider` — Google Gemini stub
- `OpenAIProvider` — OpenAI-compatible API stub
- `LocalProvider` — future local inference backend stub

## Contracts

- `GenerateRequest` — system/user prompts, max tokens, temperature, top-p
- `GenerateResponse` — generated text, provider name, confidence, token usage metadata

## Services

- `ProviderRegistry` — register and lookup provider instances
- `ProviderFactory` — lazy registration and default provider resolution
- `ProviderService` — application facade for generation calls

## Rules

- Business logic depends only on `BaseAIProvider`.
- No provider-specific logic outside provider implementations.
- Heavy backends (transformers, torch) are loaded lazily inside `generate()`.
- Reasoning engine routes through `LLMReasoningProvider` + `BaseAIProvider`.

---

# Future

Future capabilities should be added here before implementation begins.

---

# Final Rule

Every new feature must become a registered capability before entering production.
