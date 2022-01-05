from .C_wg import C_wg
from ...build import *


class C_pb(C_wg):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.kwargs = kwargs
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        return self

    def STL(self, lst, **kwargs):
        """
        type=str %,
        colors_type=str %,
        colors=P_rgb().%,
        dim=P_dim().%,
        x_ico=P_style().%,
        X_ICO=P_style().%,
        img=P_img().%,
        img_check=P_img().%,
        th=str %,
        th_hover=str %,
        th_check=str %,
        font=P_font().%,
        rd=P_rd().%,
        bd=P_bd().%,
        edit=Bool %,
        cur=str %,
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

    def ok(self, *args):
        self.STL(list(args),
                 colors_type = "txt",
                 colors = P_rgb().p_vert_th2(),
                 dim = P_dim().p_r_mb_dlg(),
                 cur = "souris_main")
    def appliquer(self, *args):
        self.STL(list(args),
                 colors_type = "txt_inv",
                 colors = P_rgb().p_vert_th2(),
                 dim = P_dim().p_r_mb_dlg(),
                 cur = "souris_main")
    def annuler(self, *args):
        self.STL(list(args),
                 colors_type = "txt_inv",
                 colors = P_rgb().p_rouge_th2(),
                 dim = P_dim().p_r_mb_dlg(),
                 cur = "souris_main")

    def txt_h9(self, *args):
        self.STL(list(args),
                 colors_type = "txt",
                 colors = P_rgb().p_th1(),
                 dim = P_dim().p_aw_h9(),
                 font = P_font().p(),
                 cur = "main")

    def plein_th1(self, *args):
        self.STL(list(args),
                 colors_type="th",
                 colors=P_rgb().p_th1(),
                 dim=P_dim().p_aw_h5(),
                 font=P_font().p(),
                 bd=P_bd().bd1_bd_th2(),
                 cur="main")
    def plein_th2(self, *args):
        self.STL(list(args),
                 colors_type="th",
                 colors=P_rgb().p_th2(),
                 dim=P_dim().p_aw_h5(),
                 font=P_font().p(),
                 cur="main")
    def plein_th3(self, *args):
        self.STL(list(args),
                 colors_type="th",
                 colors=P_rgb().p_th3(),
                 dim=P_dim().p_aw_h5(),
                 font=P_font().p(),
                 cur="main")
    def plein_bn1(self, *args):
        self.STL(list(args),
                 colors_type="th",
                 colors=P_rgb().p_bn1(),
                 dim=P_dim().p_aw_h5(),
                 font=P_font().p(),
                 cur="main")
    def plein_bn2(self, *args):
        self.STL(list(args),
                 colors_type="th",
                 colors=P_rgb().p_bn2(),
                 dim=P_dim().p_aw_h5(),
                 font=P_font().p(),
                 cur="main")

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
                 cur = "main",)
