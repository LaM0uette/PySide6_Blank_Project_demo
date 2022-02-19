from PySide6 import QtWidgets

from .StyleSheet import StyleSheet
from ....build.widgets.classes import Classe_pb
from ....build import *
from ....build.widgets import p_base

class Style:
    def __init__(
            self,
            *wgs,
            button_type=None,
            width=p_base.WG_WIDTH,
            height=p_base.WG_HEIGHT,
            font=p_base.FONT,
            font_size=p_base.FONT_SIZE,
            curseur=p_base.CUR,
            style=StyleSheet().get()
    ):
        for wg in wgs:
            wg.setStyleSheet(style)

            try:
                Fct(wg=wg, w=width, h=height).DIM()
                wg.setFont(Fct(font=font, font_size=font_size).FONT())

                wg.setFlat(True)
                wg.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

                wg.setCursor(Fct(cur=curseur).CUR())
            except: pass

            # if button_type is not None: StyleSheet().set_ico_base(wg=wg)

            # try:
            #     if button_type is not None and button_type is not None:
            #         cls = Classe_pb.Classe_pb(wg=wg,
            #                                   dim_ico=dim_height * x_ico,
            #                                   DIM_ICO=dim_height * X_ICO,
            #                                   img=img_uncheck,
            #                                   img_check=img_check,
            #                                   tm=tm_uncheck,
            #                                   tm_hover=tm_hover,
            #                                   tm_check=tm_check)
            #
            #         if button_type == "check":
            #             wg.mousePressEvent = cls.MP_CHECK
            #         elif button_type == "ico":
            #             wg.enterEvent = cls.ENT_ICO
            #             wg.leaveEvent = cls.LVE_ICO
            #             wg.mousePressEvent = cls.MP_ICO
            #         elif button_type == "zoom":
            #             wg.enterEvent = cls.ENT_ZOOM
            #             wg.leaveEvent = cls.LVE_ZOOM
            # except: pass

#fg_checked=p_base.COULEURS.get("c3"),
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
                bg_gen=Rgb().tr()
            ).get()
    )

class menu_top:
    def __init__(self, *wgs):
        self.wgs = wgs

    def rtn(self,
            button_type="zoom",
            width=P_dim().h9() * 1.2,
            curseur=P_cur().souris_main(),
            couleur_bg=Rgb().tr(),
            couleur_bg_hover=Rgb().tr(),
            couleur_bg_checked=Rgb().tr(),
            couleur_bg_checked_hover=Rgb().tr(),
            couleur_fg_checked=p_base.COULEURS.get("c3"),
            couleur_bg_pressed=Rgb().tr(),
            img_uncheck=P_img().main(),
            img_uncheck_rgb="th2",
    ):
        Style(
            *self.wgs,
            button_type=button_type,
            width=width,
            curseur=curseur,

            style=StyleSheet(
                bg=couleur_bg,
                bg_hover=couleur_bg_hover,
                bg_checked=couleur_bg_checked,
                bg_checked_hover=couleur_bg_checked_hover,
                fg_checked=couleur_fg_checked,
                bg_pressed=couleur_bg_pressed,
                img_uncheck=img_uncheck,
                img_uncheck_rgb=img_uncheck_rgb,
            ).get()
        )

    def option(self):
        self.rtn(
            img_uncheck=P_img().option()
        )
    def reduire(self):
        self.rtn(
            img_uncheck=P_img().reduire(),
            img_uncheck_rgb="bn1"
        )
    def agrandir(self):
        self.rtn(
            img_uncheck=P_img().agrandir(),
            img_uncheck_rgb="th3"
        )
    def quitter(self):
        self.rtn(
            img_uncheck=P_img().quitter(),
            img_uncheck_rgb="bn2"
        )


class txt(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            style=StyleSheet(
                bg=Rgb().th1(),
                fg=Rgb().th3(),
                bg_hover=Rgb().th3(),
                fg_hover=Rgb().th1(),
                bg_pressed=Rgb().th3(),
                border_all=P_style().bd(),
                border_rgb=Rgb().th3(),
            ).get()
    )
class txt_inv(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            style=StyleSheet(
                bg=Rgb().th3(),
                fg=Rgb().th1(),
                bg_hover=Rgb().th1(),
                fg_hover=Rgb().th3(),
                bg_pressed=Rgb().th1(),
                border_all=P_style().bd(),
                border_rgb=Rgb().th3(),
            ).get()
    )

class Demo_bd(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            style=StyleSheet(
                border_all=P_style().bd(),
                border_rgb=Rgb().bn1(),
            ).get()
    )
class Demo_rd(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            style=StyleSheet(
                radius_all=10,
            ).get()
    )

class ck_ico(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            button_type="check",

            style=StyleSheet(
                bg_gen=Rgb().tr(),
            ).get()
    )
class zoom(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            button_type="zoom",

            style=StyleSheet(
                bg_gen=Rgb().tr(),
                img_uncheck=P_img().calendrier(),
                img_uncheck_rgb=""
            ).get()
    )

