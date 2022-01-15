from .wg import wg
from .. import p_base
from ....build import *


class rtn:
    def __init__(self, *wgs,
                 colors_type=p_base.COLORS_TYPE,
                 colors=p_base.COLORS,
                 dim=p_base.DIM,
                 font=p_base.FONT,
                 hd_font=p_base.HD_FONT,
                 bd=p_base.BD,
                 rd=p_base.RD,
                 scroll=p_base.SCROLL,
                 header=p_base.HEADER,
                 cur=P_cur().croix()
                 ):
        self.wgs = wgs

        self.colors_type = colors_type
        self.colors = colors
        self.dim = dim
        self.font = font
        self.hd_font = hd_font
        self.bd = bd
        self.rd = rd
        self.scroll = scroll
        self.header = header
        self.cur = cur

    def rtn(self):
        wg(
            *self.wgs,
            colors_type=self.colors_type,
            colors=self.colors,
            dim=self.dim,
            font=self.font,
            hd_font=self.hd_font,
            bd=self.bd,
            rd=self.rd,
            scroll=self.scroll,
            header=self.header,
            cur=self.cur,
        )

    def th(self):
        self.colors_type = "th"
        self.rtn()
    def tr(self):
        self.colors_type = "tr"
        self.bd = P_bd().all().bn1()
        self.header = P_header().ff()
        self.rtn()

class base(rtn):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                         colors = P_rgb().p_th3(),
                         dim = P_dim().aw().h5(),
                         font = P_font().h5(),
                         scroll=P_scroll().nd().nd(),
        )
