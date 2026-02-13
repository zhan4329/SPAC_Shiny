# Fix Overlapping Labels in Feat vs Anno Heatmap with Enhanced Axis Controls

## Description

This PR enhances the Feature vs Annotation heatmap visualization with improvements to UI/UX, code quality, and maintainability following contributing guidelines. 

**This PR fixes the issue of overlapping labels in heatmap.**

## Related Issue/PR

This work is based on student contributions in PR #51
This PR closes Issue Saran-Nag#22

## Key Changes

### 1. Enhanced Axis Customization
- **Font Size Controls**: Numeric inputs for precise axis label font sizing (3-24pt range)
- **Y-Axis Label Rotation**: Added rotation functionality for Y-axis labels (previously only X-axis supported)
- **Label Abbreviation**: Configurable character limits to prevent overlapping labels and improve readability

### 2. UI/UX Redesign
Reorganized control panel into three collapsible sections for better usability:
- **Core Parameters**: Annotation and layer selection for primary analysis configuration
- **Plot Configuration**: Color maps, dendrograms, min/max value controls (collapsible to reduce clutter)
- **Axis Settings**: Rotation angles, font sizing, and label abbreviation options (collapsible)

### 3. Accessibility & Performance
- **Accessibility**: `alt` attributes for screen readers, accessible CSS with focus states, semantic HTML structure
- **Performance**: Replaced `renderUI`/`uiOutput` with `conditionalPanel` for reduced reactivity overhead
- **Consistency**: Reactive `adata` object, standardized `hm1` naming convention

### 4. Code Quality & Standards
- **Documentation**: NumPy-style docstrings with examples, updated contributor information
- **Error Handling**: Logging with specific exception handling
- **Code Organization**: Extracted utilities to `utils/plot_utils.py`
- **Validation**: Input validation with `req()` and defensive checks
- **Testing**: Unit tests covering edge cases (6 test methods)
- **PEP 8 Compliance**: Line lengths, formatting, clean imports

## Files Modified

- `server/feat_vs_anno_server.py` 
  - The 3 new axis controls (font size, y-axis rotation, abbreviation)
  - Error handling, validation, docstrings and PEP 8 formatting
- `ui/feat_vs_anno_ui.py` 
  - UI restructuring (new control panel aligning with nearest_neighbor tab)
  - Accessibility, naming consistency, performance
  - Docstrings and PEP 8 formatting
- `utils/plot_utils.py` - New utility functions (22 new lines, `abbreviate_labels` and `apply_axis_style`)
- `tests/test_utils/test_plot_utils.py` - Test suite (73 lines, new file, 6 tests for the above two utillity functions)
- `TECHNICAL_DETAILS.md` - Updated contributor information

## Verification Results

- [x] New layout renders correctly
- [x] All new controls functional
- [x] 508 Compliance satisfied
- [x] All unit tests passing
- [x] PEP 8 compliant satisfied
- [x] NumPy-style docstrings added
- [x] All changes follow the contributing guide
- [x] All issues from code review fixed

**Ready for Review**
