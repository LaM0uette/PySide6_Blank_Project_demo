from PySide6 import QtCore, QtWidgets, QtGui

from src.gui.Dlg import tray_ui_ui
from src.build import *


class TrayUi(tray_ui_ui.Ui_TrayUi, QtWidgets.QDialog):
    def __init__(self):
        super(TrayUi, self).__init__()

        self.width = 300
        self.height = 600
        self.opacity = 1

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.setupUi(self)
        self.INIT()


    ############################
    ##     INITIALISATION     ##
    ############################
    def IN_BASE(self):
        # Fenetre
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)
        self.setWindowOpacity(self.opacity)
    def IN_CLASSE(self):
        ### QFrame ###
        Frame.TrayUi(self.fr_main)
        ### /QFrame ###
    def IN_WG(self):
        # Base
        self.setCursor(Fct(cur=Cur().souris()).CUR())
    def IN_CONNECTIONS(self):
        pass
    def IN_ACT(self):
        pass
    def IN_WG_BASE(self):
        pass
    def INIT(self):
        self.IN_BASE()
        self.IN_CLASSE()
        self.IN_WG()
        self.IN_CONNECTIONS()
        self.IN_ACT()
        self.IN_WG_BASE()
    ############################
    ##    /INITIALISATION     ##
    ############################
