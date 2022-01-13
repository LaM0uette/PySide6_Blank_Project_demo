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
        def CHECK_BOX():
            Check_box.base(self.ck_demo_th_1, self.ck_demo_th_2, self.ck_demo_th_3).th()
            Check_box.base(self.ck_demo_tr_1, self.ck_demo_tr_2, self.ck_demo_tr_3).tr()
        def DATE_EDIT():
            Date_edit.base(self.de_demo_th).th()
            Date_edit.base(self.de_demo_tr).tr()
        def FRAME():
            Frame.base(self.fr_cb, self.fr_de, self.fr_lw, self.fr_pb, self.fr_ck,
                       self.fr_rb, self.fr_pg, self.fr_sb, self.fr_tw, self.fr_le,
                       self.fr_te, self.fr_pte, self.fr_tb, self.fr_trw, self.fr_sd,
                       self.fr_demo_cadre, self.fr_fr, self.fr_lb).cadre_bn1()
            Frame.base(self.fr_body, self.fr_tb_demo, self.fr_tb_demo_2).tr()
            Frame.base(self.fr_demo_th).th()
            Frame.menu_bottom(self.fr_menu_bottom).th()
        def LABEL():
            Label.base(self.lb_mb_version).tr()
            Label.base(self.lb_lb_demo_th).th()
            Label.base(self.lb_lb_demo_tr).tr()
            Label.h1(self.lb_cb_demo, self.lb_de_demo, self.lb_lw_demo, self.lb_pb_demo, self.lb_ck_demo,
                     self.lb_rb_demo, self.lb_pg_demo, self.lb_sb_demo, self.lb_tw_demo, self.lb_le_demo,
                     self.lb_te_demo, self.lb_pte_demo, self.lb_tb_demo, self.lb_trw_demo, self.lb_sd_demo,
                     self.lb_fr_demo, self.lb_lb_demo).bottom_bn1()
        def LIST_WIDGET():
            List_widget.base(self.lw_demo_th).th()
            List_widget.base(self.lw_demo_tr).tr()
        def PROGRESS_BAR():
            Progress_bar.base(self.pg_demo_th).th()
            Progress_bar.base(self.pg_demo_tr).tr()
        def PUSH_BUTTON():
            Push_button.menu_top(self.pb_mt_option).option()
            Push_button.menu_top(self.pb_mt_reduire).reduire()
            Push_button.menu_top(self.pb_mt_agrandir).agrandir()

            Push_button.base_txt(self.pb_demo_txt).txt()
            Push_button.base_txt(self.pb_demo_txt_inv).txt_inv()

            Push_button.base(self.pb_demo_th, self.pb_demo_ck).th()
            Push_button.base(self.pb_demo_tr).tr()
            Push_button.base(self.pb_demo_rd).demo_rd()
            Push_button.base(self.pb_demo_bd).demo_bd()

            Push_button.ck_ico(self.pb_demo_ck_ico, self.pb_demo_ico_ck).tr()

            Push_button.zoom(self.pb_demo_zoom).zoom_calendrier()
        def RADIO_BUTTON():
            Radio_button.base(self.rb_demo_th_1, self.rb_demo_th_2, self.rb_demo_th_3).th()
            Radio_button.base(self.rb_demo_tr_1, self.rb_demo_tr_2, self.rb_demo_tr_3).tr()
        def SCROLL_BOX_AREA():
            Scroll_box_area.base(self.sca_main).th()
        def SPIN_BOX():
            Spin_box.plus_minus(self.sb_demo).th()
            Spin_box.up_down(self.sb_demo_2).th()
            Spin_box.plus_minus(self.sb_demo_3).th_lr()
            Spin_box.base(self.dsb_demo).tr()


        def _func_try():
            err = f"[ {self.objectName()} ] ne fonctionne pas !"

            try: COMBO_BOX()
            except: print(f"COMBO_BOX{err}")

            try: CHECK_BOX()
            except: print(f"CHECK_BOX{err}")

            try: DATE_EDIT()
            except: print(f"DATE_EDIT{err}")

            try: FRAME()
            except: print(f"FRAME{err}")

            try: LABEL()
            except: print(f"LABEL{err}")

            try: LIST_WIDGET()
            except: print(f"LIST_WIDGET{err}")

            try: PROGRESS_BAR()
            except: print(f"PROGRESS_BAR{err}")

            try: PUSH_BUTTON()
            except: print(f"PUSH_BUTTON{err}")

            try: RADIO_BUTTON()
            except: print(f"RADIO_BUTTON{err}")

            try: SCROLL_BOX_AREA()
            except: print(f"SCROLL_BOX_AREA{err}")

            try: SPIN_BOX()
            except: print(f"SPIN_BOX{err}")
        _func_try()








        # QLineEdit | QTextEdit | QPlainTextEdit
        with C_txt() as cls:
            # Demo
            cls.demoth(self.le_demo_th)
            cls.demotr(self.le_demo_tr)
            cls.demo_th(self.te_demo_th, self.pte_demo_th)
            cls.demo_tr(self.te_demo_tr, self.pte_demo_tr)


        In_classe(ui=self)

        # QSlider
        with C_sd() as cls:
            # Demo
            cls.demo_h(self.hsd_demo)
            cls.demo_v(self.vsd_demo)

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
        for i in range(60):
            self.lw_demo_th.addItem(f"je suis l'item : {i}")
            self.lw_demo_tr.addItem(f"je suis l'item : {i}")
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
