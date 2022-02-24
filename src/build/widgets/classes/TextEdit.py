from PySide6 import QtGui

from ....build import *
from ....build.widgets import p_base

class Style:
    def __init__(
            self,
            *wgs,
            width=p_base.WG_WIDTH,
            height=p_base.WG_HEIGHT,
            font=p_base.FONT,
            font_size=p_base.FONT_SIZE,
            align_horizontal=Align().left(),
            align_vertical=Align().v_center(),

            # Couleurs BG
            bg=p_base.BG,
            bg_selection=p_base.BG_SELECTION,
            # Couleurs FG
            fg=p_base.FG,
            fg_selection=p_base.FG_SELECTION,
            fg_placeholder=p_base.FG_PLACEHOLDER,

            # Bordures
            border=p_base.WG_BORDER_WIDTH,
            border_style=p_base.WG_BORDER_STYLE,
            border_rgb=p_base.WG_BORDER_RGB,
            # Bordures hover
            border_hover=p_base.WG_BORDER_WIDTH,
            border_hover_style=p_base.WG_BORDER_STYLE,
            border_hover_rgb=p_base.WG_BORDER_RGB,

            # Rayons
            radius=p_base.WG_RADIUS,

            # Scroll
            scroll_bg=p_base.SCROLL_BG,
            scroll_width=p_base.SCROLL_WIDTH,
            scroll_height=p_base.SCROLL_HEIGHT,
            scroll_handle_bg=p_base.SCROLL_HANDLE_BG,
            scroll_handle_bg_hover=p_base.SCROLL_HANDLE_BG_HOVER,
            scroll_handle_fg=p_base.SCROLL_HANDLE_FG,
            scroll_handle_fg_hover=p_base.SCROLL_HANDLE_FG_HOVER,
            scroll_handle_min_width=p_base.SCROLL_HANDLE_MIN_WIDTH,
            scroll_handle_min_height=p_base.SCROLL_HANDLE_MIN_HEIGHT,
    ):
        style = f"""
                /* WIDGET */
                .QLineEdit, .QPlainTextEdit, .QTextEdit {{
                background-color: rgba{bg};
                selection-background-color: rgba{bg_selection};
                selection-color: rgba{fg_selection};
                }}
        
                /* BORDURES */
                .QLineEdit, .QPlainTextEdit, .QTextEdit {{
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}
                .QLineEdit:hover, .QPlainTextEdit:hover, .QTextEdit:hover {{
                border-top: {border_hover[0]}px {border_hover_style} rgba{border_hover_rgb};
                border-bottom: {border_hover[1]}px {border_hover_style} rgba{border_hover_rgb};
                border-right: {border_hover[2]}px {border_hover_style} rgba{border_hover_rgb};
                border-left: {border_hover[3]}px {border_hover_style} rgba{border_hover_rgb};
                }}
                
                /* RAYONS */
                .QComboBox, .QFontComboBox {{
                border-top-right-radius: {radius[0]}px;
                border-top-left-radius: {radius[1]}px;
                border-bottom-right-radius: {radius[2]}px;
                border-bottom-left-radius: {radius[3]}px;
                }}
                
                /* SCROLL */
                QScrollBar {{
                background-color: rgba{scroll_bg};
                width: {scroll_width}px;
                height: {scroll_height}px;
                }}
                QScrollBar::handle:horizontal {{
                min-width: {scroll_handle_min_width}px;
                }}
                QScrollBar::handle:vertical {{
                min-height: {scroll_handle_min_height}px;
                }}
                QScrollBar::handle {{
                background-color: rgba{scroll_handle_fg};
                }}
                QScrollBar::handle:hover {{
                background-color: rgba{scroll_handle_fg_hover};
                }}
                
                QScrollBar::add-page, QScrollBar::sub-page {{
                background-color: rgba{scroll_handle_bg};
                border: none;
                }}
                QScrollBar::add-page:hover, QScrollBar::sub-page:hover {{
                background-color: rgba{scroll_handle_bg_hover};
                border: none;
                }}"""

        for wg in wgs:
            wg.setStyleSheet(style)

            Fct(wg=wg, w=width, h=height).DIM()
            wg.setFont(Fct(font=font, font_size=font_size).FONT())

            try: wg.setAlignment(align_horizontal | align_vertical)
            except: pass

            wg.setCursor(Fct(cur=Cur().IBeam()).CUR())
            try: wg.viewport().setCursor(Fct(cur=Cur().IBeam()).CUR())
            except: pass

            palette_txt = QtGui.QPalette()
            palette_txt.setColor(QtGui.QPalette.Text, QtGui.QColor(*fg))
            palette_txt.setColor(QtGui.QPalette.PlaceholderText, QtGui.QColor(*fg_placeholder))
            wg.setPalette(palette_txt)


##################
##     BASE     ##
##################
class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
        )
class Base_tr(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            bg=Rgb().tr(),
            fg=Rgb().th3()
    )

class tr_taille(Style):
    def __init__(self, *wgs, h):
        super().__init__(
            *wgs,
            height=None,
            font_size=h,

            bg=Rgb().tr(),
            fg=Rgb().th3()
    )
class rgb_hex(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            bg=Rgb().tr(),
            bg_selection=Rgb().th3(),
            fg=Rgb().th3(),
            fg_selection=Rgb().th1(),
            align_horizontal=Align().h_center()
    )


##################
##     DEMO     ##
##################
class Demo_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            height=Dim().h5(),
    )
class Demo_tr(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            height=Dim().h5(),

            bg=Rgb().tr(),
    )
