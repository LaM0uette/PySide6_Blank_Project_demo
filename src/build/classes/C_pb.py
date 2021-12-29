from .C_wg import C_wg
from ...build import *


class C_pb(C_wg):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.kwargs = kwargs

    def STL(self, lst, **kwargs):
        for wg in lst:
            C_wg(wg=wg, attrs=kwargs).STL_PB()


    def menu_top(self, *args):
        self.STL(list(args),
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
                 font = P_font().p()
        )
