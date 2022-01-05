from .C_wg import C_wg
from ...build import *


class C_cb(C_wg):
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
        edit=Bool %,
        cur=str %,
        """
        for wg in lst: C_wg(wg=wg, attrs=kwargs).STL_CB()


    def th(self, *args):
        self.STL(list(args),
                 colors_type="th",
                 colors=P_rgb().p_th1(),
                 dim=P_dim().p_aw_h9(),
                 font=P_font().h4(),
                 bd=P_bd().bd0010_bd_th3(),
                 edit=True,
                 cur="souris_main")
    def font(self, *args):
        self.STL(list(args),
                 colors_type="tr",
                 colors=P_rgb().p_th1(),
                 dim=P_dim().p_aw_h9(),
                 font=P_font().h4(),
                 bd=P_bd().bd0010_bd_th3(),
                 edit=True,
                 cur="souris_main")

    def demo_th(self, *args):
        self.STL(list(args),
                 colors_type="th",
                 colors=P_rgb().p_th1(),
                 dim=P_dim().p_aw_demo(),
                 font=P_font().h3(),
                 bd=P_bd().bd0010_bd_th3(),
                 edit=True,
                 cur="souris_main")
    def demo_tr(self, *args):
        self.STL(list(args),
                 colors_type="tr",
                 colors=P_rgb().p_th1(),
                 dim=P_dim().p_aw_demo(),
                 font=P_font().h3(),
                 bd=P_bd().bd0010_bd_th3(),
                 edit=False,
                 cur="main")
