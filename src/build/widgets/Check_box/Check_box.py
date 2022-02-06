from .wg import wg
from ....build import *


class Base_th:
    def __init__(self, *wgs):
        wg(*wgs,
           couleur_bg_hover=P_rgb().bn1()
        )


class Base_tr:
    def __init__(self, *wgs):
        wg(*wgs,
           couleur_bg_hover=P_rgb().bn2()
        )

"""
colors = P_rgb().p_th3()
dim = P_dim().aw().h9()
tm="th2"
tm_check="th3"
font = P_font().h4()
"""