from PySide6 import QtGui

from src.build import *
from src.build.widgets import VBase




##################
##     BASE     ##
##################
class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
        )
class Base_tr(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            bg=Rgb().tr(),
            fg=Rgb().th3()
    )

class tr_taille(Style):
    def __init__(self, *wgs, h):
        super().__init__(
            *wgs,
            height=None,
            font_size=h,

            bg=Rgb().tr(),
            fg=Rgb().th3()
    )
class rgb_hex(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            bg=Rgb().tr(),
            bg_selection=Rgb().th3(),
            fg=Rgb().th3(),
            fg_selection=Rgb().th1(),
            align_horizontal=Align().h_center()
    )


##################
##     DEMO     ##
##################
class Demo_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            height=Dim().h5(),
    )
class Demo_tr(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            height=Dim().h5(),

            bg=Rgb().tr(),
    )
