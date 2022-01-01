from PySide6 import QtCore, QtWidgets

from ..gui import *
from ..build import *
from ..config import *
from ..In_classe import In_classe


class Dlg(dlg_ui.Ui_Dlg, QtWidgets.QWidget):
    sgn_ok = QtCore.Signal(str)

    def test(self):
        self.sgn_ok.emit("ok")

    def __init__(self):
        super(Dlg, self).__init__()

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setupUi(self)
        self.INIT()


    ### INITIALISATION
    def IN_BASE(self):
        ## Fenetre
        self.setWindowTitle(config.nom)
        self.setFixedWidth(config.widht/2)
        self.setFixedHeight(config.height/2)
        self.setWindowOpacity(config.opacity)
    def IN_CLASSE(self):
        pass


    def IN_WG(self):
        # Base
        self.setCursor(Fct(cur="souris").CUR())
        self.setStyleSheet(f"background-color: rgb{P_rgb().th2()};")

        # Frame menu_top
        self.fr_menu_top.setFixedHeight(P_dim().h_mt())

        # Icone de l'app
        dim = P_dim().p_c_mt()
        Fct(wg=self.lb_mt_ico, w=dim.get("w"), h=dim.get("h")).DIM()
        # self.lb_mt_ico.setPixmap(QtGui.QPixmap(PXM))
        self.lb_mt_ico.setScaledContents(True)
        self.lb_mt_nom.setText(config.nom)
    def IN_WG_BASE(self):
        pass
    def IN_CONNECTIONS(self):
        ## Menu_top
        self.pb_mt_quitter.clicked.connect(lambda: self.close())

        #
        self.pushButton.clicked.connect(self.test)
    def IN_ACT(self):
        pass
    def INIT(self):
        self.IN_BASE()
        self.IN_CLASSE()
        self.IN_WG()
        self.IN_WG_BASE()
        self.IN_CONNECTIONS()
        self.IN_ACT()
