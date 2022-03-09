from PySide6 import QtCore, QtWidgets

from src import *
from src.gui.ui import msg_ui
from src.gui.events.Event import Event


class Msg(msg_ui.Ui_Msg, QtWidgets.QDialog):
    dragPos: QtCore.QPoint

    def __init__(self,
                 titre,
                 msg,
                 ico,
                 tm,
                 txt_pb_ok,
                 width,
                 height,
                 opacity,
    ):
        super(Msg, self).__init__()

        self.titre = titre
        self.msg = msg
        self.ico = ico
        self.rgb = tm
        self.txt_pb_ok = txt_pb_ok
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
        ### Fenetre ###
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
        self.glay_main.setContentsMargins(v_gb.MARGIN_APP, v_gb.MARGIN_APP, v_gb.MARGIN_APP, v_gb.MARGIN_APP)
    def IN_CLASSE(self):
        ### QFrame ###
        Frame.Menu(self.fr_menu_top).top()
        Frame.Cadre(self.fr_main).th2()
        Frame.Dlg(self.fr_body).th(rgb=Rgb().th1())
        Frame.Menu(self.fr_msg_bottom).bottom_dlg()
        ### /QFrame ###


        ### QLabel ###
        Label.Base(self.lb_mt_ico).ico_custom(img=self.ico, img_rgb=self.rgb)
        Label.Base(self.lb_mt_nom, font_size=Font().h3()).tr()
        Label.Base(self.lb_msg_text).tr()
        ### /QLabel ###


        ### QPushButton ###
        PushButton.Dlg(self.pb_msg_ok).ok()
        PushButton.menu_top(self.pb_mt_quitter).quitter()
        ### /QPushButton ###
    def IN_WG(self):
        # Base
        self.setCursor(Functions().SET_CURSOR(cur=Cur().souris()))

        # Frame menu_top
        self.fr_menu_top.setFixedHeight(Dim().h9())

        # Menu_top
        self.lb_mt_nom.setText(self.titre)

        # Message
        self.lb_msg_text.setText(self.msg)

        # pb dlg
        self.pb_msg_ok.setText(self.txt_pb_ok)
        self.pb_msg_ok.setDefault(True)
    def IN_CONNECTIONS(self):
        ## Menu_top
        self.pb_mt_quitter.clicked.connect(lambda: self.close())

        # pb dlg
        self.pb_msg_ok.clicked.connect(lambda: self.close())
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