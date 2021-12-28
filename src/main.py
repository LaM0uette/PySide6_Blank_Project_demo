import sys

from PySide6 import QtCore, QtWidgets, QtGui

from .gui.main_ui import Ui_main
from .build import *
from .config import *



class main(Ui_main, QtWidgets.QWidget):
    dragPos: QtCore.QPoint
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

        self.setCursor(Fct(cur="souris").CUR())
        self.setStyleSheet(f"background-color: rgb{P_rgb().th1()};")
    def IN_CLASSE(self):
        pass
    def IN_WG(self):
        # Frame menu_top
        self.fr_menu_top.setFixedHeight(P_dim().h_mt())

        # Icone de l'app
        dim = P_dim().p_c_mt()
        Fct(wg=self.lb_mt_ico, w=dim.get("w"), h=dim.get("h")).DIM()
        self.lb_mt_ico.setPixmap(QtGui.QPixmap(PXM))
        self.lb_mt_ico.setScaledContents(True)
        self.lb_mt_nom.setText(config.nom)

        # Version de l'app
        self.lb_mt_version.setText(str(config.version))

        # Widget blanc pour centrer le nom de l'app
        Fct(wg=self.wg_mt_blank, w=dim.get("w") * 3, h=dim.get("h")).DIM()
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
    def mousePressEvent(self, event):
        cur = QtGui.QCursor()
        verifHeight = cur.pos().y() - self.pos().y()
        if event.buttons() == QtCore.Qt.LeftButton and verifHeight < P_dim().h_mt() and fen.windowState() != QtCore.Qt.WindowMaximized:
            self.dragPos = event.globalPosition().toPoint()
            event.accept()
    def mouseMoveEvent(self, event):
        cur = QtGui.QCursor()
        height_verif = cur.pos().y() - self.pos().y()

        if event.buttons() == QtCore.Qt.LeftButton and height_verif < P_dim().h_mt() and fen.windowState() != QtCore.Qt.WindowMaximized and cur.pos().y() <= 0:
            self.setCursor(Fct(cur="agrandir").CUR())
        else:
            self.setCursor(Fct(cur="souris").CUR())

        try:
            if event.buttons() == QtCore.Qt.LeftButton and height_verif < P_dim().h_mt() and fen.windowState() != QtCore.Qt.WindowMaximized:
                self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
                self.dragPos = event.globalPosition().toPoint()
                event.accept()

            if event.buttons() == QtCore.Qt.LeftButton and height_verif < P_dim().h_mt() and fen.windowState() == QtCore.Qt.WindowMaximized:
                fen.setWindowState(QtCore.Qt.WindowNoState)
                self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
                self.dragPos = event.globalPosition().toPoint()
                event.accept()

        except AttributeError:
            pass
    def mouseReleaseEvent(self, event):
        cur = QtGui.QCursor()
        height_verif = cur.pos().y() - self.pos().y()
        if height_verif < P_dim().h_mt() and fen.windowState() != QtCore.Qt.WindowMaximized and cur.pos().y() <= 0:
            self.setCursor(Fct(cur="souris").CUR())
            self.EVT_AGRANDIR_GDT()
            event.accept()
    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        event.accept()
        app.quit()


PXM = P_img().main() + "th1" + ".svg"
app = QtWidgets.QApplication(sys.argv)
splash = QtWidgets.QSplashScreen(QtGui.QPixmap(PXM).scaledToHeight(500), QtCore.Qt.WindowStaysOnTopHint)
splash.show()
app.processEvents()

fen = main()
splash.finish(fen)
fen.show()

sys.exit(app.exec())
