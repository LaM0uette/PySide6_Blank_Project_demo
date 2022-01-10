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

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.dlg = None
        self.sizegrip = QtWidgets.QSizeGrip(self)
        self.win_state = QtCore.Qt.WindowNoState

        self.setupUi(self)
        self.INIT()


    ### INITIALISATION
    def IN_BASE(self):
        # Fenetre
        self.setWindowTitle(config.nom)
        self.setWindowOpacity(config.opacity)
        self._resize()
    def IN_CLASSE(self):
        def COMBO_BOX():
            Combo_box.base(self.cb_demo_th).th()
            Combo_box.base(self.cb_demo_tr).tr()


        def _func_try():
            try: COMBO_BOX()
            except: print("COMBO_BOX ne fonctionne pas !")
        _func_try()





        # QLineEdit | QTextEdit | QPlainTextEdit
        with C_txt() as cls:
            # Demo
            cls.demoth(self.le_demo_th)
            cls.demotr(self.le_demo_tr)
            cls.demo_th(self.te_demo_th, self.pte_demo_th)
            cls.demo_tr(self.te_demo_tr, self.pte_demo_tr)

        # QScrollBoxArea
        with C_sca() as cls:
            # Demo
            cls.demo(self.sca_main)


        In_classe(ui=self)




        # QDateEdit
        with C_de() as cls:
            # Demo
            cls.demo_th(self.de_demo_th)
            cls.demo_tr(self.de_demo_tr)

        # QFrame
        with C_fr() as cls:
            # Demo
            cls.demo(self.fr_cb, self.fr_de, self.fr_lw, self.fr_pb, self.fr_ck,
                    self.fr_rb, self.fr_pg, self.fr_sb, self.fr_tw, self.fr_le,
                    self.fr_te, self.fr_pte, self.fr_tb, self.fr_trw, self.fr_sd)
            cls.demo_tb(self.fr_tb_demo, self.fr_tb_demo_2)

        # QLabel
        with C_lb() as cls:
            # Version
            cls.mb(self.lb_mb_version)

            # Demo
            cls.demo(self.lb_cb_demo, self.lb_de_demo, self.lb_lw_demo, self.lb_pb_demo, self.lb_ck_demo,
                    self.lb_rb_demo, self.lb_pg_demo, self.lb_sb_demo, self.lb_tw_demo, self.lb_le_demo,
                    self.lb_te_demo, self.lb_pte_demo, self.lb_tb_demo, self.lb_trw_demo, self.lb_sd_demo)

        # QListWidget
        with C_lw() as cls:
            # Demo
            cls.demo(self.lw_demo)

        # QPushButton
        with C_pb() as cls:
            # Menu_top
            cls.option(self.pb_mt_option)
            cls.reduire(self.pb_mt_reduire)
            cls.agrandir(self.pb_mt_agrandir)

            # Demo
            cls.demo_txt(self.pb_demo_txt)
            cls.demo_txt_inv(self.pb_demo_txt_inv)
            cls.demo_th(self.pb_demo_th)
            cls.demo_tr(self.pb_demo_tr)
            cls.demo_ck(self.pb_demo_ck)
            cls.demo_ck_ico(self.pb_demo_ck_ico, self.pb_demo_ico_ck)
            cls.demo_zoom(self.pb_demo_zoom)
            cls.demo_rd(self.pb_demo_rd)
            cls.demo_bd(self.pb_demo_bd)

        # QCheckBox
        with C_ck() as cls:
            # Demo
            cls.demo_th(self.ck_demo_th_1, self.ck_demo_th_2, self.ck_demo_th_3)
            cls.demo_tr(self.ck_demo_tr_1, self.ck_demo_tr_2, self.ck_demo_tr_3)

        # QRadioButton
        with C_rb() as cls:
            # Demo
            cls.demo_th(self.rb_demo_th_1, self.rb_demo_th_2, self.rb_demo_th_3)
            cls.demo_tr(self.rb_demo_tr_1, self.rb_demo_tr_2, self.rb_demo_tr_3)

        # QProgressBar
        with C_pg() as cls:
            # Demo
            cls.demo(self.pg_demo)

        # QSlider
        with C_sd() as cls:
            # Demo
            cls.demo_h(self.hsd_demo)
            cls.demo_v(self.vsd_demo)

        # QSpinBox | QDoubleSpinBox
        with C_sb() as cls:
            # Demo
            cls.demo_th(self.sb_demo)
            cls.demo_th_2(self.sb_demo_2)
            cls.demo_th_3(self.sb_demo_3)
            cls.demo_tr(self.dsb_demo)

        # QTableWidget
        with C_tw() as cls:
            # Demo
            cls.demo(self.tw_demo)

        # QToolBox
        with C_tb() as cls:
            # Demo
            cls.demo(self.tb_demo)

        # QTreeWidget
        with C_trw() as cls:
            cls.demo_th(self.trw_demo_th)
            cls.demo_tr(self.trw_demo_tr)


        # Demo
        for i in range(60): self.lw_demo.addItem(f"je suis l'item : {i}")
    def IN_WG(self):
        # Base
        self.setCursor(Fct(cur=P_cur().souris()).CUR())

        # Icone de l'app
        dim = P_dim().carr().h9()
        Fct(wg=self.lb_mt_ico, w=dim.get("w"), h=dim.get("h")).DIM()
        self.lb_mt_ico.setPixmap(QtGui.QPixmap(ICO_MAIN))
        self.lb_mt_ico.setScaledContents(True)
        self.lb_mt_nom.setText(config.nom)

        # Widget blanc pour centrer le nom de l'app
        dim = P_dim().w_rect_1_4().h10()
        Fct(wg=self.wg_mt_blank, w=dim.get("w") * 4, h=dim.get("h")).DIM()

        # Version de l'app
        self.lb_mb_version.setText(f" Version : {config.version}")

        # SizeGrip
        if config.resize:
            self.sizegrip.setCursor(Fct(cur=P_cur().fleche_nwse()).CUR())
            self.sizegrip.setStyleSheet("QSizeGrip {"
                                        f"image: url({P_img().resize()}th3.svg);"
                                        f"width: {P_dim().h10()}px;"
                                        f"height: {P_dim().h10()}px;"
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


    ### _ACTIONS
    def _reload(self):
        importlib.reload(config)
        importlib.reload(rld)

        self.IN_BASE()
        self.IN_CLASSE()


    ### FONCTIONS
    def FCT_OPTION(self):
        t = Dlg().OPTION()
        if t: self._reload()
        # col = Dlg().COLORS()
        # print(col)


    ### EVENT
    def _resize(self):
        if config.resize:
            self.setMinimumWidth(config.widht)
            self.setMinimumHeight(config.height)
        else:
            self.setFixedWidth(config.widht)
            self.setFixedHeight(config.height)
    def _centre_fen(self):
        center = QtGui.QScreen.availableGeometry(QtWidgets.QApplication.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        self.move(geo.topLeft())

    def EVT_AGRANDIR_GDT(self):
        if self.windowState() == QtCore.Qt.WindowMaximized:
            self.win_state = QtCore.Qt.WindowNoState
            self._centre_fen()
            self._resize()
        else:
            self.win_state = QtCore.Qt.WindowMaximized

        self.setWindowState(self.win_state)
    def EVT_REDUIRE_GDT(self):
        self.setWindowState(QtCore.Qt.WindowMinimized)
    def EVT_REDUIRE_HIDE_GDT(self):
        if config.auto_close: return self.EVT_QUITTER()
        self.hide()
        self._centre_fen()
    def EVT_QUITTER(self):
        rep = Dlg().QUITTER()

        if rep:
            app.quit()
            quit()

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

        if event.buttons() == QtCore.Qt.LeftButton and height_verif < P_dim().h9() and self.windowState() != QtCore.Qt.WindowMaximized and cur.pos().y() <= 0:
            self.setCursor(Fct(cur=P_cur().agrandir()).CUR())
        else:
            self.setCursor(Fct(cur=P_cur().souris()).CUR())

        try:
            if event.buttons() == QtCore.Qt.LeftButton and height_verif < P_dim().h9() and self.windowState() != QtCore.Qt.WindowMaximized:
                act_move(event)
            if event.buttons() == QtCore.Qt.LeftButton and height_verif < P_dim().h9() and self.windowState() == QtCore.Qt.WindowMaximized:
                self.setWindowState(QtCore.Qt.WindowNoState)
                self.win_state = QtCore.Qt.WindowNoState
                act_move(event)
        except AttributeError: pass
    def mouseReleaseEvent(self, event):
        cur = QtGui.QCursor()
        height_verif = cur.pos().y() - self.pos().y()
        if height_verif < P_dim().h9() and self.windowState() != QtCore.Qt.WindowMaximized and cur.pos().y() <= 0:
            self.setCursor(Fct(cur=P_cur().souris()).CUR())
            self.EVT_AGRANDIR_GDT()
            event.accept()
    def closeEvent(self, event):
        event.accept()
        app.quit()
    def showEvent(self, event):
        if self.win_state == QtCore.Qt.WindowMaximized:
            self.setWindowState(self.win_state)
        else:
            self.setWindowState(self.win_state)
            self._resize()


ICO_MAIN = P_img().main() + "th3" + ".svg"
app = QtWidgets.QApplication(sys.argv)
splash = QtWidgets.QSplashScreen(QtGui.QPixmap(ICO_MAIN).scaledToHeight(500), QtCore.Qt.WindowStaysOnTopHint)
splash.show()
app.processEvents()

fen = main()
splash.finish(fen)
fen.show()

sys.exit(app.exec())
