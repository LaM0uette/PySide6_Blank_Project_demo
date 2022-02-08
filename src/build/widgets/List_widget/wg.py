from ....build import *
from .. import p_base


class wg:
    def __init__(self,
                 *wgs,
                 colors_type,
                 colors,
                 dim,
                 font,
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
        /* LIST_WIDGET */
        QListWidget {{
        background-color: rgb{colors.get("c1")};
        color: rgb{colors.get("c3")};
        border: {bd.get("px")}px solid rgb{colors.get("c3")};
        }}

        /* ITEM */
        QListWidget::item {{
        background-color: rgb{colors.get("c1")};
        color: rgb{colors.get("c3")};
        }}
        QListWidget::item:selected {{
        background-color: rgb{colors.get("c2")};
        color: rgb{colors.get("bn1")};
        }}
        QListWidget::item:hover {{
        color: rgb{colors.get("bn1")};
        }}
        QListWidget::item:selected:hover {{
        color: rgb{colors.get("bn2")};
        }}

        /* BORDURES */
        .QComboBox, .QFontComboBox {{
        border-top: {bordure_width_top}px {bordure_style_top} rgba{bordure_couleur_top};
        border-bottom: {bordure_width_bottom}px {bordure_style_bottom} rgba{bordure_couleur_bottom};
        border-right: {bordure_width_right}px {bordure_style_right} rgba{bordure_couleur_right};
        border-left: {bordure_width_left}px {bordure_style_left} rgba{bordure_couleur_left};
        }}
        
        /* RAYONS */
        .QComboBox, .QFontComboBox {{
        border-top-left-radius: {rayon_top_left}px;
        border-top-right-radius: {rayon_top_right}px;
        border-bottom-right-radius: {rayon_bottom_right}px;
        border-bottom-left-radius: {rayon_bottom_left}px;
        }}
        
        /* SCROLL */
        QComboBox QScrollBar, QFontComboBox QScrollBar {{
        background-color: rgb{scroll_bg};
        width: {scroll_width}px;
        height: {scroll_height}px;
        }}
        QComboBox::handle:horizontal, QFontComboBox::handle:horizontal {{
        min-width: {scroll_handle_min_width}px;
        }}
        QComboBox::handle:vertical, QFontComboBox::handle:vertical {{
        min-height: {scroll_handle_min_height}px;
        }}
        QComboBox QScrollBar::handle, QFontComboBox QScrollBar::handle {{
        background-color: rgb{scroll_handle_fg};
        }}
        QComboBox QScrollBar::add-page, QComboBox QScrollBar::sub-page, QFontComboBox QScrollBar::add-page, QFontComboBox QScrollBar::sub-page {{
        background-color: rgb{scroll_handle_bg};
        border: none;
        }}"""

        for wg in wgs:
            wg.setStyleSheet(style)

            try:
                Fct(wg=wg, w=dim.get("w"), h=dim.get("h")).DIM()
                wg.setFont(Fct(font_size=font).FONT())

                wg.setHorizontalScrollBarPolicy(scroll_h)
                wg.setVerticalScrollBarPolicy(scroll_v)

                wg.setCursor(Fct(cur=curseur).CUR())
                wg.view().setCursor(Fct(cur=P_cur().souris_main()).CUR())
            except: pass
