# Task Details

## Development

### Task 1. Update the SPAC Dependency Pin
Location: `requirements.txt`, `environment.yml`
Date: 2026-08-07
Status: Planned

Implementation decision:
- Pin both dependency files to the exact official SPAC dev commit rather than
  a floating branch reference or a fork.

Action items:
- [ ] Replace the old SPAC commit in `requirements.txt`.
- [ ] Replace the old SPAC commit in `environment.yml`.
- [ ] Update the dependency comments to identify the selected dev commit and
  histogram-facet follow-up.
- [ ] Confirm both files reference the same official SPAC repository and
  commit.

Commit boundary:
Update the reproducible SPAC dependency baseline without adding visualization
behavior.

### Task 2. Verify the Current SPAC Dev Contract
Location: `requirements.txt`, `environment.yml`, `server/`, SPAC package environment
Date: 2026-08-07
Status: Planned

Implementation decision:
- Verify the exact pinned SPAC dev package and all affected in-repository
  template callers before downstream adapter work begins.

Action items:
- [ ] Install the SPAC package from commit
  `f9886bcde643ebf14e58a31d5ac397e28b6ea510`.
- [ ] Import `spac` and
  `spac.templates.histogram_template.run_from_json` from the installed
  environment.
- [ ] Verify that the histogram `run_from_json()` accepts
  `save_to_disk=False` and returns the in-memory figure/dataframe tuple.
- [ ] Verify the histogram keys and defaults for `Table_`,
  `Group_by`, `Max_Groups`, `Facet`, and
  `Facet_Ncol`.
- [ ] Inspect every in-repository `run_from_json()` caller and confirm
  its imported template and execution keyword.
- [ ] Verify the installed execution contract for the Nearest Neighbor and
  Ripley template callers.
- [ ] Update incompatible callers that still use renamed modules or pass
  `save_results=False`.
- [ ] Run focused smoke checks for the Histogram, Nearest Neighbor, and Ripley
  template paths after the dependency update.

Commit boundary:
Verify the installed SPAC dev contract and keep existing template callers
compatible.
