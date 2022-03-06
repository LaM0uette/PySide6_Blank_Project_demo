from src.lib.palettes import *
from src.widgets import vb_wg
from src.widgets.Frame.Build import Build


##################
##     BASE     ##
##################
class Base:
    def __init__(self, *wgs):
        self.wgs = wgs

    def th(self, rgb=Rgb().th3()):
        Build(
            *self.wgs,
            bg=rgb,
        )
    def tr(self, rgb=Rgb().th3()):
        Build(
            *self.wgs,
            bg=rgb,
        )


##################
##     MENU     ##
##################
class Menu:
    def __init__(self, *wgs, bg=Rgb().th2(), height=Dim().h9(), radius=(0, 0, vb_wg.RADIUS_SIZE - 1, vb_wg.RADIUS_SIZE - 1)):
        self.wgs = wgs
        self.bg = bg
        self.height = height
        self.radius = radius

    def top(self):
        Build(
            *self.wgs,

            height=self.height,

            bg=Rgb().th1(),
            radius=(vb_wg.RADIUS_SIZE, vb_wg.RADIUS_SIZE, 0, 0)
        )
    def bottom(self):
        Build(
            *self.wgs,

            height=Dim().h10(),

            bg=self.bg,
            radius=self.radius
        )
    def bottom_dlg(self):
        Build(
            *self.wgs,

            height=self.height,

            bg=self.bg,
            radius=self.radius
        )


####################
##     CADRES     ##
####################
class Cadre:
    def __init__(self, *wgs):
        self.wgs = wgs

    def rtn(self, rgb):
        Build(
            *self.wgs,
            bg=Rgb().tr(),
            border=(StyleBase().border(),) * 4,
            border_rgb=rgb,
            border_hover=(StyleBase().border(),) * 4,
            border_hover_rgb=rgb,
            radius = (vb_wg.RADIUS_SIZE, )*4
        )

    def th1(self): self.rtn(rgb=Rgb().th1())
    def th2(self): self.rtn(rgb=Rgb().th2())
    def th3(self): self.rtn(rgb=Rgb().th3())
    def bn1(self): self.rtn(rgb=Rgb().bn1())
    def bn2(self): self.rtn(rgb=Rgb().bn2())


####################
##     AUTRES     ##
####################
class palette_rgb(Build):
    def __init__(self, *wgs, rgb):
        super().__init__(
            *wgs,
            bg=rgb,
            radius=(40, )*4,
    )
class SplashScreen(Build):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            bg=Rgb().th1(),
            border=(StyleBase().border(),) * 4,
            border_rgb=Rgb().th3(),
            border_hover=(StyleBase().border(),) * 4,
            border_hover_rgb=Rgb().th3(),
            radius=(vb_wg.RADIUS_SIZE, )*4
    )
class TrayUi(Build):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            bg=Rgb().th1(),
            border=(StyleBase().border(),) * 4,
            border_rgb=Rgb().th3(),
            border_hover=(StyleBase().border(),) * 4,
            border_hover_rgb=Rgb().th3(),
            radius=(vb_wg.RADIUS, )*4
    )


##################
##     DEMO     ##
##################
class Demo_hover(Build):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            bg=Rgb().tr(),
            border=(StyleBase().border(),) * 4,
            border_rgb=Rgb().bn1(),
            border_hover=(StyleBase().border(),) * 4,
            border_hover_style="dashed",
            border_hover_rgb=Rgb().bn1(),
            radius=(vb_wg.RADIUS_SIZE, )*4
    )