class dlg_ok(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            width=P_dim().h6(),
            height=None,

            style=StyleSheet(
                bg=Rgb().th1(),
                fg=Rgb().vert(),
                bg_hover=Rgb().vert(),
                fg_hover=Rgb().th1(),
                bg_pressed=Rgb().vert(),
                border_all=P_style().bd(),
                border_rgb=Rgb().vert(),
            ).get()
    )
class dlg_ok_inv(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            width=P_dim().h6(),
            height=None,

            style=StyleSheet(
                bg=Rgb().vert(),
                fg=Rgb().th1(),
                bg_hover=Rgb().th1(),
                fg_hover=Rgb().vert(),
                bg_pressed=Rgb().th1(),
                border_all=P_style().bd(),
                border_rgb=Rgb().vert(),
            ).get()
    )
class dlg_nok(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            width=P_dim().h6(),
            height=None,
            style=StyleSheet(
                bg=Rgb().th1(),
                fg=Rgb().rouge(),
                bg_hover=Rgb().rouge(),
                fg_hover=Rgb().th1(),
                bg_pressed=Rgb().rouge(),
                border_all=P_style().bd(),
                border_rgb=Rgb().rouge(),
            ).get()
        )
class dlg_nok_inv(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            width=P_dim().h6(),
            height=None,
            style=StyleSheet(
                bg=Rgb().rouge(),
                fg=Rgb().th1(),
                bg_hover=Rgb().th1(),
                fg_hover=Rgb().rouge(),
                bg_pressed=Rgb().th1(),
                border_all=P_style().bd(),
                border_rgb=Rgb().rouge(),
            ).get()
        )

class plein:
    def __init__(self, *wgs):
        self.wgs = wgs


    def rtn(self,
            couleur_bg=(0, 0, 0, 0),
            couleur_fg=(0, 0, 0),
            couleur_bg_hover=(0, 0, 0, 0),
            couleur_fg_hover=(0, 0, 0),
            dim_height=P_dim().h5(),

            bordure_width_top=0,
            bordure_width_bottom=0,
            bordure_width_right=0,
            bordure_width_left=0,
            bordure_couleur_top=(0, 0, 0, 0),
            bordure_couleur_bottom=(0, 0, 0, 0),
            bordure_couleur_right=(0, 0, 0, 0),
            bordure_couleur_left=(0, 0, 0, 0),
            curseur=P_cur().main()
            ):
        Style(*self.wgs,
                 couleur_bg=couleur_bg,
                 couleur_fg=couleur_fg,
                 couleur_bg_hover=couleur_bg_hover,
                 couleur_fg_hover=couleur_fg_hover,
                 dim_height=dim_height,

                 bordure_width_top=bordure_width_top,
                 bordure_width_bottom=bordure_width_bottom,
                 bordure_width_right=bordure_width_right,
                 bordure_width_left=bordure_width_left,
                 bordure_couleur_top=bordure_couleur_top,
                 bordure_couleur_bottom=bordure_couleur_bottom,
                 bordure_couleur_right=bordure_couleur_right,
                 bordure_couleur_left=bordure_couleur_left,
                 curseur=curseur
                 )

    def th1(self):
        self.rtn(
            couleur_bg=P_rgb().th1()+(255, ),
            couleur_fg=P_rgb().th3(),
            couleur_bg_hover=P_rgb().th1()+(255, ),
            couleur_fg_hover=P_rgb().th3()+(255, ),

            bordure_width_top=P_style().bd(),
            bordure_width_bottom=P_style().bd(),
            bordure_width_right=P_style().bd(),
            bordure_width_left=P_style().bd(),
            bordure_couleur_top=P_rgb().th2() + (255,),
            bordure_couleur_bottom=P_rgb().th2() + (255,),
            bordure_couleur_right=P_rgb().th2() + (255,),
            bordure_couleur_left=P_rgb().th2() + (255,),
        )
    def th2(self):
        self.rtn(
            couleur_bg=P_rgb().th2()+(255, ),
            couleur_fg=P_rgb().th3(),
            couleur_bg_hover=P_rgb().th2()+(255, ),
            couleur_fg_hover=P_rgb().th3()+(255, ),
        )
    def th3(self):
        self.rtn(
            couleur_bg=P_rgb().th3()+(255, ),
            couleur_fg=P_rgb().th1(),
            couleur_bg_hover=P_rgb().th3()+(255, ),
            couleur_fg_hover=P_rgb().th1()+(255, ),
        )
    def bn1(self):
        self.rtn(
            couleur_bg=P_rgb().bn1()+(255, ),
            couleur_fg=P_rgb().th3(),
            couleur_bg_hover=P_rgb().bn1()+(255, ),
            couleur_fg_hover=P_rgb().th3()+(255, ),
        )
    def bn2(self):
        self.rtn(
            couleur_bg=P_rgb().bn2()+(255, ),
            couleur_fg=P_rgb().th3(),
            couleur_bg_hover=P_rgb().bn2()+(255, ),
            couleur_fg_hover=P_rgb().th3()+(255, ),
        )
