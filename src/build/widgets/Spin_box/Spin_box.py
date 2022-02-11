from . import wg
from ....build import *
from .. import p_base

import importlib
importlib.reload(wg)


class Plus_moins_th:
    def __init__(self, *wgs):
        wg.wg(*wgs)
class Plus_moins_tr:
    def __init__(self, *wgs):
        wg.wg(*wgs,
              couleur_bg=(0, 0, 0, 0),
              couleur_bg_hover=(0, 0, 0, 0),
              no_focus=True
              )

class Up_down_th:
    def __init__(self, *wgs):
        wg.wg(*wgs,
              img_up=P_img().fleche_top(),
              img_down=P_img().fleche_bottom(),
              )
class Up_down_tr:
    def __init__(self, *wgs):
        wg.wg(*wgs,
              couleur_bg=(0, 0, 0, 0),
              couleur_bg_hover=(0, 0, 0, 0),
              img_up=P_img().fleche_top(),
              img_down=P_img().fleche_bottom(),
              no_focus=True
              )


class rgb_bd_th3:
    def __init__(self, *wgs):
        wg.wg(*wgs,
              bordure_width_top=P_style().bd(),
              bordure_width_bottom=P_style().bd(),
              bordure_width_right=P_style().bd(),
              bordure_width_left=P_style().bd(),
              bordure_couleur_top=P_rgb().th3(),
              bordure_couleur_bottom=P_rgb().th3(),
              bordure_couleur_right=P_rgb().th3(),
              bordure_couleur_left=P_rgb().th3(),
              valeur_max=255
              )
class Plus_moins_bd_th3:
    def __init__(self, *wgs):
        wg.wg(*wgs,
              bordure_width_top=P_style().bd(),
              bordure_width_bottom=P_style().bd(),
              bordure_width_right=P_style().bd(),
              bordure_width_left=P_style().bd(),
              bordure_couleur_top=P_rgb().th3(),
              bordure_couleur_bottom=P_rgb().th3(),
              bordure_couleur_right=P_rgb().th3(),
              bordure_couleur_left=P_rgb().th3(),
              )
class Plus_moins_inf_bd_th3:
    def __init__(self, *wgs):
        wg.wg(*wgs,
              bordure_width_top=P_style().bd(),
              bordure_width_bottom=P_style().bd(),
              bordure_width_right=P_style().bd(),
              bordure_width_left=P_style().bd(),
              bordure_couleur_top=P_rgb().th3(),
              bordure_couleur_bottom=P_rgb().th3(),
              bordure_couleur_right=P_rgb().th3(),
              bordure_couleur_left=P_rgb().th3(),
              valeur_max=999999
              )
