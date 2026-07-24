# 16 --- Model Registry

> SoundBrain Project Bible

------------------------------------------------------------------------

# Purpose

The Model Registry defines every AI model officially supported by
SoundBrain, its responsibility, provider, lifecycle, and replacement
policy.

------------------------------------------------------------------------

# Current Registry

  Model     Role                 Status
  --------- -------------------- -----------
  CLAP      Audio Embeddings     ✅ Active
  Whisper   Speech Recognition   ✅ Active
  BGE       Text Embeddings      ✅ Active
  Qwen      LLM Reasoning        ✅ Active

------------------------------------------------------------------------

# CLAP

Purpose

-   Semantic audio embeddings
-   Audio similarity
-   Audio understanding

Input

-   Audio

Output

-   Embedding vectors

Lifecycle

-   Loaded through Runtime
-   Cached
-   Shared instance

------------------------------------------------------------------------

# Whisper

Purpose

-   Speech recognition
-   Voice transcription

Lifecycle

-   Runtime managed
-   Lazy loaded

------------------------------------------------------------------------

# BGE

Purpose

-   Knowledge indexing
-   Semantic retrieval
-   Vector search

------------------------------------------------------------------------

# Qwen

Purpose

-   Engineering reasoning
-   Recommendation generation
-   Report writing

------------------------------------------------------------------------

# Runtime Ownership

Every model:

-   Loaded only by Runtime
-   Registered in Repository
-   Uses Provider Strategy
-   Supports caching
-   Uses configuration metadata

------------------------------------------------------------------------

# Future Registry

-   Audio Foundation Model
-   Psychoacoustic Model
-   Genre Classifier
-   Plugin Recommendation Model
-   Memory Model
-   Evaluation Model

------------------------------------------------------------------------

# Model Requirements

Every new model must define:

-   Name
-   Version
-   Provider
-   Backend
-   Device support
-   Memory requirements
-   Loading strategy
-   Cache policy
-   Validation tests

------------------------------------------------------------------------

# Registry Rules

-   No direct model loading.
-   One Runtime entry point.
-   Repository owns registration.
-   Models remain replaceable.

------------------------------------------------------------------------

# Living Notes

Update this document whenever a model is added, removed, or upgraded.
