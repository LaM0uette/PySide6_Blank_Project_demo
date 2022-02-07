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

"""
colors = P_rgb().p_th3()
dim = P_dim().aw().h9()
tm="th2"
tm_check="th3"
font = P_font().h4()
"""