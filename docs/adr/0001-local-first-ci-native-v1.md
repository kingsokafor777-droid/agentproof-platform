# ADR 0001: Keep v1 local-first and CI-native

**Status:** Accepted

## Context

Agent workflow evidence can contain sensitive business context and security-relevant operational
metadata. A hosted service would create new tenancy, authentication, retention, egress, and incident
response obligations before the program has established a stable evidence contract.

## Decision

v1 runs locally and in consumer CI from sealed fixtures or already-recorded evidence. It has no hosted
control plane, collector, required API token, or deployment service. Portable SARIF, JUnit, JSON, and
Markdown artifacts remain the integration boundary.

## Consequences

Consumers own CI workspace retention and access controls. The program gains reproducibility and a
small trust boundary, but does not provide central analytics or collaboration. A hosted proposal must
satisfy the decision gates in [`../roadmap/roadmap.md`](../roadmap/roadmap.md).
