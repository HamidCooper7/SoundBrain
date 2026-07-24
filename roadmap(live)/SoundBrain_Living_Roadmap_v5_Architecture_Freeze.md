# SoundBrain Living Roadmap v5 --- Architecture Freeze Edition

> **Status:** FINAL (Living)
>
> This document becomes the single source of truth for SoundBrain. From
> this point onward, only task status should change unless a real
> architectural limitation is discovered.

------------------------------------------------------------------------

# Executive Dashboard

  Area                    Status        Progress
  ----------------------- ----------- ----------
  Infrastructure          ✅ Stable          95%
  Runtime Validation      🚧 Active          15%
  Platform Finalization   🆕 Next             0%
  Core Product            🔒 Locked          70%
  Vision V5               🚀 Future          25%

Current Sprint: **2.5 Runtime Validation**

Next Gate: **Architecture Freeze**

------------------------------------------------------------------------

# Target Architecture

``` text
User
 ↓
API Layer (CLI / Python SDK / MCP / Desktop / Future REST)
 ↓
Task
 ↓
Planner
 ↓
Task Graph
 ↓
Workflow Graph
 ↓
Capability Registry
 ↓
Runtime Scheduler
 ↓
Resource Manager
 ↓
Runtime
 ├── Repository
 ├── Loader
 ├── Download Manager
 ├── Verify Manager
 ├── Cache Manager
 ├── Placement Planner
 ├── Device Profiler
 ├── Health Monitor
 └── Telemetry
 ↓
Engine Registry
 ↓
Engine
 ↓
Backend
 ↓
Provider
 ↓
Model
```

------------------------------------------------------------------------

# Architecture Principles

-   Runtime owns execution, never business logic.
-   Business logic never loads models directly.
-   Everything is capability-driven.
-   Planner decides intent.
-   Scheduler decides execution.
-   Resource Manager decides placement.
-   Repository owns model resolution.
-   Engines are backend-agnostic.
-   Providers are replaceable.
-   Models are replaceable.
-   Every component has a single responsibility.
-   Observability is mandatory.

------------------------------------------------------------------------

# Engine Lifecycle

Download → Verify → Register → Warmup → Ready → Running → Idle → Evict →
Unload

------------------------------------------------------------------------

# Capability Layer

  Capability               Typical Engine
  ------------------------ ------------------
  Embedding                CLAP
  Transcription            Whisper
  Audio Analysis           Analysis Engine
  Reference Intelligence   Reference Engine
  Reasoning                Qwen
  Reporting                Report Engine

------------------------------------------------------------------------

# Provider Layer

-   HuggingFace
-   Ollama
-   OpenAI
-   Anthropic
-   Gemini
-   GGUF
-   MLX
-   vLLM

------------------------------------------------------------------------

# Backend Layer

-   CUDA
-   CPU
-   DirectML
-   Metal
-   TensorRT
-   OpenVINO

------------------------------------------------------------------------

# Memory Hierarchy

Disk ↓ RAM ↓ VRAM

Policies: - Hot Cache - Warm Cache - Cold Storage - Residency -
Prefetch - Eviction

------------------------------------------------------------------------

# Sprint Task List

## Sprint 2.5 --- Runtime Validation

Status: 🚧

-   [ ] Runtime Tests
-   [ ] CLAP Validation
-   [ ] Whisper Validation
-   [ ] BGE Validation
-   [ ] Qwen Validation
-   [ ] CPU Validation
-   [ ] CUDA Validation
-   [ ] Benchmark
-   [ ] runtime-v1-stable Tag

Definition of Done: - All tests pass. - Runtime stable.

------------------------------------------------------------------------

## Sprint 2.6 --- Platform Finalization

Status: 🆕

Runtime - ☐ Runtime Scheduler - ☐ Resource Manager - ☐ Download
Manager - ☐ Verify Manager - ☐ Cache Manager - ☐ Placement Planner - ☐
Device Profiler - ☐ Telemetry - ☐ Health Monitor

Platform - ☐ Capability Registry - ☐ Engine Registry - ☐ Workflow
Graph - ☐ Task Graph - ☐ Dependency Cleanup - ☐ Architecture Freeze

------------------------------------------------------------------------

## Sprint 3

-   [ ] End-to-End Pipeline
-   [ ] Analysis
-   [ ] Context
-   [ ] RAG
-   [ ] Reasoning
-   [ ] Engineering
-   [ ] Reporting

## Sprint 4

-   [ ] Multi Reference
-   [ ] Genre Intelligence
-   [ ] Frequency Reasoning
-   [ ] Stereo Reasoning
-   [ ] Dynamics Reasoning

## Sprint 5

-   [ ] Root Cause Detection
-   [ ] Recommendation Engine
-   [ ] Plugin Chains
-   [ ] Confidence Score

## Sprint 6

-   [ ] FabFilter
-   [ ] Waves
-   [ ] SSL
-   [ ] UAD
-   [ ] Ozone

## Sprint 7

-   [ ] Project Memory
-   [ ] User Memory
-   [ ] Genre Memory
-   [ ] Continuous Learning

## Sprint 8

-   [ ] MCP
-   [ ] Python SDK
-   [ ] VS Code
-   [ ] Claude Code
-   [ ] Cursor
-   [ ] Public API

## Sprint 9

-   [ ] Desktop
-   [ ] React
-   [ ] Tauri

------------------------------------------------------------------------

# Observability

Track: - Startup Time - Model Load Time - Cache Hit Ratio - RAM - VRAM -
CPU - GPU - Scheduler Latency - Pipeline Latency - Download Time -
Warmup Time

------------------------------------------------------------------------

# Decision Log

2026-07-23 - ✅ Capability-first architecture - ✅ Runtime Scheduler -
✅ Resource Manager - ✅ Memory Tiering - ✅ Telemetry - ✅ Architecture
Freeze after Sprint 2.6

------------------------------------------------------------------------

# Future Ideas (Backlog)

-   [ ] Distributed Runtime (future)
-   [ ] Cloud Workers (future)
-   [ ] Foundation Audio Model
-   [ ] Autonomous Studio
