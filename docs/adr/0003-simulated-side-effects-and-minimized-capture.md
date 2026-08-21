# ADR 0003: Model side effects and minimize captured data

**Status:** Accepted

## Context

Security regression tests need to reason about harmful sequences without reproducing harm or retaining
sensitive runtime payloads.

## Decision

Replay and corpus paths model side effects, approvals, labels, and authorization state. SDK and intake
paths capture only bounded, caller-curated metadata and defined outcomes. Prompts, arguments, return
values, error text, credentials, headers, and arbitrary callback data are outside the evidence
contract.

## Consequences

AgentProof findings apply to the modeled workflow. Consumers must ensure their evidence represents the
security facts they want to test. This prevents tests from becoming live execution harnesses and keeps
the evidence format suitable for CI review.
