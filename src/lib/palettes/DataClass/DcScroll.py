"""
DcScrollPolicy.%class(
    horizontal: any = PaScroll.%
    vertical: any = PaScroll.%
    size_adjust: any = PaSizeAdjustPolicy.%)
"""

from dataclasses import dataclass

from src.lib.palettes import *


@dataclass
class Base:

    bg = PaRgb.TH1
    width = 10
    height = 10
    handle_bg = PaRgb.TH3
    handle_bg_hover = PaRgb.TH3
    handle_fg = PaRgb.TH2
    handle_fg_hover = PaRgb.BN1
    handle_min_width = 20
    handle_min_height = 20


SCROLL_BG = PaRgb.TH1
SCROLL_WIDTH = 10
SCROLL_HEIGHT = 10
SCROLL_HANDLE_BG = PaRgb.TH3
SCROLL_HANDLE_BG_HOVER = PaRgb.TH3
SCROLL_HANDLE_FG = PaRgb.TH2
SCROLL_HANDLE_FG_HOVER = PaRgb.BN1
SCROLL_HANDLE_MIN_WIDTH = 20
SCROLL_HANDLE_MIN_HEIGHT = 20
