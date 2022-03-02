from PySide6 import QtCore, QtWidgets, QtGui

from src.gui.Dlg import msg_ui
from src.build import *
from src.In_classe import In_classe


class SplashScreen(msg_ui.Ui_Msg, QtWidgets.QDialog):
    dragPos: QtCore.QPoint

    def __init__(self):
        super(SplashScreen, self).__init__()

        self.width = 400
        self.height = 300
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
        Frame.Cadre(self.fr_main).th3()
        Frame.Base_th(self.fr_body, rgb=Rgb().th1())
        ### /QFrame ###

        # Lancement des fonctions de MEF global
        In_classe(ui=self)
    def IN_WG(self):
        # Base
        self.setCursor(Fct(cur=Cur().souris()).CUR())

        # Frame menu_top
        self.fr_menu_top.setFixedHeight(Dim().h9())
    def IN_CONNECTIONS(self):
        ## Menu_top
        self.pb_mt_quitter.clicked.connect(lambda: self.close())
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


    ###################
    ##     EVENT     ##
    ###################
    def mousePressEvent(self, event):
        cur = QtGui.QCursor()
        verifHeight = cur.pos().y() - self.pos().y()
        if event.buttons() == QtCore.Qt.LeftButton and verifHeight < Dim().h9():
            self.dragPos = event.globalPosition().toPoint()
            event.accept()
    def mouseMoveEvent(self, event):
        def act_move(event):
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
            self.dragPos = event.globalPosition().toPoint()
            event.accept()

        cur = QtGui.QCursor()
        height_verif = cur.pos().y() - self.pos().y()

        try:
            if event.buttons() == QtCore.Qt.LeftButton and height_verif < Dim().h9():
                act_move(event)
            if event.buttons() == QtCore.Qt.LeftButton and height_verif < Dim().h9():
                act_move(event)
        except AttributeError: pass
    ###################
    ##    /EVENT     ##
    ###################
