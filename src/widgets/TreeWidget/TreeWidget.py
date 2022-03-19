from src.lib.palettes import *
from src.widgets import vb_wg
from src.widgets.TreeWidget.Build import Build


##################
##     BASE     ##
##################
class Base:
    def __init__(self, *wgs):
        self.wgs = wgs

    def th(self):
        Build(
            *self.wgs,

            bg_header=Rgb.TH3,
            fg_header=Rgb.TH1,
        )
    def tr(self):
        bd_item = (0, 0, 0, 2)

        Build(
            *self.wgs,

            scroll_h=Scroll.OFF,
            scroll_v=Scroll.OFF,

            bg=Rgb().tr(),
            bg_item=Rgb().tr(),
            bg_item_hover=Rgb().tr(),
            bg_item_checked=Rgb().tr(),
            bg_item_checked_hover=Rgb().tr(),
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
    def option(self):
        bd_gen = (0, 0, 2, 0)
        bd_item = (0, 0, 0, 2)

        Build(
            *self.wgs,

            width=Dim.H5,

            scroll_h=Scroll.OFF,
            scroll_v=Scroll.OFF,

            bg=Rgb().tr(),
            bg_item=Rgb().tr(),
            bg_item_hover=Rgb().tr(),
            bg_item_checked=Rgb().tr(),
            bg_item_checked_hover=Rgb().tr(),
            bg_header=Rgb.TH1,
            fg_item=Rgb.TH3,
            fg_item_checked=Rgb.BN1,
            fg_header=Rgb.TH1,

            border=bd_gen,
            border_hover=bd_gen,
            border_rgb=Rgb.TH2,
            border_hover_rgb=Rgb.TH2,
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
