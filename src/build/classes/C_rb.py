from .C_wg import C_wg
from ...build import *


class C_rb(C_wg):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.kwargs = kwargs

    def STL(self, lst, **kwargs):
        """
        colors_type=str %,
        colors=P_rgb().%,
        dim=P_dim().%,
        img=P_img().%,
        img_check=P_img().%,
        th=str %,
        th_check=str %,
        font=P_font().%,
        rd=P_rd().%,
        bd=P_bd().%,
        cur=str %,
        """
        for wg in lst: C_wg(wg=wg, attrs=kwargs).STL_RB()


    def demo_th(self, *args):
        self.STL(list(args),
                 colors_type="th",
                 colors=P_rgb().p_th1(),
                 dim=P_dim().p_aw_demo(),
                 img=P_img().check(),
                 img_check=P_img().valider(),
                 th="th3",
                 th_check="bn1",
                 rd=P_rd().rd1_5(),
                 bd=P_bd().bd1_bd_bn1(),
                 cur="main",)
    def demo_tr(self, *args):
        self.STL(list(args),
                 colors_type="tr",
                 colors=P_rgb().p_th1(),
                 dim=P_dim().p_aw_demo(),
                 img=P_img().check(),
                 img_check=P_img().valider(),
                 th="th3",
                 th_check="bn1",
                 cur="main")
