# Code Review for PR #66: Feat vs Anno Axis Settings Improvements

## Overview
This PR improves the axis settings UI/UX for the Feature vs Annotation heatmap visualization by:
- Restructuring the UI with collapsible sections
- Adding Y-axis rotation controls
- Adding font size controls
- Adding label abbreviation functionality
- Renaming variables for consistency (hm1_ prefix)
- Improving code organization

## Files Changed
1. `server/feat_vs_anno_server.py` - 169 lines modified
2. `ui/feat_vs_anno_ui.py` - 224 lines modified

---

## ✅ Strengths

### 1. Improved UI/UX
- Good use of collapsible sections to organize controls
- Consistent with `nearest_neighbor_ui.py` styling patterns
- Responsive layout with proper scrolling (85vh height)

### 2. Feature Enhancements
- Added Y-axis label rotation (previously only X-axis)
- Added label abbreviation with character limit
- Added font size controls for axis labels
- Added font family specification ("DejaVu Sans")

### 3. Code Organization
- Extracted `get_adata()` as a reactive calculation (DRY principle)
- Consistent naming with `hm1_` prefix throughout
- Better code structure compared to previous version

### 4. Accessibility
- Added `alt="Heatmap Plot"` to render.plot decorator
- Used accessible CSS classes from style guide
- Proper focus states defined in CSS

---

## ❌ Issues Found

### CRITICAL Issues

#### 1. **Missing Module Docstrings** ⚠️
**Location:** Both `feat_vs_anno_server.py` and `feat_vs_anno_ui.py`

**Issue:** Neither file has a module-level docstring, which violates NumPy documentation standards.

**Reference:** See `server/nearest_neighbor_server.py` and `server/ripleyL_server.py` for examples.

**Required:**
```python
"""
Feature vs Annotation heatmap visualization module for SPAC Shiny application.

This module handles the server-side logic for generating hierarchical heatmaps
that visualize features (genes/proteins) against cell annotations.
"""
```

---

#### 2. **Missing Function Docstrings** ⚠️
**Location:** `feat_vs_anno_server.py`

**Issue:** Main server function lacks NumPy-style docstring.

**Current:**
```python
def feat_vs_anno_server(input, output, session, shared):
    def on_layer_check():
```

**Required:**
```python
def feat_vs_anno_server(input, output, session, shared):
    """
    Server logic for feature vs annotation heatmap visualization.

    Parameters
    ----------
    input : shiny.session.Inputs
        Shiny input object
    output : shiny.session.Outputs
        Shiny output object
    session : shiny.session.Session
        Shiny session object
    shared : dict
        Shared reactive values across server modules
    """
```

---

#### 3. **Inconsistent Docstring Format** ⚠️
**Location:** `feat_vs_anno_server.py`, line 12-18

**Issue:** `on_dendro_check()` uses triple single quotes instead of triple double quotes.

**Current:**
```python
def on_dendro_check():
    '''
    Check if dendrogram is enabled and return the appropriate values.
    ...
    '''
```

**Should be:**
```python
def on_dendro_check():
    """
    Check if dendrogram is enabled and return the appropriate values.
    
    Returns
    -------
    tuple of (bool, bool) or (None, None)
        Annotation dendrogram and feature dendrogram flags
    """
```

---

#### 4. **Incomplete Docstrings** ⚠️
**Location:** `feat_vs_anno_server.py`, lines 9, 26

**Issue:** Helper functions lack proper NumPy-style documentation.

**`on_layer_check()` needs:**
```python
def on_layer_check():
    """
    Get the selected layer name or None for original data.
    
    Returns
    -------
    str or None
        Layer name if not "Original", otherwise None
    """
```

**`get_adata()` needs enhancement:**
```python
@reactive.calc
def get_adata():
    """
    Get the main AnnData object from shared state.
    
    Returns
    -------
    anndata.AnnData
        AnnData object reconstructed from shared data components
    """
```

---

#### 5. **Missing UI Function Docstring** ⚠️
**Location:** `feat_vs_anno_ui.py`

**Issue:** Main UI function lacks documentation.

