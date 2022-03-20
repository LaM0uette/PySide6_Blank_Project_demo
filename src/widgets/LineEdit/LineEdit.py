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

            bg=PaRgb.TR,
            fg=PaRgb.TH3
        )
    def rgb_hex(self):
        Build(
            *self.wgs,

            align_horizontal=PaAlign.CENTER_HORIZONTAL,

            bg=PaRgb.TR,
            bg_selection=PaRgb.TH3,
            fg=PaRgb.TH3,
            fg_selection=PaRgb.TH1,
        )
