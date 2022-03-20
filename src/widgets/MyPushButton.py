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
        bg = PaRgb.TR

        Style(
            widget=self.widget,
            bg=bg,
            bg_hover=bg,
            bg_checked=bg,
            bg_checked_hover=bg,
            bg_pressed=bg,
            bg_checked_pressed=bg,
            fg=PaRgb.TH3,
            fg_checked=PaRgb.BN1,
        )


######################
##     MENU TOP     ##
######################
class MenuTop:
    def __init__(self, widget):
        self.widget = widget

    def _rtn(
            self,
            img=PaImg.MAIN,
            img_rgb="th2",
    ):
        bg = PaRgb.TR

        Style(
            self.widget,
            pb_type="zoom",
            dim=DcDim.Base(fixed_width=PaDim.H9 * 1.2),
            cursor=PaCur.SOURIS_MAIN,

            bg=bg,
            bg_hover=bg,
            bg_checked=bg,
            bg_checked_hover=bg,
            bg_pressed=bg,
            fg_checked=PaRgb.TH3,
            img=img,
            img_rgb=img_rgb,
        )

    def option(self):
        self._rtn(
            img=PaImg.OPTION
        )
    def reduire(self):
        self._rtn(
            img=PaImg.REDUIRE,
            img_rgb="bn1"
        )
    def agrandir(self):
        self._rtn(
            img=PaImg.AGRANDIR,
            img_rgb="th3"
        )
    def quitter(self):
        self._rtn(
            img=PaImg.QUITTER,
            img_rgb="bn2"
        )


#################
##     TXT     ##
#################
class Txt:
    def __init__(self, widget):
        self.widget = widget
        self.bd = (PaStyleBase.BORDER,) * 4
        self.bd_rgb = PaRgb.TH3

    def txt(self):
        Style(
            self.widget,
            bg=PaRgb.TH1,
            fg=PaRgb.TH3,
            bg_hover=PaRgb.TH3,
            fg_hover=PaRgb.TH1,
            bg_pressed=PaRgb.TH3,
            bg_checked=PaRgb.TH3,
            fg_checked=PaRgb.TH1,
            bg_checked_hover=PaRgb.TH1,
            fg_checked_hover=PaRgb.TH3,
            bg_checked_pressed=PaRgb.TH1,
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
            bg=PaRgb.TH3,
            fg=PaRgb.TH1,
            bg_hover=PaRgb.TH1,
            fg_hover=PaRgb.TH3,
            bg_pressed=PaRgb.TH1,
            bg_checked=PaRgb.TH1,
            fg_checked=PaRgb.TH3,
            bg_checked_hover=PaRgb.TH3,
            fg_checked_hover=PaRgb.TH1,
            bg_checked_pressed=PaRgb.TH3,
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
        self.bd = (PaStyleBase.BORDER,) * 4

    def _rtn(
            self,
            bg=PaRgb.TH1,
            fg=PaRgb.BN1,
            bg_hover=PaRgb.BN1,
            fg_hover=PaRgb.TH1,
            bg_pressed=PaRgb.BN1,
            fg_pressed=PaRgb.TH1,
            bd_rgb=PaRgb.BN1,
    ):
        Style(
            self.widget,

            size_policy=DcSizePolicy.Base(
                vertical=PaSizePolicy.EXPANDING
            ),

            dim=DcDim.Base(
                fixed_width=PaDim.H6,
                fixed_height=None,
            ),

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
            bg=PaRgb.TH1,
            fg=PaRgb.BN1,
            bg_hover=PaRgb.BN1,
            fg_hover=PaRgb.TH1,
            bg_pressed=PaRgb.BN1,
            fg_pressed=PaRgb.TH1,
            bd_rgb=PaRgb.BN1,
        )
    def ok_inv(self):
        self._rtn(
            bg=PaRgb.BN1,
            fg=PaRgb.TH1,
            bg_hover=PaRgb.TH1,
            fg_hover=PaRgb.BN1,
            bg_pressed=PaRgb.TH1,
            fg_pressed=PaRgb.BN1,
            bd_rgb=PaRgb.BN1,
        )
    def nok(self):
        self._rtn(
            bg=PaRgb.TH1,
            fg=PaRgb.BN2,
            bg_hover=PaRgb.BN2,
            fg_hover=PaRgb.TH1,
            bg_pressed=PaRgb.BN2,
            fg_pressed=PaRgb.TH1,
            bd_rgb=PaRgb.BN2,
        )
    def nok_inv(self):
        self._rtn(
            bg=PaRgb.BN2,
            fg=PaRgb.TH1,
            bg_hover=PaRgb.TH1,
            fg_hover=PaRgb.BN2,
            bg_pressed=PaRgb.TH1,
            fg_pressed=PaRgb.BN2,
            bd_rgb=PaRgb.BN2,
        )


###################
##     PLEIN     ##
###################
class Plein:
    def __init__(self, widget):
        self.widget = widget

    def _rtn(self,
             bg_gen=PaRgb.TR,
             fg_gen=PaRgb.TR,
             height=PaDim.H5,

             border_gen=(0, )*4,
             border_gen_rgb=PaRgb.TR,
             cursor=PaCur.MAIN
             ):
        Style(
            self.widget,
            dim=DcDim.Base(fixed_height=height),
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
            bg_gen=PaRgb.TH1,
            fg_gen=PaRgb.TH3,
            border_gen=(PaStyleBase.BORDER,) * 4,
            border_gen_rgb=PaRgb.TH2,
        )
    def th2(self):
        self._rtn(
            bg_gen=PaRgb.TH2,
            fg_gen=PaRgb.TH3,
        )
    def th3(self):
        self._rtn(
            bg_gen=PaRgb.TH3,
            fg_gen=PaRgb.TH1,
        )
    def bn1(self):
        self._rtn(
            bg_gen=PaRgb.BN1,
            fg_gen=PaRgb.TH3,
        )
    def bn2(self):
        self._rtn(
            bg_gen=PaRgb.BN2,
            fg_gen=PaRgb.TH3,
        )
