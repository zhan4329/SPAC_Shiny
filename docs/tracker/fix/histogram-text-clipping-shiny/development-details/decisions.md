# Decisions

### D3. Combine Export Reproduction, Implementation, and Verification
Date: 2026-10-14

Decision:
Consolidate Task 3 into Task 2, keeping Task 1 as the independent package
title improvement. Retain separate repository PRs and consumer adoption.

Rationale:
One focused export task avoids duplicate verification while preserving the
requirements for complete text, original canvas, and unchanged plot geometry.

### D2. Separate Package Title Wrapping From Shiny Export Completeness
Date: 2026-09-16

Decision:
Track title wrapping in SCSAWorkflow and PNG clipping in SPAC Shiny as one
development, using the same branch name in both repositories and separate
repository PRs. Preserve the original figure while allowing the exported
PNG to expand. This supersedes D1's package-only, fixed-canvas scope.

Rationale:
Outside legends can be valid Matplotlib content yet disappear during
fixed-boundary export. Complete export is required now; crowded layouts can
be addressed by later figure-size and font controls.

### D1. Keep Canonical Text Containment in the Histogram Template
Date: 2026-09-16
Status: Superseded by D2; retained as planning history.

Decision:
Fix title and legend containment in the SCSAWorkflow Histogram template, then
update the SPAC Shiny package pin separately after the package PR merges.

Rationale:
The template creates the text and canonical image; renderer changes cannot
make a clipped artifact complete.
