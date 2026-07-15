# SoundBrain Technical Debt

Version: 0.1.0

Last Updated: 2026-07-15

---

# Overview

This document tracks every architectural debt, missing feature,
refactor and engineering task inside SoundBrain.

Priority:

- P0 = Critical
- P1 = High
- P2 = Medium
- P3 = Low
- Future = Long-term Vision

---

# P0 — Critical

## Runtime Integration

Status: Pending

Description

Every AI model must be loaded through ModelRuntime.

Current issues

- CLAP uses hardcoded model path.
- Qwen uses hardcoded model path.
- BGE Reranker uses hardcoded model path.

Target

ModelRuntime becomes the single entry point for loading AI models.

---

## Remove Hardcoded Paths

Status: Pending

Current hardcoded files

- brain/audio/intelligence/embeddings.py
- brain/llm/qwen.py
- brain/rag/reranker.py

Target

No absolute filesystem path should exist anywhere in the project.

---

## Central Model Configuration

Status: Pending

Target

Every model should be resolved using:

ModelRepository

instead of local constants.

---

# P1 — High Priority

## Reference AI

Status: In Progress

Tasks

- Improve Prompt Builder
- Improve Formatter
- JSON Output
- Structured Recommendations
- Confidence Score
- Better Engineering Reasoning

---

## Mix Intelligence

Status: Planned

Tasks

- Frequency Balance
- Dynamic Balance
- Stereo Analysis
- Tonal Balance
- Loudness Strategy
- Human Engineering Suggestions

---

## Master Intelligence

Status: Planned

Tasks

- Loudness Optimization
- Streaming Optimization
- Dynamics
- Translation
- Commercial Master Analysis

---

## Knowledge Base

Status: Planned

Sources

- AES
- ITU
- EBU
- Dolby
- Harman
- Spotify
- Apple Music
- Engineering Books

---

# P2

## Memory

- Long-term Memory
- Session Memory
- Audio Memory

---

## Agent Planning

- Task Planner
- Reflection
- Self Critique

---

## RAG Improvements

- Metadata Search
- Hybrid Search
- Audio Retrieval
- Context Compression

---

## CLI

Commands

soundbrain analyze

soundbrain compare

soundbrain reference

soundbrain engineer

---

## REST API

Endpoints

/audio/analyze

/audio/reference

/audio/report

/audio/reason

---

# P3

## GUI

Desktop Application

Dashboard

Timeline

Visualizer

Audio Inspector

---

## DAW Integration

Ableton

FL Studio

Cubase

Reaper

Logic

---

## Plugin

VST3

AU

AAX

---

# Future

## Audio Foundation Model

Unified Audio Model

Semantic Understanding

Engineering Understanding

Generation

Editing

Restoration

Automation

---

## Autonomous Audio Intelligence

Target

SoundBrain should evolve into a complete Audio Intelligence System capable of:

- Audio Analysis
- Audio Understanding
- Audio Reasoning
- Audio Memory
- Audio Retrieval
- Audio Generation
- Audio Editing
- Audio Restoration
- DAW Automation
- Mixing
- Mastering
- Voice Interaction

---

# Completed

- Project Architecture
- Runtime Foundation
- Audio Analysis
- Audio Context
- Engineering Rules
- Comparison Engine
- Report Builder
- RAG Foundation
- Documentation
- GitHub Repository
- Clean Repository Structure

---

# Notes

Every Sprint must update this file.

No new feature should be started before reviewing this document.