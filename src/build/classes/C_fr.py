from .C_wg import C_wg
from ...build import *


class C_fr(C_wg):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.kwargs = kwargs

    def STL(self, lst, **kwargs):
        """
        colors=P_rgb().p_th1(),
        dim=P_dim().p_r_mt(),
        rd=P_rd().rd1_5(),
        bd=P_bd().bd1_bd_bn1(),
        """
        for wg in lst: C_wg(wg=wg, attrs=kwargs).STL_FR()


    def menu_top(self, *args):
        self.STL(list(args),
                 colors = P_rgb().p_u1(),
                 dim = P_dim().p_aw_mt())

    def demo(self, *args):
        self.STL(list(args),
                 colors=P_rgb().p_u1(),
                 dim=P_dim().p_all(),
                 bd=P_bd().bd1_bd_bn1(),)
