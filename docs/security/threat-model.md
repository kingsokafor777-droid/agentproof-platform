# Security Model and Threat Model

## Scope

AgentProof protects the integrity, reproducibility, and reviewability of **modeled workflow-security
evidence**. It does not secure a model provider, an MCP server, a consumer application's identity
system, or a cloud deployment. Those systems remain external dependencies whose claims may be
represented—but not trusted automatically—in a trace.

## Protected assets

| Asset | Security property | Primary control |
|---|---|---|
| Core trace and policy-result JSON | Structural integrity and schema-version clarity | Strict validation, versioned contracts, deterministic canonical identity. |
| Tool-definition provenance | Binding between a modeled capability and reviewed definition metadata | Hash-bound provenance and bounded capability inventory. |
| Fixture expectations and baselines | Reviewer-controlled reproducibility | Versioned fixtures, exact baseline comparison, deterministic benchmark harness. |
| Policy definition | Deterministic and reviewable enforcement | Closed DSL, explicit compilation/evaluation, bounded adapter artifacts. |
| CI reports | Portability and traceability | Deterministic SARIF/JUnit/JSON/Markdown output and local paths. |
| Release claim | Evidence that a published version passed stated gates | Immutable workflow pins, protected review process, build/package/SBOM evidence. |

## Threat analysis

| Threat | Example | Preventive controls | Detection and response |
|---|---|---|---|
| Forged or malformed evidence | A trace lies about sequence or injects an unknown field. | Strict Core validation, deterministic IDs, no silent unknown-field acceptance. | Fail validation; preserve the rejected artifact only under the consumer's incident policy. |
| Evidence privacy leakage | Capture records prompts, arguments, return values, or credentials. | Payload-minimized SDK boundaries, allowlisted mapping, no arbitrary attributes. | Stop capture expansion, rotate any exposed secret outside AgentProof, and add a regression fixture before re-enabling. |
| Policy bypass by ambiguity | A rule relies on a model judgment or undefined default. | Closed deterministic policy language and explicit state/approval modeling. | Treat ambiguity as a policy-design defect; add a decision record and negative fixture. |
| Baseline suppression abuse | A broad baseline masks a new finding. | Exact baseline matching, deterministic finding identity, explicit gate modes. | Compare evidence JSON, remove stale baseline entries, and require review for baseline changes. |
| Supply-chain substitution | Mutable action tag or unreviewed runtime dependency changes behavior. | Full-commit action pins, lockfiles, SBOM, package inspection, CodeQL, least privilege. | Halt publication/gate use; pin or revert to a reviewed commit and rerun evidence. |
| Unsafe execution through test harness | Replay or corpus fixture triggers a real side effect. | Mock-only side-effect model, no credentials or cloud calls in primary tests, local-first runtime. | Stop job, revoke exposed credentials externally, and add an execution-boundary regression test. |
| Report spoofing | A SARIF or JUnit report is detached from the evaluated evidence. | Stable trace/finding IDs and deterministic evidence file generation. | Re-run locally from sealed fixture/result; reject report if identities diverge. |

## Security assumptions and residual risk

AgentProof assumes a reviewer has selected meaningful workflow invariants and that source evidence
does not intentionally omit material facts. It can prove that a submitted model violates or satisfies
a deterministic policy; it cannot prove a real runtime recorded every event, nor can it replace
application authorization, data classification, endpoint defense, or human review.

The most important residual risk is **semantic incompleteness**: a trace may be well-formed yet omit a
relevant effect. Treat an AgentProof pass as evidence about the modeled workflow and reviewed policy,
not a universal guarantee of safety.

## Security reporting and change control

Do not place a suspected secret, production trace payload, or exploit reproduction in a public issue.
Use the process in [`../../SECURITY.md`](../../SECURITY.md). Security-sensitive contract changes require
a threat-model update, a reviewed ADR when the system boundary changes, deterministic positive and
negative fixtures, and a release-policy review.
