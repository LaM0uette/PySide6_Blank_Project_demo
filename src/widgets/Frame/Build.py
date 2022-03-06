import datetime

from PySide6 import QtCore

from src.build.mods import Functions
from src.lib.palettes import *
from src.widgets import vb_wg


class Build:
    def __init__(
            self,
            *wgs,
            width=VBase.WIDTH,
            height=VBase.HEIGHT,
            ombre_portee=False,
            curseur=Cur().souris(),
            # Couleurs BG
            bg=VBase.BG,
            # Bordures
            border=VBase.WG_BORDER_WIDTH,
            border_style=VBase.WG_BORDER_STYLE,
            border_rgb=VBase.WG_BORDER_RGB,
            # Bordures hover
            border_hover=VBase.WG_BORDER_WIDTH,
            border_hover_style=VBase.WG_BORDER_STYLE,
            border_hover_rgb=VBase.WG_BORDER_RGB,
            # Rayons
            radius=(0, 0, 0, 0),
    ):
        style = f"""
                /* FRAME */
                .QFrame {{
                background-color: rgba{bg};
                }}

                /* BORDURES */
                .QFrame {{
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}
                .QFrame:hover {{
                border-top: {border_hover[0]}px {border_hover_style} rgba{border_hover_rgb};
                border-bottom: {border_hover[1]}px {border_hover_style} rgba{border_hover_rgb};
                border-right: {border_hover[2]}px {border_hover_style} rgba{border_hover_rgb};
                border-left: {border_hover[3]}px {border_hover_style} rgba{border_hover_rgb};
                }}

                /* RAYONS */
                .QFrame {{
                border-top-right-radius: {radius[0]}px;
                border-top-left-radius: {radius[1]}px;
                border-bottom-right-radius: {radius[2]}px;
                border-bottom-left-radius: {radius[3]}px;
                }}"""

        for wg in wgs:
            wg.setStyleSheet(style)

            Fct(wg=wg, w=width, h=height).DIM()

            if ombre_portee:
                self.shadow = QtWidgets.QGraphicsDropShadowEffect(wg)
                self.shadow.setBlurRadius(12)
                self.shadow.setColor(QtGui.QColor(0, 0, 0, 130))
                self.shadow.setOffset(0, 0)
                wg.setGraphicsEffect(self.shadow)

            wg.setCursor(Fct(cur=curseur).CUR())
