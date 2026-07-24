
# SoundBrain Living Roadmap v6 — Ultimate Edition

> Status: Living (Architecture Freeze Candidate)

# Executive Dashboard

| Area | Status | Progress |
|---|---|---:|
| Infrastructure | ✅ Stable | 95% |
| Runtime Validation | 🚧 Active | 15% |
| Platform Finalization | 🟡 Planned | 0% |
| Core Product | 🔒 Locked | 70% |
| Long-term Vision | 🚀 Future | 25% |

## Current Objective

- Finish Sprint 2.5
- Finish Sprint 2.6
- Freeze Architecture
- Start Sprint 3

---

# Target Architecture

User
↓
API (CLI / MCP / Python SDK / Desktop)
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
- Repository
- Loader
- Download Manager
- Verify Manager
- Cache Manager
- Placement Planner
- Device Profiler
- Health Monitor
- Telemetry
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

---

# Architecture Principles

- Runtime never owns business logic.
- Capability-first architecture.
- Repository owns model resolution.
- Runtime is the only model loading entry point.
- Planner decides intent.
- Scheduler decides execution.
- Resource Manager decides placement.
- Engines are backend agnostic.
- Providers are replaceable.
- Models are replaceable.

---

# Sprint 2.5 Runtime Validation

- [ ] Runtime Tests
- [ ] CLAP Validation
- [ ] Whisper Validation
- [ ] BGE Validation
- [ ] Qwen Validation
- [ ] CPU Validation
- [ ] CUDA Validation
- [ ] Benchmark
- [ ] runtime-v1-stable

Gate:
All runtime tests must pass.

---

# Sprint 2.6 Platform Finalization

Runtime

- [ ] Runtime Scheduler
- [ ] Resource Manager
- [ ] Download Manager
- [ ] Verify Manager
- [ ] Cache Manager
- [ ] Placement Planner
- [ ] Device Profiler
- [ ] Health Monitor
- [ ] Telemetry

Platform

- [ ] Capability Registry
- [ ] Engine Registry
- [ ] Task Graph
- [ ] Workflow Graph
- [ ] Dependency Cleanup
- [ ] Architecture Freeze

---

# Sprint 3

- [ ] End-to-End Pipeline
- [ ] Audio Analysis
- [ ] Context
- [ ] RAG
- [ ] Reasoning
- [ ] Engineering
- [ ] Reporting

# Sprint 4

- [ ] Multi Reference
- [ ] Genre Intelligence
- [ ] Frequency Reasoning
- [ ] Stereo Reasoning
- [ ] Dynamics Reasoning

# Sprint 5

- [ ] Root Cause Detection
- [ ] Recommendation Engine
- [ ] Plugin Chains
- [ ] Confidence Score

# Sprint 6

- [ ] FabFilter
- [ ] Waves
- [ ] SSL
- [ ] UAD
- [ ] Ozone

# Sprint 7

- [ ] Project Memory
- [ ] User Memory
- [ ] Genre Memory
- [ ] Continuous Learning

# Sprint 8

- [ ] MCP
- [ ] Python SDK
- [ ] VS Code
- [ ] Claude Code
- [ ] Cursor
- [ ] Public API

# Sprint 9

- [ ] Desktop
- [ ] React
- [ ] Tauri

---

# Observability

Track:

- Startup Time
- Download Time
- Warmup Time
- Model Load Time
- Cache Hit Ratio
- CPU
- RAM
- GPU
- VRAM
- Scheduler Latency
- Pipeline Latency

---

# Release Gates

- [ ] Tests Passing
- [ ] Runtime Validation
- [ ] Documentation Updated
- [ ] Architecture Frozen

---

# Decision Log

- Capability-first architecture
- Runtime Scheduler
- Resource Manager
- Memory Tiering
- Telemetry
- Freeze after Sprint 2.6

---

# Future Backlog

- [ ] Distributed Runtime
- [ ] Cloud Workers
- [ ] Foundation Audio Model
- [ ] Autonomous Studio
