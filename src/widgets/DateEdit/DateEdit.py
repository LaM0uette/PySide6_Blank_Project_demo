from src.lib.palettes import *
from src.widgets import vb_wg
from src.widgets.DateEdit.Build import Build


##################
##     BASE     ##
##################
class Base:
    def __init__(self, *wgs, margin=((vb_wg.HEIGHT - vb_wg.IMG_HEIGHT) / 2, 0, (vb_wg.HEIGHT - vb_wg.IMG_HEIGHT) / 2, 0)):
        self.wgs = wgs
        self.margin = margin

    def th(self):
        Build(
            *self.wgs,

            img=PaImg.CALENDRIER,
            img_hover=PaImg.CALENDRIER,
            img_rgb="",
            img_hover_rgb="",
            img_margin=self.margin,
        )
    def tr(self):
        Build(
            *self.wgs,

            bg=PaRgb.TR,
            bg_hover=PaRgb.TR,
            bg_selection=PaRgb.TH3,
            fg=PaRgb.TH3,
            fg_selection=PaRgb.TH1,

            img=PaImg.CALENDRIER,
            img_hover=PaImg.CALENDRIER,
            img_rgb="",
            img_hover_rgb="",
            img_margin=self.margin,
        )
