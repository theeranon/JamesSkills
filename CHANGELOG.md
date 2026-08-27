# Changelog

## 0.3.1 - 2026-08-28

- Added a critical-path rule: deliver, verify, install, and push the minimum usable outcome before optional audits, documentation cleanup, taxonomy work, or extra hardening.
- Added a regression case for existing-skill adaptations that are delayed by unrelated completeness work.

## 0.3.0 - 2026-08-28

- Split the library into core, modes, standards, outputs, and internal packages with one canonical `catalog.json`.
- Restored the global output authority as `make-it-james`, including a portable deterministic linter and behavior test.
- Added `sum-meet`: one source-faithful A4 portrait HTML meeting record containing every agenda as a separate zone.
- Added `one-page-pls`: one independently usable A4 landscape artifact per detected topic or agenda, with a no-silent-loss gate.
- Rebuilt both HTML templates around IBM Plex Sans Thai, compact density, 6px radius, restrained cards, and all-page visual QA.
- Added a data-free SolutionsIMPACT output pack so the two generic workflows can apply brand identity without hardcoding it into their semantic logic.
- Added migration aliases for `james-ui-standard`, `solutionsimpact-meeting-summary-full`, and `solutionsimpact-onepagesummary` without duplicating instructions.
- Installer, doctor, and validation now operate from the typed catalog rather than assuming every skill belongs in `skills/core`.

## 0.2.0 - 2026-08-28

- Reframed skill names as natural invocation phrases rather than system modules.
- Added `give-me-solutions`, `done-for-me`, `zoom-out`, `prove-it`, `never-again`, and `final-it`.
- Added persistent conversation mode `i-have-adhd`; concise communication no longer means one arbitrary answer or lost information.
- Retired `same-page`, `read-the-room`, and `follow-the-money` from the proposed set.
- Installer now prunes retired managed links and installs only promoted core skills.

## 0.1.1 - 2026-08-28

- Added repository-owned pre-commit and pre-push validation gates.
- Installer now activates local Git hooks without GitHub Actions or paid runners.

## 0.1.0 - 2026-08-28

- Initial private skill library.
- Added router, project control, source-first research, proof gate, UI standard, and handoff.
- Added cross-platform installer, updater, validator, and doctor.
