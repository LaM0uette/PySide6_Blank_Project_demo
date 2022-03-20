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

    def ico_main(self):
        Build(
            *self.wgs,

            width=PaDim.H9,
            height=PaDim.H9,

            focus_policy=PaFocusPolicy.NO,

            bg=PaRgb.TR,
            bg_hover=PaRgb.TR,

            img=PaImg.MAIN,
            img_rgb="th3",

            scaled_contents=True,
        )
    def ico_splash(self):
        Build(
            *self.wgs,

            width=PaDim.H5,
            height=PaDim.H5,

            focus_policy=PaFocusPolicy.NO,

            bg=PaRgb.TR,
            bg_hover=PaRgb.TR,

            img=PaImg.MAIN,
            img_rgb="th3",

            scaled_contents=True,
        )
    def ico_custom(self, img=PaImg.MAIN, img_rgb="th3"):
        Build(
            *self.wgs,

            width=PaDim.H9,
            height=PaDim.H9,

            focus_policy=PaFocusPolicy.NO,

            bg=PaRgb.TR,
            bg_hover=PaRgb.TR,

            img=img,
            img_rgb=img_rgb,

            scaled_contents=True,
        )
    def th(self):
        Build(
            *self.wgs,

            focus_policy=PaFocusPolicy.NO,

            font_size=self.font_size,
        )
    def tr(self):
        Build(
            *self.wgs,

            focus_policy=PaFocusPolicy.NO,

            font_size=self.font_size,

            bg=PaRgb.TR,
            bg_hover=PaRgb.TR,
            fg=PaRgb.TH3,
            fg_hover=PaRgb.TH3,
        )
    def titre(self):
        Build(
            *self.wgs,

            focus_policy=PaFocusPolicy.NO,

            font_size=self.font_size,

            align_horizontal=PaAlign.CENTER_HORIZONTAL,

            bg=PaRgb.TR,
            bg_hover=PaRgb.TR,
            fg=PaRgb.TH3,
            fg_hover=PaRgb.TH3,
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

            height=PaDim.H9,
            indent=5,

            font_size=self.font_size,
        )
    def tr(self):
        Build(
            *self.wgs,

            height=PaDim.H9,
            indent=5,

            font_size=self.font_size,
            bg=PaRgb.TR,
            bg_hover=PaRgb.TR,
            fg=PaRgb.TH3,
            fg_hover=PaRgb.TH3,
        )
    def wg_categorie(self):
        Build(
            *self.wgs,
            font_size=PaFont.H2,

            align_horizontal=PaAlign.CENTER_HORIZONTAL,

            bg=PaRgb.TR,
            bg_hover=PaRgb.TR,
            fg=PaRgb.TH3,
            fg_hover=PaRgb.TH3,

            border=(0, PaStyleBase.BORDER, 0, 0),
            border_hover=(0, PaStyleBase.BORDER, 0, 0),
            border_rgb=PaRgb.BN2,
            border_hover_rgb=PaRgb.BN2,

            radius=(0,) * 4
        )
