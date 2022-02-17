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

            # Paramètres
            edit=p_base.EDIT,

            # Curseur
            curseur=p_base.CUR,

            # Style
            style=StyleSheet().get()
    ):
        for wg in wgs:
            wg.setStyleSheet(style)

            Fct(wg=wg, w=width, h=height).DIM()
            wg.setFont(Fct(font=font, font_size=font_size).FONT())

            wg.setEditable(edit)

            wg.setCursor(Fct(cur=curseur).CUR())
            wg.view().setCursor(Fct(cur=P_cur().souris_main()).CUR())
            if edit:
                wg.lineEdit().setFont(Fct(font_size=font_size).FONT())
                wg.lineEdit().setCursor(Fct(cur=P_cur().IBeam()).CUR())


class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            curseur=P_cur().main(),
            style=StyleSheet(
            ).get()
    )
class Base_tr(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            edit=True,
            style=StyleSheet(
                bg_gen=Rgb().tr(),
                fg=Rgb().th3(),
                bg_selection=Rgb().th3(),
                fg_selection=Rgb().th1(),
            ).get()
    )
