# ADR 0002: Make Core contracts the interoperability center

**Status:** Accepted

## Context

Framework-specific capture APIs and telemetry schemas change at different rates. Coupling policy,
replay, corpus, CI, and SDK consumers directly to a framework would fragment security semantics.

## Decision

All adapters and SDKs produce or consume versioned Core contracts. OTel, MCP, Python, and TypeScript
boundaries normalize into strict Core-shaped evidence; policy, replay, corpus, and Action behavior is
defined over that evidence.

## Consequences

Core schema evolution is a high-scrutiny compatibility event. Adapters may remain small and
framework-specific without changing deterministic policy/replay semantics. A convenience feature that
cannot be represented in the Core contract is not silently smuggled through arbitrary attributes.
