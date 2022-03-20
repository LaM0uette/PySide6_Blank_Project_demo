"""
dc_size_policy.%class(
    horizontal: SizePolicy.% \n
    vertical: SizePolicy.%)
"""

from dataclasses import dataclass

from src.lib.palettes import SizePolicy


@dataclass
class Base:

    horizontal: any = SizePolicy.PREFERED
    vertical: any = SizePolicy.PREFERED
