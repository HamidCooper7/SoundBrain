# SoundBrain Module Map

Version: 1.0

Status: ACTIVE

---

# Purpose

This document maps every major module in the SoundBrain codebase.

It defines ownership, responsibility, and allowed interactions between modules.

---

# Repository

brain/

---

# Runtime

Path

brain/runtime/

Responsibilities

- Model lifecycle
- Lazy loading
- Device selection
- Runtime cache
- Repository access

Depends On

Infrastructure only.

---

# Audio

Path

brain/audio/

Responsibilities

- Audio IO
- DSP
- Feature extraction
- Context
- Embeddings
- Comparison

Depends On

Runtime

---

# Engineering

Path

brain/engineering/

Responsibilities

- Rule Engine
- Recommendations
- Validation
- Scoring

Depends On

Audio

---

# Knowledge

Path

brain/rag/

Responsibilities

- Loading
- Chunking
- Retrieval
- Vector Search
- Reranking

Depends On

Runtime

---

# LLM

Path

brain/llm/

Responsibilities

- Prompt Builders
- Providers
- Parsing
- Validation

Depends On

Runtime

Knowledge

Engineering

---

# Reports

Path

brain/report/

Responsibilities

- JSON Export
- Human Reports
- Validation

Depends On

Engineering

Reasoning

---

# Services

Path

brain/services/

Responsibilities

- Public APIs
- Application Facade
- Use Cases

Depends On

All domain modules.

---

# CLI

Path

brain/cli/

Responsibilities

- Command-line interface

Depends On

Services only.

---

# API

Path

brain/api/

Responsibilities

- REST API

Depends On

Services only.

---

# Desktop

Path

brain/ui/

Responsibilities

- Desktop application

Depends On

Services only.

---

# Future Modules

- Vision
- Speech
- MIDI
- Agent OS
- Knowledge Graph
- Memory
- Foundation Model

---

# Final Rule

Each module owns one responsibility.

If a module begins solving another module's problems, refactor before adding features.