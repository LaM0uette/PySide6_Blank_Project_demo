from .WgClass.MyQRadioButtonStyle import Style
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
        )
    def Transparent(self):
        Style(
            widget=self.widget,

            background=DcRgbBg.Base(gen=PaRgb.TR),
            foreground=DcRgbFg.Base(
                base=PaRgb.TH3,
                checked=PaRgb.BN1,
            ),
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
        )
    def Transparent(self):
        Style(
            widget=self.widget,

            background=DcRgbBg.Base(gen=PaRgb.TR),
            foreground=DcRgbFg.Base(
                base=PaRgb.TH3,
                checked=PaRgb.BN1,
            ),

            auto_actions=DcAutoActions.Base(auto_exclusive=True),
        )