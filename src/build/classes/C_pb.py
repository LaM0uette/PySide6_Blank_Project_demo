from .C_wg import C_wg
from ...build import *


class C_pb(C_wg):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.kwargs = kwargs


    def STL(self, lst, **kwargs):
        for wg in lst:
            C_wg(
                wg=wg,
                attrs=kwargs
            ).STL_PB()
    def menu_top(self, lst):
        self.STL(lst,
                 colors=P_rgb().p_th3()
        )
