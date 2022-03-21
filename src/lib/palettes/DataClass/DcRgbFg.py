"""
DcAutoActions.%class(
    auto_repeat: bool = % \n
    auto_exclusive: bool = % \n
    auto_repeat_delay: int = % \n
    auto_repeat_interval: int = %)
"""
from dataclasses import dataclass

from src.lib.palettes import *


@dataclass
class Base:

    bg = PaRgb.TH3
    bg_hover = PaRgb.TH3
    bg_checked = PaRgb.TH1
    bg_checked_hover = PaRgb.TH1
    bg_pressed = PaRgb.TH3
    bg_checked_pressed = PaRgb.TH1

    fg = PaRgb.TH1
    fg_hover = PaRgb.BN1
    fg_checked = PaRgb.TH3
    fg_checked_hover = PaRgb.BN1
    fg_pressed = PaRgb.BN2
    fg_checked_pressed = PaRgb.BN2
