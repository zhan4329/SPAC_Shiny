# Decisions

### D3. Move Histogram Template Contract Checks to the Features Adapter
Date: 2026-08-07

Decision:
Keep this development focused on the pinned dependency baseline and existing
Ripley/Nearest Neighbor caller compatibility. Move Histogram template import,
parameter/default, and return-contract checks to
`ref/features-server-template` Tasks 4, 5, and 7.

Rationale:
The Shiny Features server currently calls `spac.visualization.histogram()`;
the Histogram template becomes an application boundary only when the adapter
delegates Features execution to it. The adapter therefore owns that contract,
while this development owns the dependency baseline and startup regressions
caused by the pin.

### D2. Clarify Progress Record Ownership
Date: 2026-08-07

Decision:
Use the overview, task details, implementation notes, decisions log, and
implementation log for distinct purposes rather than repeating the same
content across files.

Details:
- `overview.md` is authoritative for overall scope, status, and task routing.
- `task-details.md` is authoritative for task and implementation details.
- `implementation-notes.md` is authoritative for policies, rationale, and
  development guidance.
- `decisions.md` records why policies, rationale, scope, or task
  reclassification choices were made; it is not the authoritative copy.
- `implementation-log.md` records when and how task or implementation state
  changed, with pointers to the authoritative details.

Rationale:
This keeps the progress docs efficient to use while preserving historical
reasoning and execution history.

### D1. Pin SPAC to the PR #433-compatible dev commit
Date: 2026-08-07

Decision:
Update both dependency files to the official SPAC dev commit
`f9886bcde643ebf14e58a31d5ac397e28b6ea510`, verify the installed contracts
for existing template callers, and complete required compatibility fixes
before the Features adapter work.

Details:
- Pin the exact commit rather than a floating `dev` branch.
- Use the current template execution argument `save_to_disk=False`.
- Verify existing template callers before downstream Features work.
- Defer Histogram template contract checks to the Features adapter boundary.
- Keep facet UI exposure deferred to the separate Features facet PR.

Rationale:
The Features adapter must target the template version that provides the later
histogram and facet controls. Separating the dependency baseline makes API
compatibility regressions independently reviewable before the Features
refactor begins.
