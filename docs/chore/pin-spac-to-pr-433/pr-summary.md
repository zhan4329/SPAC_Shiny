# chore(deps): pin SPAC to PR #433 and restore template compatibility

## Description

This PR updates SPAC Shiny to the official SPAC merge commit containing FNLCR-DMAP/SCSAWorkflow#433's histogram-facet follow-up and updates the existing Ripley L and nearest neighbor callers to the pinned template API.

The change establishes a reproducible SPAC dependency baseline and removes the startup/runtime incompatibilities caused by the pinned package. Later features template adaptation and facet UI exposure will be developed on this PR.

## Related PRs

FNLCR-DMAP/SCSAWorkflow#433

## Changes

- Pins SPAC to official commit `f9886bcde643ebf14e58a31d5ac397e28b6ea510` in both `requirements.txt` and `environment.yml`.
- Updates Ripley L to import `spac.templates.visualize_ripley_l_template`.
- Replaces the removed `save_results=False` argument with `save_to_disk=False` in the Ripley L and nearest neighbor callers.

## Testing

- Rebuilt and restarted the Docker development application.
- Confirmed startup logs no longer report the old Ripley module import error.
- Smoke-tested all tabs including the Histogram, Nearest Neighbor, and Ripley L Shiny paths.

The repository has no focused automated tests for these server template callers, and `pytest` was unavailable in the local environment. Docker startup and the focused Shiny smoke tests were used as the runtime validation.

Initially, pinning spac to the latest commit will cause a module import error. This is fixed by the following commit updating Ripley L module names. 

## Commit Scope

- `bb70f13 chore(deps): pin SPAC to PR #433 merge commit`
- `9d425c8 fix(server): update pinned template callers`