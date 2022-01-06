from .C_wg import C_wg
from ...build import *


class C_sd(C_wg):
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
        """
        for wg in lst: C_wg(wg=wg, attrs=kwargs).STL_SD()


    def th_rond(self, *args):
        self.STL(list(args),
                 colors_type="rond",
                 colors=P_rgb().p_th1(),
                 dim=P_dim().p_aw_h8())

    def demo_h(self, *args):
        self.STL(list(args),
                 colors_type="th",
                 colors=P_rgb().p_th1(),
                 dim=P_dim().p_aw_demo())
    def demo_v(self, *args):
        self.STL(list(args),
                 colors_type="rond",
                 colors=P_rgb().p_th1(),
                 dim=P_dim().p_c_h5())
