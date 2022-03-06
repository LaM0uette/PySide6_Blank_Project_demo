from PySide6 import QtWidgets

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
            bg=Rgb().tr()
        )


##################
##     DEMO     ##
##################
class Demo(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            bg=Rgb().th1(),
    )
