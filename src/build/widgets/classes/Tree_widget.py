from PySide6 import QtCore, QtWidgets

from ....build import *
from ....build.widgets import p_base

class Style:
    def __init__(self,
                 *wgs,
                 couleur_bg=p_base.COLORS_BG,
                 couleur_bg_item=p_base.COLORS_BG_ITEM,
                 couleur_bg_item_hover=p_base.COLORS_BG_ITEM_HOVER,
                 couleur_bg_item_checked=p_base.COLORS_BG_ITEM_CHECKED,
                 couleur_bg_item_checked_hover=p_base.COLORS_BG_ITEM_CHECKED_HOVER,
                 couleur_fg=p_base.COLORS_FG,
                 couleur_fg_item=p_base.COLORS_FG_ITEM,
                 couleur_fg_item_hover=p_base.COLORS_FG_ITEM_HOVER,
                 couleur_fg_item_checked=p_base.COLORS_FG_ITEM_CHECKED,
                 couleur_fg_item_checked_hover=p_base.COLORS_FG_ITEM_CHECKED_HOVER,
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
                 scroll_h=p_base.SCROLL_H,
                 scroll_v=p_base.SCROLL_V,
                 curseur=p_base.CUR
                 ):
        style = f"""
        QHeaderView::section {{
        background-color: rgba{couleur_bg};
        color: rgb{couleur_fg};
        border: none;
        }}

        QTreeWidget {{
        background-color: rgba{couleur_bg};
        color: rgb{couleur_fg};
        }}

        QTreeWidget::item {{
        background-color: rgba{couleur_bg_item};
        color: rgb{couleur_fg_item};
        }}

        QTreeWidget::item:hover {{
        background-color: rgba{couleur_bg_item_hover};
        color: rgb{couleur_fg_item_hover};
        }}

        QTreeWidget::item:selected {{
        background-color: rgba{couleur_bg_item_checked};
        color: rgb{couleur_fg_item_checked};
        }}

        QTreeWidget::item:selected:hover {{
        background-color: rgba{couleur_bg_item_checked_hover};
        color: rgb{couleur_fg_item_checked_hover};
        }}

        /* BORDURES */
        .QTreeWidget {{
        border-top: {bordure_width_top}px {bordure_style_top} rgba{bordure_couleur_top};
        border-bottom: {bordure_width_bottom}px {bordure_style_bottom} rgba{bordure_couleur_bottom};
        border-right: {bordure_width_right}px {bordure_style_right} rgba{bordure_couleur_right};
        border-left: {bordure_width_left}px {bordure_style_left} rgba{bordure_couleur_left};
        }}

        /* RAYONS */
        .QTreeWidget {{
        border-top-left-radius: {rayon_top_left}px;
        border-top-right-radius: {rayon_top_right}px;
        border-bottom-right-radius: {rayon_bottom_right}px;
        border-bottom-left-radius: {rayon_bottom_left}px;
        }}

        /* SCROLL */
        .QTreeWidget QScrollBar {{
        background-color: rgb{scroll_bg};
        width: {scroll_width}px;
        height: {scroll_height}px;
        }}
        .QTreeWidget::handle:horizontal {{
        min-width: {scroll_handle_min_width}px;
        }}
        .QTreeWidget::handle:vertical {{
        min-height: {scroll_handle_min_height}px;
        }}
        .QTreeWidget QScrollBar::handle {{
        background-color: rgb{scroll_handle_fg};
        }}

        .QTreeWidget QScrollBar::add-page, .QTreeWidget QScrollBar::sub-page {{
        background-color: rgb{scroll_handle_bg};
        border: none;
        }}"""

        for wg in wgs:
            wg.setStyleSheet(style)

            try:
                Fct(wg=wg, w=dim_width, h=dim_height).DIM()
                wg.setFont(Fct(font=police, font_size=police_taille).FONT())

                wg.setHorizontalScrollBarPolicy(scroll_h)
                wg.setVerticalScrollBarPolicy(scroll_v)

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
              couleur_bg_item=(0, 0, 0, 0),
              couleur_bg_item_hover=(0, 0, 0, 0),
              couleur_bg_item_checked=(0, 0, 0, 0),
              couleur_bg_item_checked_hover=(0, 0, 0, 0),
              couleur_fg_item_checked=P_rgb().bn1(),
              couleur_fg_item_checked_hover=P_rgb().bn2(),
    )

class option(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              couleur_bg=(0, 0, 0, 0),
              couleur_bg_item=(0, 0, 0, 0),
              couleur_bg_item_hover=(0, 0, 0, 0),
              couleur_bg_item_checked=(0, 0, 0, 0),
              couleur_bg_item_checked_hover=(0, 0, 0, 0),
              couleur_fg_item_checked=P_rgb().bn1(),
              couleur_fg_item_checked_hover=P_rgb().bn2(),
              dim_width=P_dim().h5(),
              bordure_width_right=P_style().bd(),
              bordure_couleur_right=P_rgb().th3(),
              scroll_h=QtCore.Qt.ScrollBarAlwaysOff,
              scroll_v=QtCore.Qt.ScrollBarAlwaysOff,
    )
