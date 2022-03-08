from src.lib.palettes import *
from src.widgets import vb_wg
from src.widgets.PushButton.Build import Build




##################
##     BASE     ##
##################
class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
        )
class Base_tr(Style):
    bg = Rgb().tr()

    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            bg=self.bg,
            bg_hover=self.bg,
            bg_checked=self.bg,
            bg_checked_hover=self.bg,
            bg_pressed=self.bg,
            bg_checked_pressed=self.bg,
            fg=Rgb().th3(),
            fg_checked=Rgb().bn1(),
    )
class menu_top:
    def __init__(self, *wgs):
        self.wgs = wgs

    def rtn(self,
            img=Img().main(),
            img_rgb="th2",
            ):
        Style(
            *self.wgs,
            wg_type="zoom",
            width=Dim().h9() * 1.2,
            curseur=Cur().souris_main(),

            bg=Rgb().tr(),
            bg_hover=Rgb().tr(),
            bg_checked=Rgb().tr(),
            bg_checked_hover=Rgb().tr(),
            bg_pressed=Rgb().tr(),
            fg_checked=Rgb().th3(),
            img=img,
            img_rgb=img_rgb,
        )

    def option(self):
        self.rtn(
            img=Img().option()
        )
    def reduire(self):
        self.rtn(
            img=Img().reduire(),
            img_rgb="bn1"
        )
    def agrandir(self):
        self.rtn(
            img=Img().agrandir(),
            img_rgb="th3"
        )
    def quitter(self):
        self.rtn(
            img=Img().quitter(),
            img_rgb="bn2"
        )

#################
##     TXT     ##
#################
class txt(Style):
    bd_gen = ((StyleBase().bd(),) * 4)
    bd_rgb = Rgb().th3()

    def __init__(self, *wgs):
        super().__init__(
            *wgs,
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
            border=self.bd_gen,
            border_hover=self.bd_gen,
            border_checked=self.bd_gen,
            border_checked_hover=self.bd_gen,
            border_rgb=self.bd_rgb,
            border_hover_rgb=self.bd_rgb,
            border_checked_rgb=self.bd_rgb,
            border_checked_hover_rgb=self.bd_rgb,
    )
class txt_inv(Style):
    bd_gen = ((StyleBase().bd(),) * 4)
    bd_rgb = Rgb().th3()
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
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
            border=self.bd_gen,
            border_hover=self.bd_gen,
            border_checked=self.bd_gen,
            border_checked_hover=self.bd_gen,
            border_rgb=self.bd_rgb,
            border_hover_rgb=self.bd_rgb,
            border_checked_rgb=self.bd_rgb,
            border_checked_hover_rgb=self.bd_rgb,
    )


#################
##     DLG     ##
#################
class dlg_ok(Style):
    bd_gen = ((StyleBase().bd(),) * 4)
    rgb_gen = Rgb().bn1()

    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            width=Dim().h6(),
            height=None,

            bg=Rgb().th1(),
            fg=self.rgb_gen,
            bg_hover=self.rgb_gen,
            fg_hover=Rgb().th1(),
            bg_pressed=self.rgb_gen,
            fg_pressed=Rgb().th1(),
            border=self.bd_gen,
            border_hover=self.bd_gen,
            border_checked=self.bd_gen,
            border_checked_hover=self.bd_gen,
            border_rgb=self.rgb_gen,
            border_hover_rgb=self.rgb_gen,
            border_checked_rgb=self.rgb_gen,
            border_checked_hover_rgb=self.rgb_gen,
    )
class dlg_ok_inv(Style):
    bd_gen = ((StyleBase().bd(),) * 4)
    rgb_gen = Rgb().bn1()

    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            width=Dim().h6(),
            height=None,

            bg=self.rgb_gen,
            fg=Rgb().th1(),
            bg_hover=Rgb().th1(),
            fg_hover=self.rgb_gen,
            bg_pressed=Rgb().th1(),
            fg_pressed=self.rgb_gen,
            border=self.bd_gen,
            border_hover=self.bd_gen,
            border_checked=self.bd_gen,
            border_checked_hover=self.bd_gen,
            border_rgb=self.rgb_gen,
            border_hover_rgb=self.rgb_gen,
            border_checked_rgb=self.rgb_gen,
            border_checked_hover_rgb=self.rgb_gen,
    )
