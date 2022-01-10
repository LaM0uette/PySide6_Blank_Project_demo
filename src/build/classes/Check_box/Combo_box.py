from .wg import wg
from .. import p_base
from ....build import *


class rtn:
    def __init__(self, *wgs,
                 colors_type=p_base.COLORS_TYPE,
                 colors=p_base.COLORS,
                 dim=p_base.DIM,
                 font=p_base.FONT,
                 bd=p_base.BD,
                 rd=p_base.RD,
                 edit=p_base.EDIT,
                 cur=p_base.CUR
    ):
        self.wgs = wgs

        self.colors_type = colors_type
        self.colors = colors
        self.dim = dim
        self.font = font
        self.bd = bd
        self.rd = rd
        self.edit = edit
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
            edit=self.edit,
            cur=self.cur
        )

    def th(self):
        self.colors_type = "th"
        self.edit = False
        self.cur = P_cur().main()
        self.rtn()
    def tr(self):
        self.colors_type = "tr"
        self.edit = True
        self.cur = P_cur().souris_main()
        self.rtn()

class base(rtn):
    def __init__(self, *args):
        super().__init__(*args,
                         colors = P_rgb().p_th1(),
                         dim = P_dim().aw().h9(),
                         font = P_font().h4(),
                         bd = P_bd().bottom().th3()
        )
