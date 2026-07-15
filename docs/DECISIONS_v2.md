# SoundBrain Architecture Decisions

Version: 2.0

Status: ACTIVE

---

# Purpose

This document records long-term architectural decisions that define the direction of SoundBrain.

---

# Decision 001 — Project Identity

SoundBrain is an **Audio Intelligence System**.

It is not merely an audio analyzer or a mixing assistant.

Status: Accepted

---

# Decision 002 — Perception Before Measurement

Human perception has higher priority than raw metrics.

Status: Accepted

---

# Decision 003 — Understanding Before Recommendation

Recommendations must consider:

- Audio context
- Genre
- Artistic intent
- Reference tracks
- Psychoacoustics
- Engineering knowledge

Status: Accepted

---

# Decision 004 — Explainable AI

Every decision should contain:

- Observation
- Evidence
- Reasoning
- Confidence
- Recommendation

Status: Accepted

---

# Decision 005 — Clean Architecture

Business logic remains independent from providers, libraries and UI.

Status: Accepted

---

# Decision 006 — Provider Pattern

Providers are replaceable.

Current:

- LM Studio
- CLAP
- ChromaDB

Future:

- OpenAI
- Ollama
- Claude
- Gemini
- Qwen Audio

Status: Accepted

---

# Decision 007 — Dependency Injection

Dependencies are injected.

Hidden dependencies are forbidden.

Status: Accepted

---

# Decision 008 — Generic Reasoning Engine

There is only one reasoning engine.

Different workflows use different Prompt Builders.

Status: Accepted

---

# Decision 009 — Multimodal Intelligence

Supported modalities include:

- Audio
- Waveform
- Spectrogram
- Spectrum
- Images
- Voice
- Text
- MIDI
- DAW Sessions

Status: Accepted

---

# Decision 010 — Knowledge Graph

Engineering intelligence should be built on trusted professional knowledge.

Status: Planned

---

# Decision 011 — Agent Architecture

Future agents:

- Mix Agent
- Master Agent
- Reference Agent
- Psychoacoustic Agent
- Producer Agent
- Composer Agent
- Teacher Agent

Status: Planned

---

# Decision 012 — Audio Memory

Persistent memory is a first-class architectural component.

Status: Planned

---

# Decision 013 — Automation

Reasoning precedes automation.

Status: Planned

---

# Decision 014 — Human-Centered AI

Humans remain in control of creative decisions.

Status: Accepted

---

# Decision 015 — Long-Term Vision

V1 → Professional Audio Intelligence

V2 → Perceptual Intelligence

V3 → Autonomous Mixing

V4 → Audio Foundation Model

V5 → Autonomous Audio Intelligence System

Status: Accepted

---

# Final Rule

Whenever implementation conflicts with architecture,

architecture wins.
