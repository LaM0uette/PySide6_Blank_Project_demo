from .wg import wg
from .. import p_base
from ....build import *


class rtn:
    def __init__(self, *wgs,
                 colors_type=p_base.COLORS_TYPE,
                 colors=p_base.COLORS,
                 gradient_colors=p_base.GRADIENT_COLORS,
                 dim=p_base.DIM,
                 bd=p_base.BD,
                 rd=p_base.RD,
                 val_min=p_base.VAL_MIN,
                 val_max=p_base.VAL_MAX,
                 step=p_base.STEP,
                 cur=p_base.CUR,
                 ):
        self.wgs = wgs

        self.colors_type = colors_type
        self.colors = colors
        self.gradient_colors = gradient_colors
        self.dim = dim
        self.bd = bd
        self.rd = rd
        self.val_min = val_min
        self.val_max = val_max
        self.step = step
        self.cur = cur

    def rtn(self):
        wg(
            *self.wgs,
            colors_type=self.colors_type,
            colors=self.colors,
            gradient_colors=self.gradient_colors,
            dim=self.dim,
            bd=self.bd,
            rd=self.rd,
            val_min=self.val_min,
            val_max=self.val_max,
            step=self.step,
            cur=self.cur,
        )

    def th(self):
        self.colors_type = "th"
        self.rtn()
    def rond(self):
        self.colors_type = "rond"
        self.rtn()
    def rgb(self):
        self.colors_type = "rgb"
        self.rtn()


class base(rtn):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                         colors=P_rgb().p_th3(),
                         dim=P_dim().carr().h5(),
        )
class rgb(rtn):
    def __init__(self, *wgs, gradient_colors=p_base.GRADIENT_COLORS):
        super().__init__(*wgs,
                         colors=P_rgb().p_th2(),
                         gradient_colors=gradient_colors,
                         dim=P_dim().aw().h8(),
                         val_max=255
        )
