from .Dlg_option import Dlg_option
from .....build import *


class Option:
    def __init__(self,
                 fen,
                 width=800,
                 height=600,
                 opacity=1
    ):
        self.fen = fen
        self.width = width
        self.height = height
        self.opacity = opacity

    def _rtn(self, titre, msg, ico, tm, txt_pb_appliquer, txt_pb_ok):
        opt = Dlg_option(
            fen=self.fen,
            titre=titre,
            msg=msg,
            ico=ico,
            tm=tm,
            txt_pb_appliquer=txt_pb_appliquer,
            txt_pb_ok=txt_pb_ok,
            width=self.width,
            height=self.height,
            opacity=self.opacity
        )
        opt.exec()


    def MAIN(self, titre="OPTION", msg="", ico=P_img().info(), tm="th3", txt_pb_appliquer="Appliquer", txt_pb_ok="Ok"):
        return self._rtn(
            titre=titre,
            msg=msg,
            ico=ico,
            tm=tm,
            txt_pb_appliquer=txt_pb_appliquer,
            txt_pb_ok=txt_pb_ok
        )