class dlg_nok(Style):
    bd_gen = ((StyleBase().bd(),) * 4)
    rgb_gen = Rgb().bn2()

    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            width=Dim().h6(),
            height=None,

            bg=Rgb().th1(),
            fg=self.rgb_gen,
            bg_hover=self.rgb_gen,
            fg_hover=Rgb().th1(),
            bg_pressed=self.rgb_gen,
            fg_pressed=Rgb().th1(),
            border=self.bd_gen,
            border_hover=self.bd_gen,
            border_checked=self.bd_gen,
            border_checked_hover=self.bd_gen,
            border_rgb=self.rgb_gen,
            border_hover_rgb=self.rgb_gen,
            border_checked_rgb=self.rgb_gen,
            border_checked_hover_rgb=self.rgb_gen,
        )
class dlg_nok_inv(Style):
    bd_gen = ((StyleBase().bd(),) * 4)
    rgb_gen = Rgb().bn2()

    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            width=Dim().h6(),
            height=None,

            bg=self.rgb_gen,
            fg=Rgb().th1(),
            bg_hover=Rgb().th1(),
            fg_hover=self.rgb_gen,
            bg_pressed=Rgb().th1(),
            fg_pressed=self.rgb_gen,
            border=self.bd_gen,
            border_hover=self.bd_gen,
            border_checked=self.bd_gen,
            border_checked_hover=self.bd_gen,
            border_rgb=self.rgb_gen,
            border_hover_rgb=self.rgb_gen,
            border_checked_rgb=self.rgb_gen,
            border_checked_hover_rgb=self.rgb_gen,
        )
class plein:
    def __init__(self, *wgs):
        self.wgs = wgs

    def rtn(self,
            bg_gen=Rgb().tr(),
            fg_gen=Rgb().tr(),
            height=Dim().h5(),

            border_gen=((0, )*4),
            border_gen_rgb=Rgb().tr(),
            curseur=Cur().main()
            ):
        Style(
            *self.wgs,
            height=height,
            curseur=curseur,

            bg=bg_gen,
            bg_hover=bg_gen,
            bg_checked=bg_gen,
            bg_checked_hover=bg_gen,
            bg_pressed=bg_gen,
            bg_checked_pressed=bg_gen,
            fg=fg_gen,
            fg_hover=fg_gen,
            fg_checked=fg_gen,
            fg_checked_hover=fg_gen,
            fg_pressed=fg_gen,
            fg_checked_pressed=fg_gen,
            border=border_gen,
            border_hover=border_gen,
            border_checked=border_gen,
            border_checked_hover=border_gen,
            border_rgb=border_gen_rgb,
            border_hover_rgb=border_gen_rgb,
            border_checked_rgb=border_gen_rgb,
            border_checked_hover_rgb=border_gen_rgb,

            radius=((0, )*4)
        )

    def th1(self):
        self.rtn(
            bg_gen=Rgb().th1(),
            fg_gen=Rgb().th3(),
            border_gen=((StyleBase().bd(),) * 4),
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


##################
##     DEMO     ##
##################
class Demo_bd(Style):
    bd_gen = ((StyleBase().bd(),) * 4)
    bd_rgb = Rgb().bn1()

    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            border=self.bd_gen,
            border_hover=self.bd_gen,
            border_checked=self.bd_gen,
            border_checked_hover=self.bd_gen,
            border_rgb=self.bd_rgb,
            border_hover_rgb=self.bd_rgb,
            border_checked_rgb=self.bd_rgb,
            border_checked_hover_rgb=self.bd_rgb,
    )
class Demo_rd(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            radius=((10, )*4)
    )
class ck_ico(Style):
    bg = Rgb().tr()

    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            wg_type="check",

            bg=self.bg,
            bg_hover=self.bg,
            bg_checked=self.bg,
            bg_checked_hover=self.bg,
            fg=Rgb().th3(),
    )
class zoom(Style):
    bg = Rgb().tr()

    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            wg_type="zoom",

            bg=self.bg,
            bg_hover=self.bg,
            bg_checked=self.bg,
            bg_checked_hover=self.bg,
            bg_pressed=self.bg,
            bg_checked_pressed=self.bg,
            img=Img().calendrier(),
            img_rgb="",
    )
