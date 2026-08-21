# Roadmap and Decision Gates

## Current program state

The ten-repository AgentProof program is complete when this platform repository is released with the
same reproducible standards as the nine executable component repositories. The program remains
local-first and CI-native in v1.

## Delivered foundation

| Milestone | Delivered components | Evidence outcome |
|---|---|---|
| Contract and intake | Core, OTel, MCP | Versioned workflow evidence plus deterministic telemetry/transcript normalization. |
| Deterministic decision | Policy, Replay | Closed invariant evaluation, modeled approval state, and shortest violating paths. |
| Regression evidence | Corpus, Action | Synthetic benchmark fixtures and portable CI-native SARIF/JUnit/JSON evidence. |
| Developer adoption | Python, TypeScript | Typed, bounded capture interfaces and deterministic OTLP JSON handoff. |
| Program operation | Platform | Architecture, security, release, deployment-reference, and runbook governance. |

## Post-v1 proposals require a decision record

| Proposal | Prerequisite decision gate |
|---|---|
| Additional framework adapters | Privacy boundary, stable Core compatibility fixture, deterministic lifecycle semantics, and maintenance owner. |
| Visual evidence viewer | Local artifact format, authorization model, retention policy, and no divergence from portable evidence. |
| Hosted collaboration layer | Multi-tenancy, evidence ownership, authentication, encryption, audit logs, egress controls, incident response, and explicit local-first fallback. |
| Helm or Kubernetes delivery | Justified service boundary, security architecture, upgrade/rollback plan, resource model, admission controls, and operator owner. |
| New policy language adapters | A deterministic Core-equivalence test suite; adapters cannot become an unreviewed enforcement bypass. |

## Non-negotiable roadmap rules

No proposal may convert a modeled side effect into a live destructive test, treat a model judgment as a
gate decision, or weaken evidence reproducibility for faster adoption. Every accepted proposal must
identify its contract impact, migration path, deterministic fixtures, and release evidence.
