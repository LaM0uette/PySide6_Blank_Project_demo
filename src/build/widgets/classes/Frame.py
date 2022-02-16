from PySide6 import QtWidgets

from ....build import *
from ....build.widgets import p_base

class Style:
    def __init__(
            self,

            # Widgets
            *wgs,

            # Couleurs BG
            bg=p_base.BG,

            # Dimensions WG
            width=p_base.WIDTH,
            height=p_base.HEIGHT,

            # Bordures GEN
            border_gen_all=None,
            border_gen_style=None,
            border_gen_rgb=None,
            border_gen_top=None, border_gen_bottom=None, border_gen_right=None, border_gen_left=None,
            # Bordures
            border_all=None,
            border_style=p_base.WG_BORDER_STYLE,
            border_rgb=p_base.WG_BORDER_RGB,
            border_top=p_base.WG_BORDER_WIDTH, border_bottom=p_base.WG_BORDER_WIDTH, border_right=p_base.WG_BORDER_WIDTH, border_left=p_base.WG_BORDER_WIDTH,
            # Bordures hover
            border_all_hover=None,
            border_style_hover=p_base.WG_BORDER_STYLE,
            border_rgb_hover=p_base.WG_BORDER_RGB,
            border_top_hover=p_base.WG_BORDER_WIDTH, border_bottom_hover=p_base.WG_BORDER_WIDTH, border_right_hover=p_base.WG_BORDER_WIDTH, border_left_hover=p_base.WG_BORDER_WIDTH,

            # Rayons
            radius_all=None,
            radius_top_right=p_base.WG_RADIUS,
            radius_top_left=p_base.WG_RADIUS,
            radius_bottom_right=p_base.WG_RADIUS,
            radius_bottom_left=p_base.WG_RADIUS,
    ):
        # Bordure
        if not border_gen_all is None:
            border_top = border_gen_all
            border_bottom = border_gen_all
            border_right = border_gen_all
            border_left = border_gen_all
            border_top_hover = border_gen_all
            border_bottom_hover = border_gen_all
            border_right_hover = border_gen_all
            border_left_hover = border_gen_all
        elif border_gen_all is None:
            if not border_all is None:
                border_top = border_all
                border_bottom = border_all
                border_right = border_all
                border_left = border_all
            if not border_all_hover is None:
                border_top_hover = border_all_hover
                border_bottom_hover = border_all_hover
                border_right_hover = border_all_hover
                border_left_hover = border_all_hover

            if not border_gen_top is None:
                border_top = border_gen_top
                border_top_hover = border_gen_top
            if not border_gen_bottom is None:
                border_bottom = border_gen_bottom
                border_bottom_hover = border_gen_bottom
            if not border_gen_right is None:
                border_right = border_gen_right
                border_right_hover = border_gen_right
            if not border_gen_left is None:
                border_left = border_gen_left
                border_left_hover = border_gen_left
        # Bordure style
        if not border_gen_style is None:
            border_style = border_gen_style
            border_style_hover = border_gen_style
        # Bordure RGB
        if not border_gen_rgb is None:
            border_rgb = border_gen_rgb
            border_rgb_hover = border_gen_rgb
        # Radius
        if not radius_all is None:
            radius_top_right = radius_all
            radius_top_left = radius_all
            radius_bottom_right = radius_all
            radius_bottom_left = radius_all


        style = f"""
        /* FRAME */
        .QFrame {{
        background-color: rgba{bg};
        }}

        /* BORDURES */
        .QFrame {{
        border-top: {border_top}px {border_style} rgba{border_rgb};
        border-bottom: {border_bottom}px {border_style} rgba{border_rgb};
        border-right: {border_right}px {border_style} rgba{border_rgb};
        border-left: {border_left}px {border_style} rgba{border_rgb};
        }}
        .QFrame:hover {{
        border-top: {border_top_hover}px {border_style_hover} rgba{border_rgb_hover};
        border-bottom: {border_bottom_hover}px {border_style_hover} rgba{border_rgb_hover};
        border-right: {border_right_hover}px {border_style_hover} rgba{border_rgb_hover};
        border-left: {border_left_hover}px {border_style_hover} rgba{border_rgb_hover};
        }}

        /* RAYONS */
        .QFrame {{
        border-top-right-radius: {radius_top_right}px;
        border-top-left-radius: {radius_top_left}px;
        border-bottom-right-radius: {radius_bottom_right}px;
        border-bottom-left-radius: {radius_bottom_left}px;
        }}"""

        for wg in wgs:
            wg.setStyleSheet(style)

            Fct(wg=wg, w=width, h=height).DIM()

            wg.setFrameShape(QtWidgets.QFrame.NoFrame)


class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs)
class Base_tr(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              bg=Rgb().tr()
    )

class Menu_top(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              bg=Rgb().th1(),
              height=P_dim().h9()
    )
class Menu_bottom(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              bg=Rgb().th2(),
              height=P_dim().h10()
    )
class Menu_bottom_dlg(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              bg=Rgb().th2(),
              height=P_dim().h9()
    )

class Cadre:
    def __init__(self, *wgs):
        self.wgs = wgs

    def rtn(self, rgb):
        Style(*self.wgs,
            bg=Rgb().tr(),
            border_gen_all=P_style().bd(),
            border_gen_rgb=rgb,
        )

    def th1(self): self.rtn(rgb=Rgb().th1())
    def th2(self): self.rtn(rgb=Rgb().th2())
    def th3(self): self.rtn(rgb=Rgb().th3())
    def bn1(self): self.rtn(rgb=Rgb().bn1())
    def bn2(self): self.rtn(rgb=Rgb().bn2())

class palette_rgb(Style):
    def __init__(self, *wgs, rgb):
        super().__init__(*wgs,
              bg=rgb,
              radius_all=40,
    )


class Demo_hover(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              bg=Rgb().tr(),
              border_all=P_style().bd(),
              border_rgb=Rgb().bn1(),
              border_all_hover=P_style().bd()*2,
              border_style_hover="dashed",
              border_rgb_hover=Rgb().vert(),
    )