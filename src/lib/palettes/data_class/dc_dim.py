"""
dc_dim.%class(
    horizontal: SizePolicy.%VALUE \n
    vertical: SizePolicy.%VALUE)
"""

from dataclasses import dataclass

from src.lib.palettes import Dim


@dataclass
class Base:

    fixed_width: int = None
    fixed_height: int = None

    minimum_width: int = None
    minimum_height: int = None

    maximum_width: int = None
    maximum_height: int = None


    def __post_init__(self):
        if self.fixed_width:
            self.minimum_width = self.fixed_width
            self.maximum_width = self.fixed_width

        if self.fixed_height:
            self.minimum_height = self.fixed_height
            self.maximum_height = self.fixed_height
