# Runbook: Release Rollback or Gate Suspension

## Trigger

A published component, workflow pin, package artifact, baseline behavior, or platform statement is
found to be incompatible, insecure, or unsupported.

## Procedure

1. Identify the exact commit, artifact version, workflow action pin, and affected consumer scope.
2. Choose the narrowest safe response: revert a source commit, pin a known-good immutable revision,
   withdraw a package through its registry process, disable only the affected consumer integration, or
   suspend a gate with a documented time-bound exception.
3. Never replace a mutable tag, delete historical evidence, or broaden a baseline as a rollback
   substitute.
4. Run the full local gate and hosted CI/CodeQL for the remediation commit. If the issue changes a
   contract, provide a migration or fail-closed compatibility statement.
5. Update release notes, component status, and affected deployment references with the immutable
   remediation reference.

## Exit criteria

Consumers have an explicit safe revision or documented suspension path, hosted evidence verifies the
remediation, and the root cause has a regression fixture, ADR, or policy update as appropriate.
