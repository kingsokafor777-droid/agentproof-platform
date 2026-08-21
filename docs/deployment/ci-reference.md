# CI Deployment Reference

## Operating model

AgentProof is deployed as a **consumer CI integration**, not as a server. A consumer repository
creates or ingests local evidence with the SDKs/adapters, evaluates a policy result using the relevant
component workflow, and passes the resulting local JSON to the Action. The Action then validates local
evidence, compares an optional strict baseline, emits reports, and applies the requested gate mode.

The example below pins the Action to the reviewed platform inventory snapshot commit. Production
consumers should pin their own reviewed immutable commit and update it through normal dependency
review.

```yaml
name: AgentProof evidence gate

on:
  pull_request:

permissions:
  contents: read
  security-events: write # Only when uploading SARIF to GitHub Code Scanning.

jobs:
  agentproof:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@11d5960a326750d5838078e36cf38b85af677262
      # Produce a strict local PolicyResult JSON using the reviewed Core/Policy/Replay path.
      - name: Evaluate sealed workflow evidence
        run: ./scripts/evaluate-agentproof.sh
      - uses: kingsokafor777-droid/agentproof-action@33c5f69cab79945027efae62d386decbff376128
        with:
          policy-result: .agentproof/policy-result.json
          baseline: .agentproof/baseline.json
          output-dir: .agentproof/output
          fail-on: new
          comment-pr: "false"
      - name: Upload evidence for review retention
        uses: actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02
        with:
          name: agentproof-evidence
          path: .agentproof/output/
```

The Action's real interface consists of `policy-result` (required), optional `baseline`, `output-dir`,
`fail-on` (`none`, `new`, or `all`), and opt-in `comment-pr`. Its outputs include `decision`,
`gate-passed`, finding counts, and local SARIF/JUnit/JSON paths. Do not pass a token unless using the
explicit same-repository PR-comment capability; do not expose credentials in evidence files.

## Evidence retention

Store CI reports as private build artifacts for the retention period required by the consumer's own
policy. SARIF can be uploaded to code-scanning tooling only after validating that report content meets
the consumer's data-handling requirements. AgentProof reports are evidence artifacts, not a database
for sensitive event payloads.

## Helm and hosted deployment reference

There is intentionally **no Helm chart, collector, API service, or managed Kubernetes deployment in
v1**. AgentProof runs from reviewed repository code and CI workspace files. A future hosted or Helm
proposal must first add an ADR covering tenancy, evidence retention, authentication, encryption,
network egress, admission controls, upgrade/rollback behavior, and an explicit reason why local-first
CI is insufficient. Until that decision exists, a Helm installation is unsupported.

## Consumer preflight

1. Pin each AgentProof dependency to a reviewed release or immutable revision.
2. Generate or select only sealed, privacy-minimized local evidence.
3. Validate policy result and baseline paths are workspace-relative.
4. Use `fail-on: new` for reviewed incremental adoption; use `all` only when every active finding is
   intentionally gating.
5. Review baseline changes as security changes, not routine generated-file churn.
