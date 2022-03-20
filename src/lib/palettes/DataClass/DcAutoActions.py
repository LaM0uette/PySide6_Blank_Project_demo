"""
dc_dim.%class(
    fixed_width: int = PaDim.% \n
    fixed_height: int = PaDim.% \n
    minimum_width: int = PaDim.% \n
    minimum_height: int = PaDim.% \n
    maximum_width: int = PaDim.% \n
    maximum_height: int = PaDim.%
"""

from dataclasses import dataclass


@dataclass
class Base:

    auto_repeat: bool = False
    auto_exclusive: bool = False
    auto_repeat_delay: int = 300
    auto_repeat_interval: int = 100
