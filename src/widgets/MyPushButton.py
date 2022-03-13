from .WgClass.MyQPushButtonStyle import Style
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
        self.rgb_ok = Rgb().bn1()
        self.rgb_nok = Rgb().bn2()

    def _rtn(self):


    def ok(self):

        Style(
            self.widget,
            fixed_width=Dim().h6(),
            fixed_height=None,
            bg=Rgb().th1(),
            fg=self.rgb_ok,
            bg_hover=self.rgb_ok,
            fg_hover=Rgb().th1(),
            bg_pressed=self.rgb_ok,
            fg_pressed=Rgb().th1(),
            border=self.bd,
            border_hover=self.bd,
            border_checked=self.bd,
            border_checked_hover=self.bd,
            border_rgb=self.rgb_ok,
            border_hover_rgb=self.rgb_ok,
            border_checked_rgb=self.rgb_ok,
            border_checked_hover_rgb=self.rgb_ok,
        )
    def ok_inv(self):

        
        Style(
            self.widget,
            fixed_width=Dim().h6(),
            fixed_height=None,
            bg=self.rgb_ok,
            fg=Rgb().th1(),
            bg_hover=Rgb().th1(),
            fg_hover=self.rgb_ok,
            bg_pressed=Rgb().th1(),
            fg_pressed=self.rgb_ok,
            border=self.bd,
            border_hover=self.bd,
            border_checked=self.bd,
            border_checked_hover=self.bd,
            border_rgb=self.rgb_ok,
            border_hover_rgb=self.rgb_ok,
            border_checked_rgb=self.rgb_ok,
            border_checked_hover_rgb=self.rgb_ok,
        )
    def nok(self):
        Style(
            self.widget,
            fixed_width=Dim().h6(),
            fixed_height=None,
            bg=Rgb().th1(),
            fg=self.rgb_nok,
            bg_hover=self.rgb_nok,
            fg_hover=Rgb().th1(),
            bg_pressed=self.rgb_nok,
            fg_pressed=Rgb().th1(),
            border=self.bd,
            border_hover=self.bd,
            border_checked=self.bd,
            border_checked_hover=self.bd,
            border_rgb=self.rgb_nok,
            border_hover_rgb=self.rgb_nok,
            border_checked_rgb=self.rgb_nok,
            border_checked_hover_rgb=self.rgb_nok,
        )
    def nok_inv(self):
        Style(
            self.widget,
            fixed_width=Dim().h6(),
            fixed_height=None,
            bg=self.rgb_nok,
            fg=Rgb().th1(),
            bg_hover=Rgb().th1(),
            fg_hover=self.rgb_nok,
            bg_pressed=Rgb().th1(),
            fg_pressed=self.rgb_nok,
            border=self.bd,
            border_hover=self.bd,
            border_checked=self.bd,
            border_checked_hover=self.bd,
            border_rgb=self.rgb_nok,
            border_hover_rgb=self.rgb_nok,
            border_checked_rgb=self.rgb_nok,
            border_checked_hover_rgb=self.rgb_nok,
        )
