from PySide6 import QtCore, QtWidgets, QtGui

from ..gui import *
from ..build import *
from ..config import *
from ..In_classe import In_classe


class Dlg(dlg_ui.Ui_Dlg, QtWidgets.QWidget):
    sgn_rep = QtCore.Signal(bool)

    def __init__(self, titre="Information", msg=":)", ico=P_img().main(), txt_pb_ok="Ok", txt_pb_annuler="Annuler", **kwargs):
        super(Dlg, self).__init__()

        self.titre = titre
        self.msg = msg
        self.ico = ico
        self.txt_pb_ok = txt_pb_ok
        self.txt_pb_annuler = txt_pb_annuler

        self.kwargs = kwargs

        self.width = self.kwargs.get("w")
        if self.width is None: self.width = config.widht / 2

        self.height = self.kwargs.get("h")
        if self.height is None: self.height = config.height / 4

        self.opacity = self.kwargs.get("opacity")
        if self.opacity is None: self.opacity = 1

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowModality(QtCore.Qt.NonModal)
        self.setupUi(self)
        self.INIT()
        self.show()


    ### INITIALISATION
    def IN_BASE(self):
        ## Fenetre
        self.setWindowTitle(self.titre)
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)
        self.setWindowOpacity(self.opacity)
    def IN_CLASSE(self):  # sourcery skip: extract-duplicate-method
        In_classe(ui=self)

        # QLineEdit | QTextEdit | QPlainTextEdit
        try: pass
        except: pass
        finally: pass

        # QComboBox
        try: pass
        except: pass
        finally: pass

        # QDateEdit
        try: pass
        except: pass
        finally: pass

        # QFrame
        try:
            C_fr().menu_bottom_dlg(self.fr_pg_dlg_msg)
        except: pass
        finally: pass

        # QLabel
        try:
            C_lb().p(self.lb_msg_texte)
        except: pass
        finally: pass

        # QListWidget
        try: pass
        except: pass
        finally: pass

        # QPushButton
        try:
            C_pb().ok(self.pb_dlg_msg_ok)
        except: pass
        finally: pass

        # QCheckBox
        try: pass
        except: pass
        finally: pass

        # QRadioButton
        try: pass
        except: pass
        finally: pass

        # QProgressBar
        try: pass
        except: pass
        finally: pass

        # QScrollBoxArea
        try: pass
        except: pass
        finally: pass

        # QSpinBox | QDoubleSpinBox
        try: pass
        except: pass
        finally: pass

        # QTableWidget
        try: pass
        except: pass
        finally: pass

        # QToolBox
        try: pass
        except: pass
        finally: pass
    def IN_WG(self):
        # Base
        self.setCursor(Fct(cur="souris").CUR())
        self.setStyleSheet(f"background-color: rgb{P_rgb().th1()};")

        # Frame menu_top
        self.fr_menu_top.setFixedHeight(P_dim().h_mt())

        # Icone de l'app
        dim = P_dim().p_c_mt()
        Fct(wg=self.lb_mt_ico, w=dim.get("w"), h=dim.get("h")).DIM()
        self.lb_mt_ico.setPixmap(QtGui.QPixmap(f"{self.ico}th3.svg"))
        self.lb_mt_ico.setScaledContents(True)
        self.lb_mt_nom.setText(self.titre)
    def IN_WG_BASE(self):
        pass
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


    ### ACTIONS
    def MSG(self, ico):
        self.stk_dlg.setCurrentWidget(self.pg_dlg_msg)

        if self.ico == P_img().main():
            self.lb_mt_ico.setPixmap(QtGui.QPixmap(f"{ico}th3.svg"))
            self.lb_mt_ico.setScaledContents(True)

        # Données
        self.lb_msg_texte.setText(self.msg)
        self.pb_dlg_msg_ok.setText(self.txt_pb_ok)

        # Connection
        self.pb_dlg_msg_ok.clicked.connect(self.MSG_OK)
    def INFO(self): self.MSG(ico=P_img().info())
    def ALERTE(self): self.MSG(ico=P_img().alerte())


    ### FONCTIONS
    def MSG_OK(self): self.destroy()


    ### EVENT
    def mousePressEvent(self, event):
        cur = QtGui.QCursor()
        verifHeight = cur.pos().y() - self.pos().y()
        if event.buttons() == QtCore.Qt.LeftButton and verifHeight < P_dim().h_mt() and self.windowState() != QtCore.Qt.WindowMaximized:
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
            if event.buttons() == QtCore.Qt.LeftButton and height_verif < P_dim().h_mt() and self.windowState() != QtCore.Qt.WindowMaximized:
                act_move(event)
            if event.buttons() == QtCore.Qt.LeftButton and height_verif < P_dim().h_mt() and self.windowState() == QtCore.Qt.WindowMaximized:
                self.setWindowState(QtCore.Qt.WindowNoState)
                act_move(event)
        except AttributeError: pass
