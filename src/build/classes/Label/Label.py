from .wg import wg
from .. import p_base
from ....build import *


class rtn:
    def __init__(self, *wgs,
                 colors_type=p_base.COLORS_TYPE,
                 colors=p_base.COLORS,
                 dim=p_base.DIM,
                 align=p_base.ALIGN,
                 word_wrap=p_base.WORD_WRAP,
                 font=p_base.FONT,
                 bd=p_base.BD,
                 rd=p_base.RD
                 ):
        self.wgs = wgs

        self.colors_type = colors_type
        self.colors = colors
        self.dim = dim
        self.align = align
        self.word_wrap = word_wrap
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
            word_wrap=self.word_wrap,
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

    def bottom(self):
        self.bd = P_bd().bottom().th2()
        self.tr()

class base(rtn):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                         colors = P_rgb().p_th3(),
                         font = P_font().h4(),
        )
class h1(rtn):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                         colors = P_rgb().p_th3(),
                         font = P_font().h1(),
        )
