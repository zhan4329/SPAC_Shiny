# refactor(features): adopt histogram template workflow

[PR #86](https://github.com/FNLCR-DMAP/SPAC_Shiny/pull/86)

## Description

This PR refactors the features histogram to use the standard SPAC histogram template while preserving the current non-facet user experience.

The server now reads canonical AnnData, converts the existing features inputs to the template contract, and runs the template through the in-memory registry. The template's figure and dataframe remain the canonical results for the plot preview and CSV download.

This creates the execution boundary needed for later facet and agent-facing controls.

## Related

- Template workflow follows [Issue #73](https://github.com/FNLCR-DMAP/SPAC_Shiny/issues/73)
- Builds on the updated environment introduced by [SPAC Shiny PR #85](https://github.com/FNLCR-DMAP/SPAC_Shiny/pull/85)
- Depends on the latest histogram template introduced by [SCSAWorkflow PR #433](https://github.com/FNLCR-DMAP/SCSAWorkflow/pull/433)
- The adapter design was informed by Mousumi's commit `ffa8644`; PNG conversion was adapted from `5d65369`, with Heaven Golladay-Watkins credited as co-author.

## Changes

Everything is on the 'Features' tab. The 'Annotation' tab is unchanged.

- Use `shared["adata_main"]` instead of reconstructing AnnData.
- Normalize current UI values before mapping them to template parameters.
- Execute with `save_to_disk=False` and `show_plot=False`, with registry cleanup guaranteed in `finally`.
- Keep `Plot_By="Feature"` and `Facet=False` explicit for this PR.
- Serialize the template figure to PNG through a new helper function `fig_to_png_bytes()` in `utils/plot_utils.py`, and render the image directly through Shiny. This is to resolve rendering issue introduced by the histogram template. 
- Publish the returned dataframe only after successful execution and cleanup.
- Preserve button-gated rendering, current grouping behavior, and CSV download.

New ui controls including facets will be exposed in the next PR.

## Testing

- User-tested ordinary, grouped-Together, and repeated renders in Shiny.
- `python -m py_compile server/features_server.py utils/plot_utils.py ui/features_ui.py`
- `python -m pytest tests/test_utils/test_plot_utils.py -q` — `6 passed`
- `git diff --check`
- Focused PNG serialization and figure-closure smoke check passed.

There is not yet committed automated coverage for the new Features adapter or `fig_to_png_bytes()`.

## Notes for Review

Suggested order: `server/features_server.py`, `utils/plot_utils.py`, then `ui/features_ui.py`.

The template wrapper must be imported before the Histogram template because the template binds its loader during import.
