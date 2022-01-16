from PySide6 import QtCore, QtWidgets, QtGui

from ... import msg_ui
from .....build import *
from .....In_classe import In_classe


class Dlg_msg(msg_ui.Ui_Msg, QtWidgets.QDialog):
    dragPos: QtCore.QPoint

    def __init__(self,
                 titre,
                 msg,
                 ico,
                 txt_pb_ok,
                 width,
                 height,
                 opacity,
    ):
        super(Dlg_msg, self).__init__()

        self.titre = titre
        self.msg = msg
        self.ico = ico
        self.txt_pb_ok = txt_pb_ok
        self.width = width
        self.height = height
        self.opacity = opacity

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
            Frame.base(self.fr_main).cadre_th3()
            Frame.menu_bottom_dlg(self.fr_msg_bottom).th()
        def LABEL():
            Label.base(self.lb_msg_text).tr()
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


        # Menu_top
        dim = P_dim().carr().h9()
        Fct(wg=self.lb_mt_ico, w=dim.get("w"), h=dim.get("h")).DIM()
        self.lb_mt_ico.setPixmap(QtGui.QPixmap(f"{self.ico}th3.svg"))
        self.lb_mt_ico.setScaledContents(True)
        self.lb_mt_nom.setText(self.titre)
        self.lb_mt_ico.setPixmap(QtGui.QPixmap(f"{self.ico}th3.svg"))
        self.lb_mt_ico.setScaledContents(True)


        # Message
        self.lb_msg_text.setText(self.msg)


        # pb ok
        self.pb_msg_ok.setText(self.txt_pb_ok)
        self.pb_msg_ok.setDefault(True)
    def IN_WG_BASE(self):
        pass
    def IN_CONNECTIONS(self):
        ## Menu_top
        self.pb_mt_quitter.clicked.connect(lambda: self.close())

        # pb ok
        self.pb_msg_ok.clicked.connect(lambda: self.close())
    def IN_ACT(self):
        pass
    def INIT(self):
        self.IN_BASE()
        self.IN_CLASSE()
        self.IN_WG()
        self.IN_WG_BASE()
        self.IN_CONNECTIONS()
        self.IN_ACT()


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
