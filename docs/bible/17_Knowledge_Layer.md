# 17 --- Knowledge Layer

> SoundBrain Project Bible

------------------------------------------------------------------------

# Purpose

The Knowledge Layer provides grounded engineering knowledge to the
Reasoning Engine through Retrieval-Augmented Generation (RAG).

------------------------------------------------------------------------

# Responsibilities

-   Store engineering knowledge
-   Index documents
-   Create embeddings
-   Retrieve relevant context
-   Supply evidence to reasoning

------------------------------------------------------------------------

# Architecture

``` text
Documents
    │
    ▼
Chunking
    │
    ▼
Embeddings (BGE)
    │
    ▼
Vector Index
    │
    ▼
Retriever
    │
    ▼
Relevant Context
    │
    ▼
Reasoning Engine
```

------------------------------------------------------------------------

# Data Sources

-   Mixing guides
-   Mastering guides
-   Internal documentation
-   Best practices
-   Reference notes
-   Future user knowledge

------------------------------------------------------------------------

# Components

## Chunker

Splits documents into searchable chunks.

## Embedder

Creates semantic embeddings.

## Vector Store

Stores indexed embeddings.

## Retriever

Returns the most relevant knowledge.

## Context Builder

Formats retrieved information for the LLM.

------------------------------------------------------------------------

# Inputs

-   Engineering questions
-   Audio context
-   Measurements

------------------------------------------------------------------------

# Outputs

-   Retrieved documents
-   Ranked context
-   Evidence package

------------------------------------------------------------------------

# Rules

-   No hallucination without retrieved evidence.
-   Retrieval occurs before reasoning.
-   Embeddings generated through Runtime-managed models.
-   Knowledge remains modular and replaceable.

------------------------------------------------------------------------

# Future

-   Knowledge Graph
-   Multi-source retrieval
-   User knowledge base
-   Online synchronization

------------------------------------------------------------------------

# Living Notes

Update whenever the knowledge architecture changes.
