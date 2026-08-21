# AgentProof Platform Information Architecture

## Purpose and boundary

This repository is the **documentation and operator hub** for AgentProof. It does not introduce a
hosted control plane, execute agent tools, replay evidence, enforce policies, or publish packages.
Those responsibilities remain with the nine component repositories listed below. The platform owns
the cross-repository decisions required to operate those components as one local-first, CI-native
security system.

> **Source-of-truth rule:** A component repository owns executable behavior, its package interface,
> fixtures, and release evidence. This platform owns program-level architecture, compatibility and
> release policy, security posture, deployment reference material, and operator procedures. A conflict
> is resolved by changing the relevant component contract or this platform decision record—never by
> silently documenting a divergent behavior.

## Navigation model

| Reader need | Canonical platform document | Primary component evidence |
|---|---|---|
| Understand the full system | `docs/architecture/system-model.md` | Component inventory and component READMEs |
| Review an architectural trade-off | `docs/adr/` | Linked component contracts and tests |
| Assess security boundaries | `docs/security/threat-model.md` | Core schemas, policy evaluator, corpus fixtures, and Action outputs |
| Adopt or deploy in CI | `docs/deployment/ci-reference.md` | `agentproof-action` and SDK release artifacts |
| Decide whether a version is releasable | `docs/release/release-policy.md` | Component CI, CodeQL, SBOM, package/build evidence |
| Operate a failed workflow or investigate evidence | `docs/runbooks/` | Sealed trace, policy result, replay path, SARIF/JUnit/JSON output |
| Plan compatible changes | `docs/roadmap/roadmap.md` | Compatibility policy and ADRs |

## Component inventory snapshot

The following immutable commit references were captured on 2026-08-21. They are a review snapshot,
not a substitute for consuming an explicit package version or a downstream lockfile pin.

| # | Component | Responsibility | Snapshot commit |
|---:|---|---|---|
| 01 | [`agentproof-core`](https://github.com/kingsokafor777-droid/agentproof-core) | Versioned workflow evidence contracts, deterministic identifiers, and JSON Schema. | [`0c7f149`](https://github.com/kingsokafor777-droid/agentproof-core/commit/0c7f149bce6402cd4b91b08010a5a800b21f5d71) |
| 02 | [`agentproof-otel`](https://github.com/kingsokafor777-droid/agentproof-otel) | Offline OpenTelemetry ingestion and deterministic workflow normalization. | [`58c73b5`](https://github.com/kingsokafor777-droid/agentproof-otel/commit/58c73b582211dc28f72e11e62f0e22ca816ac7fe) |
| 03 | [`agentproof-mcp`](https://github.com/kingsokafor777-droid/agentproof-mcp) | Offline MCP transcript parsing, definition provenance, and capability inventory. | [`119f2dd`](https://github.com/kingsokafor777-droid/agentproof-mcp/commit/119f2ddc6b68b9dd6d853fed0387801c84557c7a) |
| 04 | [`agentproof-policy`](https://github.com/kingsokafor777-droid/agentproof-policy) | Deterministic invariant DSL and bounded Rego/Cedar review artifacts. | [`4417d95`](https://github.com/kingsokafor777-droid/agentproof-policy/commit/4417d951e1b389690703cdfcb4069a6627568286) |
| 05 | [`agentproof-replay`](https://github.com/kingsokafor777-droid/agentproof-replay) | Deterministic replay, approval observations, and shortest violation paths. | [`bf8f5ea`](https://github.com/kingsokafor777-droid/agentproof-replay/commit/bf8f5ea8df6107e30b9557f71b8612eefb740f34) |
| 06 | [`agentproof-corpus`](https://github.com/kingsokafor777-droid/agentproof-corpus) | Versioned synthetic fixtures and deterministic security benchmarks. | [`89ea8b4`](https://github.com/kingsokafor777-droid/agentproof-corpus/commit/89ea8b4098a6720fb0c29568d7adc577018c793c) |
| 07 | [`agentproof-action`](https://github.com/kingsokafor777-droid/agentproof-action) | CI action and deterministic SARIF/JUnit/JSON evidence. | [`33c5f69`](https://github.com/kingsokafor777-droid/agentproof-action/commit/33c5f69cab79945027efae62d386decbff376128) |
| 08 | [`agentproof-python`](https://github.com/kingsokafor777-droid/agentproof-python) | Typed Python trace capture, bounded adapter, and OTLP JSON handoff. | [`8254b4f`](https://github.com/kingsokafor777-droid/agentproof-python/commit/8254b4f1d861e5e9f7a98af35902a6dc998f5b9b) |
| 09 | [`agentproof-typescript`](https://github.com/kingsokafor777-droid/agentproof-typescript) | Typed Node trace capture, bounded lifecycle helpers, and OTLP JSON handoff. | [`cc5046b`](https://github.com/kingsokafor777-droid/agentproof-typescript/commit/cc5046b8ad4de0072a9ef0463f3f1a5973efbb42) |

## Shared vocabulary

| Term | Meaning in this program |
|---|---|
| **Trace** | A versioned, sealed record of modeled workflow events governed by the Core schema. |
| **Evidence** | Deterministic artifact that supports a security decision: a trace, fixture, result, path, or portable report. |
| **Policy result** | Deterministic evaluation result for a closed workflow invariant; it is not an LLM judgment. |
| **Replay path** | The shortest modeled sequence leading to a violated invariant, derived without executing a real tool. |
| **Baseline** | Explicitly reviewed prior evidence used for comparison by the CI Action. |
| **Deployment reference** | Non-secret configuration guidance for a consumer CI environment; it is not a managed or hosted deployment. |

## Platform acceptance criteria

The platform release is complete only when it documents the system model, component boundaries,
security model, release policy, CI deployment reference, roadmap, ADRs, and investigation runbooks;
contains no secrets or executable cloud infrastructure; validates all internal links and required
documents deterministically; and passes immutable-pinned documentation CI and CodeQL.
