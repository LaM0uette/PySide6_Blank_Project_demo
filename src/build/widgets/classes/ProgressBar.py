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
                 text_visible=p_base.TEXT_VISIBLE,
                 curseur=P_cur().souris(),
                 style=StyleSheet().get()
    ):
        for wg in wgs:
            wg.setStyleSheet(style)

            Fct(wg=wg, w=width, h=height).DIM()
            wg.setFont(Fct(font=font, font_size=font_size).FONT())

            wg.setAlignment(P_align().c().c())
            wg.setTextVisible(text_visible)

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
        super().__init__(*wgs,
              text_visible=False,
            style=StyleSheet(
                bg_gen=Rgb().tr()
            ).get()
    )
