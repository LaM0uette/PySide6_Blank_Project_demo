from .WgClass.MyQListWidgetStyle import Style
from src.lib.palettes import *


##################
##     BASE     ##
##################
class Base:
    def __init__(self, widget):
        self.widget = widget

    def Base(self):
        Style(
            widget=self.widget,
            border_item=DcBorder.Base(
                radius=(0,) * 4)
        )
    def Transparent(self):
        Style(
            widget=self.widget,
            background=DcRgbBg.Base(gen=PaRgb.TR),
            foreground_item=DcRgbBg.Base(
                base=PaRgb.TH3,
                checked=PaRgb.BN1,
            ),
            border_item=DcBorder.Base(
                radius=(0,)*4)
        )

##################
##     DEMO     ##
##################
class Demo:
    def __init__(self, widget):
        self.widget = widget

    def Base(self):
        Style(
            widget=self.widget,
            dim=DcDim.Base(fixed_height=PaDim.H5),
            border_item=DcBorder.Base(
                radius=(0,) * 4)
        )
    def Transparent(self):
        Style(
            widget=self.widget,
            dim=DcDim.Base(fixed_height=PaDim.H5),

            background=DcRgbBg.Base(gen=PaRgb.TR),
            background_item=DcRgbBg.Base(gen=PaRgb.TR),
            foreground_item=DcRgbBg.Base(
                base=PaRgb.TH3,
                checked=PaRgb.BN1,
                checked_hover=PaRgb.BN1,
            ),
            border_item=DcBorder.Base(
                gen=(0, 0, 0, 2),
                base_rgb=PaRgb.TH2,
                hover_rgb=PaRgb.TH3,
                checked_rgb=PaRgb.BN1,
                checked_hover=PaRgb.BN1,
                radius=(0,)*4)
        )
