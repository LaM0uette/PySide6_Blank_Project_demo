from .C_wg import C_wg
from ...build import *


class C_pb(C_wg):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.kwargs = kwargs

    def STL(self, lst, **kwargs):
        """
        type = "ico",
        colors_type = "tr",
        colors = P_rgb().p_th1(),
        dim = P_dim().p_r_mt(),
        x_ico = P_style().x_ico(),
        X_ICO = P_style().X_ICO(),
        img = P_img().option(),
        img_check = P_img().option(),
        th = "bn1",
        th_hover = "th3",
        th_check = "bn2",
        font = P_font().p(),
        rd = P_rd().rd1_5(),
        bd = P_bd().bd1_bd_bn1(),
        cur = P_cur().souris_main(),
        """
        for wg in lst:
            C_wg(wg=wg, attrs=kwargs).STL_PB()


    def option(self, *args):
        self.STL(list(args),
                 type="zoom",
                 colors_type = "tr",
                 colors = P_rgb().p_th1(),
                 dim = P_dim().p_r_mt(),
                 img = P_img().option(),
                 th = "th2",
                 cur = "souris_main")
    def reduire(self, *args):
        self.STL(list(args),
                 type="zoom",
                 colors_type = "tr",
                 colors = P_rgb().p_th1(),
                 dim = P_dim().p_r_mt(),
                 img = P_img().reduire(),
                 th = "bn1",
                 cur = "souris_main")
    def agrandir(self, *args):
        self.STL(list(args),
                 type="zoom",
                 colors_type = "tr",
                 colors = P_rgb().p_th1(),
                 dim = P_dim().p_r_mt(),
                 img = P_img().agrandir(),
                 th = "th3",
                 cur = "souris_main")
    def quitter(self, *args):
        self.STL(list(args),
                 type="zoom",
                 colors_type = "tr",
                 colors = P_rgb().p_th1(),
                 dim = P_dim().p_r_mt(),
                 img = P_img().quitter(),
                 th = "bn2",
                 cur = "souris_main")

    def demo_txt(self, *args):
        self.STL(list(args),
                 colors_type = "txt",
                 colors = P_rgb().p_th1(),
                 dim = P_dim().p_aw_demo(),
                 font = P_font().p(),
                 cur = "main")
    def demo_txt_inv(self, *args):
        self.STL(list(args),
                 colors_type = "txt_inv",
                 colors = P_rgb().p_vert_th1(),
                 dim = P_dim().p_aw_demo(),
                 font = P_font().p(),
                 cur = "main")
    def demo_th(self, *args):
        self.STL(list(args),
                 colors_type = "th",
                 colors = P_rgb().p_th3(),
                 dim = P_dim().p_aw_demo(),
                 font = P_font().p(),
                 cur = "main")
    def demo_tr(self, *args):
        self.STL(list(args),
                 colors_type = "tr",
                 colors = P_rgb().p_th1(),
                 dim = P_dim().p_aw_demo(),
                 font = P_font().p(),
                 cur = "main")
    def demo_ck(self, *args):
        self.STL(list(args),
                 colors_type = "th",
                 colors = P_rgb().p_th3(),
                 dim = P_dim().p_aw_demo(),
                 font = P_font().p(),
                 cur = "main")
    def demo_ck_ico(self, *args):
        self.STL(list(args),
                 type="check",
                 colors_type="tr",
                 colors=P_rgb().p_th1(),
                 dim=P_dim().p_aw_demo(),
                 img=P_img().check(),
                 img_check=P_img().valider(),
                 th="th3",
                 th_check="bn1",
                 font=P_font().p(),
                 cur="main")
    def demo_zoom(self, *args):
        self.STL(list(args),
                 type="zoom",
                 colors_type = "tr",
                 colors = P_rgb().p_th1(),
                 dim = P_dim().p_aw_demo(),
                 img = P_img().calendrier(),
                 cur = "main")
    def demo_rd(self, *args):
        self.STL(list(args),
                 colors_type = "th",
                 colors = P_rgb().p_th3(),
                 dim = P_dim().p_aw_demo(),
                 font = P_font().p(),
                 rd=P_rd().rd1_5(),
                 cur = "main")
    def demo_bd(self, *args):
        self.STL(list(args),
                 colors_type = "th",
                 colors = P_rgb().p_th3(),
                 dim = P_dim().p_aw_demo(),
                 font = P_font().p(),
                 bd=P_bd().bd1_bd_bn1(),
                 cur = "main")
