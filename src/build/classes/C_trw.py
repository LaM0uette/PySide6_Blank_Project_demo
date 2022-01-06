from .C_wg import C_wg
from ...build import *


class C_trw(C_wg):
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
        rd=P_rd().%,
        bd=P_bd().%,
        scroll=P_scroll().%,
        cur=str %,
        """
        for wg in lst: C_wg(wg=wg, attrs=kwargs).STL_TRW()

    def option(self, *args):
        self.STL(list(args),
                 colors_type="th",
                 colors=P_rgb().p_th1(),
                 dim={"w": 150, "h": None},
                 font=P_font().h4(),
                 bd=P_bd().right().th3(),
                 scroll=P_scroll().of_n(),
                 cur="souris_main")

    def demo_th(self, *args):
        self.STL(list(args),
                 colors_type="th",
                 colors=P_rgb().p_th1(),
                 dim={"w": 300, "h": 200},
                 font=P_font().h4(),
                 bd=P_bd().right().th3(),
                 scroll=P_scroll().of_n(),
                 cur="souris_main")
    def demo_tr(self, *args):
        self.STL(list(args),
                 colors_type="tr",
                 colors=P_rgb().p_th1(),
                 dim={"w": 300, "h": 200},
                 font=P_font().h4(),
                 bd=P_bd().right().th3(),
                 scroll=P_scroll().of_n(),
                 cur="souris_main")
