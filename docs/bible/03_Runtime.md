# 03 --- Runtime

> SoundBrain Project Bible

------------------------------------------------------------------------

# Purpose

The Runtime is the only entry point responsible for loading, caching,
managing and serving AI models throughout SoundBrain.

------------------------------------------------------------------------

# Responsibilities

-   Model loading
-   Lazy initialization
-   Thread-safe loading
-   Cache management
-   Device selection (CPU/CUDA)
-   Provider dispatch
-   Resource lifecycle

------------------------------------------------------------------------

# Runtime Architecture

``` text
Application
     │
     ▼
 Runtime API
     │
     ▼
 Repository
     │
     ▼
 Provider Strategy
     │
     ├── Transformers
     ├── Sentence Transformers
     ├── CLAP
     ├── Whisper
     └── Future Providers
```

------------------------------------------------------------------------

# Core Components

## Runtime

Coordinates every model request.

## Repository

Owns model definitions and lookup.

## Loader

Creates model instances.

## Cache

Maintains one instance per unique configuration.

## Device Manager

Chooses CPU or CUDA.

## Provider Strategy

Dispatches loading logic without hardcoded conditionals.

------------------------------------------------------------------------

# Runtime Rules

-   Runtime is the only model loading entry.
-   Repository owns model resolution.
-   Configuration owns filesystem paths.
-   Business code never loads models directly.
-   No duplicate loaders.
-   No eager loading unless explicitly required.

------------------------------------------------------------------------

# Current Status

## Completed

-   [x] Runtime migration
-   [x] Repository injection
-   [x] Lazy loading
-   [x] Thread-safe loading
-   [x] Provider strategy
-   [x] Cache identity improvements
-   [x] Runtime stabilization

## Pending

-   [ ] Install pytest
-   [ ] Runtime validation
-   [ ] CLAP validation
-   [ ] BGE validation
-   [ ] Qwen validation
-   [ ] CPU validation
-   [ ] CUDA validation
-   [ ] Tag runtime-v1-stable

------------------------------------------------------------------------

# Definition of Done

Runtime is considered complete only when every validation task passes
successfully.

------------------------------------------------------------------------

# Living Notes

Update this document only when Runtime architecture changes.
