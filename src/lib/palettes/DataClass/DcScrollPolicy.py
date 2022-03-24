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

    horizontal: any = PaScroll.NEED
    vertical: any = PaScroll.NEED
    size_adjust: any = PaSizeAdjustPolicy.IGNORED
