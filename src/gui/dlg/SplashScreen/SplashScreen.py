from PySide6 import QtCore, QtWidgets

from src.gui.ui import splash_screen_ui
from src import *


class SplashScreen(splash_screen_ui.Ui_SplashScreen, QtWidgets.QDialog):
    def __init__(self):
        super(SplashScreen, self).__init__()

        self.width = 600
        self.height = 400
        self.opacity = 1

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.setupUi(self)
        self.INIT()

    ############################
    ##     INITIALISATION     ##
    ############################
    def IN_BASE(self):
        ### Fenetre ###
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)
        self.setWindowOpacity(self.opacity)
    def IN_CLASSE(self):
        ### QFrame ###
        Frame.SplashScreen(self.fr_main)
        ### /QFrame ###


        ### QLabel ###
        Label.Base(self.lb_titre, font_size=Font().h3()).tr()
        Label.Base(self.lb_description, self.lb_chargement, font_size=Font().h5()).tr()
        Label.Base(self.lb_ico).ico_splash()
        ### /QLabel ###


        ### QProgressBar ###
        ProgressBar.Base(self.pg_chargement).Chargement()
        ### /QProgressBar ###
    def IN_WG(self):
        ### Base ###
        self.setCursor(Functions().SET_CURSOR(cur=Cur().souris()))

        ### Infos ###
        self.lb_titre.setText(config.nom)
        self.lb_description.setText(config.description)
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
