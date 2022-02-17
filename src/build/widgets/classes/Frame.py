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
            curseur=P_cur().souris(),
            style=StyleSheet().get()
    ):
        for wg in wgs:
            wg.setStyleSheet(style)

            Fct(wg=wg, w=width, h=height).DIM()

            wg.setCursor(Fct(cur=curseur).CUR())

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
        super().__init__(
            *wgs,
            style=StyleSheet(
                bg=Rgb().tr()
            ).get()
    )

class Menu_top(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            height=P_dim().h9(),

            style=StyleSheet(
                bg=Rgb().th1(),
            ).get()
    )
class Menu_bottom(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            height=P_dim().h10(),

            style=StyleSheet(
                bg=Rgb().th2(),
            ).get()
    )
class Menu_bottom_dlg(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            height=P_dim().h9(),

            style=StyleSheet(
            bg=Rgb().th2(),
            ).get()
    )

class Cadre:
    def __init__(self, *wgs):
        self.wgs = wgs

    def rtn(self, rgb):
        Style(
            *self.wgs,
            style=StyleSheet(
                bg=Rgb().tr(),
                border_gen_all=P_style().bd(),
                border_gen_rgb=rgb,
            ).get()
        )

    def th1(self): self.rtn(rgb=Rgb().th1())
    def th2(self): self.rtn(rgb=Rgb().th2())
    def th3(self): self.rtn(rgb=Rgb().th3())
    def bn1(self): self.rtn(rgb=Rgb().bn1())
    def bn2(self): self.rtn(rgb=Rgb().bn2())

class palette_rgb(Style):
    def __init__(self, *wgs, rgb):
        super().__init__(
            *wgs,
            style=StyleSheet(
                bg=rgb,
                radius_all=40,
            ).get()
    )


class Demo_hover(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            style=StyleSheet(
                bg=Rgb().tr(),
                border_all=P_style().bd(),
                border_rgb=Rgb().bn1(),
                border_all_hover=P_style().bd() * 2,
                border_style_hover="dashed",
                border_rgb_hover=Rgb().vert(),
            ).get()
    )
