"""
DcImg.%class(
    ico: str = PaImg.% \n
    ico_rgb: str = "%" \n
    ico_width: int = PaDim.% \n
    ico_height: int = PaDim.%)
"""

from dataclasses import dataclass

from src.lib.palettes import PaImg


@dataclass
class Base:

    base: str = PaImg.MAIN
    uncheck: str = PaImg.CHECK0
    uncheck_hover: str = PaImg.CHECK0
    check: str = PaImg.CHECK2
    check_hover: str = PaImg.CHECK2
    indeterminate: str = PaImg.CHECK1
    indeterminate_hover: str = PaImg.CHECK1
    unroll: str = PaImg.FLECHE_BOTTOM
    unroll_hover: str = PaImg.FLECHE_BOTTOM
    up: str = PaImg.PLUS
    up_hover: str = PaImg.PLUS
    down: str = PaImg.MOINS
    down_hover: str = PaImg.MOINS
    right: str = PaImg.FLECHE_RIGHT
    right_hover: str = PaImg.FLECHE_RIGHT
    left: str = PaImg.FLECHE_LEFT
    left_hover: str = PaImg.FLECHE_LEFT

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
