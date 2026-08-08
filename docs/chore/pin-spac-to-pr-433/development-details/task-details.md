# Task Details

## Development

### Task 3. Fix SPAC Template Caller Compatibility
Location: `server/ripleyL_server.py`, `server/nearest_neighbor_server.py`
Date: 2026-08-07
Status: Complete

Implementation decision:
- Update existing callers to the module names and execution keyword exposed
  by the exact pinned SPAC commit.

Action items:
- [x] Update `server/ripleyL_server.py`:
  - [x] Import from `spac.templates.visualize_ripley_l_template`.
  - [x] Replace `save_results=False` with `save_to_disk=False`.
- [x] Update `server/nearest_neighbor_server.py`:
  - [x] Replace `save_results=False` with `save_to_disk=False`.
- [x] Run static checks:
  - [x] Run `python -m compileall -q server utils`.
  - [x] Search for stale module names and keywords.
  - [x] Run `git diff --check`.
- [x] Rebuild and restart the Docker application.
- [x] Verify startup logs no longer show the import error.
- [x] Smoke-test Histogram, Nearest Neighbor, and Ripley Shiny paths.
- [x] Update the task status and implementation log with the precise time and
  validation results.

Commit boundary:
Apply only compatibility changes required by the pinned SPAC package; do not
add Features refactoring or facet UI behavior.

### Task 2. Verify the Current SPAC Dev Contract
Location: `requirements.txt`, `environment.yml`, `server/`, SPAC package environment
Date: 2026-08-07
Status: Complete

Implementation decision:
- Verify the exact pinned SPAC dev package and all affected in-repository
  template callers before downstream adapter work begins.

Action items:
- [x] Install the SPAC package from commit
  `f9886bcde643ebf14e58a31d5ac397e28b6ea510`.
- [x] Inspect every in-repository `run_from_json()` caller and confirm
  its imported template and execution keyword.
- [x] Verify the pinned execution contract for the Nearest Neighbor and
  Ripley template callers.
- [x] Identify incompatible callers that still use renamed modules or pass
  `save_results=False`.

Commit boundary:
Verify the installed SPAC dev contract and keep existing template callers
compatible.

Runtime evidence:
- The Docker application reached the SPAC Shiny import path after installing
  the pinned package.
- Startup failed at the pre-pin Ripley module import with
  `ModuleNotFoundError: No module named
  'spac.templates.visualize_ripley_template'`.
- The exact pinned source confirms the replacement modules and
  `save_to_disk` execution keyword. Histogram template contract checks are
  owned by `ref/features-server-template` Tasks 4, 5, and 7.

### Task 1. Update the SPAC Dependency Pin
Location: `requirements.txt`, `environment.yml`
Date: 2026-08-07
Status: Complete

Implementation decision:
- Pin both dependency files to the exact official SPAC dev commit rather than
  a floating branch reference or a fork.

Action items:
- [x] Replace the old SPAC commit in `requirements.txt`.
- [x] Replace the old SPAC commit in `environment.yml`.
- [x] Update the dependency comments to identify the selected dev commit and
  histogram-facet follow-up.
- [x] Confirm both files reference the same official SPAC repository and
  commit.

Implementation details:
- Both dependency files now pin the official SPAC repository at commit
  `f9886bcde643ebf14e58a31d5ac397e28b6ea510`.
- The dependency comments identify the PR #433 histogram-facet follow-up.

Evidence: See the Task 1 entry in `implementation-log.md`.

Commit boundary:
Update the reproducible SPAC dependency baseline without adding visualization
behavior.
