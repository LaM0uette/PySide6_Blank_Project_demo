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

            # Bordures
            border_all=None,
            border_style=p_base.WG_BORDER_STYLE,
            border_rgb=p_base.WG_BORDER_RGB,
            border_top=p_base.WG_BORDER_WIDTH, border_bottom=p_base.WG_BORDER_WIDTH, border_right=p_base.WG_BORDER_WIDTH, border_left=p_base.WG_BORDER_WIDTH,

            # Rayons
            radius_all=None,
            radius_top_right=p_base.WG_RADIUS,
            radius_top_left=p_base.WG_RADIUS,
            radius_bottom_right=p_base.WG_RADIUS,
            radius_bottom_left=p_base.WG_RADIUS,
    ):
        # Bordure
        if not border_all is None:
            border_top = border_all
            border_bottom = border_all
            border_right = border_all
            border_left = border_all
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
              bg=P_rgb().th1(),
              height=P_dim().h9()
    )
class Menu_bottom(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              bg=P_rgb().th2(),
              height=P_dim().h10()
    )
class Menu_bottom_dlg(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              bg=P_rgb().th2(),
              height=P_dim().h9()
    )

class Cadre:
    def __init__(self, *wgs):
        self.wgs = wgs

    def rtn(self):
        pass



class Cadre_th2(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              bg=Rgb().tr(),
              border_all=P_style().bd(),
              border_rgb=P_rgb().th2(),
    )
class Cadre_th3(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              bg=Rgb().tr(),
              border_all=P_style().bd(),
              border_rgb=P_rgb().th3(),
    )
class Cadre_bn1(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              bg=Rgb().tr(),
              border_all=P_style().bd(),
              border_rgb=P_rgb().bn1(),
    )

class palette_rgb(Style):
    def __init__(self, *wgs, rgb):
        super().__init__(*wgs,
              bg=rgb,
              radius_top_left=40,
              radius_top_right=40,
              radius_bottom_left=40,
              radius_bottom_right=40
    )
