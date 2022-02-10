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
              )


class Demo:
    def __init__(self, *wgs):
        wg.wg(*wgs,
              couleur_bg=P_rgb().th1()+(255, ),
              )
