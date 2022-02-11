from . import wg
from ....build import *
from .. import p_base

import importlib
importlib.reload(wg)


class Base_th:
    def __init__(self, *wgs):
        wg.wg(*wgs,
              tm_up="th2",
              tm_down="th2"
              )
class Base_tr:
    def __init__(self, *wgs):
        wg.wg(*wgs,
              couleur_bg=(0, 0, 0, 0),
              couleur_bg_hover=(0, 0, 0, 0),
              no_focus=True
              )
