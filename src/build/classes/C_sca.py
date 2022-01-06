from .C_wg import C_wg
from ...build import *


class C_sca(C_wg):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.kwargs = kwargs
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        return self

    def STL(self, lst, **kwargs):
        """
        colors=P_rgb().%,
        dim=P_dim().%,
        rd=P_rd().%,
        bd=P_bd().%,
        scroll=P_scroll().%,
        """
        for wg in lst: C_wg(wg=wg, attrs=kwargs).STL_SCA()


    def invisible(self, *args):
        self.STL(list(args),
                 colors = P_rgb().p_th1(),
                 dim = P_dim().all(),
                 scroll=P_scroll().off().off())

    def demo(self, *args):
        self.STL(list(args),
                 colors = P_rgb().p_th1(),
                 dim = P_dim().all(),
                 scroll=P_scroll().off().nd())
