from PySide6 import QtGui

from ....build import *
from .. import p_base


class wg:
    def __init__(self,
                 *wgs,
                 colors,
                 dim,
                 font,
                 align,

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
    ):
        style = f"""
        QLineEdit, QPlainTextEdit, QTextEdit {{
        background-color: rgb{colors.get("c1")};
        color: rgb{colors.get("bn1")};
        selection-background-color: rgb{colors.get("c3")};
        selection-color: rgb{colors.get("c1")};
        }}

        /* BORDURES */
        .QLineEdit, .QPlainTextEdit, .QTextEdit {{
        border-top: {bordure_width_top}px {bordure_style_top} rgba{bordure_couleur_top};
        border-bottom: {bordure_width_bottom}px {bordure_style_bottom} rgba{bordure_couleur_bottom};
        border-right: {bordure_width_right}px {bordure_style_right} rgba{bordure_couleur_right};
        border-left: {bordure_width_left}px {bordure_style_left} rgba{bordure_couleur_left};
        }}
        
        /* RAYONS */
        .QLineEdit, .QPlainTextEdit, .QTextEdit {{
        border-top-left-radius: {rayon_top_left}px;
        border-top-right-radius: {rayon_top_right}px;
        border-bottom-right-radius: {rayon_bottom_right}px;
        border-bottom-left-radius: {rayon_bottom_left}px;
        }}
        
        /* SCROLL */
        .QLineEdit QScrollBar, .QPlainTextEdit QScrollBar, .QTextEdit QScrollBar {{
        background-color: rgb{scroll_bg};
        width: {scroll_width}px;
        height: {scroll_height}px;
        }}
        .QLineEdit::handle:horizontal, .QPlainTextEdit::handle:horizontal, .QTextEdit::handle:horizontal {{
        min-width: {scroll_handle_min_width}px;
        }}
        .QLineEdit::handle:vertical, .QPlainTextEdit::handle:vertical, .QTextEdit::handle:vertical {{
        min-height: {scroll_handle_min_height}px;
        }}
        .QLineEdit QScrollBar::handle, .QPlainTextEdit QScrollBar::handle, .QTextEdit QScrollBar::handle {{
        background-color: rgb{scroll_handle_fg};
        }}
        
        .QLineEdit QScrollBar::add-page, .QLineEdit QScrollBar::sub-page, .QPlainTextEdit QScrollBar::add-page, .QPlainTextEdit QScrollBar::sub-page, .QTextEdit QScrollBar::add-page, .QTextEdit QScrollBar::sub-page {{
        background-color: rgb{scroll_handle_bg};
        border: none;
        }}"""

        for wg in wgs:
            wg.setStyleSheet(style)

            try:
                Fct(wg=wg, w=dim.get("w"), h=dim.get("h")).DIM()
                wg.setFont(Fct(font_size=font).FONT())

                wg.setAlignment(align)

                wg.setCursor(Fct(cur=P_cur().IBeam()).CUR())
            except: pass

            try:wg.viewport().setCursor(Fct(cur=P_cur().IBeam()).CUR())
            except: pass

            col1 = colors.get("c1")[0] - 20 if colors.get("c1")[0] > 160 else colors.get("c1")[0] + 20
            col2 = colors.get("c1")[1] - 20 if colors.get("c1")[1] > 160 else colors.get("c1")[1] + 20
            col3 = colors.get("c1")[2] - 20 if colors.get("c1")[2] > 160 else colors.get("c1")[2] + 20
            colors_placeholder = (col1, col2, col3)

            pl = QtGui.QPalette()
            pl.setColor(QtGui.QPalette.PlaceholderText, QtGui.QColor(*colors_placeholder))
            pl.setColor(QtGui.QPalette.Text, QtGui.QColor(*colors.get("c3")))
            wg.setPalette(pl)
