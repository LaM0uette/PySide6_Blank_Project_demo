from .C_wg import C_wg


class C_pb:
    def __init__(self, ui, **kwargs):

        self.ui = ui
        self.kwargs = kwargs

    def menu_top(self):
        print(self.ui.pb_mt_option.objectName())
        print(self.ui.pb_mt_reduire.objectName())
        print(self.ui.pb_mt_agrandir.objectName())
        print(self.ui.pb_mt_quitter.objectName())
