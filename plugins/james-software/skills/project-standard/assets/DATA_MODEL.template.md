# Data model

Last verified: {{DATE}}

## Canonical facts

Not confirmed

## Entities and relationships

Not confirmed

## Constraints and lifecycle

Not confirmed

## Permissions

State a role-by-action matrix before any narrative description. One row per role, one column per action; do not summarize this as prose.

| Role | Can view | Can create | Can approve | Can edit others' records | Notes / boundary |
|---|---|---|---|---|---|
| Not confirmed | | | | | |

For every action a role can approve or edit, name who that action is *performed on*. An actor approving, editing, or confirming a record that names itself as the counterparty (e.g. a supplier approving its own purchase order, an employee editing their own approval record) is a boundary defect — record it under `Need decision` in `PROJECT.md`, not as a routine implementation detail.

Do not treat SQL injection, XSS, or transport-layer attacks as the primary risk to check for here — competent current models largely defend against those by default. The primary risk this matrix exists to catch is a logic/permission leak: the system granting a role access, visibility, or approval authority the requirement never intended, whether or not any classic security vulnerability is present.

## Derived data, caches, and snapshots

Not confirmed

## Migration and rollback

Not confirmed
