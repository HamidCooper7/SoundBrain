# 04 --- AI Stack

> SoundBrain Project Bible

------------------------------------------------------------------------

# Purpose

The AI Stack defines every intelligence component used by SoundBrain and
the role each model plays inside the platform.

------------------------------------------------------------------------

# AI Pipeline

``` text
Audio
 │
 ▼
Feature Extraction
 │
 ▼
Embeddings
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
```

------------------------------------------------------------------------

# Model Registry

  Component   Purpose                  Status
  ----------- ------------------------ --------
  CLAP        Audio embeddings         ✅
  Whisper     Speech / transcription   ✅
  BGE         Text embeddings          ✅
  Qwen        Reasoning LLM            ✅
  RAG         Knowledge retrieval      ✅

------------------------------------------------------------------------

# Component Roles

## CLAP

-   Semantic audio embeddings
-   Audio similarity
-   Audio understanding

## Whisper

-   Speech transcription
-   Voice analysis foundation

## BGE

-   Knowledge indexing
-   Semantic search
-   Retrieval embeddings

## Qwen

-   Engineering reasoning
-   Report generation
-   Decision explanation

## RAG

-   Retrieve engineering knowledge
-   Provide grounded context to the LLM

------------------------------------------------------------------------

# Future Models

-   Audio Foundation Model
-   Psychoacoustic Model
-   Genre Classifier
-   Plugin Recommendation Model
-   Memory Model

------------------------------------------------------------------------

# Design Rules

-   Runtime owns model loading.
-   Repository owns model definitions.
-   Components are replaceable.
-   Providers remain independent.
-   Models communicate through interfaces only.

------------------------------------------------------------------------

# Living Notes

Update this file whenever a model is added, removed, or replaced.
