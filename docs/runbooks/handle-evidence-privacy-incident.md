# Runbook: Handle an Evidence Privacy Incident

## Trigger

A trace, report, fixture, log, baseline, pull-request comment, or artifact may contain a prompt,
argument, return value, exception text, credential, header, or other data excluded by the AgentProof
privacy boundary.

## Procedure

1. Stop further publication, artifact upload, and PR commenting for the affected workflow. Do not
   reproduce the payload in an issue or chat transcript.
2. Follow the consumer organization's incident process for access control, retention, deletion, and
   credential rotation. AgentProof does not manage external secrets or artifact retention.
3. Identify the capture or mapping boundary that admitted the data. Preserve a minimal non-sensitive
   forensic description and the affected immutable revision.
4. Remove the capture path or narrow its allowlist. Add a deterministic negative test proving the
   prohibited field is rejected or never emitted.
5. Update the component threat model and this platform model if the boundary or residual risk changed.
6. Release the remediation according to [`../release/release-policy.md`](../release/release-policy.md)
   and document any consumer action required to invalidate exposed reports or rotate credentials.

## Exit criteria

The affected boundary is fail-closed, a regression test and hosted evidence pass, externally managed
credentials are handled by their owner, and public communications contain no sensitive payload.
