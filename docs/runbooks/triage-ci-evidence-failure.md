# Runbook: Triage a CI Evidence Failure

## Trigger

An AgentProof consumer CI job fails, an Action gate reports new findings, or a portable report appears
inconsistent with local expectations.

## Immediate safety rule

Do not disable the gate, delete evidence, or update a baseline merely to unblock the pipeline. Preserve
the job URL, commit SHA, generated report paths, policy-result identity, and baseline revision.

## Procedure

1. Identify whether failure occurred during evidence production, strict validation, policy evaluation,
   replay, Action baseline comparison, report upload, or a surrounding consumer workflow step.
2. Retrieve the local `policy-result`, normalized evidence JSON, SARIF, JUnit, and Markdown output
   from the failed job's artifact. Treat them as potentially sensitive according to consumer policy.
3. Re-run the relevant component command locally from the same immutable source revision and sealed
   inputs. Do not add credentials, production traces, or live tool access to make the reproduction
   succeed.
4. Compare trace/finding identifiers, policy version, baseline entries, and gate mode. A changed input
   or unpinned dependency invalidates direct comparison.
5. Classify the result: **real finding**, **invalid/malformed evidence**, **baseline mismatch**,
   **policy regression**, or **toolchain/infrastructure failure**.
6. For a real finding, fix the modeled application/control issue or explicitly accept it through a
   reviewed policy/baseline change. For infrastructure failure, repair the deterministic workflow and
   rerun all affected gates.

## Exit criteria

The incident is closed only when a reviewer can point to the corrected source/policy/baseline, a
reproduced deterministic result, and a successful hosted job on the exact remediation commit.
