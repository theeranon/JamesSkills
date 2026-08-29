# House Framework Contract

## Objects

| Object | Meaning | Reuse expectation |
|---|---|---|
| Framework | A reusable model of constructs, relationships, and decision or operating logic | Several materially different scenarios |
| Pattern | A recurring arrangement that helps design or diagnose work | Reusable but narrower than a framework |
| Method | A repeatable way to perform a bounded job | Similar executions |
| Tool | A mechanism used inside a method or framework | Task-specific |
| Template | A reusable output structure | Similar artifacts |
| Checklist | A completeness or risk guard | Similar reviews |
| Principle | A durable rule that shapes judgment | Broad decisions |

Do not promote a sequence of activities into a framework merely because it has a name or diagram.

## Use, upgrade, or build

### Use

Use an approved house framework when its problem, constructs, decision logic, boundaries, and evidence fit. Adapt examples, language, and delivery context without claiming the core changed.

`Use existing` describes the reuse branch. It does not erase lifecycle:

- approved: active use within the approved boundary
- pilot: bounded pilot use only, with observation and no universal claim
- candidate or source-gap: analysis and design input only, not active company law
- superseded or retired: historical trace only unless an explicit exception exists

Always display kind, lifecycle, version, and permitted scope beside the reuse decision.

### Upgrade

Upgrade when the existing framework still owns the problem but needs a reusable improvement. Produce a candidate version and a diff. Keep the active version unchanged until approval.

- Patch: clarification, evidence, or examples without changing decision logic.
- Minor: a backward-compatible construct, branch, or use case.
- Major: a changed promise, construct relationship, boundary, or decision logic.

Minor and major changes require owner approval and regression cases before activation.

### Build

Build a new framework only when existing house frameworks cannot own the recurring problem without distorting their promise or logic. The report must identify every close candidate and explain why use or upgrade fails.

## Lifecycle

```text
observed need
-> candidate
-> pilot
-> approved
-> superseded or retired
```

- Candidate: researched model with a working name, not yet company law.
- Pilot: used in a bounded real case with explicit observation.
- Approved: passed cross-case and counter-case proof and has an owner approval record.
- Superseded: retained for history; new work uses a named successor.
- Retired: unavailable for new work but preserved for old project traceability.

## Approval packet

The approver must be able to decide from one report:

- why this capability is needed now
- which house assets were searched
- why reuse, upgrade, or new creation is proposed
- what research supports or challenges the model
- how the model works
- what the proposed name and visual communicate
- where it succeeds and fails
- what changed from the active version
- what becomes active after approval

Three new name options are required only for a new framework or a material rename. Reuse preserves the registered name.
