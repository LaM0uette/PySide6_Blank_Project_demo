from .C_wg import C_wg
from ...build import *


class C_lb(C_wg):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.kwargs = kwargs

    def STL(self, lst, **kwargs):
        """
        colors_type = "tr",
        colors = P_rgb().p_th1(),
        dim = P_dim().p_r_mt(),
        x_ico = P_style().x_ico(),
        img = P_img().option(),
        th = "bn1",
        font = P_font().p(),
        align = P_align().c_c(),
        rd = P_rd().rd1_5(),
        bd = P_bd().bd1_bd_bn1(),
        """
        for wg in lst:
            C_wg(wg=wg, attrs=kwargs).STL_LB()

    def titre(self, *args):
        self.STL(list(args),
                 colors_type = "tr",
                 colors = P_rgb().p_u3(),
                 dim = P_dim().p_aw_h8(),
                 font=P_font().titre(),
                 align=P_align().c_c())
    def sous_titre(self, *args):
        self.STL(list(args),
                 colors_type = "tr",
                 colors = P_rgb().p_u3(),
                 dim = P_dim().p_aw_h9(),
                 font=P_font().sous_titre(),
                 align=P_align().c_c())
