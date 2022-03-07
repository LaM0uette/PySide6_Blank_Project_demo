from src.lib.palettes import *
from src.widgets import vb_wg
from src.widgets.CheckBox.Build import Build


##################
##     BASE     ##
##################
class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            bg_corner=Rgb().th1(),

            border=((StyleBase().bd(),) * 4),
            border_rgb=Rgb().th3(),
        )
class Base_tr(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            header_h=False,
            header_v=False,

            bg_corner=Rgb().th1(),
            bg=Rgb().tr(),
            bg_item=Rgb().tr(),
            bg_item_hover=Rgb().tr(),
            bg_item_checked=Rgb().th3(),
            bg_item_checked_hover=Rgb().th3(),
            fg_item=Rgb().th3(),
            fg_item_checked=Rgb().th1(),
    )


##################
##     DEMO     ##
##################
class Demo_th(Style):
    bd_gen = ((1, )*4)
    rgb_hd = Rgb().th1()
    rgb_item = Rgb().th2()

    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            height=Dim().h4(),

            border=((StyleBase().bd(),) * 4),
            border_rgb=Rgb().th3(),

            bg_corner=Rgb().th1(),
            border_hd=self.bd_gen,
            border_hd_hover=self.bd_gen,
            border_hd_checked=self.bd_gen,
            border_hd_checked_hover=self.bd_gen,
            border_hd_rgb=self.rgb_hd,
            border_hd_hover_rgb=self.rgb_hd,
            border_hd_checked_rgb=self.rgb_hd,
            border_hd_checked_hover_rgb=self.rgb_hd,

            border_item=self.bd_gen,
            border_item_hover=self.bd_gen,
            border_item_checked=self.bd_gen,
            border_item_checked_hover=self.bd_gen,
            border_item_rgb=self.rgb_item,
            border_item_hover_rgb=self.rgb_item,
            border_item_checked_rgb=self.rgb_item,
            border_item_checked_hover_rgb=self.rgb_item,
    )
class Demo_tr(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            height=Dim().h4(),
            header_h=False,
            header_v=False,

            bg_corner=Rgb().th1(),
            bg=Rgb().tr(),
            bg_item=Rgb().tr(),
            bg_item_hover=Rgb().tr(),
            bg_item_checked=Rgb().th3(),
            bg_item_checked_hover=Rgb().th3(),
            fg_item=Rgb().th3(),
            fg_item_checked=Rgb().th1(),
    )
