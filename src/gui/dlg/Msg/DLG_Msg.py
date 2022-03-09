from src import *
from src.gui.dlg.Msg.Msg import Msg


class DLG_Msg:
    def __init__(self,
                 width=650,
                 height=250,
                 opacity=1
    ):
        self.width = width
        self.height = height
        self.opacity = opacity

    def _rtn(self, titre, msg, ico, tm, txt_pb_ok):
        msg = Msg(
            titre=titre,
            msg=msg,
            ico=ico,
            tm=tm,
            txt_pb_ok=txt_pb_ok,
            width=self.width,
            height=self.height,
            opacity=self.opacity
        )
        msg.exec()


    def INFO(self, titre="INFO", msg="", ico=Img().info(), tm="th3", txt_pb_ok="Ok"):
        self._rtn(
            titre=titre,
            msg=msg,
            ico=ico,
            tm=tm,
            txt_pb_ok=txt_pb_ok
        )
    def ALERTE(self, titre="ALERTE", msg="", ico=Img().alerte(), tm="th3", txt_pb_ok="Ok"):
        self._rtn(
            titre=titre,
            msg=msg,
            ico=ico,
            tm=tm,
            txt_pb_ok=txt_pb_ok
        )