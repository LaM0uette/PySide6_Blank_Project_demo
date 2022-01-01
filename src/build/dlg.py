from .classes.Classe_dlg import *


class Dlg:
    def __init__(self, msg):

        self.msg = msg

    def VERIF_CHOIX(self, titre, msg_verif, ico=None):
        dlg = MB_REPONSE(titre=titre, msg=self.msg, ico=ico, msg_verif=msg_verif)
        return dlg.exec()
    def INFO(self):
        dlg = MB_INFO(titre="Info", msg=self.msg, ico=P_img().info() + "th3")
        dlg.exec()
    def MSG_ERREUR(self):
        dlg = MB_ALERTE(titre="Erreur", msg=self.msg, ico=P_img().alerte() + "th3")
        dlg.exec()
