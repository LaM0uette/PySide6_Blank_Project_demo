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

    def _rtn(self, titre, msg, ico, txt_pb_ok):
        msg = Dlg_msg(titre=titre,
                      msg=msg,
                      ico=ico,
                      txt_pb_ok=txt_pb_ok,
                      width=self.width,
                      height=self.height,
                      opacity=self.opacity)
        msg.exec()


    def INFO(self, titre="INFO", msg="", ico=P_img().info(), txt_pb_ok="Ok"):
        self._rtn(titre=titre, msg=msg, ico=ico, txt_pb_ok=txt_pb_ok,)
    def ALERTE(self, titre="ALERTE", msg="", ico=P_img().alerte(), txt_pb_ok="Ok"):
        self._rtn(titre=titre, msg=msg, ico=ico, txt_pb_ok=txt_pb_ok, )
