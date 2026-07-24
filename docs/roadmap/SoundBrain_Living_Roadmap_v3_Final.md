# SoundBrain Living Roadmap v3 (Final)

> Status: **Living** Last Updated: 2026-07-23

------------------------------------------------------------------------

# Dashboard

  -----------------------------------------------------------------------
  Phase               Progress                     Status
  ------------------- ---------------------------- ----------------------
  Phase 0 ·           ███████████████████░ 95%     ✅ Stable
  Infrastructure                                   

  Sprint 2.5 ·        ███░░░░░░░░░░░░░░░░ 15%      🚧 Active
  Runtime Validation                               

  Sprint 2.6 ·        ░░░░░░░░░░░░░░░░░░░ 0%       🆕 Next
  Platform                                         
  Finalization                                     

  Sprint 3 · Core     ░░░░░░░░░░░░░░░░░░░ 0%       🔒 Locked
  Integration                                      

  Vision V5           █████░░░░░░░░░░░░░░ 25%      🚀 Long Term
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# Current Focus

Current Sprint: **2.5 Runtime Validation**

Next Milestone:

-   Runtime Validation
-   Runtime Download
-   Runtime Verify
-   Runtime Cache
-   Architecture Freeze

------------------------------------------------------------------------

# Architecture

``` text
User
 ↓
API / CLI / MCP
 ↓
Application
 ↓
Orchestrator
 ├─ Planner
 ├─ Router
 └─ Executor
 ↓
Pipeline Engine
 ↓
Services
 ↓
Runtime
 ├─ Repository
 ├─ Loader
 ├─ Cache
 ├─ Download
 ├─ Verify
 └─ Device
 ↓
Models
 ↓
Analysis
 ↓
Context
 ↓
Knowledge (RAG)
 ↓
Reasoning
 ↓
Engineering
 ↓
Report
 ↓
Memory
```

------------------------------------------------------------------------

# Phase 0 (95%)

-   [x] Runtime
-   [x] Repository
-   [x] Config
-   [x] Dependency Injection
-   [x] Service Layer
-   [x] Pipeline
-   [x] RAG
-   [x] Reasoning
-   [x] Memory
-   [x] Report
-   [x] Agents

------------------------------------------------------------------------

# Sprint 2.5

-   [ ] Runtime Tests
-   [ ] CLAP Validation
-   [ ] Whisper Validation
-   [ ] BGE Validation
-   [ ] Qwen Validation
-   [ ] CPU Validation
-   [ ] CUDA Validation
-   [ ] Stable Runtime Tag

Gate: all items must pass.

------------------------------------------------------------------------

# Sprint 2.6

## Runtime

-   [ ] Download Manager
-   [ ] Verify Manager
-   [ ] Cache Manager
-   [ ] Health Check
-   [ ] Capability Registry

## Planner

-   [ ] Task Planning
-   [ ] Capability Selection
-   [ ] Engine Selection

## Workflow

-   [ ] Workflow Graph
-   [ ] Stage Execution
-   [ ] Pipeline Coordination

## Architecture

-   [ ] Dependency Cleanup
-   [ ] Final Validation
-   [ ] Architecture Freeze

------------------------------------------------------------------------

# Sprint 3

-   Audio → Analysis
-   Analysis → Context
-   Context → RAG
-   RAG → Reasoning
-   Reasoning → Engineering
-   Engineering → Report
-   End-to-End Validation

------------------------------------------------------------------------

# Sprint 4

Reference Intelligence

-   Multi Reference
-   Genre Intelligence
-   Frequency Reasoning
-   Stereo Reasoning
-   Dynamics Reasoning

------------------------------------------------------------------------

# Sprint 5

Mix Intelligence

-   Root Cause Detection
-   Recommendation Engine
-   Plugin Chain
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

Memory

-   Project Memory
-   User Memory
-   Genre Memory
-   Continuous Learning

------------------------------------------------------------------------

# Sprint 8

Platform

-   MCP
-   VS Code
-   Claude Code
-   Cursor
-   Public API

------------------------------------------------------------------------

# Sprint 9

Desktop

-   React
-   Tauri
-   Python Backend

------------------------------------------------------------------------

# Vision

## V2

-   Knowledge Graph
-   Psychoacoustics

## V3

-   Studio Intelligence

## V4

-   Audio Foundation Model

## V5

-   Autonomous Audio Intelligence

------------------------------------------------------------------------

# Core Rules

-   Runtime never knows model names.
-   Repository owns model resolution.
-   Runtime loads models only.
-   Planner decides capabilities.
-   Services coordinate work.
-   Pipeline executes stages.
-   Business Logic never loads models directly.

------------------------------------------------------------------------

# Immediate Next Action

1.  Finish Sprint 2.5
2.  Complete Sprint 2.6
3.  Freeze Architecture
4.  Begin Sprint 3
