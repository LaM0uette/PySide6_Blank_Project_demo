from . import wg
from ....build import *
from .. import p_base

import importlib
importlib.reload(wg)


class Base_th:
    def __init__(self, *wgs):
        wg.wg(*wgs)
class Base_rond:
    def __init__(self, *wgs):
        wg.wg(*wgs)
class rgb:
    def __init__(self, *wgs):
        wg.wg(*wgs,
              valeur_max=255
              )