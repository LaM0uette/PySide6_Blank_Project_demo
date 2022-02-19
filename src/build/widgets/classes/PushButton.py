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
            x_ico=P_style().x_ico(),
            X_ICO=P_style().X_ICO(),
            font=p_base.FONT,
            font_size=p_base.FONT_SIZE,
            img=p_base.IMG_UNROLL,
            img_hover=p_base.IMG_UNROLL_HOVER,
            img_check=p_base.IMG_CHECK,
            img_check_hover=p_base.IMG_CHECK_HOVER,
            img_rgb=p_base.IMG_UNROLL_RGB,
            img_hover_rgb=p_base.IMG_UNROLL_HOVER_RGB,
            img_check_rgb=p_base.IMG_CHECK_RGB,
            img_check_hover_rgb=p_base.IMG_CHECK_HOVER_RGB,
            curseur=p_base.CUR,
            style=StyleSheet().get()
    ):
        for wg in wgs:
            wg.setStyleSheet(style)

            Fct(wg=wg, w=width, h=height).DIM()
            wg.setFont(Fct(font=font, font_size=font_size).FONT())

            wg.setFlat(True)
            wg.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

            wg.setCursor(Fct(cur=curseur).CUR())

            if button_type is not None and img is not None:
                Fct(wg=wg, img=f"{img}{img_rgb}", dim=height * x_ico).ICON()

            if button_type is not None:
                cls = Classe_pb.Classe_pb(wg=wg,
                                          dim_ico=height * x_ico,
                                          DIM_ICO=height * X_ICO,
                                          img=img,
                                          img_check=img_check,
                                          img_rgb=img_rgb,
                                          tm_hover=tm_hover,
                                          tm_check=tm_check)

                if button_type == "check":
                    wg.mousePressEvent = cls.MP_CHECK
                elif button_type == "ico":
                    wg.enterEvent = cls.ENT_ICO
                    wg.leaveEvent = cls.LVE_ICO
                    wg.mousePressEvent = cls.MP_ICO
                elif button_type == "zoom":
                    wg.enterEvent = cls.ENT_ZOOM
                    wg.leaveEvent = cls.LVE_ZOOM

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
            img=P_img().main(),
            img_rgb="th2",
    ):
        Style(
            *self.wgs,
            button_type="zoom",
            width=P_dim().h9() * 1.2,
            img=img,
            img_rgb=img_rgb,
            curseur=P_cur().souris_main(),

            style=StyleSheet(
                bg=Rgb().tr(),
                bg_hover=Rgb().tr(),
                bg_checked=Rgb().tr(),
                bg_checked_hover=Rgb().tr(),
                bg_pressed=Rgb().tr(),
                fg_checked=p_base.COULEURS.get("c3"),
            ).get()
        )

    def option(self):
        self.rtn(
            img=P_img().option()
        )
    def reduire(self):
        self.rtn(
            img=P_img().reduire(),
            img_rgb="bn1"
        )
    def agrandir(self):
        self.rtn(
            img=P_img().agrandir(),
            img_rgb="th3"
        )
    def quitter(self):
        self.rtn(
            img=P_img().quitter(),
            img_rgb="bn2"
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
                bg_checked=Rgb().th3(),
                fg_checked=Rgb().th1(),
                bg_checked_hover=Rgb().th1(),
                fg_checked_hover=Rgb().th3(),
                bg_checked_pressed=Rgb().th1(),
                border_gen_all=P_style().bd(),
                border_gen_rgb=Rgb().th3(),
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
                bg_checked=Rgb().th1(),
                fg_checked=Rgb().th3(),
                bg_checked_hover=Rgb().th3(),
                fg_checked_hover=Rgb().th1(),
                bg_checked_pressed=Rgb().th3(),
                border_gen_all=P_style().bd(),
                border_gen_rgb=Rgb().th3(),
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
                border_gen_all=P_style().bd(),
                border_gen_rgb=Rgb().vert(),
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
                border_gen_all=P_style().bd(),
                border_gen_rgb=Rgb().vert(),
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
                border_gen_all=P_style().bd(),
                border_gen_rgb=Rgb().rouge(),
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
                border_gen_all=P_style().bd(),
                border_gen_rgb=Rgb().rouge(),
            ).get()
        )

class plein:
    def __init__(self, *wgs):
        self.wgs = wgs

    def rtn(self,
            bg_gen=Rgb().tr(),
            fg_gen=Rgb().tr(),
            height=P_dim().h5(),

            border_gen_all=0,
            border_gen_rgb=Rgb().tr(),
            curseur=P_cur().main()
            ):
        Style(
            *self.wgs,
            height=height,
            curseur=curseur,

            style=StyleSheet(
                bg_gen=bg_gen,
                fg_gen=fg_gen,
                border_gen_all=border_gen_all,
                border_gen_rgb=border_gen_rgb,
            ).get()
        )

    def th1(self):
        self.rtn(
            bg_gen=Rgb().th1(),
            fg_gen=Rgb().th3(),
            border_gen_all=P_style().bd(),
            border_gen_rgb=Rgb().th2(),
        )
    def th2(self):
        self.rtn(
            bg_gen=Rgb().th2(),
            fg_gen=Rgb().th3(),
        )
    def th3(self):
        self.rtn(
            bg_gen=Rgb().th3(),
            fg_gen=Rgb().th1(),
        )
    def bn1(self):
        self.rtn(
            bg_gen=Rgb().bn1(),
            fg_gen=Rgb().th3(),
        )
    def bn2(self):
        self.rtn(
            bg_gen=Rgb().bn2(),
            fg_gen=Rgb().th3(),
        )


class Demo_bd(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            style=StyleSheet(
                border_gen_all=P_style().bd(),
                border_gen_rgb=Rgb().bn1(),
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
