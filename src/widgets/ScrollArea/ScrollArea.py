from src.lib.palettes import *
from src.widgets import vb_wg
from src.widgets.ScrollArea.Build import Build


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
