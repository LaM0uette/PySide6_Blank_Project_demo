from .wg import wg
from .. import p_base
from ....build import *


class rtn:
    def __init__(self, *wgs,
                 colors_type=p_base.COLORS_TYPE,
                 colors=p_base.COLORS,
                 dim=p_base.DIM,
                 tm=p_base.TM,
                 font=p_base.FONT_SIZE,
                 bd=p_base.BD,
                 rd=p_base.RD,
                 align=p_base.ALIGN,
                 pb_sb=p_base.PB_SB,
                 pb_side=p_base.PB_SIDE,
                 no_focus=p_base.NO_FOCUS,
                 val_min=p_base.VAL_MIN,
                 val_max=p_base.VAL_MAX,
                 step=p_base.STEP,
                 cur=p_base.CUR,
                 ):
        self.wgs = wgs

        self.colors_type = colors_type
        self.colors = colors
        self.dim = dim
        self.tm = tm
        self.font = font
        self.bd = bd
        self.rd = rd
        self.align = align
        self.pb_sb = pb_sb
        self.pb_side = pb_side
        self.no_focus = no_focus
        self.val_min = val_min
        self.val_max = val_max
        self.step = step
        self.cur = cur

    def rtn(self):
        wg(
            *self.wgs,
            colors_type=self.colors_type,
            colors=self.colors,
            dim=self.dim,
            tm=self.tm,
            font=self.font,
            bd=self.bd,
            rd=self.rd,
            align=self.align,
            pb_sb=self.pb_sb,
            pb_side=self.pb_side,
            no_focus=self.no_focus,
            val_min=self.val_min,
            val_max=self.val_max,
            step=self.step,
            cur=self.cur
        )

    def th(self):
        self.colors_type = "th"
        self.rtn()
    def tr(self):
        self.colors_type = "tr"
        self.rtn()

    def th_lr(self):
        self.pb_side = "lr"
        self.th()
    def bd_th3(self):
        self.bd = P_bd().all().th3()
        self.rd = P_rd().all().px_5()
        self.tr()



class base(rtn):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                         colors=P_rgb().p_th3(),
                         dim=P_dim().w_rect_2().h9(),
                         font=P_font().h3(),
                         no_focus=True
        )
class plus_minus(rtn):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                         colors=P_rgb().p_th3(),
                         dim=P_dim().w_rect_2().h9(),
                         tm="th2",
                         font=P_font().h3(),
                         pb_sb=P_pb_sb().pl_mi(),
                         no_focus=True
        )
class plus_minus_infini(rtn):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                         colors=P_rgb().p_th3(),
                         dim=P_dim().w_rect_4().h9(),
                         tm="th2",
                         font=P_font().h3(),
                         pb_sb=P_pb_sb().pl_mi(),
                         val_max=5000
        )
class up_down(rtn):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                         colors=P_rgb().p_th3(),
                         dim=P_dim().w_rect_2().h9(),
                         tm="th2",
                         font=P_font().h3(),
                         pb_sb=P_pb_sb().up_do(),
                         no_focus=True
        )
class rgb(rtn):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                         colors=P_rgb().p_th3(),
                         dim=P_dim().w_rect_3().h9(),
                         tm="th2",
                         font=P_font().h3(),
                         pb_sb=P_pb_sb().pl_mi(),
                         pb_side="lr",
                         val_max=255
        )
