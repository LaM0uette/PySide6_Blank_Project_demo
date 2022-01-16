from .wg import wg
from .. import p_base
from ....build import *


class rtn:
    def __init__(self, *wgs,
                 colors_type=p_base.COLORS_TYPE,
                 colors=p_base.COLORS,
                 dim=p_base.DIM,
                 align=p_base.ALIGN,
                 font=p_base.FONT,
                 bd=p_base.BD,
                 rd=p_base.RD
                 ):
        self.wgs = wgs

        self.colors_type = colors_type
        self.colors = colors
        self.dim = dim
        self.align = align
        self.font = font
        self.bd = bd
        self.rd = rd

    def rtn(self):
        wg(
            *self.wgs,
            colors_type=self.colors_type,
            colors=self.colors,
            dim=self.dim,
            align=self.align,
            font=self.font,
            bd=self.bd,
            rd=self.rd,
        )

    def th(self):
        self.colors_type = "th"
        self.rtn()
    def tr(self):
        self.colors_type = "tr"
        self.rtn()

    def bottom_tr2(self):
        self.bd = P_bd().bottom().th2()
        self.tr()
    def bottom_th2(self):
        self.bd = P_bd().bottom().th2()
        self.th()

class base(rtn):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                         colors = P_rgb().p_th3(),
                         dim=P_dim().aw().h9(),
                         font = P_font().h4(),
                         align = P_align().l().c()
        )
class base_bloc(rtn):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                         colors = P_rgb().p_th3(),
                         dim=P_dim().aw().h5(),
                         font = P_font().h4(),
                         align = P_align().l().c(),
                         bd=P_bd().all().bn1(),
                         rd=P_rd().all().px_5()
        )
class h1(rtn):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                         colors = P_rgb().p_th3(),
                         font = P_font().h1(),
        )
class h2(rtn):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                         colors = P_rgb().p_th3(),
                         font = P_font().h2(),
        )
class h3(rtn):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                         colors = P_rgb().p_th3(),
                         font = P_font().h3(),
        )
class h4(rtn):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                         colors = P_rgb().p_th3(),
                         font = P_font().h4(),
        )
class h5(rtn):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                         colors = P_rgb().p_th3(),
                         font = P_font().h5(),
        )