**Required:**
```python
def feat_vs_anno_ui():
    """
    Create the feature vs annotation heatmap visualization UI.
    
    Returns
    -------
    shiny.ui.NavPanel
        UI components for the feature vs annotation heatmap feature
    """
```

---

### MAJOR Issues

#### 6. **Poor Error Handling** ⚠️
**Location:** `feat_vs_anno_server.py`, lines 52-55

**Issue:** Generic exception handling with only print statement. Errors should be logged and shown to users.

**Current:**
```python
except Exception as e:
    print("Heatmap generation failed:", e)
    return None
```

**Should be (per Contributing Guidelines):**
```python
except ValueError as e:
    error_msg = f"Heatmap generation failed with invalid parameters: {str(e)}"
    logger.error(error_msg)
    # Consider showing error to user via notification
    return None
except Exception as e:
    error_msg = f"Unexpected error during heatmap generation: {str(e)}"
    logger.error(error_msg)
    return None
```

**Reference:** Contributing guide states "Make sure to log error messages" and "Error messages should include enough context on what is expected."

---

#### 7. **Missing Input Validation** ⚠️
**Location:** `feat_vs_anno_server.py`, line 41

**Issue:** No `req()` checks for required inputs before processing.

**Should add:**
```python
@output
@render.plot(alt="Heatmap Plot")
@reactive.event(input.go_hm1, ignore_none=True)
def spac_Heatmap():
    req(input.hm1_anno())
    req(input.hm1_layer())
    
    adata = get_adata()
    if adata is None:
        return None
```

**Reference:** See `nearest_neighbor_server.py` for proper use of `req()`.

---

#### 8. **Nested Function Definition** ⚠️
**Location:** `feat_vs_anno_server.py`, line 88

**Issue:** `abbreviate_labels()` is defined inside the rendering function, making it untestable and inefficient.

**Should be:** Move to module level or to `utils/data_processing.py`

```python
def abbreviate_labels(labels, limit):
    """
    Abbreviate label text to specified character limit.
    
    Parameters
    ----------
    labels : list of matplotlib.text.Text
        Axis labels to abbreviate
    limit : int
        Maximum character length for each label
        
    Returns
    -------
    list of str
        Abbreviated label texts
    """
    return [label.get_text()[:limit] if label.get_text() else "" for label in labels]
```

---

#### 9. **Potential None Reference Error** ⚠️
**Location:** `feat_vs_anno_server.py`, line 128

**Issue:** `update_min_max()` doesn't check if `input.hm1_anno()` exists before using it.

**Current:**
```python
mask = adata.obs[input.hm1_anno()].notna()
```

**Should be:**
```python
@reactive.effect
@reactive.event(input.hm1_layer)
def update_min_max():
    req(input.hm1_anno())
    req(input.hm1_layer())
    
    adata = get_adata()
    # ... rest of code
```

---

### MINOR Issues

#### 10. **Inconsistent Spacing** ⚠️
**Location:** `ui/feat_vs_anno_ui.py`, line 88

**Issue:** Missing space after comma in color map list.

**Current:**
```python
"cividis","coolwarm", "RdYlBu", "Spectral",
```

**Should be:**
```python
"cividis", "coolwarm", "RdYlBu", "Spectral",
```

---

#### 11. **TODO Comments** ⚠️
**Location:** Multiple places

**Issue:** Two TODO comments present - should be tracked as issues.

1. Line 114 in UI: `# TODO: Add figure configuration as in nearest_neighbor_ui.py`
2. Line 127 in UI: `# TODO: Decide whether to refactor it to input_numeric as in nn`

**Action:** Create GitHub issues for these and reference them in comments.

---

#### 12. **Unused Import** ⚠️
**Location:** `ui/feat_vs_anno_ui.py`, line 2

**Issue:** `accessible_slider` is imported but not used (only `ui` is used).

**Should be:** Remove unused import:
```python
from shiny import ui
# from utils.accessibility import accessible_slider  # Not currently used
```

---

#### 13. **Missing ARIA Labels** ⚠️
**Location:** Throughout `feat_vs_anno_ui.py`

**Issue:** Input elements lack explicit ARIA labels for screen readers.

