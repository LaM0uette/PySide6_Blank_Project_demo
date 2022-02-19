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
            align_horizontal=Align().left(),
            align_vertical=Align().v_center(),
            style=StyleSheet()
    ):

        for wg in wgs:
            wg.setStyleSheet(style.get())

            Fct(wg=wg, w=width, h=height).DIM()
            wg.setFont(Fct(font=font, font_size=font_size).FONT())

            try: wg.setAlignment(align_horizontal | align_vertical)
            except: pass

            wg.setCursor(Fct(cur=P_cur().IBeam()).CUR())
            try: wg.viewport().setCursor(Fct(cur=P_cur().IBeam()).CUR())
            except: pass

            wg.setPalette(style.get_txt_palette())


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
            style=StyleSheet(
                bg=Rgb().tr(),
                fg=Rgb().th3()
            )
    )

class tr_taille(Style):
    def __init__(self, *wgs, h):
        super().__init__(
            *wgs,
            height=None,
            font_size=h,

            style=StyleSheet(
                bg=Rgb().tr(),
                fg=Rgb().th3()
            )
    )


class Demo_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            height=P_dim().h5(),

            style=StyleSheet(
            )
    )
class Demo_tr(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            height=P_dim().h5(),

            style=StyleSheet(
                bg=Rgb().tr(),
            )
    )
