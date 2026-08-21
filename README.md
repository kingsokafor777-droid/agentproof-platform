# AgentProof Platform

**AgentProof Platform** is the architecture, security, release, deployment-reference, and operator
documentation hub for the AgentProof workflow-security regression-testing program.

AgentProof treats a tool-using agent workflow as a security system. Its components normalize sealed
evidence, evaluate deterministic workflow invariants, replay modeled sequences, and emit portable
CI evidence before unsafe composed paths reach production. This repository explains how those
components fit together and how to operate the evidence boundary without creating a hosted control
plane or live-tool dependency.

## Start here

| If you need to… | Read… |
|---|---|
| Understand scope, vocabulary, and every shipped component | [`docs/information-architecture.md`](docs/information-architecture.md) |
| Review end-to-end data flow and trust boundaries | [`docs/architecture/system-model.md`](docs/architecture/system-model.md) |
| Review why a program-level decision was made | [`docs/adr/`](docs/adr/) |
| Assess threat boundaries and residual risks | [`docs/security/threat-model.md`](docs/security/threat-model.md) |
| Add AgentProof to a consumer CI workflow | [`docs/deployment/ci-reference.md`](docs/deployment/ci-reference.md) |
| Approve a component release | [`docs/release/release-policy.md`](docs/release/release-policy.md) |
| Triage failed evidence or an action run | [`docs/runbooks/`](docs/runbooks/) |
| Plan an approved change | [`docs/roadmap/roadmap.md`](docs/roadmap/roadmap.md) |

## Non-goals

This repository does **not** ship an agent runtime, hosted SaaS, telemetry collector, credential
store, cloud environment, Helm chart, live tool adapter, or package registry publication. **No hosted
control plane is permitted in v1.** Deployment
references are intentionally non-secret and CI-native. Unsafe behavior remains modeled by sealed
fixtures and mock boundaries in the relevant component repositories.

## Local validation

```bash
python3 scripts/validate_docs.py
```

The validator is intentionally dependency-free and offline. It verifies required documentation,
cross-repository inventory consistency, relative Markdown links, required policy language, and that
the platform contains no credential-shaped files.

## Governance

The platform follows a docs-as-code model. Architectural behavior changes require an ADR, contract
or compatibility changes require the affected component repository to release its own evidence, and
all release claims require reproducible CI evidence. See [`CONTRIBUTING.md`](CONTRIBUTING.md) and
[`docs/release/release-policy.md`](docs/release/release-policy.md).
