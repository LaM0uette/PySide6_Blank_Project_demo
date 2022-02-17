from PySide6 import QtWidgets, QtCore

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
            font_size_hd=p_base.FONT_SIZE_HD,
            scroll_h=p_base.SCROLL_H,
            scroll_v=p_base.SCROLL_V,
            header_h=p_base.HEADER_H,
            header_v=p_base.HEADER_V,
            curseur=P_cur().croix(),
            style=StyleSheet().get()
    ):
        for wg in wgs:
            wg.setStyleSheet(style)
            wg.horizontalHeader().setStyleSheet(style)
            wg.verticalHeader().setStyleSheet(style)

            try:
                Fct(wg=wg, w=width, h=height).DIM()
                wg.setFont(Fct(font=font, font_size=font_size).FONT())
                wg.horizontalHeader().setFont(Fct(font_size=font_size_hd).FONT())
                wg.verticalHeader().setFont(Fct(font_size=font_size_hd).FONT())

                wg.setHorizontalScrollBarPolicy(scroll_h)
                wg.setVerticalScrollBarPolicy(scroll_v)
                wg.horizontalHeader().setVisible(header_h)
                wg.verticalHeader().setVisible(header_v)

                wg.setCursor(Fct(cur=curseur).CUR())
                wg.viewport().setCursor(Fct(cur=curseur).CUR())

                wg.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
                wg.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
                wg.verticalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
                wg.setFrameShape(QtWidgets.QFrame.NoFrame)

                wg.resizeColumnsToContents()
            except: pass


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
                bg_gen=Rgb().tr(),
                bg_item_gen=Rgb().tr(),
                fg_checked=p_base.COULEURS.get("bn1"),
                fg_checked_hover=p_base.COULEURS.get("bn2"),
            ).get()
    )


class Demo_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            height=P_dim().h5(),

            style=StyleSheet(
                fg_checked=p_base.COULEURS.get("bn1"),
                fg_checked_hover=p_base.COULEURS.get("bn2"),
            ).get()
    )
class Demo_tr(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            height=P_dim().h5(),

            style=StyleSheet(
                bg_gen=Rgb().tr(),
                bg_item_gen=Rgb().tr(),
                fg_checked=p_base.COULEURS.get("bn1"),
                fg_checked_hover=p_base.COULEURS.get("bn2"),
            ).get()
    )
