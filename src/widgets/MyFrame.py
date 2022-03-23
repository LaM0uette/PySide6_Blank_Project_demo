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
