from . import wg
from ....build import *
from .. import p_base

import importlib
importlib.reload(wg)


class Base_th:
    def __init__(self, *wgs):
        wg.wg(*wgs)
class Base_tr:
    def __init__(self, *wgs):
        wg.wg(*wgs,
              couleur_bg=(0, 0, 0, 0),
              couleur_bg_hover=(0, 0, 0, 0),
              couleur_bg_checked=(0, 0, 0, 0),
              couleur_bg_checked_hover=(0, 0, 0, 0),
              couleur_fg_checked=p_base.COULEURS.get("c3"),
              )

class menu_top:
    def __init__(self, *wgs):
        self.wgs = wgs

    def rtn(self,
            type_bouton="zoom",
            couleur_bg=(0, 0, 0, 0),
            couleur_bg_hover=(0, 0, 0, 0),
            couleur_bg_checked=(0, 0, 0, 0),
            couleur_bg_checked_hover=(0, 0, 0, 0),
            couleur_fg_checked=p_base.COULEURS.get("c3"),
            couleur_bg_pressed=(0, 0, 0, 0),
            img_uncheck=P_img().main(),
            tm_uncheck="th2",
            dim_width=P_dim().h9()*1.2,
            curseur=P_cur().souris_main()
    ):
        wg.wg(*self.wgs,
              type_bouton=type_bouton,
              couleur_bg=couleur_bg,
              couleur_bg_hover=couleur_bg_hover,
              couleur_bg_checked=couleur_bg_checked,
              couleur_bg_checked_hover=couleur_bg_checked_hover,
              couleur_fg_checked=couleur_fg_checked,
              couleur_bg_pressed=couleur_bg_pressed,
              img_uncheck=img_uncheck,
              tm_uncheck=tm_uncheck,
              dim_width=dim_width,
              curseur=curseur
              )


    def option(self):
        self.rtn(
            img_uncheck=P_img().option()
        )
    def reduire(self):
        self.rtn(
            img_uncheck=P_img().reduire(),
            tm_uncheck="bn1"
        )
    def agrandir(self):
        self.rtn(
            img_uncheck=P_img().agrandir(),
            tm_uncheck="th3"
        )
    def quitter(self):
        self.rtn(
            img_uncheck=P_img().quitter(),
            tm_uncheck="bn2"
        )


class txt:
    def __init__(self, *wgs):
        wg.wg(*wgs,
              couleur_bg=P_rgb().th1() + (255,),
              couleur_fg=P_rgb().th3(),
              couleur_bg_hover=P_rgb().th3() + (255,),
              couleur_fg_hover=P_rgb().th1(),
              couleur_bg_pressed=P_rgb().th3() + (255,),

              bordure_width_top=P_style().bd(),
              bordure_width_bottom=P_style().bd(),
              bordure_width_right=P_style().bd(),
              bordure_width_left=P_style().bd(),
              bordure_couleur_top=P_rgb().th3() + (255,),
              bordure_couleur_bottom=P_rgb().th3() + (255,),
              bordure_couleur_right=P_rgb().th3() + (255,),
              bordure_couleur_left=P_rgb().th3() + (255,),
              )
class txt_inv:
    def __init__(self, *wgs):
        wg.wg(*wgs,
              couleur_bg=P_rgb().th3()+(255, ),
              couleur_fg=P_rgb().th1(),
              couleur_bg_hover=P_rgb().th1()+(255, ),
              couleur_fg_hover=P_rgb().th3(),
              couleur_bg_pressed=P_rgb().th1() + (255,),

              bordure_width_top=P_style().bd(),
              bordure_width_bottom=P_style().bd(),
              bordure_width_right=P_style().bd(),
              bordure_width_left=P_style().bd(),
              bordure_couleur_top=P_rgb().th3()+(255, ),
              bordure_couleur_bottom=P_rgb().th3()+(255, ),
              bordure_couleur_right=P_rgb().th3()+(255, ),
              bordure_couleur_left=P_rgb().th3()+(255, ),
        )

class Demo_bd:
    def __init__(self, *wgs):
        wg.wg(*wgs,
              bordure_width_top=P_style().bd(),
              bordure_width_bottom=P_style().bd(),
              bordure_width_right=P_style().bd(),
              bordure_width_left=P_style().bd(),
              bordure_couleur_top=P_rgb().bn1() + (255,),
              bordure_couleur_bottom=P_rgb().bn1() + (255,),
              bordure_couleur_right=P_rgb().bn1() + (255,),
              bordure_couleur_left=P_rgb().bn1() + (255,),
              )
class Demo_rd:
    def __init__(self, *wgs):
        wg.wg(*wgs,
              rayon_top_left=10,
              rayon_top_right=10,
              rayon_bottom_left=10,
              rayon_bottom_right=10,
        )

