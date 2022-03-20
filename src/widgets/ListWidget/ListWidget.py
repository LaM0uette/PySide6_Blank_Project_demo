from src.lib.palettes import *
from src.widgets import vb_wg
from src.widgets.ListWidget.Build import Build


##################
##     BASE     ##
##################
class Base:
    def __init__(self, *wgs):
        self.wgs = wgs

    def th(self):
        Build(
            *self.wgs,

            fg_item_checked=PaRgb.BN1,

            border=(PaStyleBase.BORDER,) * 4,
            border_rgb=PaRgb.TH3
        )
    def tr(self):
        Build(
            *self.wgs,

            bg=PaRgb.TR,
            bg_item=PaRgb.TR,
            bg_item_hover=PaRgb.TR,
            bg_item_checked=PaRgb.TR,
            bg_item_checked_hover=PaRgb.TR,
            fg_item=PaRgb.TH3,
            fg_item_checked=PaRgb.BN1,

            radius_item=(0,)*4
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

            height=PaDim.H5,

            fg_item_checked=PaRgb.BN1,
            border=(PaStyleBase.BORDER,) * 4,
            border_rgb=PaRgb.TH3
        )
    def tr(self):
        bd_item = (0, 0, 0, 2)

        Build(
            *self.wgs,

            height=PaDim.H5,

            bg=PaRgb.TR,
            bg_item=PaRgb.TR,
            bg_item_hover=PaRgb.TR,
            bg_item_checked=PaRgb.TR,
            bg_item_checked_hover=PaRgb.TR,
            fg_item=PaRgb.TH3,
            fg_item_checked=PaRgb.BN1,

            border_item=bd_item,
            border_item_hover=bd_item,
            border_item_checked=bd_item,
            border_item_checked_hover=bd_item,
            border_item_rgb=PaRgb.TH2,
            border_item_hover_rgb=PaRgb.TH3,
            border_item_checked_rgb=PaRgb.BN1,
            border_item_checked_hover_rgb=PaRgb.BN1,

            radius_item=(0,) * 4
        )
