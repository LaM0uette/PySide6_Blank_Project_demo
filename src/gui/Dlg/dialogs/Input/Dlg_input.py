from PySide6 import QtCore, QtWidgets, QtGui

from ... import input_ui
from .....build import *
from .....In_classe import In_classe


class Dlg_input(input_ui.Ui_Input, QtWidgets.QDialog):
    dragPos: QtCore.QPoint
    rep = False
    input = ""

    def __init__(self,
                 titre,
                 msg,
                 ico,
                 tm,
                 txt_pb_ok,
                 txt_pb_annuler,
                 width,
                 height,
                 opacity,
    ):
        super(Dlg_input, self).__init__()

        self.titre = titre
        self.msg = msg
        self.ico = ico
        self.tm = tm
        self.txt_pb_ok = txt_pb_ok
        self.txt_pb_annuler = txt_pb_annuler
        self.width = width
        self.height = height
        self.opacity = opacity

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setupUi(self)
        self.INIT()


    ############################
    ##     INITIALISATION     ##
    ############################
    def IN_BASE(self):
        # Fenetre
        self.setWindowTitle(self.titre)
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)
        self.setWindowOpacity(self.opacity)
    def IN_CLASSE(self):
        ### QFrame ###
        Frame.Cadre(self.fr_main).th3()
        Frame.Menu_bottom_dlg(self.fr_input_bottom)
        ### /QFrame ###


        ### QLabel ###
        Label.Base_tr(self.lb_input_text)
        ### /QLabel ###


        ### QPushButton ###
        PushButton.dlg_ok(self.pb_input_ok)
        PushButton.dlg_nok_inv(self.pb_input_annuler)
        ### /QPushButton ###


        ### QText ###
        TextEdit.Demo_th(self.le_input_text)
        ### /QText ###

        # Lancement des fonctions de MEF global
        In_classe(ui=self)
    def IN_WG(self):
        # Base
        self.setCursor(Fct(cur=Cur().souris()).CUR())
        self.setStyleSheet(f"background-color: rgb{P_rgb().th1()};")

        # Frame menu_top
        self.fr_menu_top.setFixedHeight(P_dim().h9())

        # Menu_top
        dim = P_dim().carr().h9()
        Fct(wg=self.lb_mt_ico, w=dim.get("w"), h=dim.get("h")).DIM()
        self.lb_mt_ico.setPixmap(QtGui.QPixmap(f"{self.ico}{self.tm}.svg"))
        self.lb_mt_ico.setScaledContents(True)
        self.lb_mt_nom.setText(self.titre)

        # Message
        self.lb_input_text.setText(f"{self.msg}: ")
        self.le_input_text.setPlaceholderText(f"{self.msg}...")

        # pb dlg
        self.pb_input_ok.setText(self.txt_pb_ok)
        self.pb_input_annuler.setText(self.txt_pb_annuler)
        self.pb_input_annuler.setDefault(True)
    def IN_CONNECTIONS(self):
        # Menu_top
        self.pb_mt_quitter.clicked.connect(lambda: self.close())

        # pb dlg
        self.pb_input_ok.clicked.connect(lambda: self.OK())
        self.pb_input_annuler.clicked.connect(lambda: self.close())
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
    def OK(self):
        self.rep = True
        self.input = self.le_input_text.text()
        self.close()
    #######################
    ##    /FONCTIONS     ##
    #######################


    ###################
    ##     EVENT     ##
    ###################
    def mousePressEvent(self, event):
        cur = QtGui.QCursor()
        verifHeight = cur.pos().y() - self.pos().y()
        if event.buttons() == QtCore.Qt.LeftButton and verifHeight < P_dim().h9() and self.windowState() != QtCore.Qt.WindowMaximized:
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
            if event.buttons() == QtCore.Qt.LeftButton and height_verif < P_dim().h9() and self.windowState() != QtCore.Qt.WindowMaximized:
                act_move(event)
            if event.buttons() == QtCore.Qt.LeftButton and height_verif < P_dim().h9() and self.windowState() == QtCore.Qt.WindowMaximized:
                self.setWindowState(QtCore.Qt.WindowNoState)
                act_move(event)
        except AttributeError: pass
    ###################
    ##    /EVENT     ##
    ###################
