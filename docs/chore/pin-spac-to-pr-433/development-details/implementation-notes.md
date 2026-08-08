# Implementation Notes

## Branch and PR Sequence

Create `chore/pin-spac-to-pr-433` from `dev`. After it is merged,
create `ref/features-server-template` from the updated `dev`.
Create `feat/features-facet` only after the Features server template refactor
PR is merged.

## Prior-Branch Evidence

Mousumi's `ref/features-template` branch updated the dependency pin and
changed `server/ripleyL_server.py` to import
`visualize_ripley_l_template`. It left other template callers using the
older execution argument, so use the branch as evidence for compatibility
scope rather than cherry-picking it wholesale.

## Verification

Run focused checks for the existing Nearest Neighbor and Ripley template
callers after installing the selected SPAC commit. Histogram template
contract checks belong to `ref/features-server-template`, where the Features
server will first delegate execution to that template. Record implementation
evidence in the implementation log when work begins.

## Contract Findings

Source inspection of the pinned SPAC `0.9.3` package confirmed that the Ripley
visualization module was renamed to `visualize_ripley_l_template` and that
template callers now use `save_to_disk` instead of `save_results`. The
existing Ripley and Nearest Neighbor callers still use the pre-pin API; the
required code changes are tracked in Task 3.

## Current Status

- Task 1 was implemented and committed as
  `bb70f1346f76d1abce439a08adde19793f4ad5b0`.
- The pinned package is installed. Application startup currently fails at the
  pre-pin Ripley module import; Task 3 owns the compatibility fixes.
- Task 3 compatibility fixes and focused smoke checks are complete.
- Histogram template contract checks are tracked by the Features adapter
  development.
