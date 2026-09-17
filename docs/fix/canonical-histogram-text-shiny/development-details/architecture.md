# Architecture

```text
Histogram template
  -> Matplotlib figure: title wrapping, existing legend placement and layout
  -> SPAC Shiny fig_to_png_bytes(): measure content and expand export boundary
  -> complete canonical PNG at the figure's configured DPI
  -> SPAC Shiny render.image: deliver those bytes
```

The package returns a Matplotlib figure. Shiny serializes that figure once,
then passes the PNG bytes to `render.image`. The figure's canvas and the
exported image boundary are distinct objects in this flow.
