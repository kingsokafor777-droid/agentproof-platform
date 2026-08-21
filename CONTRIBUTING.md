# Contributing

AgentProof Platform is docs-as-code for security-sensitive cross-repository behavior. Contributions
must be reviewable, deterministic, and bounded by the source-of-truth rule in
[`docs/information-architecture.md`](docs/information-architecture.md).

## Required change discipline

| Change type | Required companion evidence |
|---|---|
| Architecture or trust-boundary change | ADR, updated system/security model, and link to the affected component contract. |
| Contract or compatibility statement | Component release note, deterministic fixture or test reference, and migration impact. |
| CI/deployment reference | Least-privilege permission review, immutable action pins, and validated local example. |
| Release-policy or baseline guidance | Security review rationale and explicit rollback/exception handling. |
| Runbook update | Trigger, safe action, reproducible procedure, and measurable exit criteria. |

Run `make check` before opening a pull request. Do not add secrets, live traces, credentials,
unreviewed mutable workflow tags, or assertions about components that cannot be traced to their public
repository evidence.
