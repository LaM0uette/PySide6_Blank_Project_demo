from src.lib.palettes import *
from src.widgets import vb_wg
from src.widgets.Label.Build import Build


##################
##     BASE     ##
##################
class Base:
    def __init__(self, *wgs, font_size=vb_wg.FONT_SIZE):
        self.wgs = wgs
        self.font_size = font_size

    def th(self):
        Build(
            *self.wgs,

            font_size=self.font_size,
        )
    def tr(self):
        Build(
            *self.wgs,

            font_size=self.font_size,

            bg=Rgb().tr(),
            bg_hover=Rgb().tr(),
            fg=Rgb().th3(),
            fg_hover=Rgb().th3(),
        )
    def titre(self):
        Build(
            *self.wgs,

            font_size=self.font_size,

            align_horizontal=Align().center_horizontal(),

            bg=Rgb().tr(),
            bg_hover=Rgb().tr(),
            fg=Rgb().th3(),
            fg_hover=Rgb().th3(),
        )


##################
##     DEMO     ##
##################
class Demo:
    def __init__(self, *wgs, font_size=vb_wg.FONT_SIZE):
        self.wgs = wgs
        self.font_size = font_size

    def th(self):
        Build(
            *self.wgs,

            height=Dim().h9(),

            font_size=self.font_size,
        )
    def tr(self):
        Build(
            *self.wgs,

            height=Dim().h9(),

            font_size=self.font_size,
            bg=Rgb().tr(),
            bg_hover=Rgb().tr(),
            fg=Rgb().th3(),
            fg_hover=Rgb().th3(),
        )
    def wg_categorie(self):
        Build(
            *self.wgs,
            font_size=self.font_size,

            align_horizontal=Align().center_horizontal(),

            bg=Rgb().tr(),
            bg_hover=Rgb().tr(),
            fg=Rgb().th3(),
            fg_hover=Rgb().th3(),

            border=(0, StyleBase().border(), 0, 0),
            border_hover=(0, StyleBase().border(), 0, 0),
            border_rgb=Rgb().bn1(),
            border_hover_rgb=Rgb().bn1(),

            radius=(0,) * 4
        )
