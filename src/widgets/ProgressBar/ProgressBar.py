from src.lib.palettes import *
from src.widgets import vb_wg
from src.widgets.ProgressBar.Build import Build


##################
##     BASE     ##
##################
class Base:
    def __init__(self, *wgs):
        self.wgs = wgs

    def th(self):
        Build(
            *self.wgs,

            border=(StyleBase.BORDER,) * 4,
            border_hover=(StyleBase.BORDER,) * 4,
            border_rgb=Rgb().th3(),
            border_hover_rgb=Rgb().th3(),
        )
    def tr(self):
        Build(
            *self.wgs,

            text_visible=False,

            bg=Rgb().tr(),

            border=(StyleBase.BORDER,) * 4,
            border_hover=(StyleBase.BORDER,) * 4,
            border_rgb=Rgb().th3(),
            border_hover_rgb=Rgb().th3(),
        )
    def Chargement(self):
        Build(
            *self.wgs,

            border=(StyleBase.BORDER,) * 4,
            border_hover=(StyleBase.BORDER,) * 4,
            border_rgb=Rgb().th3(),
            border_hover_rgb=Rgb().th3(),

            radius_chunk=(3, 0, 3, 0)
        )


##################
##     DEMO     ##
##################
class Demo:
    def __init__(self, *wgs):
        self.wgs = wgs
    def th(self):
        Build(
            *self.wgs,

            border=(StyleBase.BORDER,) * 4,
            border_hover=(StyleBase.BORDER,) * 4,
            border_rgb=Rgb().th3(),
            border_hover_rgb=Rgb().th3(),

            radius_chunk=(3, 0, 3, 0)
        )
    def tr(self):
        Build(
            *self.wgs,

            text_visible=False,

            bg=Rgb().tr(),

            border=(StyleBase.BORDER,) * 4,
            border_hover=(StyleBase.BORDER,) * 4,
            border_rgb=Rgb().th3(),
            border_hover_rgb=Rgb().th3(),

            radius_chunk=(3, 0, 3, 0)
        )
