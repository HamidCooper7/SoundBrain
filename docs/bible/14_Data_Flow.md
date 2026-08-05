# 14 --- Data Flow

> SoundBrain Project Bible

------------------------------------------------------------------------

# End-to-End Data Flow

``` text
Audio File
    │
    ▼
Input Validation
    │
    ▼
Audio Loader
    │
    ▼
Feature Extraction
    │
    ▼
Deterministic Measurements
    │
    ▼
Context Builder
    │
    ▼
Knowledge Retrieval (RAG)
    │
    ▼
LLM Reasoning
    │
    ▼
Engineering Intelligence
    │
    ▼
Report Generator
    │
    ▼
Memory & Learning
```

------------------------------------------------------------------------

# Stage 1 --- Input

-   Audio validation
-   Metadata extraction
-   Format normalization

------------------------------------------------------------------------

# Stage 2 --- Analysis

-   Loudness
-   Dynamics
-   Spectrum
-   Stereo
-   Transients

Output: Structured measurements.

------------------------------------------------------------------------

# Stage 3 --- Context

Convert measurements into engineering context.

Output: Semantic engineering facts.

------------------------------------------------------------------------

# Stage 4 --- Knowledge

Retrieve relevant engineering information.

Output: Grounded context.

------------------------------------------------------------------------

# Stage 5 --- Reasoning

Combine:

-   Measurements
-   Context
-   Knowledge

Output: Engineering decisions.

------------------------------------------------------------------------

# Stage 6 --- Engineering

Generate:

-   Problems
-   Priorities
-   Solutions
-   Processing chain

------------------------------------------------------------------------

# Stage 7 --- Report

Produce:

-   Human report
-   Structured report
-   Future JSON export

------------------------------------------------------------------------

# Stage 8 --- Memory

Store:

-   Project history
-   User preferences
-   Learned patterns

------------------------------------------------------------------------

# Design Principles

-   Sequential pipeline
-   Deterministic before AI
-   Grounded reasoning
-   Modular stages
-   Replaceable components

------------------------------------------------------------------------

# Living Notes

Update when pipeline stages change.
