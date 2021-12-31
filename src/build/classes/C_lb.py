from .C_wg import C_wg
from ...build import *


class C_lb(C_wg):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.kwargs = kwargs

    def STL(self, lst, **kwargs):
        """
        colors_type=str %,
        colors=P_rgb().%,
        dim=P_dim().%,
        x_ico=P_style().%,
        img=P_img().%,
        th=str %,
        font=P_font().%,
        align=P_align().%,
        rd=P_rd().%,
        bd=P_bd().%,
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
    def h3_titre(self, *args):
        self.STL(list(args),
                 colors_type = "tr",
                 colors = P_rgb().p_u3(),
                 dim = P_dim().p_aw_h9(),
                 font=P_font().h3_titre(),
                 align=P_align().c_c())

    def demo(self, *args):
        self.STL(list(args),
                 colors_type = "tr",
                 colors = P_rgb().p_th3(),
                 dim = P_dim().p_aw_h8(),
                 font=P_font().titre(),
                 align=P_align().c_b(),
                 bd = P_bd().bd0010_bd_bn1())
