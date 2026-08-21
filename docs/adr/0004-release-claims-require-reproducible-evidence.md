# ADR 0004: Require reproducible evidence before release claims

**Status:** Accepted

## Context

Infrastructure-quality portfolio claims are meaningful only when a reviewer can inspect source,
recreate the gate, and see the exact hosted result.

## Decision

Each component requires deterministic local validation, immutable-pinned least-privilege CI, hosted
quality and security analysis, artifact/dependency evidence appropriate to its language, and explicit
documentation before the program marks it shipped.

## Consequences

Publication may be delayed by a failing gate. A passing local check is necessary but insufficient.
Baseline updates, contract changes, and fixes to hosted workflow setup are treated as evidence-bearing
changes and rerun through the full affected gate.
