from . import *


class Dlg:
    def __init__(self, **kwargs):

        self.kwargs = kwargs
        self.rtn = None

        self.dlg = Dialog(**self.kwargs)


    def RTN_SGN_REP(self, val): self.rtn = val



    # MODELES
    def INFO(self):
        self.dlg.MSG(ico=P_img().info())
        self.dlg.exec()
    def ALERTE(self):
        self.dlg.MSG(ico=P_img().alerte())
        self.dlg.exec()
    def REP(self):
        self.dlg.sgn_rep.connect(self.RTN_SGN_REP)
        self.dlg.REP()
        self.dlg.exec()
        return self.rtn
    def INPUT(self):
        self.dlg.sgn_txt.connect(self.RTN_SGN_REP)
        self.dlg.INPUT()
        self.dlg.exec()
        return self.rtn


    # CUSTOMS
    def QUITTER(self):
        self.dlg = Dialog(msg="\tVoulez vous fermer cette application ?", ico=P_img().alerte())
        self.dlg.sgn_rep.connect(self.RTN_SGN_REP)
        self.dlg.REP()
        self.dlg.exec()
        return self.rtn
