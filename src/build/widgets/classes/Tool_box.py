from PySide6 import QtWidgets

from ....build import *
from ....build.widgets import p_base

class Style:
    def __init__(self,
                 *wgs,
                 couleur_bg=p_base.COULEUR_BG,
                 couleur_bg_hover=p_base.COULEUR_BG_HOVER,
                 couleur_bg_checked=p_base.COULEUR_BG_CHECKED,
                 couleur_bg_checked_hover=p_base.COULEUR_BG_CHECKED_HOVER,
                 couleur_fg=p_base.COULEUR_FG,
                 couleur_fg_hover=p_base.COULEUR_FG_HOVER,
                 couleur_fg_checked=p_base.COULEUR_FG_CHECKED,
                 couleur_fg_checked_hover=p_base.COULEUR_FG_CHECKED_HOVER,
                 dim_width=p_base.DIM_WIDTH,
                 dim_height=p_base.DIM_HEIGHT,
                 police=p_base.FONT,
                 police_taille=p_base.FONT_SIZE,
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
                 curseur=p_base.CUR
                 ):
        style = f"""
        QToolBox::tab {{
        background-color: rgba{couleur_bg};
        color: rgb{couleur_fg};
        }}

        QToolBox::tab:hover {{
        background-color: rgba{couleur_bg_hover};
        color: rgb{couleur_fg_hover};
        }}

        QToolBox::tab:selected {{
        background-color: rgba{couleur_bg_checked};
        color: rgb{couleur_fg_checked};
        }}

        QToolBox::tab:selected:hover {{
        background-color: rgba{couleur_bg_checked_hover};
        color: rgb{couleur_fg_checked_hover};
        }}

        /* BORDURES */
        .QToolBox {{
        border-top: {bordure_width_top}px {bordure_style_top} rgba{bordure_couleur_top};
        border-bottom: {bordure_width_bottom}px {bordure_style_bottom} rgba{bordure_couleur_bottom};
        border-right: {bordure_width_right}px {bordure_style_right} rgba{bordure_couleur_right};
        border-left: {bordure_width_left}px {bordure_style_left} rgba{bordure_couleur_left};
        }}

        /* RAYONS */
        .QToolBox {{
        border-top-left-radius: {rayon_top_left}px;
        border-top-right-radius: {rayon_top_right}px;
        border-bottom-right-radius: {rayon_bottom_right}px;
        border-bottom-left-radius: {rayon_bottom_left}px;
        }}

        /* SCROLL */
        .QToolBox QScrollBar {{
        background-color: rgb{scroll_bg};
        width: {scroll_width}px;
        height: {scroll_height}px;
        }}
        .QToolBox::handle:horizontal {{
        min-width: {scroll_handle_min_width}px;
        }}
        .QToolBox::handle:vertical {{
        min-height: {scroll_handle_min_height}px;
        }}
        .QToolBox QScrollBar::handle {{
        background-color: rgb{scroll_handle_fg};
        }}

        .QToolBox QScrollBar::add-page, .QToolBox QScrollBar::sub-page {{
        background-color: rgb{scroll_handle_bg};
        border: none;
        }}"""

        for wg in wgs:
            wg.setStyleSheet(style)

            try:
                Fct(wg=wg, w=dim_width, h=dim_height).DIM()
                wg.setFont(Fct(font=police, font_size=police_taille).FONT())

                wg.setFrameShape(QtWidgets.QFrame.NoFrame)

                wg.setCursor(Fct(cur=curseur).CUR())
            except: pass


class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs)
class Base_tr(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              couleur_bg=(0, 0, 0, 0),
              couleur_bg_hover=(0, 0, 0, 0),
              couleur_bg_checked=(0, 0, 0, 0),
              couleur_bg_checked_hover=(0, 0, 0, 0),
              couleur_fg_checked=p_base.COULEURS.get("c3"),
    )
