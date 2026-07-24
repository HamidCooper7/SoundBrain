# 02 --- Architecture

> SoundBrain Project Bible

------------------------------------------------------------------------

# High-Level Architecture

``` text
                 User / API / CLI
                       │
                       ▼
                 Audio Input Layer
                       │
                       ▼
          Deterministic Analysis Layer
                       │
                       ▼
              Context Construction
                       │
                       ▼
             Knowledge Layer (RAG)
                       │
                       ▼
              LLM Reasoning Engine
                       │
                       ▼
          Engineering Intelligence
                       │
                       ▼
              Report Generation
                       │
                       ▼
                Memory & Learning
```

------------------------------------------------------------------------

# Core Layers

## 1. Audio Input

-   Audio loading
-   Format validation
-   Metadata extraction

## 2. Analysis

-   Loudness
-   Dynamics
-   Spectral analysis
-   Stereo analysis
-   Tempo / key / rhythm (future)

## 3. Context

Transforms raw measurements into structured engineering context.

## 4. Knowledge

Retrieves relevant engineering knowledge using RAG.

## 5. Reasoning

LLM combines measurements + context + retrieved knowledge to explain
issues and recommend actions.

## 6. Engineering

Generates actionable mix/master recommendations.

## 7. Report

Produces structured reports for the user.

## 8. Memory

Stores project history and future learning.

------------------------------------------------------------------------

# Data Flow

Audio ↓ Measurements ↓ Context ↓ Knowledge ↓ Reasoning ↓ Engineering ↓
Report ↓ Memory

------------------------------------------------------------------------

# Architectural Rules

-   Runtime is the only model loading entry.
-   Repository resolves all models.
-   Config owns filesystem paths.
-   Business logic never loads models directly.
-   Layers communicate only through defined interfaces.
-   Validation before feature expansion.

------------------------------------------------------------------------

# Living Notes

Modify this document only when the architecture changes.
