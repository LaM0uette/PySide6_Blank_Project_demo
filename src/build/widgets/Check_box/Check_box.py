from .wg import wg
from .. import p_base
from ....build import *


class rtn:
    def __init__(self, *wgs,
                 colors_type=p_base.COLORS_TYPE,
                 colors=p_base.COLORS,
                 dim=p_base.DIM,
                 img=P_img().check(),
                 img_check=P_img().valider(),
                 tm=p_base.TM,
                 tm_check=p_base.TM_CHECK,
                 font=p_base.FONT,
                 bd=p_base.BD,
                 rd=p_base.RD,
                 cur=p_base.CUR
                 ):
        self.wgs = wgs

        self.colors_type = colors_type
        self.colors = colors
        self.dim = dim
        self.img = img
        self.img_check = img_check
        self.tm = tm
        self.tm_check = tm_check
        self.font = font
        self.bd = bd
        self.rd = rd
        self.cur = cur

    def rtn(self):
        wg(
            *self.wgs,
            colors_type=self.colors_type,
            colors=self.colors,
            dim=self.dim,
            img=self.img,
            img_check=self.img_check,
            tm=self.tm,
            tm_check=self.tm_check,
            font=self.font,
            bd=self.bd,
            rd=self.rd,
            cur=self.cur
        )

    def th(self):
        self.colors_type = "th"
        self.cur = P_cur().main()
        self.bd = P_bd().all().bn1()
        self.rd = P_rd().all().px_5()
        self.rtn()
    def tr(self):
        self.colors_type = "tr"
        self.cur = P_cur().souris_main()
        self.rtn()

class base(rtn):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                         colors = P_rgb().p_th3(),
                         dim = P_dim().aw().h9(),
                         tm="th2",
                         tm_check="th3",
                         font = P_font().h4()
        )