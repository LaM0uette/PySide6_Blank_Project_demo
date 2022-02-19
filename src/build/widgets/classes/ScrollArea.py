from PySide6 import QtWidgets

from .StyleSheet import StyleSheet
from ....build import *
from ....build.widgets import p_base

class Style:
    def __init__(
            self,
            *wgs,
            width=p_base.WIDTH,
            height=p_base.HEIGHT,
            scroll_h=p_base.SCROLL_H,
            scroll_v=p_base.SCROLL_V,
            style=StyleSheet()
    ):
        for wg in wgs:
            wg.setStyleSheet(style.get())

            Fct(wg=wg, w=width, h=height).DIM()

            wg.setHorizontalScrollBarPolicy(scroll_h)
            wg.setVerticalScrollBarPolicy(scroll_v)

            wg.setFrameShape(QtWidgets.QFrame.NoFrame)


class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            style=StyleSheet(
            )
        )
class Base_tr(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
            style=StyleSheet(
                bg=Rgb().tr()
            )
        )


class Demo(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            style=StyleSheet(
                bg=Rgb().th1(),
            )
    )
