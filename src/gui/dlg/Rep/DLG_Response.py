from src import *
from src.gui.dlg.Rep.Response import Response


class DLG_Response:
    def __init__(
            self,
            width=650,
            height=250,
            opacity=1
    ):
        self.width = width
        self.height = height
        self.opacity = opacity

    def _rtn(self, title, msg, ico, ico_rgb, txt_ok, txt_cancel):
        _reponse = Response(
            title=title,
            msg=msg,
            ico=ico,
            ico_rgb=ico_rgb,
            txt_ok=txt_ok,
            txt_cancel=txt_cancel,
            width=self.width,
            height=self.height,
            opacity=self.opacity
        )
        _reponse.exec()
        return _reponse.rep


    def INFO(self, title="INFO", msg="", ico=Img().info(), ico_rgb="th3", txt_ok="Ok", txt_cancel="Annuler"):
        return self._rtn(
            title=title,
            msg=msg,
            ico=ico,
            ico_rgb=ico_rgb,
            txt_ok=txt_ok,
            txt_cancel=txt_cancel
        )
    def ALERTE(self, title="ALERTE", msg="", ico=Img().alerte(), ico_rgb="th3", txt_ok="Valider", txt_cancel="Annuler"):
        return self._rtn(
            title=title,
            msg=msg,
            ico=ico,
            ico_rgb=ico_rgb,
            txt_ok=txt_ok,
            txt_cancel=txt_cancel
        )
    def QUITTER(self, title="Quitter", msg="Voulez vous quitter cette application ?", ico=Img().quitter(), ico_rgb="bn2", txt_ok="Quitter", txt_cancel="Annuler"):
        return self._rtn(
            title=title,
            msg=msg,
            ico=ico,
            ico_rgb=ico_rgb,
            txt_ok=txt_ok,
            txt_cancel=txt_cancel
        )
