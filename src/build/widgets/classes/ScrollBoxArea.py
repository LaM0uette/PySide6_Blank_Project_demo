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
            style=StyleSheet().get()
    ):
        for wg in wgs:
            wg.setStyleSheet(style)

            Fct(wg=wg, w=width, h=height).DIM()

            wg.setHorizontalScrollBarPolicy(scroll_h)
            wg.setVerticalScrollBarPolicy(scroll_v)

            wg.setFrameShape(QtWidgets.QFrame.NoFrame)


class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            style=StyleSheet(
            ).get()
        )
class Base_tr(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
            style=StyleSheet(
                bg=Rgb().tr()
            ).get()
        )


class Demo(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            style=StyleSheet(
                bg=Rgb().th1(),
                border_all=3,
                border_rgb=Rgb().bn1(),
                border_all_hover=6,
                border_rgb_hover=Rgb().bn2()
            ).get()
    )
