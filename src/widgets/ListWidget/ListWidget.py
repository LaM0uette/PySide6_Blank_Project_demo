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

            fg_item_checked=Rgb.BN1,

            border=(StyleBase.BORDER,)*4,
            border_rgb=Rgb.TH3
        )
    def tr(self):
        Build(
            *self.wgs,

            bg=Rgb.TR,
            bg_item=Rgb.TR,
            bg_item_hover=Rgb.TR,
            bg_item_checked=Rgb.TR,
            bg_item_checked_hover=Rgb.TR,
            fg_item=Rgb.TH3,
            fg_item_checked=Rgb.BN1,

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

            fg_item_checked=Rgb.BN1,
            border=(StyleBase.BORDER,) * 4,
            border_rgb=Rgb.TH3
        )
    def tr(self):
        bd_item = (0, 0, 0, 2)

        Build(
            *self.wgs,

            height=PaDim.H5,

            bg=Rgb.TR,
            bg_item=Rgb.TR,
            bg_item_hover=Rgb.TR,
            bg_item_checked=Rgb.TR,
            bg_item_checked_hover=Rgb.TR,
            fg_item=Rgb.TH3,
            fg_item_checked=Rgb.BN1,

            border_item=bd_item,
            border_item_hover=bd_item,
            border_item_checked=bd_item,
            border_item_checked_hover=bd_item,
            border_item_rgb=Rgb.TH2,
            border_item_hover_rgb=Rgb.TH3,
            border_item_checked_rgb=Rgb.BN1,
            border_item_checked_hover_rgb=Rgb.BN1,

            radius_item=(0,) * 4
        )
