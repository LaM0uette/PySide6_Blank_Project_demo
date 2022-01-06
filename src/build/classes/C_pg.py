from .C_wg import C_wg
from ...build import *


class C_pg(C_wg):
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
        dim=P_dim().%,
        rd=P_rd().%,
        bd=P_bd().%,
        pad=float %,
        """
        for wg in lst: C_wg(wg=wg, attrs=kwargs).STL_PG()


    def demo(self, *args):
        self.STL(list(args),
                 colors=P_rgb().p_th1(),
                 dim=P_dim().aw().h8(),
                 bd=P_bd().rl().bn1(),
                 pad="bd", )
