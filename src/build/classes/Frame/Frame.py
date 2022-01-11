from .wg import wg
from .. import p_base
from ....build import *


class rtn:
    def __init__(self, *wgs,
                 colors_type=p_base.COLORS_TYPE,
                 colors=p_base.COLORS,
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
    def cadre(self):
        self.colors_type = "tr"
        self.bd = P_bd().all().bn1()
        self.rtn()

    def menu_top(self):
        self.colors_type = "th"
        self.colors = P_rgb().p_th1()
        self.dim = P_dim().aw().h9()
        self.rtn()
    def menu_bot(self):
        self.colors_type = "th"
        self.colors = P_rgb().p_th2()
        self.dim = P_dim().aw().h10()
        self.rtn()

class base(rtn):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                         colors = P_rgb().p_th3(),
                         dim = P_dim().all(),
        )
