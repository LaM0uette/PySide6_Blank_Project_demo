from .Dlg_input import Dlg_input
from .....build import *


class Input:
    def __init__(self,
                 width=600,
                 height=200,
                 opacity=1
    ):
        self.width = width
        self.height = height
        self.opacity = opacity

    def _rtn(self, titre, msg, ico, tm, txt_pb_ok, txt_pb_annuler):
        _input = Dlg_input(
            titre=titre,
            msg=msg,
            ico=ico,
            tm=tm,
            txt_pb_ok=txt_pb_ok,
            txt_pb_annuler=txt_pb_annuler,
            width=self.width,
            height=self.height,
            opacity=self.opacity
        )
        _input.exec()

        return msg.rep, msg.input


    def TXT(self, titre="INPUT", msg="", ico=P_img().info(), tm="th3", txt_pb_ok="Ok", txt_pb_annuler="Annuler"):
        return self._rtn(
            titre=titre,
            msg=msg,
            ico=ico,
            tm=tm,
            txt_pb_ok=txt_pb_ok,
            txt_pb_annuler=txt_pb_annuler
        )
