from .C_wg import C_wg
from ...build import *
# print(self.ui.pb_mt_option.objectName())

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

    def menu_top(self, lst):
        for wg in lst: C_wg(

            wg=wg,
            s=P_rgb().th3()

        ).STL_PB()
