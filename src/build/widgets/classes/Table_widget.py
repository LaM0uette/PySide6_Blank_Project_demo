from PySide6 import QtWidgets, QtCore

from ....build import *
from ....build.widgets import p_base

class Style:
    def __init__(self,
                 *wgs,
                 couleur_bg=p_base.COULEUR_BG,
                 couleur_bg_checked=p_base.COULEUR_BG_CHECKED,
                 couleur_bg_checked_hover=p_base.COULEUR_BG_CHECKED_HOVER,
                 couleur_bg_item=p_base.COULEUR_BG_ITEM,
                 couleur_bg_item_hover=p_base.COULEUR_BG_ITEM_HOVER,
                 couleur_fg=p_base.COULEUR_FG,
                 couleur_fg_checked=p_base.COULEUR_FG_CHECKED,
                 couleur_fg_checked_hover=p_base.COULEUR_FG_CHECKED_HOVER,
                 couleur_fg_item=p_base.COULEUR_FG_ITEM,
                 couleur_fg_item_hover=p_base.COULEUR_FG_ITEM_HOVER,
                 couleur_grid=p_base.COULEUR_GRID,
                 dim_width=p_base.DIM_WG_WIDTH,
                 dim_height=p_base.DIM_WG_HEIGHT,
                 police=p_base.FONT,
                 police_taille=p_base.FONT_SIZE,
                 police_hd_taille=p_base.HD_FONT_SIZE,
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
                 header_h=p_base.HEADER_H,
                 header_v=p_base.HEADER_V,
                 curseur=p_base.CUR
                 ):
        style_main = f"""
        /* CORNER */
        QTableCornerButton::section {{
        background-color: rgba{couleur_bg};
        }}

        /* TABLE_WIDGET */
        QTableWidget {{
        background-color: rgba{couleur_bg};
        gridline-color: rgb{couleur_grid};
        color: rgb{couleur_fg};
        }}

        /* ITEM */
        QTableWidget::item {{
        background-color: rgba{couleur_bg_item};
        color: rgb{couleur_fg_item};
        }}
        QTableWidget::item:hover {{
        background-color: rgba{couleur_bg_item_hover};
        color: rgb{couleur_fg_item_hover};
        }}
        QTableWidget::item:selected {{
        background-color: rgba{couleur_bg_checked};
        color: rgb{couleur_fg_checked};
        }}
        QTableWidget::item:selected:hover {{
        background-color: rgba{couleur_bg_checked_hover};
        color: rgb{couleur_fg_checked_hover};
        }}

        /* BORDURES */
        .QTableWidget {{
        border-top: {bordure_width_top}px {bordure_style_top} rgba{bordure_couleur_top};
        border-bottom: {bordure_width_bottom}px {bordure_style_bottom} rgba{bordure_couleur_bottom};
        border-right: {bordure_width_right}px {bordure_style_right} rgba{bordure_couleur_right};
        border-left: {bordure_width_left}px {bordure_style_left} rgba{bordure_couleur_left};
        }}

        /* RAYONS */
        .QTableWidget {{
        border-top-left-radius: {rayon_top_left}px;
        border-top-right-radius: {rayon_top_right}px;
        border-bottom-right-radius: {rayon_bottom_right}px;
        border-bottom-left-radius: {rayon_bottom_left}px;
        }}

        /* SCROLL */
        .QTableWidget QScrollBar {{
        background-color: rgb{scroll_bg};
        width: {scroll_width}px;
        height: {scroll_height}px;
        }}
        .QTableWidget::handle:horizontal {{
        min-width: {scroll_handle_min_width}px;
        }}
        .QTableWidget::handle:vertical {{
        min-height: {scroll_handle_min_height}px;
        }}
        .QTableWidget QScrollBar::handle {{
        background-color: rgb{scroll_handle_fg};
        }}
        .QTableWidget QScrollBar::add-page, .QTableWidget QScrollBar::sub-page {{
        background-color: rgb{scroll_handle_bg};
        border: none;
        }}"""

        style_header = f"""
        QHeaderView::section {{
        background-color: rgba{couleur_bg};
        color: rgb{couleur_fg};
        border-style: none;
        }}
        QHeaderView::section:checked {{
        background-color: rgba{couleur_bg_checked};
        color: rgb{couleur_fg_checked};
        }}"""

        for wg in wgs:
            wg.setStyleSheet(style_main)
            wg.horizontalHeader().setStyleSheet(style_header)
            wg.verticalHeader().setStyleSheet(style_header)

            try:
                Fct(wg=wg, w=dim_width, h=dim_height).DIM()
                wg.setFont(Fct(font=police, font_size=police_taille).FONT())
                wg.horizontalHeader().setFont(Fct(font_size=police_hd_taille).FONT())
                wg.verticalHeader().setFont(Fct(font_size=police_hd_taille).FONT())

                wg.setHorizontalScrollBarPolicy(scroll_h)
                wg.setVerticalScrollBarPolicy(scroll_v)
                wg.horizontalHeader().setVisible(header_h)
                wg.verticalHeader().setVisible(header_v)

                wg.setCursor(Fct(cur=curseur).CUR())
                wg.viewport().setCursor(Fct(cur=curseur).CUR())

                wg.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
                wg.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
                wg.verticalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
                wg.setFrameShape(QtWidgets.QFrame.NoFrame)

                wg.resizeColumnsToContents()
            except: pass


class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs)
class Base_tr(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              couleur_bg=(0, 0, 0, 0),
              couleur_bg_item=(0, 0, 0, 0),
              couleur_bg_checked=(0, 0, 0, 0),
              couleur_bg_item_hover=(0, 0, 0, 0),
              couleur_bg_checked_hover=(0, 0, 0, 0),
              couleur_fg_checked=p_base.COULEURS.get("bn1"),
              couleur_fg_checked_hover=p_base.COULEURS.get("bn2"),
    )


class Demo_th(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              couleur_fg_checked=p_base.COULEURS.get("bn1"),
              couleur_fg_checked_hover=p_base.COULEURS.get("bn2"),
              dim_height=P_dim().h5(),
    )
class Demo_tr(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              couleur_bg=(0, 0, 0, 0),
              couleur_bg_item=(0, 0, 0, 0),
              couleur_bg_checked=(0, 0, 0, 0),
              couleur_bg_item_hover=(0, 0, 0, 0),
              couleur_bg_checked_hover=(0, 0, 0, 0),
              couleur_fg_checked=p_base.COULEURS.get("bn1"),
              couleur_fg_checked_hover=p_base.COULEURS.get("bn2"),
              dim_height=P_dim().h5()
    )