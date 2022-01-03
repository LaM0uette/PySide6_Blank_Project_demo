from .C_wg import C_wg
from ...build import *


class C_de(C_wg):
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
        font=P_font().%,
        align=P_align().%,
        rd=P_rd().%,
        bd=P_bd().%,
        cur=str %,
        """
        for wg in lst: C_wg(wg=wg, attrs=kwargs).STL_DE()


    def demo_th(self, *args):
        self.STL(list(args),
                 colors_type="th",
                 colors = P_rgb().p_th3(),
                 dim = P_dim().p_aw_demo(),
                 font=P_font().p(),
                 cur="main")
    def demo_tr(self, *args):
        self.STL(list(args),
                 colors_type="tr",
                 colors = P_rgb().p_th1(),
                 dim = P_dim().p_aw_demo(),
                 font=P_font().p(),
                 cur="main")
