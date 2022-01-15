from PySide6 import QtCore, QtWidgets, QtGui

from ...gui import *
from ...build import *
from ...config import *
from ...In_classe import In_classe


class Msg(dlg_ui.Ui_Dlg, QtWidgets.QDialog):
    sgn_txt = QtCore.Signal(str)

    def __init__(self, **kwargs):
        super(Msg, self).__init__()

        self.kwargs = kwargs
        self.reload = False

        self.titre = self.kwargs.get("titre")
        if self.titre is None:
            self.titre = "Information"

        self.msg = self.kwargs.get("msg")
        if self.msg is None:
            self.msg = ":)"

        self.ico = self.kwargs.get("ico")
        if self.ico is None:
            self.ico = P_img().main()

        self.txt_pb_ok = self.kwargs.get("txt_pb_ok")
        if self.txt_pb_ok is None:
            self.txt_pb_ok = "Ok"



        self.width = self.kwargs.get("width")
        if self.width is None: self.width = config.widht / 2

        self.height = self.kwargs.get("height")
        if self.height is None: self.height = config.height / 4

        self.opacity = self.kwargs.get("opacity")
        if self.opacity is None: self.opacity = 1

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setupUi(self)
        self.INIT()


    ### INITIALISATION
    def IN_BASE(self):
        ## Fenetre
        self.setWindowTitle(self.titre)
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)
        self.setWindowOpacity(self.opacity)
    def IN_CLASSE(self):
        def FRAME():
            Frame.menu_bottom_dlg(self.fr_msg_bottom).th()
            Frame.base(self.fr_main).cadre_th3()
            Frame.base(self.fr_msg_body).th()
        def LABEL():
            Label.base(self.lb_rep_text).tr()
        def PUSH_BUTTON():
            Push_button.dlg_ok(self.pb_msg_ok).txt()

        def _func_try():
            err = f"[ {self.objectName()} ] ne fonctionne pas !"

            try: FRAME()
            except: print(f"FRAME{err}")

            try: LABEL()
            except: print(f"LABEL{err}")

            try: PUSH_BUTTON()
            except: print(f"PUSH_BUTTON{err}")
        _func_try()

        In_classe(ui=self)
    def IN_WG(self):
        # Base
        self.setCursor(Fct(cur=P_cur().souris()).CUR())
        self.setStyleSheet(f"background-color: rgb{P_rgb().th1()};")

        # Frame menu_top
        self.fr_menu_top.setFixedHeight(P_dim().h9())

        # Icone de l'app
        dim = P_dim().carr().h9()
        Fct(wg=self.lb_mt_ico, w=dim.get("w"), h=dim.get("h")).DIM()
        self.lb_mt_ico.setPixmap(QtGui.QPixmap(f"{self.ico}th3.svg"))
        self.lb_mt_ico.setScaledContents(True)
        self.lb_mt_nom.setText(self.titre)
    def IN_WG_BASE(self):
        # Option
        self.pb_dlg_option_appliquer.setVisible(False)
        self.stk_option.setCurrentWidget(self.pg_opt_menu)
    def IN_CONNECTIONS(self):
        ## Menu_top
        self.pb_mt_quitter.clicked.connect(lambda: self.close())
    def IN_ACT(self):
        pass
    def INIT(self):
        self.IN_BASE()
        self.IN_CLASSE()
        self.IN_WG()
        self.IN_WG_BASE()
        self.IN_CONNECTIONS()
        self.IN_ACT()


    ### _ACTIONS
    def _set_ico(self, ico=None):
        if ico is None: ico = self.ico
        self.lb_mt_ico.setPixmap(QtGui.QPixmap(f"{ico}th3.svg"))
        self.lb_mt_ico.setScaledContents(True)
    def _close(self): self.close()


    ### FONCTIONS
    def MSG(self, ico):
        self._set_ico(ico=ico)

        # Données
        self.lb_msg_text.setText(self.msg)
        self.pb_msg_ok.setText(self.txt_pb_ok)
        self.pb_msg_ok.setDefault(True)

        # Connection
        self.pb_msg_ok.clicked.connect(self._close)


    ### EVENT
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
