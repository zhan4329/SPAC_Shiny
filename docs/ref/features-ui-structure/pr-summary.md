# refactor(features): reorganize UI and use static group controls

## Description

This PR refactors the SPAC Shiny Features tab into focused control and result components, organizes the existing inputs in `features_ui.py` into clearer configuration sections, and replaces server-inserted Group By controls in `features_server.py` with stable conditional UI in `features_ui.py`.

The refactor preserves the current histogram behavior.

## Related

- The section-based organization follows [Issue #73](https://github.com/FNLCR-DMAP/SPAC_Shiny/issues/73).
- This development is independent of PR #86.

## Changes

- Changes the Features layout from 2/10 to 3/9 control/result columns.
- Extracts `_controls_panel()` and `_plot_panel()`; Adds a local `_collapsible_section()` helper for presentation-only disclosure behavior.
- Organizes Feature and Table as always-visible Core Parameters, Group By and log controls under Plot Configuration, and label rotation under Figure Configuration.
- Makes Render Plot span the width of the controls panel by adding `w-100` in the button class.
- Declares Annotation, Plot Together, and Stack Type as nested conditional UI; Removes the corresponding dynamic insertion targets, reactive state, and insertion/removal effects from `features_server.py`.
- Updates Features annotation choices through the existing central `effect_update_server.py`.

## Testing

- User-tested the complete Features workflow in Shiny, including disclosure sections, ordinary and grouped rendering, Plot Together and Stack Type conditions, repeated toggling and rendering, label rotation, plot display, and CSV download.
- Full application import in the existing local Docker image passed.
- Rendered UI construction, unique identifiers, preserved defaults, 3/9 layout, and conditional-expression checks passed.
- Direct ordinary, grouped-separate, grouped-together, repeated-render, dataframe, and download-path checks passed.
- `python tests/test_utils/test_plot_utils.py -v` — `6 passed` in the project Docker image.
- Python AST syntax checks and `git diff --check dev...HEAD` passed.

## Notes for Review

Suggested review order:

1. `ui/features_ui.py` for the extracted composition, disclosure sections, and static conditional controls.
2. `server/effect_update_server.py` for centralized Annotation choices.
3. `server/features_server.py` for removal of the dynamic UI lifecycle while retaining the existing render arguments.

The static dependent inputs retain their selections while hidden; the renderer ignores them whenever Group By is disabled. 

A better reusable cross-tab visualization design (and CSS styling) are postponed.
