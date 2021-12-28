from .C_wg import C_wg
from ...build import *


class C_pb(C_wg):
    def __init__(self, ui, **kwargs):
        super().__init__(**kwargs)

        self.ui = ui
        self.kwargs = kwargs

        self.menu_top([
            self.ui.pb_mt_option,
            self.ui.pb_mt_reduire,
            self.ui.pb_mt_agrandir,
            self.ui.pb_mt_quitter,
        ])

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
