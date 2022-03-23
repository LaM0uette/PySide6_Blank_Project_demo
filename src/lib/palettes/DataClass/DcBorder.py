"""
DcIco.%class(
    ico: str = PaImg.% \n
    ico_rgb: str = "%" \n
    ico_width: int = PaDim.% \n
    ico_height: int = PaDim.%)
"""

from dataclasses import dataclass

from src.lib.palettes import PaRgb


@dataclass
class Base:

    base: tuple = (0,)*4
    base_style: str = "solid"
    base_rgb: str = PaRgb.TR
    hover: tuple = None
    hover_style: str = None
    hover_rgb: str = None
    checked: tuple = None
    checked_style: str = None
    checked_rgb: str = None
    checked_hover: tuple = None
    checked_hover_style: str = None
    checked_hover_rgb: str = None

    radius: tuple = (3,)*4
