from .C_wg import C_wg
from ...build import *


class C_lw(C_wg):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.kwargs = kwargs

    def STL(self, lst, **kwargs):
        """
        colors=P_rgb().%,
        dim=P_dim().%,
        font=P_font().%,
        rd=P_rd().%,
        bd=P_bd().%,
        scroll=P_scroll().%,
        cur=str %,
        """
        for wg in lst: C_wg(wg=wg, attrs=kwargs).STL_LW()


    def demo(self, *args):
        self.STL(list(args),
                 colors=P_rgb().p_th1(),
                 dim=P_dim().p_list_demo(),
                 font=P_font().p(),
                 cur="souris_main",
                 scroll=P_scroll().of_n(),)
