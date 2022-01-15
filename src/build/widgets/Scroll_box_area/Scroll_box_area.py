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
                 scroll=p_base.SCROLL,
                 ):
        self.wgs = wgs

        self.colors_type = colors_type
        self.colors = colors
        self.dim = dim
        self.bd = bd
        self.rd = rd
        self.scroll = scroll

    def rtn(self):
        wg(
            *self.wgs,
            colors_type=self.colors_type,
            colors=self.colors,
            dim=self.dim,
            bd=self.bd,
            rd=self.rd,
            scroll=self.scroll,
        )

    def th(self):
        self.colors_type = "th"
        self.rtn()
    def tr(self):
        self.colors_type = "tr"
        self.rtn()

    def invisible(self):
        self.scroll = P_scroll().off().off()
        self.tr()


class base(rtn):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                         colors=P_rgb().p_th1(),
                         scroll=P_scroll().off().nd()
        )
