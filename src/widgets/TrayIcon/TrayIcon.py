from src.lib.palettes import *
from src.widgets import vb_wg
from src.widgets.TrayIcon.Build import Build


##################
##     BASE     ##
##################
class Main(Build):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,

            bg=Rgb.TH1,
            bg_item=Rgb.TH1,
            bg_item_checked=Rgb.TH1,
            fg=Rgb().th3(),
            fg_item=Rgb().th3(),
            fg_item_checked=Rgb().bn1(),

            border=(StyleBase.BORDER, )*4,
            border_rgb=Rgb.TH2,

            border_item=(0, StyleBase.BORDER, 0, 0),
            border_item_checked=(0, StyleBase.BORDER, 0, 0),
            border_item_rgb=Rgb.TH1,
            border_item_checked_rgb=Rgb.TH2,
            radius_item=(0, )*4,

            height_separator=3,
            margin=(2, 2, 15, 15),
        )
