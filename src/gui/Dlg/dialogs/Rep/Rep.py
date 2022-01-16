from .Dlg_rep import Dlg_rep
from .....build import *


class Rep:
    def __init__(self,
                 width=600,
                 height=200,
                 opacity=1
    ):
        self.width = width
        self.height = height
        self.opacity = opacity

    def _rtn(self, titre, msg, ico, txt_pb_ok, txt_pb_annuler):
        msg = Dlg_rep(
            titre=titre,
            msg=msg,
            ico=ico,
            txt_pb_ok=txt_pb_ok,
            txt_pb_annuler=txt_pb_annuler,
            width=self.width,
            height=self.height,
            opacity=self.opacity
        )
        msg.exec()

        return msg.rep


    def INFO(self, titre="INFO", msg="", ico=P_img().info(), txt_pb_ok="Ok", txt_pb_annuler="Annuler"):
        return self._rtn(
            titre=titre,
            msg=msg,
            ico=ico,
            txt_pb_ok=txt_pb_ok,
            txt_pb_annuler=txt_pb_annuler
        )
    def ALERTE(self, titre="ALERTE", msg="", ico=P_img().alerte(), txt_pb_ok="Valider", txt_pb_annuler="Annuler"):
        return self._rtn(
            titre=titre,
            msg=msg,
            ico=ico,
            txt_pb_ok=txt_pb_ok,
            txt_pb_annuler=txt_pb_annuler
        )
    def QUITTER(self, titre="ALERTE", msg="Voulez vous quitter cette application ?", ico=P_img().alerte(), txt_pb_ok="Valider", txt_pb_annuler="Annuler"):
        return self._rtn(
            titre=titre,
            msg=msg,
            ico=ico,
            txt_pb_ok=txt_pb_ok,
            txt_pb_annuler=txt_pb_annuler
        )
