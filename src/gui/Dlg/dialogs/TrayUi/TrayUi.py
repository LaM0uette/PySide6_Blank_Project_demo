from PySide6 import QtCore, QtWidgets, QtGui

from src.gui.Dlg import tray_ui_ui
from src.build import *


class TrayUi(tray_ui_ui.Ui_TrayUi, QtWidgets.QDialog):
    def __init__(self):
        super(TrayUi, self).__init__()

        self.width = 300
        self.height = 600
        self.opacity = 1

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.Tool)
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
        Frame.Menu_top(self.fr_menu_top)
        Frame.Base_th(self.fr_body, rgb=Rgb().th1())
        ### /QFrame ###


        ### QPushButton ###
        PushButton.menu_top(self.pb_mt_quitter).quitter()
        PushButton.pin(self.pb_mt_pin)
        ### /QPushButton ###
    def IN_WG(self):
        # Base
        self.setCursor(Fct(cur=Cur().souris()).CUR())
    def IN_CONNECTIONS(self):
        # Menu_top
        self.pb_mt_quitter.clicked.connect(lambda: self.close())
        self.pb_mt_pin.clicked.connect(lambda: self.PIN())
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


    #######################
    ##     FONCTIONS     ##
    #######################
    def PIN(self):
        if self.pb_mt_pin.isChecked():
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        else:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    #######################
    ##    /FONCTIONS     ##
    #######################
