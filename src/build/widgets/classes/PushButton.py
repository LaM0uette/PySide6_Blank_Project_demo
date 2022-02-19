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
            bg=Rgb().tr(),
            bg_hover=Rgb().tr(),
            bg_checked=Rgb().tr(),
            bg_checked_hover=Rgb().tr(),
            fg_checked=p_base.COULEURS.get("c3"),
            bg_pressed=Rgb().tr(),
            img_uncheck=P_img().main(),
            img_uncheck_rgb="th2",
    ):
        Style(
            *self.wgs,
            button_type=button_type,
            width=width,
            curseur=curseur,

            style=StyleSheet(
                bg=bg,
                bg_hover=bg_hover,
                bg_checked=bg_checked,
                bg_checked_hover=bg_checked_hover,
                fg_checked=fg_checked,
                bg_pressed=bg_pressed,
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
            bg=Rgb().tr(),
            fg=Rgb().tr(),
            bg_hover=Rgb().tr(),
            fg_hover=Rgb().tr(),
            height=P_dim().h5(),

            border_all=0,
            border_rgb=Rgb().tr(),
            curseur=P_cur().main()
            ):
        Style(
            *self.wgs,
            height=height,
            curseur=curseur,

            style=StyleSheet(
                bg=bg,
                fg=fg,
                bg_hover=bg_hover,
                fg_hover=fg_hover,
                border_all=border_all,
                border_rgb=border_rgb,
            ).get()
        )

    def th1(self):
        self.rtn(
            bg=P_rgb().th1(),
            fg=P_rgb().th3(),
            bg_hover=P_rgb().th1(),
            fg_hover=P_rgb().th3(),
            border_all=P_style().bd(),
            border_rgb=P_rgb().th2(),
        )
    def th2(self):
        self.rtn(
            bg=P_rgb().th2(),
            fg=P_rgb().th3(),
            bg_hover=P_rgb().th2(),
            fg_hover=P_rgb().th3(),
        )
    def th3(self):
        self.rtn(
            bg=P_rgb().th3(),
            fg=P_rgb().th1(),
            bg_hover=P_rgb().th3(),
            fg_hover=P_rgb().th1(),
        )
    def bn1(self):
        self.rtn(
            bg=P_rgb().bn1(),
            fg=P_rgb().th3(),
            bg_hover=P_rgb().bn1(),
            fg_hover=P_rgb().th3(),
        )
    def bn2(self):
        self.rtn(
            bg=P_rgb().bn2(),
            fg=P_rgb().th3(),
            bg_hover=P_rgb().bn2(),
            fg_hover=P_rgb().th3(),
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
