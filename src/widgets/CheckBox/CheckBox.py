from src.lib.palettes import *
from src.widgets import vb_wg
from src.widgets.CheckBox.Build import Build


##################
##     BASE     ##
##################
class Base_th(Build):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            img_margin=(0, 0, 0, (vb_wg.HEIGHT - (vb_wg.HEIGHT * StyleBase().x_ico())) / 2),
        )
class Base_tr(Build):
    def __init__(self, *wgs, bg=Rgb().tr(), fg=Rgb().th3()):
        super().__init__(
            *wgs,
            bg=bg,
            bg_hover=bg,
            bg_checked=bg,
            bg_checked_hover=bg,
            fg=fg,
            fg_checked=fg,
            img_margin=(0, 0, 0, (vb_wg.HEIGHT - (vb_wg.HEIGHT * StyleBase().x_ico())) / 2),
        )

class Base:
    def __init__(self, *wgs, margin=(0, 0, 0, (vb_wg.HEIGHT-(vb_wg.HEIGHT*StyleBase().x_ico()))/2)):
        self.wgs = wgs
        self.margin = margin

    def Base_th(self):
        Build(
            *self.wgs,
            img_margin=self.margin,
        )
    def Base_tr(self, bg=Rgb().tr(), fg=Rgb().th3()):
        Build(
            *self.wgs,
            bg=bg,
            bg_hover=bg,
            bg_checked=bg,
            bg_checked_hover=bg,
            fg=fg,
            fg_checked=fg,
            img_margin=self.margin,
        )
