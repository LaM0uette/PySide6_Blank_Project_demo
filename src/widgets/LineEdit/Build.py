from PySide6 import QtGui

from src.build.mods import Functions
from src.lib.palettes import *
from src.widgets import vb_wg


class Build:
    def __init__(
            self,
            *wgs,

            # Dimensions
            width=vb_wg.WIDTH,
            height=vb_wg.HEIGHT,

            # Police
            font=vb_wg.FONT,
            font_size=vb_wg.FONT_SIZE,

            # Paramètres
            align_horizontal=PaAlign.LEFT,
            align_vertical=PaAlign.CENTER_VERTICAL,
            clear_button=False,
            echo_mode=PaEchoMode.NORMAL,
            focus_policy=vb_wg.FOCUS_POLICY,
            frame=False,
            input_mask=PaInputMask.NO,
            max_length=vb_wg.MAX_LENGTH,

            # Couleurs BG
            bg=vb_wg.BG,
            bg_selection=vb_wg.BG_SELECTION,
            # Couleurs FG
            fg=vb_wg.FG,
            fg_selection=vb_wg.FG_SELECTION,
            fg_placeholder=vb_wg.FG_PLACEHOLDER,

            # Bordures
            border=vb_wg.BORDER_WIDTH,
            border_style=vb_wg.BORDER_STYLE,
            border_rgb=vb_wg.BORDER_RGB,
            # Bordures hover
            border_hover=vb_wg.BORDER_WIDTH,
            border_hover_style=vb_wg.BORDER_STYLE,
            border_hover_rgb=vb_wg.BORDER_RGB,

            # Rayons
            radius=vb_wg.RADIUS,
    ):
        """
        *Align: QtCore.Qt : Align().%nomAlign() \n
        *Border_Style: str() : dashed | dot-dash | dot-dot-dash | dotted | double | groove | inset | outset | ridge | solid | none \n
        *PaCur: list() : PaCur().%nomCurseur() \n
        *PaDim: int() : PaDim().%nomDim() \n
        *PaEchoMode: QtWidgets.QLineEdit : PaEchoMode().%nomEcho() \n
        *PaFocusPolicy: QtCore.Qt : PaFocusPolicy().%nomFocus \n
        *PaFont: int() : PaFont().%nomFont() \n
        *PaInputMask: str() : PaInputMask().%nomInput() \n
        *RgbBox: tuple() : RgbBox().%nomCouleur() \n
        *Tuple: tuple() : (int(), int(), int(), int()) == (Top, Bottom, Right, Left) | (TopRight, TopLeft, BottomRight, BottomLeft) \n

        :param wgs: Widgets séparés par ","
        :param width: *PaDim
        :param height: *PaDim
        :param font: str()
        :param font_size: *PaFont
        :param align_horizontal: *Align
        :param align_vertical: *Align
        :param clear_button: bool()
        :param echo_mode: *PaEchoMode
        :param focus_policy: *PaFocusPolicy
        :param frame: bool()
        :param input_mask: *PaInputMask
        :param max_length: int()
        :param bg: *RgbBox
        :param bg_selection: *RgbBox
        :param fg: *RgbBox
        :param fg_selection: *RgbBox
        :param fg_placeholder: *RgbBox
        :param border: *Tuple
        :param border_style: *Border_Style
        :param border_rgb: *RgbBox
        :param border_hover: *Tuple
        :param border_hover_style: *Border_Style
        :param border_hover_rgb: *RgbBox
        :param radius: *Tuple
        """

        style = f"""
                /* WIDGET */
                QLineEdit {{
                background-color: rgba{bg};
                selection-background-color: rgba{bg_selection};
                selection-color: rgba{fg_selection};
                }}

                /* BORDURES */
                QLineEdit {{
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}
                QLineEdit:hover {{
                border-top: {border_hover[0]}px {border_hover_style} rgba{border_hover_rgb};
                border-bottom: {border_hover[1]}px {border_hover_style} rgba{border_hover_rgb};
                border-right: {border_hover[2]}px {border_hover_style} rgba{border_hover_rgb};
                border-left: {border_hover[3]}px {border_hover_style} rgba{border_hover_rgb};
                }}

                /* RAYONS */
                QLineEdit {{
                border-top-right-radius: {radius[0]}px;
                border-top-left-radius: {radius[1]}px;
                border-bottom-right-radius: {radius[2]}px;
                border-bottom-left-radius: {radius[3]}px;
                }}"""
        for wg in wgs:
            # Dimensions
            Functions().SET_DIM(wg, width=width, height=height)

            # Police
            Functions().SET_FONT(wg, font=font, font_size=font_size)

            # Paramètres
            wg.setAlignment(align_horizontal | align_vertical)
            wg.setClearButtonEnabled(clear_button)
            wg.setEchoMode(echo_mode)
            wg.setFocusPolicy(focus_policy)
            wg.setFrame(frame)
            wg.setInputMask(input_mask)
            wg.setMaxLength(max_length)

            # Palettes
            palette_txt = QtGui.QPalette()
            palette_txt.setColor(QtGui.QPalette.Text, QtGui.QColor(*fg))
            palette_txt.setColor(QtGui.QPalette.PlaceholderText, QtGui.QColor(*fg_placeholder))
            wg.setPalette(palette_txt)

            # Curseur
            wg.setCursor(Functions().SET_CURSOR(PaCur.IBEAM))

            # Style
            wg.setStyleSheet(style)
