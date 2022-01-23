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

    def _rtn(self, titre, ico, tm, txt_pb_annuler):
        pg = Dlg_progress(
            titre=titre,
            ico=ico,
            tm=tm,
            txt_pb_annuler=txt_pb_annuler,
            width=self.width,
            height=self.height,
            opacity=self.opacity
        )
        pg.exec()



    def PG(self, titre="CHARGEMENT", ico=P_img().info(), tm="th3", txt_pb_annuler="Annuler"):
        return self._rtn(
            titre=titre,
            ico=ico,
            tm=tm,
            txt_pb_annuler=txt_pb_annuler
        )
