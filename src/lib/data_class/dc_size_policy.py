from dataclasses import dataclass

from src.lib.palettes import SizePolicy


@dataclass
class Base:
    horizontal = SizePolicy.PREFERED
    vertical = SizePolicy.PREFERED
