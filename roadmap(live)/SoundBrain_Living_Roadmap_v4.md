
# SoundBrain Living Roadmap v4

> Status: Living Roadmap
> Purpose: Single source of truth before implementation.

---

# Executive Dashboard

| Area | Progress | Status |
|------|----------|--------|
| Infrastructure | ███████████████████░ 95% | ✅ Stable |
| Runtime Validation | ███░░░░░░░░░░░░░░░░ 15% | 🚧 Active |
| Platform Runtime | ░░░░░░░░░░░░░░░░░░░ 0% | 🆕 Next |
| Core Product | ██████████████░░░░░ 70% | 🚧 |
| Long-term Vision | █████░░░░░░░░░░░░░░ 25% | 🚀 |

---

# Current Mission

1. Finish Sprint 2.5
2. Complete Sprint 2.6
3. Freeze Architecture
4. Build Sprint 3+
5. Ship V1

---

# Architecture Evolution

Current

User
→ Application
→ Runtime
→ Model

Target

User
→ Task
→ Planner
→ Orchestrator
→ Workflow
→ Capability Registry
→ Runtime Scheduler
→ Resource Manager
→ Runtime
→ Engine
→ Backend
→ Model

---

# Runtime Stack

Runtime
- Repository
- Loader
- Download Manager
- Verify Manager
- Cache Manager
- Device Manager
- Resource Manager
- Runtime Scheduler
- Health Monitor

---

# New Platform Components

## Planner
- Task decomposition
- Capability selection
- Workflow creation

## Runtime Scheduler
- Device selection
- Backend selection
- Precision selection
- Execution ordering

## Resource Manager
- RAM allocation
- VRAM allocation
- CPU balancing
- Resource limits

## Device Profiler
- CPU
- GPU
- RAM
- VRAM
- Disk throughput

## Placement Planner
- Disk
- RAM
- VRAM
- Residency policy

## Capability Registry
- Embedding
- Transcription
- Audio Analysis
- Reference Intelligence
- Reasoning
- Report Generation

## Engine Registry
- Whisper
- CLAP
- Qwen
- Embedding
- Reranker
- Future Engines

---

# Memory Hierarchy

Disk
↓
RAM
↓
VRAM

Policies
- Hot cache
- Warm cache
- Cold storage
- Eviction
- Residency
- Prefetch

---

# Sprint 2.5

- Runtime tests
- Model validation
- CPU validation
- CUDA validation
- Stable runtime tag

Gate:
All runtime tests pass.

---

# Sprint 2.6

Platform Finalization

- Runtime Scheduler
- Resource Manager
- Download Manager
- Verify Manager
- Cache Manager
- Capability Registry
- Engine Registry
- Workflow Graph
- Health Monitor
- Architecture Cleanup
- Architecture Freeze

Gate:
No architectural breaking changes after completion.

---

# Sprint 3

Core Integration

- Audio Pipeline
- Analysis
- Context
- RAG
- Reasoning
- Engineering
- Report
- End-to-End validation

---

# Sprint 4

Reference Intelligence

- Multi-reference
- Genre awareness
- Frequency reasoning
- Dynamics reasoning
- Stereo reasoning

---

# Sprint 5

Mix Intelligence

- Root cause detection
- Recommendations
- Plugin chains
- Confidence score

---

# Sprint 6

Plugin Intelligence

- FabFilter
- Waves
- SSL
- UAD
- Ozone

---

# Sprint 7

Memory

- Project memory
- User memory
- Genre memory
- Learning

---

# Sprint 8

Platform

- MCP
- VS Code
- Claude Code
- Cursor
- API

---

# Sprint 9

Desktop

- React
- Tauri
- Python Backend

---

# Architecture Principles

- Runtime never owns business logic.
- Business logic never loads models.
- Planner decides intent.
- Scheduler decides execution.
- Resource Manager decides placement.
- Repository owns model resolution.
- Engines are backend-agnostic.
- Models are replaceable.
- Everything is capability-driven.
- Components have a single responsibility.
- Observability is mandatory.

---

# Observability

Track

- Load time
- Cache hit ratio
- Memory usage
- VRAM usage
- CPU usage
- GPU usage
- Scheduler latency
- Pipeline latency

---

# Inspiration

## From Colibri

Adopt
- Memory tiering
- Runtime scheduling
- Predictive prefetch
- Usage-based caching
- Lightweight runtime

Avoid
- MoE-specific execution
- LLM-only assumptions

## From OpenJarvis

Adopt
- Typed architecture
- Composition layer
- Planner abstraction
- Tool separation
- Memory abstraction

Avoid
- General assistant assumptions
- Domain-independent workflows

---

# Vision

V2
- Better Runtime

V3
- Studio Intelligence

V4
- Audio Foundation Platform

V5
- Autonomous Audio Intelligence

---

# Definition of Ready

Before Sprint 3

- Runtime stable
- Architecture frozen
- Registry complete
- Scheduler operational
- Validation passing
- Documentation updated

