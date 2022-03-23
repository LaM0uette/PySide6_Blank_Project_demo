from .WgClass.MyQFrameStyle import Style
from src.lib.palettes import *


##################
##     BASE     ##
##################
class Base:
    def __init__(self, widget):
        self.widget = widget

    def Base(self, rgb=PaRgb.TH3):
        Style(
            widget=self.widget,
            background=DcRgbBg.Base(gen=rgb)
        )
    def Transparent(self, rgb=PaRgb.TR):
        Style(
            widget=self.widget,
            background=DcRgbBg.Base(gen=rgb)
        )


##################
##     MENU     ##
##################
class Menu:
    def __init__(self, widget):
        self.widget = widget

    def top(self):
        Style(
            self.widget,

            dim=DcDim.Base(fixed_height=PaDim.H9),

            background=DcRgbBg.Base(gen=PaRgb.TH1),
            border=DcBorder.Base(radius=(3, 3, 0, 0))
        )
    def bottom(self):
        Style(
            self.widget,

            dim=DcDim.Base(fixed_height=PaDim.H10),

            background=DcRgbBg.Base(gen=PaRgb.TH2),
            border=DcBorder.Base(radius=(0, 0, 3, 3))
        )
    def bottom_dlg(self):
        Style(
            self.widget,

            dim=DcDim.Base(fixed_height=PaDim.H9),

            background=DcRgbBg.Base(gen=PaRgb.TH2),
            border=DcBorder.Base(radius=(0, 0, 3, 3))
        )


####################
##     CADRES     ##
####################
class Cadre:
    def __init__(self, widget):
        self.widget = widget

    def rtn(self, rgb, bg=(PaStyleBase.BORDER, )*4):
        Style(
            self.widget,

            background=DcRgbBg.Base(gen=PaRgb.TR),
            border=DcBorder.Base(
                gen=bg,
                gen_rgb=rgb,
                radius=(3, )*4
            )
        )

    def th1(self): self.rtn(rgb=PaRgb.TH1)
    def th2(self): self.rtn(rgb=PaRgb.TH2)
    def th3(self): self.rtn(rgb=PaRgb.TH3)
    def bn1(self): self.rtn(rgb=PaRgb.BN1)
    def bn2(self): self.rtn(rgb=PaRgb.BN2)
