"""
DcRgbFg.%class(
    gen = PaRgb.%

    base: tuple = PaRgb.%
    hover: tuple = PaRgb.%
    indeterminate: tuple = PaRgb.%
    indeterminate_hover: tuple = PaRgb.%
    checked: tuple = PaRgb.%
    checked_hover: tuple = PaRgb.%

    pressed: tuple = PaRgb.%
    indeterminate_pressed: tuple = PaRgb.%
    checked_pressed: tuple = PaRgb.%

    selection: tuple = PaRgb.%)
"""
from dataclasses import dataclass

from src.lib.palettes import *


@dataclass
class Base:
    gen: tuple = None

    base: tuple = PaRgb.TH1
    hover: tuple = PaRgb.BN1
    indeterminate: tuple = PaRgb.TH1
    indeterminate_hover: tuple = PaRgb.TH1
    checked: tuple = PaRgb.TH3
    checked_hover: tuple = PaRgb.BN1

    pressed: tuple = PaRgb.BN2
    indeterminate_pressed: tuple = PaRgb.BN2
    checked_pressed: tuple = PaRgb.BN2

    selection: tuple = PaRgb.TH3


    def __post_init__(self):
        if self.gen:
            self.base = self.gen
            self.hover = self.gen
            self.indeterminate = self.gen
            self.indeterminate_hover = self.gen
            self.checked = self.gen
            self.checked_hover = self.gen

            self.pressed = self.gen
            self.indeterminate_pressed = self.gen
            self.checked_pressed = self.gen
