from .StyleSheet import StyleSheet
from ....build import *
from ....build.widgets import p_base

class Style:
    def __init__(
            self,

            # Widgets
            *wgs,

            # Dimensions WG
            width=p_base.WG_WIDTH,
            height=p_base.WG_HEIGHT,

            # Police
            font=p_base.FONT,
            font_size=p_base.FONT_SIZE,

            # Curseur
            curseur=P_cur().souris_main(),

            # Style
            style=StyleSheet().GET()
    ):

        for wg in wgs:
            wg.setStyleSheet(style)

            Fct(wg=wg, w=width, h=height).DIM()
            wg.setFont(Fct(font=font, font_size=font_size).FONT())

            wg.setCursor(Fct(cur=curseur).CUR())


class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            style=StyleSheet(
                radius_all=5
            ).GET()
        )
class Base_tr(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            style=StyleSheet(
                bg_gen=Rgb().tr(),
                fg=Rgb().th3(),
                fg_checked=Rgb().th3()
            ).GET()
        )