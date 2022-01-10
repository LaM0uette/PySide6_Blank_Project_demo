from .C_wg import C_wg
from ...build import *


class C_cb:
    def __init__(self):
        pass

    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        return self

    def STL(self, lst, **kwargs):
        for wg in lst: C_wg(wg=wg, attrs=kwargs).STL_CB()


    def th(self, *args):
        self.STL(list(args),
                 colors_type="th",
                 colors=P_rgb().p_th1(),
                 dim=P_dim().aw().h9(),
                 font=P_font().h4(),
                 bd=P_bd().bottom().th3(),
                 edit=True,
                 cur="souris_main")
    def font(self, *args):
        self.STL(list(args),
                 colors_type="tr",
                 colors=P_rgb().p_th1(),
                 dim=P_dim().aw().h9(),
                 font=P_font().h4(),
                 bd=P_bd().bottom().th3(),
                 edit=True,
                 cur="souris_main")

    def demo_th(self, *args):
        self.STL(list(args),
                 colors_type="th",
                 colors=P_rgb().p_th1(),
                 dim=P_dim().aw().h8(),
                 font=P_font().h3(),
                 bd=P_bd().bottom().th3(),
                 edit=True,
                 cur="souris_main")
    def demo_tr(self, *args):
        self.STL(list(args),
                 colors_type="tr",
                 colors=P_rgb().p_th1(),
                 dim=P_dim().aw().h8(),
                 font=P_font().h3(),
                 bd=P_bd().bottom().th3(),
                 edit=False,
                 cur="main")