**Example improvement:**
```python
ui.input_numeric(
    "hm1_x_label_rotation",
    "Rotate X Axis Labels (degrees)",
    min=0,
    max=90,
    value=50,
    **{"aria-label": "X axis label rotation angle in degrees"}
)
```

**Reference:** Copilot instructions state "Use semantic HTML elements and proper ARIA labels."

---

#### 14. **Magic Numbers** ⚠️
**Location:** `feat_vs_anno_server.py`, line 106

**Issue:** Hardcoded layout values without explanation.

**Current:**
```python
fig.fig.tight_layout(rect=[0.02, 0.02, 0.98, 0.98])  # Prevent the label to exceed the right border
```

**Should be:** Define constants or add more detailed explanation:
```python
# Adjust figure layout with small margins to prevent label clipping
# rect format: [left, bottom, right, top] as fraction of figure size
LAYOUT_RECT = [0.02, 0.02, 0.98, 0.98]
fig.fig.tight_layout(rect=LAYOUT_RECT)
```

---

#### 15. **Inconsistent Line Length** ⚠️
**Location:** Multiple places

**Issue:** Some lines exceed 79 characters (PEP 8 guideline).

**Examples:**
- Line 88-92 in server file
- Several lines in UI file

**Note:** While the project may allow longer lines, PEP 8 recommends 79 characters for code.

---

### DOCUMENTATION Issues

#### 16. **Missing Function Return Context** ⚠️
**Location:** `feat_vs_anno_server.py`, `spac_Heatmap()`

**Issue:** No docstring explaining what the function renders or returns.

**Should add:**
```python
@output
@render.plot(alt="Heatmap Plot")
@reactive.event(input.go_hm1, ignore_none=True)
def spac_Heatmap():
    """
    Render hierarchical heatmap of features vs annotations.
    
    This function generates a clustered heatmap showing the relationship
    between selected features (columns) and cell annotations (rows).
    
    Returns
    -------
    matplotlib.figure.Figure or None
        Heatmap figure with optional dendrograms, or None if generation fails
    """
```

---

#### 17. **No Examples in Docstrings** ⚠️
**Location:** All helper functions

**Issue:** NumPy style recommends including usage examples where appropriate.

**Example for `abbreviate_labels()`:**
```python
Examples
--------
>>> labels = [MockLabel("very_long_name"), MockLabel("short")]
>>> abbreviate_labels(labels, 5)
['very_', 'short']
```

---

### CODE QUALITY Issues

#### 18. **Tight Coupling** ⚠️
**Location:** `feat_vs_anno_server.py`, line 28-34

**Issue:** Direct reconstruction of AnnData from shared components could fail silently if data structure changes.

**Suggestion:** Add defensive checks:
```python
@reactive.calc
def get_adata():
    """Get the main AnnData object from shared state."""
    try:
        return ad.AnnData(
            X=shared['X_data'].get(),
            obs=pd.DataFrame(shared['obs_data'].get()),
            var=pd.DataFrame(shared['var_data'].get()),
            layers=shared['layers_data'].get(),
            dtype=shared['X_data'].get().dtype
        )
    except KeyError as e:
        logger.error(f"Missing required data component: {e}")
        return None
```

---

#### 19. **Repetitive Code** ⚠️
**Location:** `feat_vs_anno_server.py`, lines 98-105

**Issue:** Font setting loop is repeated for x and y labels.

**Could refactor to:**
```python
def set_label_font(labels, fontsize, fontfamily="DejaVu Sans"):
    """Set font properties for axis labels."""
    for label in labels:
        label.set_fontsize(fontsize)
        label.set_fontfamily(fontfamily)

# Usage:
set_label_font(fig.ax_heatmap.get_xticklabels(), axis_fontsize)
set_label_font(fig.ax_heatmap.get_yticklabels(), axis_fontsize)
```

---

#### 20. **No Unit Tests** ⚠️
**Location:** Project structure

**Issue:** Contributing guidelines state "All contributed code should have unittests."

**Required:** Create `tests/test_feat_vs_anno_server.py` with tests for:
- `on_layer_check()`
- `on_dendro_check()`
- `abbreviate_labels()`
- Input validation
- Error handling

---

## 📋 Commit Message Review

