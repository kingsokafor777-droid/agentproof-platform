# System Model

## Operating thesis

AgentProof makes workflow-level security claims from **sealed, versioned, deterministic evidence**.
It does not decide whether a prompt is good, execute a model, connect to a tool, or replace an
application authorization system. A consumer supplies already-recorded or synthetic evidence; the
program validates structure, evaluates a closed invariant, models a replay path, and emits portable
results for a local developer or CI gate.

```text
application trace | MCP transcript | sealed SDK capture
       │                    │                 │
       └───────────── normalise / parse ───────┘
                              │
                              ▼
                   Core versioned WorkflowTrace
                              │
                     policy + deterministic replay
                              │
                finding + approval state + shortest path
                              │
         corpus benchmark | GitHub Action | SDK local CLI
                              │
                              ▼
                   SARIF · JUnit · JSON · Markdown evidence
```

## Component boundaries

| Boundary | Upstream evidence | Output | Trust rule |
|---|---|---|---|
| Capture and intake | Explicit SDK observations, OTLP JSON, or MCP transcript | Strict Core-shaped trace or intake result | Intake is untrusted until schema and provenance checks complete. |
| Contract | Normalized input | Versioned `WorkflowTrace`, finding, policy-result model, deterministic identifiers | Core is framework-neutral and has no vendor runtime dependency. |
| Decision | Strict trace and closed policy definition | Stable policy result and findings | Enforcement is deterministic; an LLM cannot decide a CI gate. |
| Reconstruction | Trace and policy result | Modeled state transitions and shortest violating path | Replay simulates side effects and never invokes an external tool. |
| Evidence delivery | Local result and optional approved baseline | SARIF, JUnit, JSON, Markdown, and an optional PR comment | Output is portable evidence, not a source of truth for authorization. |

## Trust boundaries

| Boundary | Accepted | Rejected or intentionally excluded |
|---|---|---|
| **Evidence ingress** | Versioned JSON evidence whose identity, sequence, and required fields validate. | Live callback payloads, implicit environment state, unbounded arbitrary attributes, and malformed or future contract fields. |
| **Privacy boundary** | Caller-curated identifiers, labels, modeled outcomes, approval state, and safe provenance. | Prompts, tool arguments, return values, exception text, headers, credentials, serialized tool metadata, and arbitrary callback kwargs. |
| **Decision boundary** | Closed policy declarations and deterministic trace facts. | Natural-language or model-generated pass/fail decisions. |
| **Execution boundary** | Deterministic local parsing, validation, replay, report generation, and CI upload. | Tool invocation, cloud API calls, telemetry export, collector configuration, or hosted control-plane coordination. |
| **Publication boundary** | Reviewed source, release evidence, package/artifact checks, SBOM, and CI results. | Publishing merely because code builds locally; release claims require reproducible hosted evidence. |

## System invariants

1. A trace is not evidence until it passes the Core contract for the declared schema version.
2. Event relationships, identity fields, timestamps, and ordering must be explicit enough to replay
   deterministically; missing meaning is a validation failure, not a permissive default.
3. A policy outcome is a function of reviewed policy text and sealed evidence. It must be stable for
   the same inputs.
4. All potentially unsafe action paths remain modeled. A path report is evidence of a simulated
   workflow state, not proof that a real target was accessed.
5. Portable reports link to immutable trace/finding identity and retain enough context for a reviewer
   to reproduce the decision locally.
6. A baseline is an explicit review artifact. It is not a blanket suppression mechanism and cannot
   transform invalid evidence into passing evidence.

## Compatibility model

Core schema versions define the interoperability center. Adapters and SDKs may add bounded capture
ergonomics but must emit validated Core-shaped evidence; policy, replay, corpus, and Action paths
consume only their documented contracts. Consumers pin concrete component versions or immutable
source revisions in CI. This platform's inventory is a review snapshot, never a dependency resolver.

See [`../information-architecture.md`](../information-architecture.md) for the component inventory and
[`../release/release-policy.md`](../release/release-policy.md) for compatibility and release rules.
