from .WgClass.MyQPushButtonStyle import Style, t
from src.lib.palettes import *


##################
##     BASE     ##
##################
class Base:
    def __init__(self, widget):
        self.widget = widget

    def Base(self):
        t(
            widget=self.widget,
        )
    def Transparent(self):
        bg = Rgb.TR

        Style(
            widget=self.widget,
            bg=bg,
            bg_hover=bg,
            bg_checked=bg,
            bg_checked_hover=bg,
            bg_pressed=bg,
            bg_checked_pressed=bg,
            fg=Rgb.TH3,
            fg_checked=Rgb.BN1,
        )


######################
##     MENU TOP     ##
######################
class MenuTop:
    def __init__(self, widget):
        self.widget = widget

    def _rtn(
            self,
            img=Img.MAIN,
            img_rgb="th2",
    ):
        bg = Rgb.TR

        Style(
            self.widget,
            pb_type="zoom",
            fixed_width=Dim.H9 * 1.2,
            cursor=Cur.SOURIS_MAIN,

            bg=bg,
            bg_hover=bg,
            bg_checked=bg,
            bg_checked_hover=bg,
            bg_pressed=bg,
            fg_checked=Rgb.TH3,
            img=img,
            img_rgb=img_rgb,
        )

    def option(self):
        self._rtn(
            img=Img.OPTION
        )
    def reduire(self):
        self._rtn(
            img=Img.REDUIRE,
            img_rgb="bn1"
        )
    def agrandir(self):
        self._rtn(
            img=Img.AGRANDIR,
            img_rgb="th3"
        )
    def quitter(self):
        self._rtn(
            img=Img.QUITTER,
            img_rgb="bn2"
        )


#################
##     TXT     ##
#################
class Txt:
    def __init__(self, widget):
        self.widget = widget
        self.bd = (StyleBase.BORDER,)*4
        self.bd_rgb = Rgb.TH3

    def txt(self):
        Style(
            self.widget,
            bg=Rgb.TH1,
            fg=Rgb.TH3,
            bg_hover=Rgb.TH3,
            fg_hover=Rgb.TH1,
            bg_pressed=Rgb.TH3,
            bg_checked=Rgb.TH3,
            fg_checked=Rgb.TH1,
            bg_checked_hover=Rgb.TH1,
            fg_checked_hover=Rgb.TH3,
            bg_checked_pressed=Rgb.TH1,
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
            bg=Rgb.TH3,
            fg=Rgb.TH1,
            bg_hover=Rgb.TH1,
            fg_hover=Rgb.TH3,
            bg_pressed=Rgb.TH1,
            bg_checked=Rgb.TH1,
            fg_checked=Rgb.TH3,
            bg_checked_hover=Rgb.TH3,
            fg_checked_hover=Rgb.TH1,
            bg_checked_pressed=Rgb.TH3,
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
        self.bd = (StyleBase.BORDER,)*4

    def _rtn(
            self,
            bg=Rgb.TH1,
            fg=Rgb.BN1,
            bg_hover=Rgb.BN1,
            fg_hover=Rgb.TH1,
            bg_pressed=Rgb.BN1,
            fg_pressed=Rgb.TH1,
            bd_rgb=Rgb.BN1,
    ):
        Style(
            self.widget,
            size_policy_v=SizePolicy.EXPANDING,
            fixed_width=Dim.H6,
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
            bg=Rgb.TH1,
            fg=Rgb.BN1,
            bg_hover=Rgb.BN1,
            fg_hover=Rgb.TH1,
            bg_pressed=Rgb.BN1,
            fg_pressed=Rgb.TH1,
            bd_rgb=Rgb.BN1,
        )
    def ok_inv(self):
        self._rtn(
            bg=Rgb.BN1,
            fg=Rgb.TH1,
            bg_hover=Rgb.TH1,
            fg_hover=Rgb.BN1,
            bg_pressed=Rgb.TH1,
            fg_pressed=Rgb.BN1,
            bd_rgb=Rgb.BN1,
        )
    def nok(self):
        self._rtn(
            bg=Rgb.TH1,
            fg=Rgb.BN2,
            bg_hover=Rgb.BN2,
            fg_hover=Rgb.TH1,
            bg_pressed=Rgb.BN2,
            fg_pressed=Rgb.TH1,
            bd_rgb=Rgb.BN2,
        )
    def nok_inv(self):
        self._rtn(
            bg=Rgb.BN2,
            fg=Rgb.TH1,
            bg_hover=Rgb.TH1,
            fg_hover=Rgb.BN2,
            bg_pressed=Rgb.TH1,
            fg_pressed=Rgb.BN2,
            bd_rgb=Rgb.BN2,
        )


###################
##     PLEIN     ##
###################
class Plein:
    def __init__(self, widget):
        self.widget = widget

    def _rtn(self,
             bg_gen=Rgb.TR,
             fg_gen=Rgb.TR,
             height=Dim.H5,

             border_gen=(0, )*4,
             border_gen_rgb=Rgb.TR,
             cursor=Cur.MAIN
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
            bg_gen=Rgb.TH1,
            fg_gen=Rgb.TH3,
            border_gen=(StyleBase.BORDER,) * 4,
            border_gen_rgb=Rgb.TH2,
        )
    def th2(self):
        self._rtn(
            bg_gen=Rgb.TH2,
            fg_gen=Rgb.TH3,
        )
    def th3(self):
        self._rtn(
            bg_gen=Rgb.TH3,
            fg_gen=Rgb.TH1,
        )
    def bn1(self):
        self._rtn(
            bg_gen=Rgb.BN1,
            fg_gen=Rgb.TH3,
        )
    def bn2(self):
        self._rtn(
            bg_gen=Rgb.BN2,
            fg_gen=Rgb.TH3,
        )
