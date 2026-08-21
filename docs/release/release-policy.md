# Release Policy

## Release unit

Every AgentProof component releases independently because the program is contract-oriented. This
platform does not publish a combined runtime. A platform release states the documented compatibility
position and links to the component evidence on which it relies.

## Required evidence before `✅ Shipped`

| Gate | Minimum evidence | Release blocker |
|---|---|---|
| Scope and contract | README, explicit non-goals, compatibility statement, changelog, and versioned interface. | Ambiguous contract or undocumented behavior change. |
| Deterministic verification | Offline tests and fixtures; lint/format/static checks appropriate to the language; stated coverage gate where executable code exists. | Network, credential, real-tool, or nondeterministic primary test dependency. |
| Supply chain | Lockfile where applicable, inspected build/package artifact, SBOM or equivalent inventory, immutable workflow pins. | Mutable third-party workflow reference or unreviewed production dependency drift. |
| Hosted evidence | Least-privilege CI and CodeQL or equivalent analysis pass on the release commit. | Failed, skipped, or missing required hosted gate. |
| Security boundary | Threat model or security notes, no secrets, and a documented disclosure route. | Unbounded capture or evidence that can invoke live destructive behavior. |

## Semantic-versioning policy

| Change | Expected version action |
|---|---|
| Documentation clarification with no normative behavior change | Patch release or documentation commit. |
| Backward-compatible field, adapter, report, or policy feature | Minor release; document the default and compatibility behavior. |
| Changed required field, finding identity, replay semantics, or policy outcome | Major release or a new schema/contract version with a migration path. |
| Security fix that changes acceptance behavior | Patch or minor according to compatibility impact, plus a security note and regression fixture. |

No component may claim compatibility based solely on source similarity. The producer and consumer must
validate the declared contract version with deterministic fixtures.

## Promotion sequence

1. Author or update the contract, ADR, threat model, and deterministic fixtures.
2. Run the complete local quality gate with no credentials, cloud calls, or live tools.
3. Inspect generated artifacts, package contents, and dependency inventory.
4. Obtain review for policy, baseline, compatibility, and security-boundary changes.
5. Push the reviewed source release and verify hosted CI and CodeQL on the exact commit.
6. Update public status only after the prior evidence is complete; package registry publication, if
   separately approved, is a separate administrative action.

## Rollback and revocation

Source rollback means reverting to a previously verified immutable commit and rerunning hosted gates.
An invalid baseline is removed or narrowed; a flawed report is regenerated from sealed evidence; a
release with a security flaw is documented through the security process. Do not delete evidence merely
to make a dashboard or status badge green.

## Platform release policy

This repository is docs-as-code. Its release gate validates required documents, internal links,
component inventory, policy language, secret-shaped files, and workflow pinning. A platform document
that changes a runtime contract must be accompanied by the component change that implements it.
