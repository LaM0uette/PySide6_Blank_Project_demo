from PySide6 import QtWidgets

from ....build import *
from ....build.widgets import p_base

class Style:
    def __init__(
            self,

            # Widgets
            *wgs,
            couleur_bg=p_base._COLORS_BG,
            dim_width=p_base.WIDTH,
            dim_height=p_base.HEIGHT,
            bordure_width_top=p_base.WG_BORDER_WIDTH,
            bordure_width_bottom=p_base.WG_BORDER_WIDTH,
            bordure_width_right=p_base.WG_BORDER_WIDTH,
            bordure_width_left=p_base.WG_BORDER_WIDTH,
            bordure_style_top=p_base.WG_BORDER_STYLE,
            bordure_style_bottom=p_base.WG_BORDER_STYLE,
            bordure_style_right=p_base.WG_BORDER_STYLE,
            bordure_style_left=p_base.WG_BORDER_STYLE,
            bordure_couleur_top=p_base.WG_BORDER_RGB,
            bordure_couleur_bottom=p_base.WG_BORDER_RGB,
            bordure_couleur_right=p_base.WG_BORDER_RGB,
            bordure_couleur_left=p_base.WG_BORDER_RGB,
            rayon_top_left=p_base.WG_RADIUS,
            rayon_top_right=p_base.WG_RADIUS,
            rayon_bottom_right=p_base.WG_RADIUS,
            rayon_bottom_left=p_base.WG_RADIUS,
    ):
        style = f"""
        /* FRAME */
        .QFrame {{
        background-color: rgba{couleur_bg};
        }}

        /* BORDURES */
        .QFrame {{
        border-top: {bordure_width_top}px {bordure_style_top} rgba{bordure_couleur_top};
        border-bottom: {bordure_width_bottom}px {bordure_style_bottom} rgba{bordure_couleur_bottom};
        border-right: {bordure_width_right}px {bordure_style_right} rgba{bordure_couleur_right};
        border-left: {bordure_width_left}px {bordure_style_left} rgba{bordure_couleur_left};
        }}

        /* RAYONS */
        .QFrame {{
        border-top-left-radius: {rayon_top_left}px;
        border-top-right-radius: {rayon_top_right}px;
        border-bottom-right-radius: {rayon_bottom_right}px;
        border-bottom-left-radius: {rayon_bottom_left}px;
        }}"""

        for wg in wgs:
            wg.setStyleSheet(style)

            Fct(wg=wg, w=dim_width, h=dim_height).DIM()

            wg.setFrameShape(QtWidgets.QFrame.NoFrame)


class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs)
class Base_tr(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              couleur_bg=(0, 0, 0, 0)
    )

class Menu_top(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              couleur_bg=P_rgb().th1()+(255, ),
              dim_height=P_dim().h9()
    )
class Menu_bottom(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              couleur_bg=P_rgb().th2()+(255, ),
              dim_height=P_dim().h10()
    )
class Menu_bottom_dlg(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              couleur_bg=P_rgb().th2()+(255, ),
              dim_height=P_dim().h9()
    )


class Cadre_th2(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              couleur_bg=(0, 0, 0, 0),
              bordure_width_top=P_style().bd(),
              bordure_width_bottom=P_style().bd(),
              bordure_width_right=P_style().bd(),
              bordure_width_left=P_style().bd(),
              bordure_couleur_top=P_rgb().th2()+(255, ),
              bordure_couleur_bottom=P_rgb().th2()+(255, ),
              bordure_couleur_right=P_rgb().th2()+(255, ),
              bordure_couleur_left=P_rgb().th2()+(255, )
    )
class Cadre_th3(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              couleur_bg=(0, 0, 0, 0),
              bordure_width_top=P_style().bd(),
              bordure_width_bottom=P_style().bd(),
              bordure_width_right=P_style().bd(),
              bordure_width_left=P_style().bd(),
              bordure_couleur_top=P_rgb().th3()+(255, ),
              bordure_couleur_bottom=P_rgb().th3()+(255, ),
              bordure_couleur_right=P_rgb().th3()+(255, ),
              bordure_couleur_left=P_rgb().th3()+(255, )
    )
class Cadre_bn1(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              couleur_bg=(0, 0, 0, 0),
              bordure_width_top=P_style().bd(),
              bordure_width_bottom=P_style().bd(),
              bordure_width_right=P_style().bd(),
              bordure_width_left=P_style().bd(),
              bordure_couleur_top=P_rgb().bn1()+(255, ),
              bordure_couleur_bottom=P_rgb().bn1()+(255, ),
              bordure_couleur_right=P_rgb().bn1()+(255, ),
              bordure_couleur_left=P_rgb().bn1()+(255, )
    )

class palette_rgb(Style):
    def __init__(self, *wgs, rgb):
        super().__init__(*wgs,
              couleur_bg=rgb+(255, ),
              rayon_top_left=40,
              rayon_top_right=40,
              rayon_bottom_left=40,
              rayon_bottom_right=40
    )
