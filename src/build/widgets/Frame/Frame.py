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
              couleur_bg=(0, 0, 0, 0)
              )
class Menu_top:
    def __init__(self, *wgs):
        wg.wg(*wgs,
              couleur_bg=P_rgb().th1()+(255, ),
              dim_height=P_dim().h9(),
              )
class Menu_bottom:
    def __init__(self, *wgs):
        wg.wg(*wgs,
              couleur_bg=P_rgb().th2()+(255, ),
              dim_height=P_dim().h10()
              )
class Menu_bottom_dlg:
    def __init__(self, *wgs):
        wg.wg(*wgs,
              couleur_bg=P_rgb().th2()+(255, ),
              dim_height=P_dim().h9()
              )


class Cadre_th2:
    def __init__(self, *wgs):
        wg.wg(*wgs,
              couleur_bg=(0, 0, 0, 0),
              bordure_width_top=P_style().bd(),
              bordure_width_bottom=P_style().bd(),
              bordure_width_right=P_style().bd(),
              bordure_width_left=P_style().bd(),
              bordure_couleur_top=P_rgb().th2()+(255, ),
              bordure_couleur_bottom=P_rgb().th2()+(255, ),
              bordure_couleur_right=P_rgb().th2()+(255, ),
              bordure_couleur_left=P_rgb().th2()+(255, ),
              )
class Cadre_th3:
    def __init__(self, *wgs):
        wg.wg(*wgs,
              couleur_bg=(0, 0, 0, 0),
              bordure_width_top=P_style().bd(),
              bordure_width_bottom=P_style().bd(),
              bordure_width_right=P_style().bd(),
              bordure_width_left=P_style().bd(),
              bordure_couleur_top=P_rgb().th3()+(255, ),
              bordure_couleur_bottom=P_rgb().th3()+(255, ),
              bordure_couleur_right=P_rgb().th3()+(255, ),
              bordure_couleur_left=P_rgb().th3()+(255, ),
              )
class Cadre_bn1:
    def __init__(self, *wgs):
        wg.wg(*wgs,
              couleur_bg=(0, 0, 0, 0),
              bordure_width_top=P_style().bd(),
              bordure_width_bottom=P_style().bd(),
              bordure_width_right=P_style().bd(),
              bordure_width_left=P_style().bd(),
              bordure_couleur_top=P_rgb().bn1()+(255, ),
              bordure_couleur_bottom=P_rgb().bn1()+(255, ),
              bordure_couleur_right=P_rgb().bn1()+(255, ),
              bordure_couleur_left=P_rgb().bn1()+(255, ),
              )
