from .C_wg import C_wg
from ...build import *


class C_de(C_wg):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.kwargs = kwargs

    def STL(self, lst, **kwargs):
        """
        colors_type = "tr",
        colors = P_rgb().p_th1(),
        dim = P_dim().p_r_mt(),
        font = P_font().p(),
        align = P_align().c_c(),
        rd = P_rd().rd1_5(),
        bd = P_bd().bd1_bd_bn1(),
        """
        for wg in lst: C_wg(wg=wg, attrs=kwargs).STL_DE()


    def demo(self, *args):
        self.STL(list(args),
                 colors = P_rgb().p_th1(),
                 dim = P_dim().p_aw_demo(),
                 font=P_font().p(),)
