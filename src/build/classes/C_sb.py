from .C_wg import C_wg
from ...build import *


class C_sb(C_wg):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.kwargs = kwargs

    def STL(self, lst, **kwargs):
        """
        colors_type=str %,
        colors=P_rgb().%,
        dim=P_dim().%,
        font=P_font(). %,
        rd=P_rd().%,
        bd=P_bd().%,
        align=P_align().%,
        edit=Bool %,
        pb_sb=P_pb_sb(). %,
        cur=str %,
        """
        for wg in lst: C_wg(wg=wg, attrs=kwargs).STL_SB()


    def demo_th(self, *args):
        self.STL(list(args),
                 colors_type="th",
                 colors=P_rgb().p_th1(),
                 dim=P_dim().p_h6_h8_demo(),
                 font=P_font().sous_titre(),
                 align=P_align().c_c(),
                 edit=True,
                 pb_sb=P_pb_sb().pl_mi(),
                 cur="main")
    def demo_tr(self, *args):
        self.STL(list(args),
                 colors_type="tr",
                 colors=P_rgb().p_th1(),
                 dim=P_dim().p_aw_demo(),
                 font=P_font().sous_titre(),
                 align=P_align().c_c(),
                 edit=False,
                 pb_sb=P_pb_sb().no(),
                 cur="souris_main")
