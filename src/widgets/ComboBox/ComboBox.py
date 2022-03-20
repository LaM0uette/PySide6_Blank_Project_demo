from src.lib.palettes import *
from src.widgets import vb_wg
from src.widgets.ComboBox.Build import Build


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

            edit=True,
            cursor=PaCur.SOURIS_MAIN,

            bg=PaRgb.TR,
            bg_hover=PaRgb.TR,
            bg_selection=PaRgb.TH3,
            fg=PaRgb.TH3,
            fg_selection=PaRgb.TH1,
        )
    def font(self, font=vb_wg.FONT):
        Build(
            *self.wgs,
            font=font
        )
