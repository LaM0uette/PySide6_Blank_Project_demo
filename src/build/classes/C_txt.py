from .C_wg import C_wg
from ...build import *


class C_txt(C_wg):
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
        """
        for wg in lst:
            C_wg(wg=wg, attrs=kwargs).STL_TXT()


    def tr_h1(self, *args):
        self.STL(list(args),
                 colors_type = "tr",
                 colors = P_rgb().p_th1(),
                 dim = P_dim().p_all(),
                 font=P_font().h1(),
                 align=P_align().c().c())
    def tr_h2(self, *args):
        self.STL(list(args),
                 colors_type = "tr",
                 colors = P_rgb().p_th1(),
                 dim = P_dim().p_all(),
                 font=P_font().h2(),
                 align=P_align().c().c())
    def tr_h3(self, *args):
        self.STL(list(args),
                 colors_type = "tr",
                 colors = P_rgb().p_th1(),
                 dim = P_dim().p_all(),
                 font=P_font().h3(),
                 align=P_align().c().c())
    def tr_h4(self, *args):
        self.STL(list(args),
                 colors_type = "tr",
                 colors = P_rgb().p_th1(),
                 dim = P_dim().p_all(),
                 font=P_font().h4(),
                 align=P_align().c().c())
    def tr_h5(self, *args):
        self.STL(list(args),
                 colors_type = "tr",
                 colors = P_rgb().p_th1(),
                 dim = P_dim().p_all(),
                 font=P_font().h5(),
                 align=P_align().c().c())

    def tr(self, *args):
        self.STL(list(args),
                 colors_type = "tr",
                 colors = P_rgb().p_th1(),
                 dim = P_dim().aw().h9(),
                 font=P_font().h3(),
                 align=P_align().l().c(),
                 bd = P_bd().bottom().th2())

    def demoth(self, *args):
        self.STL(list(args),
                 colors_type = "th",
                 colors = P_rgb().p_th3(),
                 dim = P_dim().p_aw_demo(),
                 font=P_font().h2(),
                 align=P_align().c().c(),
                 bd = P_bd().bottom().th2())
    def demotr(self, *args):
        self.STL(list(args),
                 colors_type = "tr",
                 colors = P_rgb().p_th1(),
                 dim = P_dim().p_aw_demo(),
                 font=P_font().h2(),
                 align=P_align().c().c(),
                 bd = P_bd().bottom().th2())
    def demo_th(self, *args):
        self.STL(list(args),
                 colors_type = "th",
                 colors = P_rgb().p_th3(),
                 dim = P_dim().p_list_demo(),
                 font=P_font().p(),
                 align=P_align().c().c(),
                 rd=P_rd().rd1_30(),)
    def demo_tr(self, *args):
        self.STL(list(args),
                 colors_type = "tr",
                 colors = P_rgb().p_th1(),
                 dim = P_dim().p_list_demo(),
                 font=P_font().p(),
                 align=P_align().c().c(),
                 bd = P_bd().all().th2())
