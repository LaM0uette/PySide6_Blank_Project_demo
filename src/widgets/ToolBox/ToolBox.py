from PySide6 import QtWidgets

from src.build import *
from src.build.widgets import VBase




##################
##     BASE     ##
##################
class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
        )
class Base_tr(Style):
    bd_hd = (0, StyleBase().bd(), 0, 0)
    rgb_hb = Rgb().bn1()

    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            bg=Rgb().tr(),
            bg_hover=Rgb().tr(),
            fg=Rgb().th3(),
            border_hd=self.bd_hd,
            border_hd_hover=self.bd_hd,
            border_hd_checked=self.bd_hd,
            border_hd_checked_hover=self.bd_hd,
            border_hd_rgb=self.rgb_hb,
            border_hd_hover_rgb=self.rgb_hb,
            border_hd_checked_rgb=self.rgb_hb,
            border_hd_checked_hover_rgb=self.rgb_hb,
            border=((StyleBase().bd(), )*4),
            border_hover=((StyleBase().bd(), )*4),
            border_rgb=Rgb().th3(),
            border_hover_rgb=Rgb().th3(),
            radius_tab=((0, )*4)
    )


##################
##     DEMO     ##
##################
class Demo_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
        )
class Demo_tr(Style):
    bd_hd = (0, StyleBase().bd(), 0, 0)
    rgb_hb = Rgb().bn1()

    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            bg=Rgb().tr(),
            bg_hover=Rgb().tr(),
            fg=Rgb().th3(),
            border_hd=self.bd_hd,
            border_hd_hover=self.bd_hd,
            border_hd_checked=self.bd_hd,
            border_hd_checked_hover=self.bd_hd,
            border_hd_rgb=self.rgb_hb,
            border_hd_hover_rgb=self.rgb_hb,
            border_hd_checked_rgb=self.rgb_hb,
            border_hd_checked_hover_rgb=self.rgb_hb,
            border=((StyleBase().bd(), )*4),
            border_hover=((StyleBase().bd(), )*4),
            border_rgb=Rgb().th3(),
            border_hover_rgb=Rgb().th3(),
            radius_tab=((0, )*4)
    )
