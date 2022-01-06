from .C_wg import C_wg
from ...build import *


class C_lb(C_wg):
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
        x_ico=P_style().%,
        img=P_img().%,
        th=str %,
        font=P_font().%,
        align=P_align().%,
        rd=P_rd().%,
        bd=P_bd().%,
        word_wrap=Bool %,
        """
        for wg in lst:
            C_wg(wg=wg, attrs=kwargs).STL_LB()

    def h1(self, *args):
        self.STL(list(args),
                 colors_type = "tr",
                 colors = P_rgb().p_u3(),
                 dim = P_dim().aw().h7(),
                 font=P_font().h1(),
                 align=P_align().c().c())
    def h2(self, *args):
        self.STL(list(args),
                 colors_type = "tr",
                 colors = P_rgb().p_u3(),
                 dim = P_dim().aw().h8(),
                 font=P_font().h2(),
                 align=P_align().c().c())
    def h3(self, *args):
        self.STL(list(args),
                 colors_type = "tr",
                 colors = P_rgb().p_u3(),
                 dim = P_dim().aw().h9(),
                 font=P_font().h3(),
                 align=P_align().c().c())
    def h4(self, *args):
        self.STL(list(args),
                 colors_type = "tr",
                 colors = P_rgb().p_u3(),
                 dim = P_dim().aw().h9(),
                 font=P_font().h4(),
                 align=P_align().c().c())
    def p(self, *args):
        self.STL(list(args),
                 colors_type = "tr",
                 colors = P_rgb().p_u3(),
                 dim = P_dim().p_all(),
                 font=P_font().p(),
                 align=P_align().l().c(),
                 word_wrap=True,)

    def mb(self, *args):
        self.STL(list(args),
                 colors_type = "tr",
                 colors = P_rgb().p_u3(),
                 dim = P_dim().p_aw_mb(),
                 font=P_font().h4(),
                 align=P_align().l().c())

    def demo(self, *args):
        self.STL(list(args),
                 colors_type = "tr",
                 colors = P_rgb().p_th3(),
                 dim = P_dim().aw().h7(),
                 font=P_font().h1(),
                 align=P_align().c().b(),
                 bd = P_bd().bottom().bn1())
