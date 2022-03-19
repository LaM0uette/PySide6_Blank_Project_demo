from src.lib.palettes import *
from src.widgets import vb_wg
from src.widgets.LineEdit.Build import Build


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
    def rgb_hex(self):
        Build(
            *self.wgs,

            align_horizontal=Align.CENTER_HORIZONTAL,

            bg=Rgb.TR,
            bg_selection=Rgb.TH3,
            fg=Rgb.TH3,
            fg_selection=Rgb.TH1,
        )
