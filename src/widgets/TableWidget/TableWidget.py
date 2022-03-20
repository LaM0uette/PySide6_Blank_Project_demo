from src.lib.palettes import *
from src.widgets import vb_wg
from src.widgets.TableWidget.Build import Build


##################
##     BASE     ##
##################
class Base:
    def __init__(self, *wgs):
        self.wgs = wgs

    def th(self):
        Build(
            *self.wgs,

            bg_corner=PaRgb.TH1,

            border=(PaStyleBase.BORDER,) * 4,
            border_rgb=PaRgb.TH3,
        )
    def tr(self):
        Build(
            *self.wgs,

            header_h=False,
            header_v=False,

            bg_corner=PaRgb.TH1,
            bg=PaRgb.TR,
            bg_item=PaRgb.TR,
            bg_item_hover=PaRgb.TR,
            bg_item_checked=PaRgb.TH3,
            bg_item_checked_hover=PaRgb.TH3,
            fg_item=PaRgb.TH3,
            fg_item_checked=PaRgb.TH1,
        )


##################
##     DEMO     ##
##################
class Demo:
    def __init__(self, *wgs):
        self.wgs = wgs
    def th(self):
        bd_gen = ((1,) * 4)
        rgb_hd = PaRgb.TH1
        rgb_item = PaRgb.TH2

        Build(
            *self.wgs,

            height=PaDim.H4,

            bg_corner=PaRgb.TH1,

            border=(PaStyleBase.BORDER,) * 4,
            border_rgb=PaRgb.TH3,
            border_hd=bd_gen,
            border_hd_hover=bd_gen,
            border_hd_checked=bd_gen,
            border_hd_checked_hover=bd_gen,
            border_hd_rgb=rgb_hd,
            border_hd_hover_rgb=rgb_hd,
            border_hd_checked_rgb=rgb_hd,
            border_hd_checked_hover_rgb=rgb_hd,
            border_item=bd_gen,
            border_item_hover=bd_gen,
            border_item_checked=bd_gen,
            border_item_checked_hover=bd_gen,
            border_item_rgb=rgb_item,
            border_item_hover_rgb=rgb_item,
            border_item_checked_rgb=rgb_item,
            border_item_checked_hover_rgb=rgb_item,
        )
    def tr(self):
        Build(
            *self.wgs,

            height=PaDim.H4,
            header_h=False,
            header_v=False,

            bg_corner=PaRgb.TH1,
            bg=PaRgb.TR,
            bg_item=PaRgb.TR,
            bg_item_hover=PaRgb.TR,
            bg_item_checked=PaRgb.TH3,
            bg_item_checked_hover=PaRgb.TH3,
            fg_item=PaRgb.TH3,
            fg_item_checked=PaRgb.TH1,
        )
