import sys

from PySide6 import QtCore, QtWidgets, QtGui

from .gui.main_ui import Ui_main
from .build import *
from .config import config



class main(Ui_main, QtWidgets.QWidget):
    def __init__(self):
        super(main, self).__init__()

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setupUi(self)
        self.INIT()

    ### INITIALISATION
    def IN_BASE(self):
        ## Fenetre
        self.setWindowTitle(config.nom)
        self.setFixedWidth(config.widht)
        self.setFixedHeight(config.height)
        self.setWindowOpacity(config.opacity)
    def IN_CLASSE(self):
        pass
    def IN_WG(self):
        ## Frame menu_top
        # self.fr_menu_top.setFixedHeight(Data("dim").GET_CLS("h_menu_top"))

        ## Icone de l'app
        # dim = dct_pal.get("dim").get("c_menu_top")
        # functions.DIM(wg=self.lb_mt_ico, w=dim.get("w"), h=dim.get("h"))
        # self.lb_mt_ico.setPixmap(QtGui.QPixmap(PXM))
        self.lb_mt_ico.setScaledContents(True)
        self.lb_mt_nom.setText(config.nom)

        ## Version de l'app
        self.lb_mt_version.setText(str(config.version))

        ## Widget blanc pour centrer le nom de l'app
        # functions.DIM(wg=self.wg_mt_blank, w=dim.get("w") * 3, h=dim.get("h"))
    def IN_WG_BASE(self):
        pass
    def IN_CONNECTIONS(self):
        ## Menu_top
        self.pb_mt_option.clicked.connect(lambda: self.FCT_OPTION())
        self.pb_mt_reduire.clicked.connect(lambda: self.EVT_REDUIRE_GDT())
        self.pb_mt_agrandir.clicked.connect(lambda: self.EVT_AGRANDIR_GDT())
        self.pb_mt_quitter.clicked.connect(lambda: self.EVT_REDUIRE_HIDE_GDT())
    def IN_ACT(self):
        pass
    def INIT(self):
        self.IN_BASE()
        self.IN_CLASSE()
        self.IN_WG()
        self.IN_WG_BASE()
        self.IN_CONNECTIONS()
        self.IN_ACT()


    ### FONCTIONS
    def FCT_OPTION(self):
        pass


    ### EVENT
    def EVT_CENTRE_FEN(self):
        center = QtGui.QScreen.availableGeometry(QtWidgets.QApplication.primaryScreen()).center()
        geo = fen.frameGeometry()
        geo.moveCenter(center)
        fen.move(geo.topLeft())

        self.setFixedWidth(config.widht)
        self.setFixedHeight(config.height)
    def EVT_AGRANDIR_GDT(self):
        if fen.windowState() == QtCore.Qt.WindowMaximized:
            fen.setWindowState(QtCore.Qt.WindowNoState)
            self.EVT_CENTRE_FEN()
        else:
            fen.setWindowState(QtCore.Qt.WindowMaximized)
    def EVT_REDUIRE_GDT(self):
        fen.setWindowState(QtCore.Qt.WindowNoState)
        self.EVT_CENTRE_FEN()
        fen.setWindowState(QtCore.Qt.WindowMinimized)
    def EVT_REDUIRE_HIDE_GDT(self):
        if config.auto_close: return self.EVT_QUITTER()
        self.hide()
        self.EVT_CENTRE_FEN()
    def EVT_QUITTER(self):
        app.quit()
        quit()
    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        event.accept()
        app.quit()


app = QtWidgets.QApplication(sys.argv)
app.processEvents()

fen = main()
fen.show()

sys.exit(app.exec())
