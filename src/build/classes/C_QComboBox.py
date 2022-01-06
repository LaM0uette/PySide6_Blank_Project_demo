from . import p_base
from .styles import *
from ...build import *


class rtn(Init_wg):
    def __init__(self, *args,
                 colors_type=p_base.COLORS_TYPE,
                 colors=p_base.COLORS,
                 dim=p_base.DIM,
                 font=p_base.FONT,
                 rd=p_base.RD,
                 bd=p_base.BD,
                 edit=p_base.EDIT,
                 cur=p_base.CUR):
        super().__init__(*args, wg_type="cb",
                         colors_type=colors_type,
                         colors=colors,
                         dim=dim,
                         font=font,
                         rd=rd,
                         bd=bd,
                         edit=edit,
                         cur=cur)


class base(rtn):
    def __init__(self, *args,
                 colors_type="th",
                 font=p_base.FONT,
                 rd=p_base.RD,
                 bd=p_base.BD,
                 edit=p_base.EDIT,
                 cur=p_base.CUR):
        super().__init__(*args,
                         colors_type=colors_type,
                         colors=P_rgb().p_th1(),
                         dim=P_dim().aw().h9(),
                         font=font,
                         rd=rd,
                         bd=bd,
                         edit=edit,
                         cur=cur)





"""
        def demo_th(self, *args):
            self.STL(list(args),
                     colors_type="th",
                     colors=P_rgb().p_th1(),
                     dim=P_dim().aw().h8(),
                     font=P_font().h3(),
                     bd=P_bd().bottom().th3(),
                     edit=True,
                     cur="souris_main")
"""