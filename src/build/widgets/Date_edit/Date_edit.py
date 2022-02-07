from .wg import wg
from .. import p_base
from ....build import *


class rtn:
    def __init__(self, *wgs,
                 colors_type=p_base.COLORS_TYPE,
                 colors=p_base.COLORS,
                 dim=p_base.DIM,
                 font=p_base.FONT_SIZE,
                 bd=p_base.BD,
                 rd=p_base.RD,
                 align=p_base.ALIGN,
                 cur=p_base.CUR
                 ):
        self.wgs = wgs

        self.colors_type = colors_type
        self.colors = colors
        self.dim = dim
        self.font = font
        self.bd = bd
        self.rd = rd
        self.align = align
        self.cur = cur

    def rtn(self):
        wg(
            *self.wgs,
            colors_type=self.colors_type,
            colors=self.colors,
            dim=self.dim,
            font=self.font,
            bd=self.bd,
            rd=self.rd,
            align=self.align,
            cur=self.cur
        )

    def th(self):
        self.colors_type = "th"
        self.rtn()
    def tr(self):
        self.colors_type = "tr"
        self.rtn()

class base(rtn):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                         colors = P_rgb().p_th3(),
                         dim = P_dim().aw().h9(),
                         font = P_font().h4(),
                         bd = P_bd().bottom().th3()
        )
