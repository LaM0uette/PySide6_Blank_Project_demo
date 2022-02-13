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
              couleur_bg_item=(0, 0, 0, 0),
              couleur_bg_item_hover=(0, 0, 0, 0),
              couleur_bg_item_checked=(0, 0, 0, 0),
              couleur_bg_item_checked_hover=(0, 0, 0, 0),
              couleur_fg_item_checked=P_rgb().bn1(),
              couleur_fg_item_checked_hover=P_rgb().bn2(),
              )

class option:
    def __init__(self, *wgs):
        wg.wg(*wgs,
              couleur_bg=(0, 0, 0, 0),
              couleur_bg_item=(0, 0, 0, 0),
              couleur_bg_item_hover=(0, 0, 0, 0),
              couleur_bg_item_checked=(0, 0, 0, 0),
              couleur_bg_item_checked_hover=(0, 0, 0, 0),
              couleur_fg_item_checked=P_rgb().bn1(),
              couleur_fg_item_checked_hover=P_rgb().bn2(),
              )