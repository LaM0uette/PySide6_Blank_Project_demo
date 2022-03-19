from src.lib.palettes import *
from src.widgets import vb_wg
from src.widgets.TextEdit.Build import Build


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
    def tr(self):
        Build(
            *self.wgs,

            bg=Rgb.TR,
            fg=Rgb.TH3
        )


##################
##     DEMO     ##
##################
class Demo:
    def __init__(self, *wgs):
        self.wgs = wgs

    def th(self):
        Build(
            *self.wgs,

            height=Dim.H5
        )
    def tr(self):
        Build(
            *self.wgs,

            height=Dim.H5,

            bg=Rgb.TR,
            fg=Rgb.TH3
        )
