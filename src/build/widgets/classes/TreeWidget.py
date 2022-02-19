from PySide6 import QtCore, QtWidgets

from .StyleSheet import StyleSheet
from ....build import *
from ....build.widgets import p_base

class Style:
    def __init__(
            self,
            *wgs,
            width=p_base.WIDTH,
            height=p_base.HEIGHT,
            font=p_base.FONT,
            font_size=p_base.FONT_SIZE,
            scroll_h=p_base.SCROLL_H,
            scroll_v=p_base.SCROLL_V,
            curseur=p_base.CUR,
            style=StyleSheet()
    ):
        for wg in wgs:
            wg.setStyleSheet(style.get())

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
            )
        )
class Base_tr(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            scroll_h=QtCore.Qt.ScrollBarAlwaysOff,
            scroll_v=QtCore.Qt.ScrollBarAlwaysOff,

            style=StyleSheet(
                bg_gen=Rgb().tr(),
                bg_item_gen=Rgb().tr(),
                fg_item=Rgb().th3(),
                fg_item_checked=Rgb().bn1(),
                border_item_gen_left=2,
                border_item_rgb=Rgb().th2(),
                border_item_rgb_hover=Rgb().th3(),
                border_item_rgb_checked=Rgb().bn1(),
                border_item_rgb_checked_hover=Rgb().bn1(),
            )
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
                bg_item_gen=Rgb().tr(),
                fg_item=Rgb().th3(),
                fg_item_checked=Rgb().bn1(),
                border_item_gen_left=2,
                border_item_rgb=Rgb().th2(),
                border_item_rgb_hover=Rgb().th3(),
                border_item_rgb_checked=Rgb().bn1(),
                border_item_rgb_checked_hover=Rgb().bn1(),
            )
    )
