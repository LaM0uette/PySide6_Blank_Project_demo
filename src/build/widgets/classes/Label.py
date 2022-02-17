from .StyleSheet import StyleSheet
from ....build import *
from ....build.widgets import p_base

class Style:
    def __init__(
            self,
            *wgs,
            width=None,
            height=None,
            font=p_base.FONT,
            font_size=p_base.FONT_SIZE,
            align_horizontal=Align().left(),
            align_vertical=Align().v_center(),
            word_wrap=p_base.WORD_WRAP,
            curseur=p_base.CUR,
            style=StyleSheet().get()
    ):
        for wg in wgs:
            wg.setStyleSheet(style)

            Fct(wg=wg, w=width, h=height).DIM()
            wg.setFont(Fct(font=font, font_size=font_size).FONT())

            wg.setAlignment(align_horizontal | align_vertical)
            wg.setWordWrap(word_wrap)

            wg.setCursor(Fct(cur=curseur).CUR())


class Base_th(Style):
    def __init__(self, *wgs, font_size=p_base.FONT_SIZE):
        super().__init__(
            *wgs,
            font_size=font_size,
            style=StyleSheet(
            ).get()
    )
class Base_tr(Style):
    def __init__(self, *wgs, font_size=p_base.FONT_SIZE):
        super().__init__(
            *wgs,
            font_size=font_size,
            style=StyleSheet(
                bg_gen=Rgb().tr(),
                fg_gen=Rgb().th3(),
            ).get()
    )

class Titre(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            font_size=P_font().h1(),
            align_horizontal=Align().h_center(),
            style=StyleSheet(
                bg_gen=Rgb().tr(),
                fg_gen=Rgb().th3(),
            ).get()
    )


class DemoCat(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            font_size=P_font().h2(),
            align_horizontal=Align().h_center(),
            style=StyleSheet(
                bg_gen=Rgb().tr(),
                fg_gen=Rgb().th3(),
                border_gen_bottom=P_style().bd(),
                border_gen_rgb=Rgb().bn1(),
            ).get()
    )
