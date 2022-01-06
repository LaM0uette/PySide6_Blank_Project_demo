from .C_wg import C_wg
from ...build import *


class C_sb(C_wg):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.kwargs = kwargs
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        return self

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
        pb_side=""=str %,
        min=int | float %,
        max=int | float %,
        step=int | float %,
        cur=str %,
        """
        for wg in lst: C_wg(wg=wg, attrs=kwargs).STL_SB()

    def th1(self, *args):
        self.STL(list(args),
                 colors_type="th",
                 colors=P_rgb().p_th1(),
                 dim=P_dim().w_rect_2().h8(),
                 font=P_font().h3(),
                 align=P_align().c().c(),
                 edit=True,
                 pb_sb=P_pb_sb().no(),
                 min=0,
                 max=100,
                 step=1,
                 bd=P_bd().bottom().th3(),
                 cur="souris_main")
    def th1_full(self, *args):
        self.STL(list(args),
                 colors_type="th",
                 colors=P_rgb().p_th1(),
                 dim=P_dim().w_rect_2().h8(),
                 font=P_font().h3(),
                 align=P_align().c().c(),
                 edit=True,
                 pb_sb=P_pb_sb().no(),
                 min=0,
                 max=99999,
                 step=1,
                 bd=P_bd().bottom().th3(),
                 cur="souris_main")
    def th1_(self, *args):
        self.STL(list(args),
                 colors_type="th",
                 colors=P_rgb().p_th2(),
                 dim=P_dim().w_rect_2().h8(),
                 font=P_font().h3(),
                 align=P_align().c().c(),
                 edit=True,
                 pb_sb=P_pb_sb().no(),
                 min=0,
                 max=255,
                 step=1,
                 bd=P_bd().all().th3(),
                 rd=P_rd().left().px_5(),
                 cur="souris_main")

    def demo_th(self, *args):
        self.STL(list(args),
                 colors_type="th",
                 colors=P_rgb().p_th1(),
                 dim=P_dim().w_rect_4().h8(),
                 font=P_font().h2(),
                 align=P_align().c().c(),
                 edit=True,
                 pb_sb=P_pb_sb().pl_mi(),
                 pb_side="lr",
                 min=0,
                 max=50,
                 step=2,
                 cur="main")
    def demo_th_2(self, *args):
        self.STL(list(args),
                 colors_type="th",
                 colors=P_rgb().p_th1(),
                 dim=P_dim().w_rect_4().h8(),
                 font=P_font().h2(),
                 align=P_align().c().c(),
                 edit=True,
                 pb_sb=P_pb_sb().pl_mi(),
                 pb_side="tb",
                 min=0,
                 max=50,
                 step=2,
                 cur="main")
    def demo_th_3(self, *args):
        self.STL(list(args),
                 colors_type="th",
                 colors=P_rgb().p_th1(),
                 dim=P_dim().w_rect_4().h8(),
                 font=P_font().h2(),
                 align=P_align().c().c(),
                 edit=True,
                 pb_sb=P_pb_sb().up_do(),
                 pb_side="tb",
                 min=0,
                 max=50,
                 step=2,
                 cur="main")
    def demo_tr(self, *args):
        self.STL(list(args),
                 colors_type="tr",
                 colors=P_rgb().p_th1(),
                 dim=P_dim().aw().h8(),
                 font=P_font().h2(),
                 align=P_align().c().c(),
                 edit=False,
                 min=0,
                 max=20,
                 step=0.2,
                 cur="souris_main")
