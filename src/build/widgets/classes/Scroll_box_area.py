from PySide6 import QtWidgets

from ....build import *
from ....build.widgets import p_base

class Style:
    def __init__(self,
                 *wgs,
                 couleur_bg=p_base._COLORS_BG,
                 dim_width=p_base.DIM_WIDTH,
                 dim_height=p_base.DIM_HEIGHT,
                 bordure_width_top=p_base.BD_WIDTH,
                 bordure_width_bottom=p_base.BD_WIDTH,
                 bordure_width_right=p_base.BD_WIDTH,
                 bordure_width_left=p_base.BD_WIDTH,
                 bordure_style_top=p_base.BD_STYLE,
                 bordure_style_bottom=p_base.BD_STYLE,
                 bordure_style_right=p_base.BD_STYLE,
                 bordure_style_left=p_base.BD_STYLE,
                 bordure_couleur_top=p_base.BD_COULEUR,
                 bordure_couleur_bottom=p_base.BD_COULEUR,
                 bordure_couleur_right=p_base.BD_COULEUR,
                 bordure_couleur_left=p_base.BD_COULEUR,
                 rayon_top_left=p_base.RD_WG,
                 rayon_top_right=p_base.RD_WG,
                 rayon_bottom_right=p_base.RD_WG,
                 rayon_bottom_left=p_base.RD_WG,
                 scroll_bg=p_base.SCROLL_BG,
                 scroll_handle_bg=p_base.SCROLL_HANDLE_BG,
                 scroll_handle_fg=p_base.SCROLL_HANDLE_FG,
                 scroll_width=p_base.SCROLL_WIDTH,
                 scroll_height=p_base.SCROLL_HEIGHT,
                 scroll_handle_min_width=p_base.SCROLL_HANDLE_MIN_WIDTH,
                 scroll_handle_min_height=p_base.SCROLL_HANDLE_MIN_HEIGHT,
                 scroll_h=p_base.SCROLL_H,
                 scroll_v=p_base.SCROLL_V,
                 ):
        style = f"""
        .QScrollArea .QWidget {{
        background-color: rgba{couleur_bg};
        }}

        /* BORDURES */
        .QScrollArea {{
        border-top: {bordure_width_top}px {bordure_style_top} rgba{bordure_couleur_top};
        border-bottom: {bordure_width_bottom}px {bordure_style_bottom} rgba{bordure_couleur_bottom};
        border-right: {bordure_width_right}px {bordure_style_right} rgba{bordure_couleur_right};
        border-left: {bordure_width_left}px {bordure_style_left} rgba{bordure_couleur_left};
        }}

        /* RAYONS */
        .QScrollArea {{
        border-top-left-radius: {rayon_top_left}px;
        border-top-right-radius: {rayon_top_right}px;
        border-bottom-right-radius: {rayon_bottom_right}px;
        border-bottom-left-radius: {rayon_bottom_left}px;
        }}

        /* SCROLL */
        QScrollArea QScrollBar {{
        background-color: rgb{scroll_bg};
        width: {scroll_width}px;
        height: {scroll_height}px;
        }}
        QScrollArea::handle:horizontal {{
        min-width: {scroll_handle_min_width}px;
        }}
        QScrollArea::handle:vertical {{
        min-height: {scroll_handle_min_height}px;
        }}
        QScrollArea QScrollBar::handle {{
        background-color: rgb{scroll_handle_fg};
        }}

        QScrollArea QScrollBar::add-page, QScrollArea QScrollBar::sub-page {{
        background-color: rgb{scroll_handle_bg};
        border: none;
        }}"""

        for wg in wgs:
            wg.setStyleSheet(style)

            try:
                Fct(wg=wg, w=dim_width, h=dim_height).DIM()

                wg.setHorizontalScrollBarPolicy(scroll_h)
                wg.setVerticalScrollBarPolicy(scroll_v)

                wg.setFrameShape(QtWidgets.QFrame.NoFrame)
            except: pass


class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs)
class Base_tr(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              couleur_bg=(0, 0, 0, 0),
    )


class Demo(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              couleur_bg=P_rgb().th1()+(255, ),
    )
