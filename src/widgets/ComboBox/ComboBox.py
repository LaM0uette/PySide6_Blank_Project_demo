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
            cursor=Cur.SOURIS_MAIN,

            bg=Rgb().tr(),
            bg_hover=Rgb().tr(),
            bg_selection=Rgb.TH3,
            fg=Rgb.TH3,
            fg_selection=Rgb.TH1,
        )
    def font(self, font=vb_wg.FONT):
        Build(
            *self.wgs,
            font=font
        )
