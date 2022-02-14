from PySide6 import QtGui

from ....build import *
from ....build.widgets import p_base

class Style:
    def __init__(self,
                 *wgs,
                 couleur_bg=p_base._COLORS_BG,
                 couleur_bg_placeholder=p_base.COLORS_BG_PLACEHOLDER,
                 couleur_bg_selection=p_base.COLORS_BG_SELECTION,
                 couleur_fg=p_base._COLORS_FG,
                 couleur_fg_placeholder=p_base.COLORS_FG_PLACEHOLDER,
                 couleur_fg_selection=p_base.COLORS_FG_SELECTION,
                 dim_width=p_base.WG_WIDTH,
                 dim_height=p_base.WG_HEIGHT,
                 police=p_base.FONT,
                 police_taille=p_base.FONT_SIZE,
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
                 scroll_bg=p_base.SCROLL_BG,
                 scroll_handle_bg=p_base.SCROLL_HANDLE_BG,
                 scroll_handle_fg=p_base.SCROLL_HANDLE_FG,
                 scroll_width=p_base.SCROLL_WIDTH,
                 scroll_height=p_base.SCROLL_HEIGHT,
                 scroll_handle_min_width=p_base.SCROLL_HANDLE_MIN_WIDTH,
                 scroll_handle_min_height=p_base.SCROLL_HANDLE_MIN_HEIGHT,
                 align=p_base.ALIGN,
                 ):
        style = f"""
        .QLineEdit, .QPlainTextEdit, .QTextEdit {{
        background-color: rgba{couleur_bg};
        selection-background-color: rgb{couleur_bg_selection};
        selection-color: rgb{couleur_fg_selection};
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
                Fct(wg=wg, w=dim_width, h=dim_height).DIM()
                wg.setFont(Fct(font=police, font_size=police_taille).FONT())

                wg.setAlignment(align)

                wg.setCursor(Fct(cur=P_cur().IBeam()).CUR())
            except: pass

            try: wg.viewport().setCursor(Fct(cur=P_cur().IBeam()).CUR())
            except: pass

            pl = QtGui.QPalette()
            pl.setColor(QtGui.QPalette.PlaceholderText, QtGui.QColor(*couleur_fg_placeholder))
            pl.setColor(QtGui.QPalette.Text, QtGui.QColor(*couleur_fg))
            wg.setPalette(pl)


class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs)
class Base_tr(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              couleur_bg=(0, 0, 0, 0),
    )

class tr_taille(Style):
    def __init__(self, *wgs, h):
        super().__init__(*wgs,
              couleur_bg=(0, 0, 0, 0),
              dim_height=None,
              police_taille=h
    )


class Demo_th(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              dim_height=P_dim().h5()
    )
class Demo_tr(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              couleur_bg=(0, 0, 0, 0),
              dim_height=P_dim().h5()
    )
