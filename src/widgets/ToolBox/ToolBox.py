from src.lib.palettes import *
from src.widgets import vb_wg
from src.widgets.ToolBox.Build import Build


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
        bd_hd = (0, StyleBase.BORDER, 0, 0)
        rgb_hb = Rgb().bn1()

        Build(
            *self.wgs,

            bg=Rgb().tr(),
            bg_hover=Rgb().tr(),
            fg=Rgb.TH3,

            border_hd=bd_hd,
            border_hd_hover=bd_hd,
            border_hd_checked=bd_hd,
            border_hd_checked_hover=bd_hd,
            border_hd_rgb=rgb_hb,
            border_hd_hover_rgb=rgb_hb,
            border_hd_checked_rgb=rgb_hb,
            border_hd_checked_hover_rgb=rgb_hb,
            border=(StyleBase.BORDER,) * 4,
            border_hover=(StyleBase.BORDER,) * 4,
            border_rgb=Rgb.TH3,
            border_hover_rgb=Rgb.TH3,

            radius_tab=(0,) * 4
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
        )
    def tr(self):
        bd_hd = (0, StyleBase.BORDER, 0, 0)
        rgb_hb = Rgb().bn1()

        Build(
            *self.wgs,

            bg=Rgb().tr(),
            bg_hover=Rgb().tr(),
            fg=Rgb.TH3,

            border_hd=bd_hd,
            border_hd_hover=bd_hd,
            border_hd_checked=bd_hd,
            border_hd_checked_hover=bd_hd,
            border_hd_rgb=rgb_hb,
            border_hd_hover_rgb=rgb_hb,
            border_hd_checked_rgb=rgb_hb,
            border_hd_checked_hover_rgb=rgb_hb,
            border=(StyleBase.BORDER,) * 4,
            border_hover=(StyleBase.BORDER,) * 4,
            border_rgb=Rgb.TH3,
            border_hover_rgb=Rgb.TH3,

            radius_tab=(0,) * 4
        )
