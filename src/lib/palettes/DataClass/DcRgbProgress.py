"""
DcRgbFg.%class(
    gen = PaRgb.% \n
    base: tuple = PaRgb.% \n
    hover: tuple = PaRgb.% \n
    texte: tuple = PaRgb.% \n
    texte_hover: tuple = PaRgb.%
"""
from dataclasses import dataclass

from src.lib.palettes import *


@dataclass
class Base:
    gen: tuple = None

    base: tuple = PaRgb.TH1
    hover: tuple = PaRgb.BN1
    texte: tuple = PaRgb.TH3
    texte_hover: tuple = PaRgb.TH3


    def __post_init__(self):
        if self.gen:
            self.base = self.gen
            self.hover = self.gen
            self.texte = self.gen
            self.texte_hover = self.gen
