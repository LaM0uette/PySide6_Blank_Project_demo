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

            width=Dim.H9,
            height=Dim.H9,

            focus_policy=FocusPolicy.NO,

            bg=Rgb.TR,
            bg_hover=Rgb.TR,

            img=Img.MAIN,
            img_rgb="th3",

            scaled_contents=True,
        )
    def ico_splash(self):
        Build(
            *self.wgs,

            width=Dim.H5,
            height=Dim.H5,

            focus_policy=FocusPolicy.NO,

            bg=Rgb.TR,
            bg_hover=Rgb.TR,

            img=Img.MAIN,
            img_rgb="th3",

            scaled_contents=True,
        )
    def ico_custom(self, img=Img.MAIN, img_rgb="th3"):
        Build(
            *self.wgs,

            width=Dim.H9,
            height=Dim.H9,

            focus_policy=FocusPolicy.NO,

            bg=Rgb.TR,
            bg_hover=Rgb.TR,

            img=img,
            img_rgb=img_rgb,

            scaled_contents=True,
        )
    def th(self):
        Build(
            *self.wgs,

            focus_policy=FocusPolicy.NO,

            font_size=self.font_size,
        )
    def tr(self):
        Build(
            *self.wgs,

            focus_policy=FocusPolicy.NO,

            font_size=self.font_size,

            bg=Rgb.TR,
            bg_hover=Rgb.TR,
            fg=Rgb.TH3,
            fg_hover=Rgb.TH3,
        )
    def titre(self):
        Build(
            *self.wgs,

            focus_policy=FocusPolicy.NO,

            font_size=self.font_size,

            align_horizontal=Align.CENTER_HORIZONTAL,

            bg=Rgb.TR,
            bg_hover=Rgb.TR,
            fg=Rgb.TH3,
            fg_hover=Rgb.TH3,
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

            height=Dim.H9,
            indent=5,

            font_size=self.font_size,
        )
    def tr(self):
        Build(
            *self.wgs,

            height=Dim.H9,
            indent=5,

            font_size=self.font_size,
            bg=Rgb.TR,
            bg_hover=Rgb.TR,
            fg=Rgb.TH3,
            fg_hover=Rgb.TH3,
        )
    def wg_categorie(self):
        Build(
            *self.wgs,
            font_size=Font.H2,

            align_horizontal=Align.CENTER_HORIZONTAL,

            bg=Rgb.TR,
            bg_hover=Rgb.TR,
            fg=Rgb.TH3,
            fg_hover=Rgb.TH3,

            border=(0, StyleBase.BORDER, 0, 0),
            border_hover=(0, StyleBase.BORDER, 0, 0),
            border_rgb=Rgb.BN2,
            border_hover_rgb=Rgb.BN2,

            radius=(0,) * 4
        )
