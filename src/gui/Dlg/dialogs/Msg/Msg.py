from .Dlg_msg import Dlg_msg
from .....build import *


class Msg:
    def __init__(self,
                 titre="",
                 msg="",
                 ico=P_img().main(),
                 txt_pb_ok="Ok",
                 width=600,
                 height=200,
                 opacity=1
    ):
        self.titre = titre
        self.msg = msg
        self.ico = ico
        self.txt_pb_ok = txt_pb_ok
        self.width = width
        self.height = height
        self.opacity = opacity


    def _rtn(self):
        msg = Dlg_msg(titre=self.titre,
                      msg=self.msg,
                      ico=self.ico,
                      txt_pb_ok=self.txt_pb_ok,
                      width=self.width,
                      height=self.height,
                      opacity=self.opacity)
        msg.exec()


    def INFO(self):
        self.ico = P_img().info()
        self._rtn()
    def ALERTE(self):
        self.ico = P_img().alerte()
        self._rtn()
