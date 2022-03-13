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

    def rtn(
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
