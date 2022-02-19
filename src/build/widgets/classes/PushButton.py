from PySide6 import QtWidgets

from .StyleSheet import StyleSheet
from ....build import *
from ....build.widgets import p_base

class Style:
    def __init__(
            self,
            *wgs,
            wg_type=None,
            width=p_base.WG_WIDTH,
            height=p_base.WG_HEIGHT,
            font=p_base.FONT,
            font_size=p_base.FONT_SIZE,
            curseur=p_base.CUR,
            style=StyleSheet()
    ):
        for wg in wgs:
            wg.setStyleSheet(style.get())

            Fct(wg=wg, w=width, h=height).DIM()
            wg.setFont(Fct(font=font, font_size=font_size).FONT())

            wg.setFlat(True)
            wg.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

            wg.setCursor(Fct(cur=curseur).CUR())

            cls = style.get_cls_pb(wg=wg, wg_type=wg_type)

            if wg_type == "check":
                wg.mousePressEvent = cls.MP_CHECK
            elif wg_type == "ico":
                wg.enterEvent = cls.ENT_ICO
                wg.leaveEvent = cls.LVE_ICO
                wg.mousePressEvent = cls.MP_ICO
            elif wg_type == "zoom":
                    wg.enterEvent = cls.ENT_ZOOM
                    wg.leaveEvent = cls.LVE_ZOOM


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
                bg_gen=Rgb().tr(),
                fg=Rgb().th3(),
                fg_checked=Rgb().bn1(),
            )
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
            wg_type="zoom",
            width=P_dim().h9() * 1.2,
            curseur=P_cur().souris_main(),

            style=StyleSheet(
                bg=Rgb().tr(),
                bg_hover=Rgb().tr(),
                bg_checked=Rgb().tr(),
                bg_checked_hover=Rgb().tr(),
                bg_pressed=Rgb().tr(),
                fg_checked=p_base.COULEURS.get("c3"),
                img=img,
                img_rgb=img_rgb,
            )
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
            )
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
            )
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
            )
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
            )
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
            )
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
            )
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
            )
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
            )
    )
class Demo_rd(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            style=StyleSheet(
                radius_all=10,
            )
    )

class ck_ico(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            wg_type="check",

            style=StyleSheet(
                bg_gen=Rgb().tr(),
                fg=Rgb().th3(),
            )
    )
class zoom(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            wg_type="zoom",

            style=StyleSheet(
                bg_gen=Rgb().tr(),
                img=P_img().calendrier(),
                img_rgb="",
            )
    )
