from PySide6 import QtCore, QtWidgets

from .StyleSheet import StyleSheet
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
            scroll_h=p_base.SCROLL_H,
            scroll_v=p_base.SCROLL_V,
            curseur=p_base.CUR,
            style=StyleSheet().get()
    ):
        for wg in wgs:
            wg.setStyleSheet(style)

            Fct(wg=wg, w=width, h=height).DIM()
            wg.setFont(Fct(font=font, font_size=font_size).FONT())

            wg.setHorizontalScrollBarPolicy(scroll_h)
            wg.setVerticalScrollBarPolicy(scroll_v)

            wg.setFrameShape(QtWidgets.QFrame.NoFrame)

            wg.setCursor(Fct(cur=curseur).CUR())


class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            style=StyleSheet(
            ).get()
        )
class Base_tr(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            scroll_h=QtCore.Qt.ScrollBarAlwaysOff,
            scroll_v=QtCore.Qt.ScrollBarAlwaysOff,

            style=StyleSheet(
                bg_gen=Rgb().tr(),
            ).get()
    )

class option(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            width=P_dim().h5(),
            scroll_h=QtCore.Qt.ScrollBarAlwaysOff,
            scroll_v=QtCore.Qt.ScrollBarAlwaysOff,

            style=StyleSheet(
                bg_gen=Rgb().tr(),
            ).get()
    )
