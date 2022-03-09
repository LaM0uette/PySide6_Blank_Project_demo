from PySide6 import QtCore, QtWidgets, QtGui

from src import *
from src.gui.ui import input_ui
from src.gui.events.Event import Event


class Input(input_ui.Ui_Input, QtWidgets.QDialog):
    dragPos: QtCore.QPoint
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
        super(Input, self).__init__()

        self.titre = titre
        self.msg = msg
        self.ico = ico
        self.rgb = tm
        self.txt_pb_ok = txt_pb_ok
        self.txt_pb_annuler = txt_pb_annuler
        self.width = width
        self.height = height
        self.opacity = opacity

        self.INIT()

        ### CREATION DES EVENT ###
        self.evt = Event(self)
        self.mousePressEvent = self.evt.mousePressEvent
        self.mouseMoveEvent = self.evt.mouseMoveEvent

    ############################
    ##     INITIALISATION     ##
    ############################
    def IN_BASE(self):
        # Fenetre
        self.setWindowTitle(self.titre)
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)
        self.setWindowOpacity(self.opacity)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setGraphicsEffect(Shadow().ombre_portee(self))
        self.setWindowModality(QtCore.Qt.ApplicationModal)
    def IN_SETUP_UI(self):
        ### Ui ###
        self.setupUi(self)
        self.vlay_main.setContentsMargins(v_gb.MARGIN_APP, v_gb.MARGIN_APP, v_gb.MARGIN_APP, v_gb.MARGIN_APP)
    def IN_CLASSE(self):
        ### QFrame ###
        Frame.Menu(self.fr_menu_top).top()
        Frame.Cadre(self.fr_main).th2()
        Frame.Base(self.fr_body).th(rgb=Rgb().th1())
        Frame.Menu(self.fr_input_bottom).bottom_dlg()
        ### /QFrame ###


        ### QLabel ###
        Label.Base(self.lb_mt_ico).ico_custom(img=self.ico, img_rgb=self.rgb)
        Label.Base(self.lb_mt_nom, font_size=Font().h3()).tr()
        Label.Base(self.lb_input_text).tr()
        ### /QLabel ###


        ### QPushButton ###
        PushButton.Dlg(self.pb_input_ok).ok()
        PushButton.Dlg(self.pb_input_annuler).nok_inv()
        PushButton.menu_top(self.pb_mt_quitter).quitter()
        ### /QPushButton ###


        ### QText ###
        LineEdit.Base(self.le_input_text).th()
        ### /QText ###
    def IN_WG(self):
        # Base
        self.setCursor(Functions().SET_CURSOR(cur=Cur().souris()))

        # Frame menu_top
        self.fr_menu_top.setFixedHeight(Dim().h9())

        # Menu_top
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
        self.IN_SETUP_UI()
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
        if event.buttons() == QtCore.Qt.LeftButton and 10< verifHeight < Dim().h9()+10:
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
            if event.buttons() == QtCore.Qt.LeftButton and 10< height_verif < Dim().h9()+10:
                act_move(event)
            if event.buttons() == QtCore.Qt.LeftButton and 10< height_verif < Dim().h9()+10:
                act_move(event)
        except AttributeError: pass
    ###################
    ##    /EVENT     ##
    ###################
