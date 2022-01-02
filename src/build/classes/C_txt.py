from .C_wg import C_wg
from ...build import *


class C_txt(C_wg):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.kwargs = kwargs

    def STL(self, lst, **kwargs):
        """
        colors_type=str %,
        colors=P_rgb().%,
        dim=P_dim().%,
        font=P_font().%,
        align=P_align().%,
        rd=P_rd().%,
        bd=P_bd().%,
        """
        for wg in lst:
            C_wg(wg=wg, attrs=kwargs).STL_TXT()


    def tr(self, *args):
        self.STL(list(args),
                 colors_type = "tr",
                 colors = P_rgb().p_th1(),
                 dim = P_dim().p_aw_h9(),
                 font=P_font().h3(),
                 align=P_align().l_c(),
                 bd = P_bd().bd0010_bd_th2())

    def demoth(self, *args):
        self.STL(list(args),
                 colors_type = "th",
                 colors = P_rgb().p_th3(),
                 dim = P_dim().p_aw_demo(),
                 font=P_font().h2(),
                 align=P_align().c_c(),
                 bd = P_bd().bd0010_bd_th2())
    def demotr(self, *args):
        self.STL(list(args),
                 colors_type = "tr",
                 colors = P_rgb().p_th1(),
                 dim = P_dim().p_aw_demo(),
                 font=P_font().h2(),
                 align=P_align().c_c(),
                 bd = P_bd().bd0010_bd_th2())
    def demo_th(self, *args):
        self.STL(list(args),
                 colors_type = "th",
                 colors = P_rgb().p_th3(),
                 dim = P_dim().p_list_demo(),
                 font=P_font().p(),
                 align=P_align().c_c(),
                 rd=P_rd().rd1_30(),)
    def demo_tr(self, *args):
        self.STL(list(args),
                 colors_type = "tr",
                 colors = P_rgb().p_th1(),
                 dim = P_dim().p_list_demo(),
                 font=P_font().p(),
                 align=P_align().c_c(),
                 bd = P_bd().bd1_bd_th2())
