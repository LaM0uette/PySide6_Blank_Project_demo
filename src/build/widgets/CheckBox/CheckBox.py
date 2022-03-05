from src import *
from src.build.widgets.CheckBox.Build import Build


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
    bg = Rgb().tr()

    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            bg=self.bg,
            bg_hover=self.bg,
            bg_checked=self.bg,
            bg_checked_hover=self.bg,
            fg=Rgb().th3(),
            fg_checked=Rgb().th3(),
            img_margin=(0, 0, 0, (vb_wg.HEIGHT - (vb_wg.HEIGHT * StyleBase().x_ico())) / 2),
        )
