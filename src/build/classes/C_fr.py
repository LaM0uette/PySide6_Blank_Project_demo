from .C_wg import C_wg
from ...build import *


class C_fr(C_wg):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.kwargs = kwargs

    def STL(self, lst, **kwargs):
        """
        colors=P_rgb().%,
        dim=P_dim().%,
        rd=P_rd().%,
        bd=P_bd().%,
        """
        for wg in lst: C_wg(wg=wg, attrs=kwargs).STL_FR()


    def dialog(self, *args):
        self.STL(list(args),
                 colors = P_rgb().p_u1(),
                 dim = P_dim().p_all(),
                 bd=P_bd().bd1_bd_th3(),)
    def menu_top(self, *args):
        self.STL(list(args),
                 colors = P_rgb().p_u1(),
                 dim = P_dim().p_aw_mt())
    def menu_bottom(self, *args):
        self.STL(list(args),
                 colors = P_rgb().p_u2(),
                 dim = P_dim().p_aw_mb())

    def demo(self, *args):
        self.STL(list(args),
                 colors=P_rgb().p_u1(),
                 dim=P_dim().p_all(),
                 bd=P_bd().bd1_bd_bn1(),)
    def demo_tb(self, *args):
        self.STL(list(args),
                 colors=P_rgb().p_th1(),
                 dim=P_dim().p_all(),
                 bd=P_bd().bd0010_bd_bn1(),)
