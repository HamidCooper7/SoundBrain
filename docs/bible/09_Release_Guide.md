# 09 --- Release Guide

> SoundBrain Project Bible

------------------------------------------------------------------------

# Release Workflow

``` text
Development
    │
    ▼
Unit Tests
    │
    ▼
Integration Tests
    │
    ▼
Validation Gates
    │
    ▼
Documentation Review
    │
    ▼
Version Tag
    │
    ▼
Release
```

------------------------------------------------------------------------

# Pre-Release Checklist

## Code

-   [ ] Feature complete
-   [ ] No critical bugs
-   [ ] No architecture violations
-   [ ] No TODOs blocking release

## Validation

-   [ ] Runtime validation passed
-   [ ] Unit tests passed
-   [ ] Integration tests passed
-   [ ] End-to-end tests passed

## Documentation

-   [ ] Roadmap updated
-   [ ] Changelog updated
-   [ ] Project Bible updated
-   [ ] API docs updated

## Versioning

-   [ ] Version number updated
-   [ ] Git tag created
-   [ ] Release notes written

------------------------------------------------------------------------

# Release Types

## Patch

-   Bug fixes
-   Documentation

## Minor

-   New features
-   Backward compatible

## Major

-   Architecture changes
-   Breaking changes

------------------------------------------------------------------------

# Release Rules

-   Never release without passing validation gates.
-   Never skip documentation updates.
-   Every release must have a changelog.
-   Every sprint completion updates the roadmap.

------------------------------------------------------------------------

# Living Notes

Update this document whenever the release process changes.
