from . import wg
from ....build import *
from .. import p_base

import importlib
importlib.reload(wg)


class Base_th:
    def __init__(self, *wgs):
        wg.wg(*wgs,
           curseur=P_cur().main(),
           bordure_couleur_bottom=P_rgb().th2()+(255, ),
           bordure_width_bottom=P_style().bd()
        )
class Base_tr:
    def __init__(self, *wgs):
        wg.wg(*wgs,
           couleur_bg=(0, 0, 0, 0),
           couleur_bg_hover=(0, 0, 0, 0),
           edit=True
        )