class ck_ico:
    def __init__(self, *wgs):
        wg.wg(*wgs,
              type_bouton="check",

              couleur_bg=(0, 0, 0, 0),
              couleur_bg_hover=(0, 0, 0, 0),
              couleur_bg_checked=(0, 0, 0, 0),
              couleur_bg_checked_hover=(0, 0, 0, 0),
              couleur_fg_checked=p_base.COULEURS.get("c3"),
              couleur_bg_pressed=(0, 0, 0, 0),
              couleur_bg_checked_pressed=(0, 0, 0, 0),
              )
class zoom:
    def __init__(self, *wgs):
        wg.wg(*wgs,
              type_bouton="zoom",

              couleur_bg=(0, 0, 0, 0),
              couleur_bg_hover=(0, 0, 0, 0),
              couleur_bg_checked=(0, 0, 0, 0),
              couleur_bg_checked_hover=(0, 0, 0, 0),
              couleur_fg_checked=p_base.COULEURS.get("c3"),
              couleur_bg_pressed=(0, 0, 0, 0),
              couleur_bg_checked_pressed=(0, 0, 0, 0),
              img_uncheck=P_img().calendrier(),
              tm_uncheck=""
              )

class dlg_ok:
    def __init__(self, *wgs):
        wg.wg(*wgs,
              couleur_bg=P_rgb().th1() + (255,),
              couleur_fg=P_rgb().vert(),
              couleur_bg_hover=P_rgb().vert() + (255,),
              couleur_fg_hover=P_rgb().th1(),
              couleur_bg_pressed=P_rgb().vert() + (255,),
              bordure_width_top=P_style().bd(),
              bordure_width_bottom=P_style().bd(),
              bordure_width_right=P_style().bd(),
              bordure_width_left=P_style().bd(),
              bordure_couleur_top=P_rgb().vert() + (255,),
              bordure_couleur_bottom=P_rgb().vert() + (255,),
              bordure_couleur_right=P_rgb().vert() + (255,),
              bordure_couleur_left=P_rgb().vert() + (255,),
              dim_width=P_dim().h6(),
              dim_height=None
              )
class dlg_ok_inv:
    def __init__(self, *wgs):
        wg.wg(*wgs,
              couleur_bg=P_rgb().vert() + (255,),
              couleur_fg=P_rgb().th1(),
              couleur_bg_hover=P_rgb().th1() + (255,),
              couleur_fg_hover=P_rgb().vert(),
              couleur_bg_pressed=P_rgb().th1() + (255,),
              bordure_width_top=P_style().bd(),
              bordure_width_bottom=P_style().bd(),
              bordure_width_right=P_style().bd(),
              bordure_width_left=P_style().bd(),
              bordure_couleur_top=P_rgb().vert() + (255,),
              bordure_couleur_bottom=P_rgb().vert() + (255,),
              bordure_couleur_right=P_rgb().vert() + (255,),
              bordure_couleur_left=P_rgb().vert() + (255,),
              dim_width=P_dim().h6(),
              dim_height=None
              )
class dlg_nok:
    def __init__(self, *wgs):
        wg.wg(*wgs,
              couleur_bg=P_rgb().th1() + (255,),
              couleur_fg=P_rgb().rouge(),
              couleur_bg_hover=P_rgb().rouge() + (255,),
              couleur_fg_hover=P_rgb().th1(),
              couleur_bg_pressed=P_rgb().rouge() + (255,),
              bordure_width_top=P_style().bd(),
              bordure_width_bottom=P_style().bd(),
              bordure_width_right=P_style().bd(),
              bordure_width_left=P_style().bd(),
              bordure_couleur_top=P_rgb().rouge() + (255,),
              bordure_couleur_bottom=P_rgb().rouge() + (255,),
              bordure_couleur_right=P_rgb().rouge() + (255,),
              bordure_couleur_left=P_rgb().rouge() + (255,),
              dim_width=P_dim().h6(),
              dim_height=None
        )
class dlg_nok_inv:
    def __init__(self, *wgs):
        wg.wg(*wgs,
              couleur_bg=P_rgb().rouge()+(255, ),
              couleur_fg=P_rgb().th1(),
              couleur_bg_hover=P_rgb().th1()+(255, ),
              couleur_fg_hover=P_rgb().rouge(),
              couleur_bg_pressed=P_rgb().th1()+(255, ),
              bordure_width_top=P_style().bd(),
              bordure_width_bottom=P_style().bd(),
              bordure_width_right=P_style().bd(),
              bordure_width_left=P_style().bd(),
              bordure_couleur_top=P_rgb().rouge()+(255, ),
              bordure_couleur_bottom=P_rgb().rouge()+(255, ),
              bordure_couleur_right=P_rgb().rouge()+(255, ),
              bordure_couleur_left=P_rgb().rouge()+(255, ),
              dim_width=P_dim().h6(),
              dim_height=None
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
        wg.wg(*self.wgs,
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
