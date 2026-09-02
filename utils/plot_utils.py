"""
Plotting utility functions for SPAC Shiny application.

This module provides reusable helper functions for customizing matplotlib
plots, such as axis label formatting and styling.
"""

import io
from typing import List

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib.text import Text


def fig_to_png_bytes(fig) -> bytes:
    """Serialize a figure to uncropped PNG bytes and close it.

    The figure's configured DPI is preserved. Objects exposing an underlying
    Matplotlib figure through ``.fig`` are also supported.

    Parameters
    ----------
    fig
        Matplotlib figure or figure-owning object to serialize.

    Returns
    -------
    bytes
        PNG data preserving the figure's intrinsic boundary.
    """

    underlying = fig.fig if hasattr(fig, "fig") else fig
    try:
        with io.BytesIO() as buffer:
            underlying.savefig(
                buffer,
                format="png",
                dpi=underlying.get_dpi(),
                bbox_inches=None,
            )
            return buffer.getvalue()
    finally:
        plt.close(underlying)


def png_bytes_to_figure(png_bytes: bytes):
    """Create a display-only Matplotlib wrapper for PNG bytes.

    The returned figure contains the rasterized image rather than the
    original plot artists. Its DPI and layout exist only to support stable
    presentation through Shiny's ``render.plot``.

    Parameters
    ----------
    png_bytes : bytes
        PNG data to display.

    Returns
    -------
    matplotlib.figure.Figure
        Decoration-free wrapper containing the complete PNG.
    """

    image = mpimg.imread(io.BytesIO(png_bytes))
    height_px, width_px = image.shape[:2]
    display_dpi = 100

    fig, ax = plt.subplots(
        figsize=(width_px / display_dpi, height_px / display_dpi),
        dpi=display_dpi,
    )
    ax.imshow(image)
    ax.axis("off")
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)

    # Keep the image flush with the wrapper during Shiny redraws.
    fig.set_layout_engine(
        "tight",
        pad=0,
        h_pad=0,
        w_pad=0,
        rect=(0, 0, 1, 1),
    )
    return fig


def abbreviate_labels(labels: List[Text], limit: int) -> List[str]:
    """
    Abbreviate a list of matplotlib Text objects.

    Parameters
    ----------
    labels : List[matplotlib.text.Text]
        List of label objects to abbreviate.
    limit : int
        Maximum number of characters allowed.

    Returns
    -------
    List[str]
        List of abbreviated label strings.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> fig, ax = plt.subplots()
    >>> ax.set_xticklabels(["LongLabel1", "LongLabel2", "Short"])
    >>> abbreviated = abbreviate_labels(ax.get_xticklabels(), limit=5)
    >>> print(abbreviated)
    ['LongL', 'LongL', 'Short']
    """
    return [label.get_text()[:limit] if label.get_text() else ""
            for label in labels]


def apply_axis_style(labels: List[Text], fontsize: int,
                     fontfamily: str = "DejaVu Sans") -> None:
    """
    Apply font size and family to axis labels.

    Parameters
    ----------
    labels : List[matplotlib.text.Text]
        List of label objects to style.
    fontsize : int
        Font size to apply.
    fontfamily : str, optional
        Font family to apply, by default "DejaVu Sans".

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> fig, ax = plt.subplots()
    >>> ax.set_xlabel("X Label")
    >>> apply_axis_style(ax.get_xticklabels(), fontsize=12)
    """
    for label in labels:
        label.set_fontsize(fontsize)
        label.set_fontfamily(fontfamily)
