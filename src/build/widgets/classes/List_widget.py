from .StyleSheet import StyleSheet
from ....build import *
from ....build.widgets import p_base

class Style:
    def __init__(self,
                 *wgs,
                 width=p_base.WG_WIDTH,
                 height=p_base.WG_HEIGHT,
                 font=p_base.FONT,
                 font_size=p_base.FONT_SIZE,
                 scroll_h=p_base.SCROLL_H,
                 scroll_v=p_base.SCROLL_V,
                 curseur=P_cur().croix(),
                 style=StyleSheet().get()
    ):
        for wg in wgs:
            wg.setStyleSheet(style)

            Fct(wg=wg, w=width, h=height).DIM()
            wg.setFont(Fct(font=font, font_size=font_size).FONT())

            wg.setHorizontalScrollBarPolicy(scroll_h)
            wg.setVerticalScrollBarPolicy(scroll_v)

            wg.setCursor(Fct(cur=curseur).CUR())
            wg.viewport().setCursor(Fct(cur=P_cur().souris_main()).CUR())


class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            style=StyleSheet(
                fg_item_checked=Rgb().bn1(),
            ).get()
        )
class Base_tr(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            style=StyleSheet(
                bg_gen=Rgb().tr(),
                bg_item_gen=Rgb().tr(),
                fg_item=Rgb().th3(),
                fg_item_checked=Rgb().bn1(),
            ).get()
    )


class Demo_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            height=P_dim().h5(),

            style=StyleSheet(
                fg_item_checked=Rgb().bn1(),
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
                fg_item=Rgb().th3(),
                fg_item_checked=Rgb().bn1(),
            ).get()

    )
