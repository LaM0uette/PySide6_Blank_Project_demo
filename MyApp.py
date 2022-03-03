import sys

from PySide6 import QtCore, QtWidgets, QtGui

from src import *


class main(Ui_main, QtWidgets.QWidget):
    dragPos: QtCore.QPoint

    def __init__(self):
        super(main, self).__init__()

        self.INIT(
            [self.IN_BASE, "Configuration des éléments principaux"],
            [self.IN_SETUP_UI, "Setup de l'interface graphique"],
            [self.IN_CLASSE, "Initialisation des Widgets"],
            [self.IN_WG, "Configuration de base des Widgets"],
            [self.IN_CONNECTIONS, "Ajout des connexions"],
            [self.IN_ACT, "Fonctions de base"],
            [self.IN_WG_BASE, "Etat de base des Widgets"],
            [self.IN_TRAY, "Finalisation de la configuration"]
        )

    ############################
    ##     INITIALISATION     ##
    ############################
    def IN_BASE(self):
        self.setWindowTitle(config.nom)
        self.setWindowIcon(QtGui.QPixmap(f"{Img().main()}th3.svg"))
        self.setWindowOpacity(config.opacity)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    def IN_SETUP_UI(self):
        self.setupUi(self)
    def IN_CLASSE(self):
        pass
    def IN_WG(self):
        pass
    def IN_CONNECTIONS(self):
        pass
    def IN_ACT(self):
        pass
    def IN_WG_BASE(self):
        pass
    def IN_TRAY(self):
        pass
    def INIT(self, *args):
        for fct in args:
            fct[0]()
    ############################
    ##    /INITIALISATION     ##
    ############################

    Align().top()


    #####################
    ##     ACTIONS     ##
    #####################
    #####################
    ##    /ACTIONS     ##
    #####################


    #######################
    ##     FONCTIONS     ##
    #######################
    #######################
    ##    /FONCTIONS     ##
    #######################


    ###################
    ##     EVENT     ##
    ###################
    ###################
    ##    /EVENT     ##
    ###################


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.processEvents()

    fen = main()
    fen.show()

    sys.exit(app.exec())
