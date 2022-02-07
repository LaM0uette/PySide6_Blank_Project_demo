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
              couleur_bg=(0, 0, 0, 0)
              )
class Menu_bottom:
    def __init__(self, *wgs):
        wg.wg(*wgs,
              couleur_bg=P_rgb().th2()+(255, ),
              wg_dim_height=P_dim().h9()
              )


class Cadre_bn1:
    def __init__(self, *wgs):
        wg.wg(*wgs,
              couleur_bg=(0, 0, 0, 0),
              bordure_width_top=P_style().bd(),
              bordure_width_bottom=P_style().bd(),
              bordure_width_right=P_style().bd(),
              bordure_width_left=P_style().bd(),
              bordure_couleur_top=P_rgb().bn1(),
              bordure_couleur_bottom=P_rgb().bn1(),
              bordure_couleur_right=P_rgb().bn1(),
              bordure_couleur_left=P_rgb().bn1(),
              )



"""

from .wg import wg
from .. import p_base
from ....build import *


class rtn:
    def __init__(self, *wgs,
                 colors_type=p_base.COLORS_TYPE,
                 colors=p_base.COULEURS,
                 dim=p_base.DIM,
                 bd=p_base.BD,
                 rd=p_base.RD,
                 ):
        self.wgs = wgs

        self.colors_type = colors_type
        self.colors = colors
        self.dim = dim
        self.bd = bd
        self.rd = rd

    def rtn(self):
        wg(
            *self.wgs,
            colors_type=self.colors_type,
            colors=self.colors,
            dim=self.dim,
            bd=self.bd,
            rd=self.rd,
        )

    def th(self):
        self.colors_type = "th"
        self.rtn()
    def tr(self):
        self.colors_type = "tr"
        self.rtn()

    def th1(self):
        self.colors = P_rgb().p_th1()
        self.th()

    def cadre_th2(self):
        self.bd = P_bd().all().th2()
        self.tr()
    def cadre_th3(self):
        self.bd = P_bd().all().th3()
        self.tr()
    def cadre_bn1(self):
        self.bd = P_bd().all().bn1()
        self.tr()

    def radius(self):
        self.rd = P_rd().all().px_15()
        self.th()


class base(rtn):
    def __init__(self, *wgs, colors=P_rgb().p_th3(), dim=p_base.DIM):
        super().__init__(*wgs,
                         colors=colors,
                         dim=dim
        )
class menu_top(rtn):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                         colors=P_rgb().p_th1(),
                         dim=P_dim().aw().h9(),
        )
class menu_bottom(rtn):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                         colors=P_rgb().p_th2(),
                         dim=P_dim().aw().h10(),
        )
class menu_bottom_dlg(rtn):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                         colors=P_rgb().p_th2(),
                         dim=P_dim().aw().h9()
        )


"""