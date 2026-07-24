# 25 --- Dependency Injection

> SoundBrain Project Bible

------------------------------------------------------------------------

# Purpose

Dependency Injection (DI) decouples object creation from business logic,
making every component modular, testable, and replaceable.

------------------------------------------------------------------------

# Goals

-   Loose coupling
-   Testability
-   Replaceable implementations
-   Clear ownership
-   Explicit dependencies

------------------------------------------------------------------------

# High-Level Architecture

``` text
Configuration
      │
      ▼
Dependency Container
      │
      ▼
Service Construction
      │
      ▼
Application Services
      │
      ▼
Business Logic
```

------------------------------------------------------------------------

# Injection Strategy

## Constructor Injection

Primary method for all services.

## Interface-Based Design

Components depend on contracts, not implementations.

## Composition Root

Application startup is responsible for object creation.

------------------------------------------------------------------------

# Runtime Integration

Runtime dependencies are injected rather than instantiated internally.

Examples:

-   Repository
-   Provider Strategy
-   Cache
-   Configuration
-   Logger

------------------------------------------------------------------------

# Benefits

-   Easier unit testing
-   Mock-friendly architecture
-   Independent modules
-   Improved maintainability
-   Better scalability

------------------------------------------------------------------------

# Rules

-   Never instantiate dependencies inside business logic.
-   Runtime receives Repository through injection.
-   Configuration is injected.
-   Public interfaces define dependencies.
-   No global service locator.

------------------------------------------------------------------------

# Future

-   Automatic dependency container
-   Plugin registration
-   Dynamic service discovery
-   Environment-specific composition

------------------------------------------------------------------------

# Living Notes

Update whenever dependency management changes.
