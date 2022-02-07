from .wg import wg
from .. import p_base
from ....build import *


class Base_th:
    def __init__(self, *wgs):
        wg(*wgs)


class Base_tr:
    def __init__(self, *wgs):
        wg(*wgs,
           couleur_bg=(0, 0, 0, 0),
           couleur_bg_hover=(0, 0, 0, 0),
           couleur_bg_checked=(0, 0, 0, 0),
           couleur_bg_checked_hover=(0, 0, 0, 0),
           couleur_fg_checked=p_base.COLORS.get("c3"),
        )
