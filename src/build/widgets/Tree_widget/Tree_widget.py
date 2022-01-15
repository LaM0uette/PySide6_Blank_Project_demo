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
                 scroll=p_base.SCROLL,
                 cur=p_base.CUR,
                 ):
        self.wgs = wgs

        self.colors_type = colors_type
        self.colors = colors
        self.dim = dim
        self.font = font
        self.bd = bd
        self.rd = rd
        self.scroll = scroll
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
            scroll=self.scroll,
            cur=self.cur,
        )

    def th(self):
        self.colors_type = "th"
        self.rtn()
    def tr(self):
        self.colors_type = "tr"
        self.rtn()

    def option(self):
        self.dim = P_dim().ah().h5()
        self.bd = P_bd().right().th3()
        self.scroll=P_scroll().off().off()
        self.tr()


class base(rtn):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                         colors=P_rgb().p_th3(),
                         font=P_font().h4(),
                         scroll=P_scroll().off().nd(),
                         cur=P_cur().souris_main()
        )
