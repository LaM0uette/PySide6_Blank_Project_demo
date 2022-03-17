from .WgClass.MyQToolButtonStyle import Style
from src.lib.palettes import *


##################
##     BASE     ##
##################
class Base:
    def __init__(self, widget):
        self.widget = widget

    def Base(self):
        Style(
            widget=self.widget,
        )
    def Transparent(self):
        bg = Rgb().tr()

        Style(
            widget=self.widget,
            bg=bg,
            bg_hover=bg,
            bg_checked=bg,
            bg_checked_hover=bg,
            bg_pressed=bg,
            bg_checked_pressed=bg,
            fg=Rgb().th3(),
            fg_checked=Rgb().bn1(),
        )


######################
##     MENU TOP     ##
######################
class MenuTop:
    def __init__(self, widget):
        self.widget = widget

    def _rtn(
            self,
            img=Img().main(),
            img_rgb="th2",
    ):
        bg = Rgb().tr()

        Style(
            self.widget,
            pb_type="zoom",
            fixed_width=Dim().h9() * 1.2,
            cursor=Cur().souris_main(),

            bg=bg,
            bg_hover=bg,
            bg_checked=bg,
            bg_checked_hover=bg,
            bg_pressed=bg,
            fg_checked=Rgb().th3(),
            img=img,
            img_rgb=img_rgb,
        )

    def option(self):
        self._rtn(
            img=Img().option()
        )
    def reduire(self):
        self._rtn(
            img=Img().reduire(),
            img_rgb="bn1"
        )
    def agrandir(self):
        self._rtn(
            img=Img().agrandir(),
            img_rgb="th3"
        )
    def quitter(self):
        self._rtn(
            img=Img().quitter(),
            img_rgb="bn2"
        )


#################
##     TXT     ##
#################
class Txt:
    def __init__(self, widget):
        self.widget = widget
        self.bd = (StyleBase().border(),)*4
        self.bd_rgb = Rgb().th3()

    def txt(self):
        Style(
            self.widget,
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
            border=self.bd,
            border_hover=self.bd,
            border_checked=self.bd,
            border_checked_hover=self.bd,
            border_rgb=self.bd_rgb,
            border_hover_rgb=self.bd_rgb,
            border_checked_rgb=self.bd_rgb,
            border_checked_hover_rgb=self.bd_rgb,
        )
    def inverse(self):
        Style(
            self.widget,
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
            border=self.bd,
            border_hover=self.bd,
            border_checked=self.bd,
            border_checked_hover=self.bd,
            border_rgb=self.bd_rgb,
            border_hover_rgb=self.bd_rgb,
            border_checked_rgb=self.bd_rgb,
            border_checked_hover_rgb=self.bd_rgb,
        )


#################
##     DLG     ##
#################
class Dlg:
    def __init__(self, widget):
        self.widget = widget
        self.bd = (StyleBase().border(),)*4

    def _rtn(
            self,
            bg=Rgb().th1(),
            fg=Rgb().bn1(),
            bg_hover=Rgb().bn1(),
            fg_hover=Rgb().th1(),
            bg_pressed=Rgb().bn1(),
            fg_pressed=Rgb().th1(),
            bd_rgb=Rgb().bn1(),
    ):
        Style(
            self.widget,
            size_policy_v=SizePolicy().expanding(),
            fixed_width=Dim().h6(),
            fixed_height=None,
            bg=bg,
            fg=fg,
            bg_hover=bg_hover,
            fg_hover=fg_hover,
            bg_pressed=bg_pressed,
            fg_pressed=fg_pressed,
            border=self.bd,
            border_hover=self.bd,
            border_checked=self.bd,
            border_checked_hover=self.bd,
            border_rgb=bd_rgb,
            border_hover_rgb=bd_rgb,
            border_checked_rgb=bd_rgb,
            border_checked_hover_rgb=bd_rgb,
        )

    def ok(self):
        self._rtn(
            bg=Rgb().th1(),
            fg=Rgb().bn1(),
            bg_hover=Rgb().bn1(),
            fg_hover=Rgb().th1(),
            bg_pressed=Rgb().bn1(),
            fg_pressed=Rgb().th1(),
            bd_rgb=Rgb().bn1(),
        )
    def ok_inv(self):
        self._rtn(
            bg=Rgb().bn1(),
            fg=Rgb().th1(),
            bg_hover=Rgb().th1(),
            fg_hover=Rgb().bn1(),
            bg_pressed=Rgb().th1(),
            fg_pressed=Rgb().bn1(),
            bd_rgb=Rgb().bn1(),
        )
    def nok(self):
        self._rtn(
            bg=Rgb().th1(),
            fg=Rgb().bn2(),
            bg_hover=Rgb().bn2(),
            fg_hover=Rgb().th1(),
            bg_pressed=Rgb().bn2(),
            fg_pressed=Rgb().th1(),
            bd_rgb=Rgb().bn2(),
        )
    def nok_inv(self):
        self._rtn(
            bg=Rgb().bn2(),
            fg=Rgb().th1(),
            bg_hover=Rgb().th1(),
            fg_hover=Rgb().bn2(),
            bg_pressed=Rgb().th1(),
            fg_pressed=Rgb().bn2(),
            bd_rgb=Rgb().bn2(),
        )


###################
##     PLEIN     ##
###################
class Plein:
    def __init__(self, widget):
        self.widget = widget

    def _rtn(self,
             bg_gen=Rgb().tr(),
             fg_gen=Rgb().tr(),
             height=Dim().h5(),

             border_gen=(0, )*4,
             border_gen_rgb=Rgb().tr(),
             cursor=Cur().main()
             ):
        Style(
            self.widget,
            fixed_height=height,
            cursor=cursor,

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

            radius=(0, )*4
        )

    def th1(self):
        self._rtn(
            bg_gen=Rgb().th1(),
            fg_gen=Rgb().th3(),
            border_gen=(StyleBase().border(),) * 4,
            border_gen_rgb=Rgb().th2(),
        )
    def th2(self):
        self._rtn(
            bg_gen=Rgb().th2(),
            fg_gen=Rgb().th3(),
        )
    def th3(self):
        self._rtn(
            bg_gen=Rgb().th3(),
            fg_gen=Rgb().th1(),
        )
    def bn1(self):
        self._rtn(
            bg_gen=Rgb().bn1(),
            fg_gen=Rgb().th3(),
        )
    def bn2(self):
        self._rtn(
            bg_gen=Rgb().bn2(),
            fg_gen=Rgb().th3(),
        )
