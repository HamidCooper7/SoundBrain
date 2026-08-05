# 18 --- RAG Architecture

> SoundBrain Project Bible

------------------------------------------------------------------------

# Purpose

Retrieval-Augmented Generation (RAG) grounds every engineering decision
with retrieved knowledge before any LLM reasoning.

------------------------------------------------------------------------

# Architecture

``` text
Engineering Query
        │
        ▼
 Context Builder
        │
        ▼
 Query Embedding (BGE)
        │
        ▼
 Vector Search
        │
        ▼
 Top-K Results
        │
        ▼
 Context Assembly
        │
        ▼
 Qwen Reasoning
        │
        ▼
 Engineering Output
```

------------------------------------------------------------------------

# Pipeline

1.  Build query
2.  Generate embedding
3.  Search vector index
4.  Rank results
5.  Assemble context
6.  Send to LLM
7.  Produce grounded answer

------------------------------------------------------------------------

# Components

## Query Builder

-   Creates semantic query

## Embedder

-   Generates BGE embeddings

## Retriever

-   Finds relevant chunks

## Ranker

-   Orders retrieved evidence

## Context Assembler

-   Formats retrieved knowledge

## Reasoning Engine

-   Uses evidence to produce recommendations

------------------------------------------------------------------------

# Inputs

-   Measurements
-   Engineering context
-   User request

------------------------------------------------------------------------

# Outputs

-   Retrieved evidence
-   Engineering recommendations
-   Explainable reasoning

------------------------------------------------------------------------

# Rules

-   Retrieval before reasoning
-   Evidence-first responses
-   Runtime manages embedding models
-   Replaceable vector store

------------------------------------------------------------------------

# Future

-   Hybrid search
-   Multi-vector retrieval
-   Graph retrieval
-   Online knowledge synchronization

------------------------------------------------------------------------

# Living Notes

Update whenever the RAG pipeline changes.
