from .Dlg_progress import Dlg_progress
from .....build import *


class Progress:
    def __init__(self,
                 width=600,
                 height=200,
                 opacity=1
    ):
        self.width = width
        self.height = height
        self.opacity = opacity

    def _rtn(self, titre, msg, ico, tm, txt_pb_ok, txt_pb_annuler):
        msg = Dlg_progress(
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
        msg.exec()

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
