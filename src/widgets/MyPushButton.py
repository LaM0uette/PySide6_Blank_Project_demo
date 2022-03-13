from .WgClass.MyQPushButtonStyle import Style
from src.lib.palettes import *


##################
##     BASE     ##
##################
class Base(Style):
    def __init__(self, widget):
        super().__init__(
            widget,
        )
class Transparent(Style):
    def __init__(self, widget):
        bg = Rgb().tr()

        super().__init__(
            widget,
            bg=bg,
            bg_hover=bg,
            bg_checked=bg,
            bg_checked_hover=bg,
            bg_pressed=bg,
            bg_checked_pressed=bg,
            fg=Rgb().th3(),
            fg_checked=Rgb().bn1(),
        )
