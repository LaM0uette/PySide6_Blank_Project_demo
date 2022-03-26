"""
DcAbstractItemView.%class(
    auto_scroll: bool = %
    auto_scroll_margin: int = %
    tab_navigation: bool = %
    drag_drop: any = DcScrollPolicy.%
    alternative_row_colors: bool = %
    selection_mode: any = PaSelectionMode.%
    selection_behavior: any = PaSelectionBehavior.%)
"""

from dataclasses import dataclass

from src.lib.palettes import *


@dataclass
class Base:

    auto_scroll: bool = True
    auto_scroll_margin: int = 16
    tab_navigation: bool = True
    drag_drop: any = DcScrollPolicy.Base
    alternative_row_colors: bool = True
    selection_mode: any = PaSelectionMode.SINGLE
    selection_behavior: any = PaSelectionBehavior.ROW
