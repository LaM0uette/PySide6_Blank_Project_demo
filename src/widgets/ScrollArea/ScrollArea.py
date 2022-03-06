from src.lib.palettes import *
from src.widgets import vb_wg
from src.widgets.ScrollArea.Build import Build


##################
##     BASE     ##
##################
class Base:
    def __init__(self, *wgs):
        self.wgs = wgs

    def th(self):
        Build(
            *self.wgs,
        )
    def tr(self, bg=Rgb().tr()):
        Build(
            *self.wgs,

            bg=bg,
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
