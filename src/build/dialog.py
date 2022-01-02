from PySide6 import QtCore, QtWidgets, QtGui

from ..gui import *
from ..build import *
from ..config import *
from ..In_classe import In_classe


class Dialog(dlg_ui.Ui_Dlg, QtWidgets.QDialog):
    sgn_rep = QtCore.Signal(bool)
    sgn_txt = QtCore.Signal(str)

    def __init__(self, **kwargs):
        super(Dialog, self).__init__()

        self.kwargs = kwargs

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

        self.txt_pb_annuler = self.kwargs.get("txt_pb_annuler")
        if self.txt_pb_annuler is None:
            self.txt_pb_annuler = "Annuler"


        self.width = self.kwargs.get("w")
        if self.width is None: self.width = config.widht / 2

        self.height = self.kwargs.get("h")
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
    def IN_CLASSE(self):  # sourcery skip: extract-duplicate-method
        # QScrollBoxArea
        try: pass
        except: pass
        finally: pass

        # QLineEdit | QTextEdit | QPlainTextEdit
        try:
            C_txt().tr(self.le_input)
        except: pass
        finally: pass

        In_classe(ui=self)

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
            C_fr().menu_bottom_dlg(self.fr_pg_dlg_rep)
            C_fr().menu_bottom_dlg(self.fr_pg_dlg_input)
        except: pass
        finally: pass

        # QLabel
        try:
            C_lb().p(self.lb_msg_texte)
            C_lb().p(self.lb_rep_texte)
            C_lb().p(self.lb_input_texte)
        except: pass
        finally: pass

        # QListWidget
        try: pass
        except: pass
        finally: pass

        # QPushButton
        try:
            C_pb().ok(self.pb_dlg_msg_ok)
            C_pb().ok(self.pb_dlg_rep_ok)
            C_pb().annuler(self.pb_dlg_rep_annuler)
            C_pb().ok(self.pb_dlg_input_ok)
            C_pb().annuler(self.pb_dlg_input_annuler)
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
        self.pb_dlg_msg_ok.clicked.connect(self.OK)
    def REP(self):
        self.stk_dlg.setCurrentWidget(self.pg_dlg_rep)

        if self.ico == P_img().main():
            self.lb_mt_ico.setPixmap(QtGui.QPixmap(f"{self.ico}th3.svg"))
            self.lb_mt_ico.setScaledContents(True)

        # Données
        self.lb_rep_texte.setText(self.msg)
        self.pb_dlg_rep_ok.setText(self.txt_pb_ok)
        self.pb_dlg_rep_annuler.setText(self.txt_pb_annuler)

        # Connection
        self.pb_dlg_rep_ok.clicked.connect(self.REP_OK)
        self.pb_dlg_rep_annuler.clicked.connect(self.OK)
    def INPUT(self):
        self.stk_dlg.setCurrentWidget(self.pg_dlg_input)

        if self.ico == P_img().main():
            self.lb_mt_ico.setPixmap(QtGui.QPixmap(f"{self.ico}th3.svg"))
            self.lb_mt_ico.setScaledContents(True)

        # Données
        self.lb_input_texte.setText(self.msg)
        self.pb_dlg_input_ok.setText(self.txt_pb_ok)
        self.pb_dlg_input_annuler.setText(self.txt_pb_annuler)

        # Connection
        self.pb_dlg_input_ok.clicked.connect(self.INPUT_OK)
        self.pb_dlg_input_annuler.clicked.connect(self.OK)


    ### FONCTIONS
    def OK(self): self.close()
    def REP_OK(self):
        self.sgn_rep.emit(True)
        self.close()
    def INPUT_OK(self):
        self.sgn_txt.emit(self.le_input.text())
        self.close()


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
