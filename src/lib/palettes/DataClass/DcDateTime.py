"""
DcDateTime.%class(
    date: tuple = (%, %, %)
    time: tuple = (%, %, %))
"""
import datetime
from dataclasses import dataclass


@dataclass
class Base:

    d = datetime.datetime.now().strftime("%Y_%m_%d").split("_")

    date: tuple = (d[0], d[1], d[2])
    time: tuple = None

    def __post_init__(self):
        if not self.time:
            self.time = (0, 0, 0)
