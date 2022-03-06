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
class Menu_top(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            height=Dim().h9(),

            bg=Rgb().th1(),
            radius=(VBase.RADIUS, VBase.RADIUS, 0, 0)
    )
class Menu_bottom(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            height=Dim().h10(),

            bg=Rgb().th2(),
            radius=(0, 0, VBase.RADIUS-1, VBase.RADIUS-1)
    )
class Menu_bottom_dlg(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            height=Dim().h9(),

            bg=Rgb().th2(),
            radius=(0, 0, VBase.RADIUS-1, VBase.RADIUS-1)
    )


####################
##     AUTRES     ##
####################
class Cadre:
    def __init__(self, *wgs, ombre_portee=False):
        self.wgs = wgs
        self.ombre_portee = ombre_portee

    def rtn(self, rgb):
        Style(
            *self.wgs,
            ombre_portee=self.ombre_portee,
            bg=Rgb().tr(),
            border=((StyleBase().bd(),) * 4),
            border_rgb=rgb,
            border_hover=((StyleBase().bd(),) * 4),
            border_hover_rgb=rgb,
            radius = ((VBase.RADIUS+1, )*4)
        )

    def th1(self): self.rtn(rgb=Rgb().th1())
    def th2(self): self.rtn(rgb=Rgb().th2())
    def th3(self): self.rtn(rgb=Rgb().th3())
    def bn1(self): self.rtn(rgb=Rgb().bn1())
    def bn2(self): self.rtn(rgb=Rgb().bn2())
class palette_rgb(Style):
    def __init__(self, *wgs, rgb):
        super().__init__(
            *wgs,
            bg=rgb,
            radius=((40, )*4),
    )
class SplashScreen(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            ombre_portee=True,
            bg=Rgb().th1(),
            border=((StyleBase().bd(),) * 4),
            border_rgb=Rgb().th3(),
            border_hover=((StyleBase().bd(),) * 4),
            border_hover_rgb=Rgb().th3(),
            radius=((VBase.RADIUS, )*4)
    )
class TrayUi(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            ombre_portee = True,
            bg=Rgb().th1(),
            border=((StyleBase().bd(),) * 4),
            border_rgb=Rgb().th3(),
            border_hover=((StyleBase().bd(),) * 4),
            border_hover_rgb=Rgb().th3(),
            radius=((VBase.RADIUS, )*4)
    )


##################
##     DEMO     ##
##################
class Demo_hover(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            bg=Rgb().tr(),
            border=((StyleBase().bd(),) * 4),
            border_rgb=Rgb().bn1(),
            border_hover=((StyleBase().bd(),) * 4),
            border_hover_style="dashed",
            border_hover_rgb=Rgb().bn1(),
            radius = ((VBase.RADIUS+1, )*4)
    )
