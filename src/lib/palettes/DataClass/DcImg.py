"""
DcImg.%class(
    base: str = PaImg.%
    uncheck: str = PaImg.%
    uncheck_hover: str = PaImg.%
    check: str = PaImg.%
    check_hover: str = PaImg.%
    indeterminate: str = PaImg.%
    indeterminate_hover: str = PaImg.%
    unroll: str = PaImg.%
    unroll_hover: str = PaImg.%
    up: str = PaImg.%
    up_hover: str = PaImg.%
    down: str = PaImg.%
    down_hover: str = PaImg.%
    right: str = PaImg.%
    right_hover: str = PaImg.%
    left: str = PaImg.%
    left_hover: str = PaImg.%

    base_rgb: str = "%"
    uncheck_rgb: str = "%"
    uncheck_hover_rgb: str = "%"
    check_rgb: str = "%"
    check_hover_rgb: str = "%"
    indeterminate_rgb: str = "%"
    indeterminate_hover_rgb: str = "%"
    unroll_rgb: str = "%"
    unroll_hover_rgb: str = "%"
    up_rgb: str = "%"
    up_hover_rgb: str = "%"
    down_rgb: str = "%"
    down_hover_rgb: str = "%"
    right_rgb: str = "%"
    right_hover_rgb: str = "%"
    left_rgb: str = "%"
    left_hover_rgb: str = "%")
"""

from dataclasses import dataclass

from src.lib.palettes import PaImg


@dataclass
class Base:
    width: int = None
    height: int = None

    base: str = PaImg.MAIN
    uncheck: str = PaImg.CHECK0
    uncheck_hover: str = None
    check: str = PaImg.CHECK2
    check_hover: str = None
    indeterminate: str = PaImg.CHECK1
    indeterminate_hover: str = None
    unroll: str = PaImg.FLECHE_BOTTOM
    unroll_hover: str = None
    up: str = PaImg.PLUS
    up_hover: str = None
    down: str = PaImg.MOINS
    down_hover: str = None
    right: str = PaImg.FLECHE_RIGHT
    right_hover: str = None
    left: str = PaImg.FLECHE_LEFT
    left_hover: str = None

    base_rgb: str = "th2"
    uncheck_rgb: str = "th2"
    uncheck_hover_rgb: str = "bn1"
    check_rgb: str = "th2"
    check_hover_rgb: str = "bn1"
    indeterminate_rgb: str = "th3"
    indeterminate_hover_rgb: str = "th1"
    unroll_rgb: str = "th2"
    unroll_hover_rgb: str = "bn1"
    up_rgb: str = "th2"
    up_hover_rgb: str = "bn1"
    down_rgb: str = "th2"
    down_hover_rgb: str = "bn1"
    right_rgb: str = "th3"
    right_hover_rgb: str = "bn1"
    left_rgb: str = "th3"
    left_hover_rgb: str = "bn1"


    def __post_init__(self):
        self.uncheck_hover = self.uncheck_hover or self.uncheck
        self.check_hover = self.check_hover or self.check
        self.indeterminate_hover = self.indeterminate_hover or self.indeterminate
        self.unroll_hover = self.unroll_hover or self.unroll
        self.up_hover = self.up_hover or self.up
        self.down_hover = self.down_hover or self.down
        self.right_hover = self.right_hover or self.right
        self.left_hover = self.left_hover or self.left