### Commits in PR:
1. `fix(fva): annotate input title`
2. `changing sliders to numeric in Feat vs Annotation window`
3. `fix: solve image-has-no-accessible-title-issue`
4. `refactor(fva): move another adata extraction process out`
5. `chore(fva): rename all ui labels with 'hm1'`
6. `chore(fva): update feat_vs_anno_server.py for better readability`
7. `refactor(fva): restructure feat vs anno tab ui/server logic`
8. `fix(ui): Prevent labels to exceed borders in FvA tab`
9. `feat(ui): improve Feat. vs Anno. tab ui as in Nearest Neighbor tab`
10. `Update feat_vs_anno_server.py with better readability for the labels`

### Issues:
- ❌ Commit #2: Not in conventional format (missing type/scope)
- ❌ Commit #10: Not in conventional format at all
- ⚠️ Commit #5, #6: Could be squashed together
- ✅ Commits #1, #3, #4, #7, #8, #9: Follow conventional format correctly

**Recommendation:** Squash commits before merging and ensure all follow conventional format.

---

## 📊 Checklist from Contributing Guidelines

### Pull Request Guidelines
- [ ] **Additional tests included** - No tests added
- [ ] **Documentation updated** - No docstrings added
- [ ] **Works for all supported OS** - Cannot verify without tests

### General Code Quality
- [ ] **Modular code** - ✅ Good separation of concerns
- [ ] **Functions do one thing** - ✅ Mostly good
- [ ] **All code has unittests** - ❌ No tests provided
- [ ] **Functions that change in place don't return** - ✅ N/A for this PR
- [ ] **NumPy style docstrings** - ❌ Missing or incomplete
- [ ] **PEP 8 compliance** - ⚠️ Minor violations

### Error Handling
- [ ] **Reuse utility functions** - ⚠️ Could improve
- [ ] **Error messages include context** - ❌ Only print statements
- [ ] **Use double quotes for user values** - N/A
- [ ] **Log error messages** - ❌ Not implemented

### Figures
- [ ] **Include axis names and titles** - ✅ From SPAC library
- [ ] **Programmatic labeling** - ✅ Good
- [ ] **No hard-coded titles** - ✅ Good

### Accessibility
- [ ] **Color contrast ratios** - ✅ Using theme colors
- [ ] **Keyboard accessible** - ✅ UI structure supports it
- [ ] **ARIA labels** - ⚠️ Could add more
- [ ] **Alt text for plots** - ✅ Added

---

## 🔧 Recommended Actions Before Merge

### Must Fix (Blocking)
1. Add module-level docstrings to both files
2. Add NumPy-style docstrings to all functions
3. Fix docstring quote style (`"""` not `'''`)
4. Add proper error handling with logging
5. Add input validation with `req()`
6. Remove unused import (`accessible_slider`)

### Should Fix (High Priority)
7. Move `abbreviate_labels()` to utils or module level
8. Add defensive checks in `get_adata()`
9. Add unit tests for new functionality
10. Create GitHub issues for TODO comments
11. Squash and clean up commit messages

### Nice to Have (Low Priority)
12. Add more ARIA labels
13. Extract magic numbers to constants
14. Refactor repetitive font-setting code
15. Add usage examples to docstrings
16. Fix minor PEP 8 line length issues

---

## 💡 Suggestions for Future PRs

1. **Test-Driven Development**: Write tests before implementing features
2. **Documentation First**: Write docstrings as you write functions
3. **Incremental Commits**: Make smaller, focused commits that are easy to review
4. **Utility Functions**: Check `utils/` folder for reusable code before implementing
5. **Error Handling Pattern**: Establish a consistent error handling utility across the project

---

## 🎯 Overall Assessment

**Status:** ⚠️ **Needs Revisions Before Merge**

**Positives:**
- Good UI/UX improvements
- Feature additions are valuable
- Code structure improvements
- Follows project styling patterns

**Concerns:**
- Missing critical documentation
- Inadequate error handling
- No unit tests
- Some code quality issues

**Recommendation:** Request changes to address documentation and error handling before merging. The functionality is good, but the code doesn't meet the project's quality standards as defined in the contributing guidelines.

**Estimated Effort to Fix:** 2-3 hours for must-fix items, 4-6 hours including tests.
