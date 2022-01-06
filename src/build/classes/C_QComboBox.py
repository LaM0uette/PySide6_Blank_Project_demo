from . import base
from .styles import *


class rtn(Init_wg):
    def __init__(self, *args,
                 colors_type=base.COLORS_TYPE,
                 colors=base.COLORS,
                 dim=base.DIM,
                 font=base.FONT,
                 rd=base.RD,
                 bd=base.BD,
                 edit=base.EDIT,
                 cur=base.CUR):
        super().__init__(*args, wg_type="cb",
                         colors_type=colors_type,
                         colors=colors,
                         dim=dim,
                         font=font,
                         rd=rd,
                         bd=bd,
                         edit=edit,
                         cur=cur)


class test(rtn):
    def __init__(self, *args):
        super().__init__(*args, colors_type="th")





"""
colors_type="th",
colors=P_rgb().p_th1(),
dim=P_dim().aw().h9(),
font=P_font().h4(),
rd=P_rd().%
bd=P_bd().bottom().th3(),
edit=True,
cur="souris_main")
"""