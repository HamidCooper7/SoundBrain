# 12 --- Project Rules

> SoundBrain Project Bible

------------------------------------------------------------------------

# Core Principles

-   Runtime First
-   Stability Before Features
-   Validation Before Expansion
-   Modular Architecture
-   Single Source of Truth

------------------------------------------------------------------------

# Architecture Rules

-   [ ] Runtime is the only model loading entry point.
-   [ ] Repository owns model resolution.
-   [ ] Configuration owns filesystem paths.
-   [ ] Business logic never loads models directly.
-   [ ] Every layer communicates only through public interfaces.

------------------------------------------------------------------------

# Development Rules

## DO

-   [ ] Keep commits small.
-   [ ] Write documentation with features.
-   [ ] Add tests for new functionality.
-   [ ] Update the Living Roadmap after each sprint.
-   [ ] Preserve backward compatibility whenever possible.

## DON'T

-   [ ] Bypass Runtime.
-   [ ] Hardcode filesystem paths.
-   [ ] Duplicate loaders.
-   [ ] Introduce architecture drift.
-   [ ] Skip validation gates.

------------------------------------------------------------------------

# Commit Convention

Feature: - feat: ...

Bug Fix: - fix: ...

Documentation: - docs: ...

Refactor: - refactor: ...

Testing: - test: ...

Chore: - chore: ...

------------------------------------------------------------------------

# Definition of Done

A task is complete only if:

-   [ ] Implementation finished
-   [ ] Tests passed
-   [ ] Documentation updated
-   [ ] Roadmap updated
-   [ ] No critical issues remain

------------------------------------------------------------------------

# Code Review Checklist

-   [ ] Architecture respected
-   [ ] Runtime unchanged unless required
-   [ ] No duplicated logic
-   [ ] Naming consistent
-   [ ] Tests included

------------------------------------------------------------------------

# Living Notes

This document defines the permanent engineering rules for the SoundBrain
project and should change only by deliberate architectural decision.
