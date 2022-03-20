"""
dc_ico.%class(
    ico: str = Img.% \n
    ico_rgb: str = "%" \n
    ico_width: int = Dim.% \n
    ico_height: int = Dim.%
"""

from dataclasses import dataclass


@dataclass
class Base:

    ico: str = None
    ico_rgb: str = ""
    ico_width: int = None
    ico_height: int = None
