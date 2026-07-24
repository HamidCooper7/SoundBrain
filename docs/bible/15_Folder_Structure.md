# 15 --- Folder Structure

> SoundBrain Project Bible

------------------------------------------------------------------------

# Purpose

This document defines the logical folder organization of the SoundBrain
project.

------------------------------------------------------------------------

# High-Level Structure

``` text
SoundBrain/
│
├── brain/
│   ├── audio/
│   ├── analysis/
│   ├── context/
│   ├── knowledge/
│   ├── reasoning/
│   ├── engineering/
│   ├── report/
│   ├── runtime/
│   ├── models/
│   ├── repository/
│   ├── providers/
│   ├── config/
│   ├── utils/
│   └── memory/
│
├── tests/
│
├── docs/
│
├── scripts/
│
├── models/
│
├── examples/
│
├── assets/
│
└── README.md
```

------------------------------------------------------------------------

# Directory Responsibilities

## brain/

Core application source code.

## audio/

Audio loading and feature extraction.

## analysis/

Deterministic signal analysis.

## context/

Engineering context generation.

## knowledge/

RAG retrieval and knowledge management.

## reasoning/

LLM orchestration and reasoning.

## engineering/

Engineering recommendations.

## report/

Report generation and exporters.

## runtime/

Runtime manager, cache, loader and lifecycle.

## models/

Model specifications and metadata.

## repository/

Model registry and lookup.

## providers/

Model loading providers.

## config/

Configuration and environment.

## utils/

Shared utilities.

## memory/

Future long-term memory system.

------------------------------------------------------------------------

# Supporting Directories

## tests/

All automated tests.

## docs/

Project documentation.

## scripts/

Development utilities.

## models/

Downloaded model files.

## examples/

Sample inputs and outputs.

## assets/

Images, diagrams and static resources.

------------------------------------------------------------------------

# Folder Rules

-   One responsibility per directory.
-   No circular dependencies.
-   Runtime remains isolated.
-   Business logic never accesses model files directly.
-   Documentation lives in docs/.

------------------------------------------------------------------------

# Living Notes

Update this document whenever the folder layout changes.
