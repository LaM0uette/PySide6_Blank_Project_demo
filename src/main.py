import sys

from PySide6 import QtCore, QtWidgets, QtGui

from .gui import *
from .build import *
from .config import *
from .In_classe import In_classe



class main(main_ui.Ui_main, QtWidgets.QWidget):
    dragPos: QtCore.QPoint
    def __init__(self):
        super(main, self).__init__()

        self.dlg = None
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.sizegrip = QtWidgets.QSizeGrip(self)

        self.setupUi(self)
        self.INIT()


    ### INITIALISATION
    def IN_BASE(self):
        ## Fenetre
        self.setWindowTitle(config.nom)
        self.setWindowOpacity(config.opacity)

        if config.resize:
            self.setMinimumWidth(config.widht)
            self.setMinimumHeight(config.height)
        else:
            self.setFixedWidth(config.widht)
            self.setFixedHeight(config.height)
    def IN_CLASSE(self):  # sourcery skip: extract-method
        # QLineEdit | QTextEdit | QPlainTextEdit
        try:
            # Demo
            C_txt().demoth(self.le_demo_th)
            C_txt().demotr(self.le_demo_tr)
            C_txt().demo_th(self.te_demo_th, self.pte_demo_th)
            C_txt().demo_tr(self.te_demo_tr, self.pte_demo_tr)
        except: pass
        finally: pass

        # QScrollBoxArea
        try:
            # Demo
            C_sca().demo(self.sca_main)
        except: pass
        finally: pass

        In_classe(ui=self)

        # QComboBox
        try:
            # Demo
            C_cb().demo_th(self.cb_demo_th)
            C_cb().demo_tr(self.cb_demo_tr)
        except: pass
        finally: pass

        # QDateEdit
        try:
            # Demo
            C_de().demo_th(self.de_demo_th)
            C_de().demo_tr(self.de_demo_tr)
        except: pass
        finally: pass

        # QFrame
        try:
            # Demo
            C_fr().demo(self.fr_cb, self.fr_de, self.fr_lw, self.fr_pb, self.fr_ck,
                        self.fr_rb, self.fr_pg, self.fr_sb, self.fr_tw, self.fr_le,
                        self.fr_te, self.fr_pte)
            C_fr().demo_tb(self.fr_tb_demo, self.fr_tb_demo_2)
        except: pass
        finally: pass

        # QLabel
        try:
            # Version
            C_lb().mb(self.lb_mb_version)

            # Demo
            C_lb().demo(self.lb_cb_demo, self.lb_de_demo, self.lb_lw_demo, self.lb_pb_demo, self.lb_ck_demo,
                        self.lb_rb_demo, self.lb_pg_demo, self.lb_sb_demo, self.lb_tw_demo, self.lb_le_demo,
                        self.lb_te_demo, self.lb_pte_demo)
        except: pass
        finally: pass

        # QListWidget
        try:
            # Demo
            C_lw().demo(self.lw_demo)
        except: pass
        finally: pass

        # QPushButton
        try:
            # Menu_top
            C_pb().option(self.pb_mt_option)
            C_pb().reduire(self.pb_mt_reduire)
            C_pb().agrandir(self.pb_mt_agrandir)

            # Demo
            C_pb().demo_txt(self.pb_demo_txt)
            C_pb().demo_txt_inv(self.pb_demo_txt_inv)
            C_pb().demo_th(self.pb_demo_th)
            C_pb().demo_tr(self.pb_demo_tr)
            C_pb().demo_ck(self.pb_demo_ck)
            C_pb().demo_ck_ico(self.pb_demo_ck_ico, self.pb_demo_ico_ck)
            C_pb().demo_zoom(self.pb_demo_zoom)
            C_pb().demo_rd(self.pb_demo_rd)
            C_pb().demo_bd(self.pb_demo_bd)
        except: pass
        finally: pass

        # QCheckBox
        try:
            # Demo
            C_ck().demo_th(self.ck_demo_th_1, self.ck_demo_th_2, self.ck_demo_th_3)
            C_ck().demo_tr(self.ck_demo_tr_1, self.ck_demo_tr_2, self.ck_demo_tr_3)
        except: pass
        finally: pass

        # QRadioButton
        try:
            # Demo
            C_rb().demo_th(self.rb_demo_th_1, self.rb_demo_th_2, self.rb_demo_th_3)
            C_rb().demo_tr(self.rb_demo_tr_1, self.rb_demo_tr_2, self.rb_demo_tr_3)
        except: pass
        finally: pass

        # QProgressBar
        try:
            # Demo
            C_pg().demo(self.pg_demo)
        except: pass
        finally: pass

        # QSpinBox | QDoubleSpinBox
        try:
            # Demo
            C_sb().demo_th(self.sb_demo)
            C_sb().demo_th_2(self.sb_demo_2)
            C_sb().demo_th_3(self.sb_demo_3)
            C_sb().demo_tr(self.dsb_demo)
        except: pass
        finally: pass

        # QTableWidget
        try:
            # Demo
            C_tw().demo(self.tw_demo)
        except: pass
        finally: pass

        # QToolBox
        try:
            # Demo
            C_tb().demo(self.tb_demo)
        except: pass
        finally: pass


        # Demo
        for i in range(60): self.lw_demo.addItem(f"je suis l'item : {i}")
    def IN_WG(self):
        # Base
        self.setCursor(Fct(cur="souris").CUR())

        # Icone de l'app
        dim = P_dim().p_c_mt()
        Fct(wg=self.lb_mt_ico, w=dim.get("w"), h=dim.get("h")).DIM()
        self.lb_mt_ico.setPixmap(QtGui.QPixmap(PXM))
        self.lb_mt_ico.setScaledContents(True)
        self.lb_mt_nom.setText(config.nom)

        # Widget blanc pour centrer le nom de l'app
        dim = P_dim().p_r_mb()
        Fct(wg=self.wg_mt_blank, w=dim.get("w") * 4, h=dim.get("h")).DIM()

        # Version de l'app
        self.lb_mb_version.setText(f" Version : {config.version}")

        # SizeGrip
        if config.resize:
            self.sizegrip.setCursor(Fct(cur="fleche_nwse").CUR())
            self.sizegrip.setStyleSheet("QSizeGrip {"
                                   f"image: url({P_img().resize()}th3.svg);"
                                   f"width: {P_dim().h_mb()}px;"
                                   f"height: {P_dim().h_mb()}px;"
                                   "}")
            self.hlay_menu_bottom.addWidget(self.sizegrip)
    def IN_WG_BASE(self):
        pass
    def IN_CONNECTIONS(self):
        ## Menu_top
        self.pb_mt_option.clicked.connect(lambda: self.FCT_OPTION())
        self.pb_mt_reduire.clicked.connect(lambda: self.EVT_REDUIRE_GDT())
        self.pb_mt_agrandir.clicked.connect(lambda: self.EVT_AGRANDIR_GDT())
        self.pb_mt_quitter.clicked.connect(lambda: self.EVT_REDUIRE_HIDE_GDT())
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
    ""


    ### FONCTIONS
    def FCT_OPTION(self):
        Dlg(msg="trtretdrtdrt").ALERTE()


    ### EVENT
    def EVT_CENTRE_FEN(self):
        center = QtGui.QScreen.availableGeometry(QtWidgets.QApplication.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        self.move(geo.topLeft())

        if config.resize:
            self.setMinimumWidth(config.widht)
            self.setMinimumHeight(config.height)
        else:
            self.setFixedWidth(config.widht)
            self.setFixedHeight(config.height)
    def EVT_AGRANDIR_GDT(self):
        if self.windowState() == QtCore.Qt.WindowMaximized:
            self.setWindowState(QtCore.Qt.WindowNoState)
            self.EVT_CENTRE_FEN()
            self.sizegrip.show()
        else:
            self.setWindowState(QtCore.Qt.WindowMaximized)
            self.sizegrip.hide()
    def EVT_REDUIRE_GDT(self):
        self.setWindowState(QtCore.Qt.WindowNoState)
        self.sizegrip.show()
        self.EVT_CENTRE_FEN()
        self.setWindowState(QtCore.Qt.WindowMinimized)
    def EVT_REDUIRE_HIDE_GDT(self):
        if config.auto_close: return self.EVT_QUITTER()
        self.hide()
        self.EVT_CENTRE_FEN()
    def EVT_QUITTER(self):
        rep = Dlg().QUITTER()

        if rep:
            app.quit()
            quit()
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

        if event.buttons() == QtCore.Qt.LeftButton and height_verif < P_dim().h_mt() and self.windowState() != QtCore.Qt.WindowMaximized and cur.pos().y() <= 0:
            self.setCursor(Fct(cur="agrandir").CUR())
        else:
            self.setCursor(Fct(cur="souris").CUR())

        try:
            if event.buttons() == QtCore.Qt.LeftButton and height_verif < P_dim().h_mt() and self.windowState() != QtCore.Qt.WindowMaximized:
                act_move(event)
            if event.buttons() == QtCore.Qt.LeftButton and height_verif < P_dim().h_mt() and self.windowState() == QtCore.Qt.WindowMaximized:
                self.setWindowState(QtCore.Qt.WindowNoState)
                self.sizegrip.show()
                act_move(event)
        except AttributeError:
            pass
    def mouseReleaseEvent(self, event):
        cur = QtGui.QCursor()
        height_verif = cur.pos().y() - self.pos().y()
        if height_verif < P_dim().h_mt() and self.windowState() != QtCore.Qt.WindowMaximized and cur.pos().y() <= 0:
            self.setCursor(Fct(cur="souris").CUR())
            self.EVT_AGRANDIR_GDT()
            event.accept()
    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        event.accept()
        app.quit()


PXM = P_img().main() + "th3" + ".svg"
app = QtWidgets.QApplication(sys.argv)
splash = QtWidgets.QSplashScreen(QtGui.QPixmap(PXM).scaledToHeight(500), QtCore.Qt.WindowStaysOnTopHint)
splash.show()
app.processEvents()

fen = main()
splash.finish(fen)
fen.show()

sys.exit(app.exec())
