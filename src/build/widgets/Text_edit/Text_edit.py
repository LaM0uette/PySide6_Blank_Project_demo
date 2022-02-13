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

class tr_taille:
    def __init__(self, *wgs, h):
        wg.wg(*wgs,
              couleur_bg=(0, 0, 0, 0),
              police_taille=h
              )


class Demo_th:
    def __init__(self, *wgs):
        wg.wg(*wgs,
              dim_height=P_dim().h5()
              )
class Demo_tr:
    def __init__(self, *wgs):
        wg.wg(*wgs,
              couleur_bg=(0, 0, 0, 0),
              dim_height=P_dim().h5()
              )
