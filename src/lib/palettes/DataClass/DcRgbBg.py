"""
DcAutoActions.%class(
    auto_repeat: bool = % \n
    auto_exclusive: bool = % \n
    auto_repeat_delay: int = % \n
    auto_repeat_interval: int = %
"""
from dataclasses import dataclass

from src.lib.palettes import *


@dataclass
class Base:

    # Base
    base: tuple = PaRgb.TH3
    alternative: tuple = PaRgb.TH2
    hover: tuple = PaRgb.TH3
    indeterminate: tuple = PaRgb.TH2
    indeterminate_hover: tuple = PaRgb.TH2
    checked: tuple = PaRgb.TH1
    checked_hover: tuple = PaRgb.TH1

    # Pressed
    pressed: tuple = PaRgb.TH3
    checked_pressed: tuple = PaRgb.TH1
    indeterminate_pressed: tuple = PaRgb.TH1

    # Selection
    selection: tuple = PaRgb.TH1

    # Item
    item: tuple = PaRgb.TH3
    item_hover: tuple = PaRgb.TH3
    item_checked: tuple = PaRgb.TH1
    item_checked_hover: tuple = PaRgb.TH1

    # Progress
    chunk: tuple = PaRgb.TH2
    chunk_hover: tuple = PaRgb.BN1

    # Slider
    groove: tuple = PaRgb.TH3
    groove_hover: tuple = PaRgb.TH3
    groove_pressed: tuple = PaRgb.TH3
    handle: tuple = PaRgb.TH2
    handle_hover: tuple = PaRgb.TH2
    handle_pressed: tuple = PaRgb.BN1

    # Autres
    gridline: tuple = PaRgb.TH2
    separator: tuple = PaRgb.BN1
