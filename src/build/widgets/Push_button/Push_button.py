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