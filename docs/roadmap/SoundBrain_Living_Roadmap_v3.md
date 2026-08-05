# SoundBrain Living Roadmap v3 (Draft)

> Status: Proposed Architecture Update Replaces: Living Roadmap v2 after
> Architecture Audit

------------------------------------------------------------------------

# Dashboard

  Phase                               Progress             Status
  -------------------------- -------------------------- ------------
  Phase 0 • Infrastructure    ███████████████████░ 95%       ✅
  Sprint 2.5 • Validation     ███░░░░░░░░░░░░░░░░ 15%    ⛔ Blocked
  Sprint 2.6 • Platform Layer ░░░░░░░░░░░░░░░░░░░ 0%         🆕
  Phase 1 • V1 Product        ██████████████░░░░░ 70%        🚧
  Vision (V5)                 █████░░░░░░░░░░░░░░ 25%        🚀
  

------------------------------------------------------------------------

# Master Vision

    User
     │
     ▼
    Task
     │
     ▼
    Planner
     │
     ▼
    Workflow
     │
     ▼
    Application Services
     │
     ▼
    Runtime
     │
     ▼
    Engine Registry
     │
     ▼
    Engine
     │
     ▼
    Backend
     │
     ▼
    Model
     │
     ▼
    Analysis
     │
     ▼
    Context
     │
     ▼
    Knowledge (RAG)
     │
     ▼
    Reasoning
     │
     ▼
    Engineering
     │
     ▼
    Report
     │
     ▼
    Memory
     │
     ▼
    Learning

------------------------------------------------------------------------

# Phase 0 --- Infrastructure (Completed)

-   Clean Architecture
-   Runtime
-   Repository
-   Configuration
-   Dependency Injection
-   Cache
-   Thread-safe Loading
-   Lazy Loading
-   CLAP / Whisper / BGE / Qwen foundation

------------------------------------------------------------------------

# Sprint 2.5 --- Runtime Validation

-   [ ] Install pytest
-   [ ] Runtime Tests
-   [ ] CLAP Validation
-   [ ] BGE Validation
-   [ ] Qwen Validation
-   [ ] CPU Validation
-   [ ] CUDA Validation
-   [ ] Tag runtime-v1-stable

Gate: Sprint 2.6 stays locked until Runtime Validation passes.

------------------------------------------------------------------------

# Sprint 2.6 --- Platform Layer (NEW)

## Planner

-   [ ] Task Planner
-   [ ] Capability Discovery
-   [ ] Engine Selection

## Engine Registry

-   [ ] Engine Registry
-   [ ] Engine Factory
-   [ ] Engine Interface

## Workflow Engine

-   [ ] Workflow Graph
-   [ ] Pipeline Execution
-   [ ] Stage Coordination

## Model Lifecycle

-   [ ] Download Manager
-   [ ] Verification
-   [ ] Cache Manager
-   [ ] Health Checks

------------------------------------------------------------------------

# Sprint 3 --- Core Integration

-   [ ] Audio → Analysis
-   [ ] Analysis → Context
-   [ ] Context → Knowledge
-   [ ] Knowledge → Reasoning
-   [ ] Reasoning → Engineering
-   [ ] Engineering → Report
-   [ ] End-to-End Validation

------------------------------------------------------------------------

# Sprint 4

Reference Intelligence

-   Multi-reference
-   Genre-aware comparison
-   Frequency reasoning
-   Dynamics reasoning
-   Stereo reasoning

------------------------------------------------------------------------

# Sprint 5

Mix Intelligence

-   Root Cause Detection
-   Engineering Priorities
-   Plugin Chain Suggestions
-   Confidence Score

------------------------------------------------------------------------

# Sprint 6

Plugin Intelligence

-   FabFilter
-   Waves
-   SSL
-   UAD
-   Ozone

------------------------------------------------------------------------

# Sprint 7

Memory & Learning

-   Project Memory
-   User Memory
-   Genre Memory
-   Continuous Learning

------------------------------------------------------------------------

# Sprint 8

Platform

-   MCP Server
-   Claude Code
-   Cursor
-   VS Code
-   Public API

------------------------------------------------------------------------

# Sprint 9

Desktop

-   React
-   Tauri
-   Python Backend

------------------------------------------------------------------------

# Long-term

-   Psychoacoustics
-   Knowledge Graph
-   Foundation Model
-   Autonomous Audio Intelligence

------------------------------------------------------------------------

# Core Rules

-   Runtime never knows model names.
-   API never calls models directly.
-   Planner selects tasks.
-   Workflow orchestrates execution.
-   Engine Registry resolves engines.
-   Repository owns models.
-   Download Manager owns model acquisition.
-   Runtime executes only.
