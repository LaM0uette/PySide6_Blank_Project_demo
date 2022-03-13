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
        super().__init__(
            widget,
            bg=Rgb().tr(),
            bg_hover=Rgb().tr(),
            bg_checked=Rgb().tr(),
            bg_checked_hover=Rgb().tr(),
            bg_pressed=Rgb().tr(),
            bg_checked_pressed=Rgb().tr(),
            fg=Rgb().th3(),
            fg_checked=Rgb().bn1(),
        )
