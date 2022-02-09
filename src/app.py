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

        self.sizegrip = QtWidgets.QSizeGrip(self)
        self.win_state = QtCore.Qt.WindowNoState

        self.setupUi(self)
        self.INIT()


    ############################
    ##     INITIALISATION     ##
    ############################
    def IN_BASE(self):
        # Fenetre
        self.setWindowTitle(config.nom)
        self.setWindowOpacity(config.opacity)
        self._resize()
    def IN_CLASSE(self):
        ### QCheckBox ###
        Check_box.Base_th(self.ck_demo_th_1, self.ck_demo_th_2, self.ck_demo_th_3)
        Check_box.Base_tr(self.ck_demo_tr_1, self.ck_demo_tr_2, self.ck_demo_tr_3)
        ### /QCheckBox ###


        ### QComboBox ###
        Combo_box.Base_th(self.cb_demo_th)
        Combo_box.Base_tr(self.cb_demo_tr)
        ### /QComboBox ###


        ### QDateEdit ###
        Date_edit.Base_th(self.de_demo_th)
        Date_edit.Base_tr(self.de_demo_tr)
        ### /QDateEdit ###


        ### QFrame ###
        Frame.Base_th(self.fr_demo_th, self.fr_tb_demo_th_1, self.fr_tb_demo_th_2)
        Frame.Base_tr(self.fr_tb_demo_tr_1, self.fr_tb_demo_tr_2)
        Frame.Base_th(self.fr_body)
        Frame.Cadre_bn1(self.fr_cb, self.fr_de, self.fr_lw, self.fr_pb, self.fr_ck,
                        self.fr_rb, self.fr_pg, self.fr_sb, self.fr_tw, self.fr_le,
                        self.fr_te, self.fr_pte, self.fr_tb, self.fr_trw, self.fr_sd,
                        self.fr_demo_cadre, self.fr_fr, self.fr_lb)
        Frame.Menu_bottom(self.fr_menu_bottom)
        ### /QFrame ###


        ### QLabel ###
        Label.Base_th(self.lb_lb_demo_th)
        Label.Base_tr(self.lb_mb_version, self.lb_lb_demo_tr)
        Label.DemoCat(self.lb_cb_demo, self.lb_de_demo, self.lb_lw_demo, self.lb_pb_demo, self.lb_ck_demo,
                      self.lb_rb_demo, self.lb_pg_demo, self.lb_sb_demo, self.lb_tw_demo, self.lb_le_demo,
                      self.lb_te_demo, self.lb_pte_demo, self.lb_tb_demo, self.lb_trw_demo, self.lb_sd_demo,
                      self.lb_fr_demo, self.lb_lb_demo)
        ### /QLabel ###


        ### QListWidget ###
        List_widget.Demo_th(self.lw_demo_th)
        List_widget.Demo_tr(self.lw_demo_tr)
        ### /QListWidget ###


        ### QListWidget ###
        Progress_bar.Base_th(self.pg_demo_th)
        Progress_bar.Base_tr(self.pg_demo_tr)
        ### /QListWidget ###


        ### QPushButton ###
        ### /QPushButton ###


        ### QRadioButton ###
        Radio_button.Base_th(self.rb_demo_th_1, self.rb_demo_th_2, self.rb_demo_th_3)
        Radio_button.Base_tr(self.rb_demo_tr_1, self.rb_demo_tr_2, self.rb_demo_tr_3)
        ### /QRadioButton ###


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
        def SCROLL_BOX_AREA():
            Scroll_box_area.base(self.sca_main).th()
        def SLIDER():
            Slider.base(self.hsd_demo).th()
            Slider.base(self.vsd_demo).rond()
        def SPIN_BOX():
            Spin_box.plus_minus(self.sb_demo).th()
            Spin_box.up_down(self.sb_demo_2).th()
            Spin_box.plus_minus(self.sb_demo_3).th_lr()
            Spin_box.base(self.dsb_demo).tr()
        def TABLE_WIDGET():
            Table_widget.base(self.tw_demo_th).th()
            Table_widget.base(self.tw_demo_tr).tr()
        def TEXT_EDIT():
            Text_edit.base(self.le_demo_th).th()
            Text_edit.base(self.le_demo_tr).bottom_tr2()
            Text_edit.base_bloc(self.te_demo_th, self.pte_demo_th).th()
            Text_edit.base_bloc(self.te_demo_tr, self.pte_demo_tr).tr()
        def TOOL_BOX():
            Tool_box.base(self.tb_demo_th).th()
            Tool_box.base(self.tb_demo_tr).tr()
        def TREE_WIDGET():
            Tree_widget.base(self.trw_demo_th).th()
            Tree_widget.base(self.trw_demo_tr).tr()

        # Lancement des fonctions de MEF
        def _func_try():
            err = f"[ {self.objectName()} ] ne fonctionne pas !"

            try: PUSH_BUTTON()
            except: print(f"PUSH_BUTTON{err}")

            try: SCROLL_BOX_AREA()
            except: print(f"SCROLL_BOX_AREA{err}")

            try: SLIDER()
            except: print(f"SLIDER{err}")

            try: SPIN_BOX()
            except: print(f"SPIN_BOX{err}")

            try: TABLE_WIDGET()
            except: print(f"TABLE_WIDGET{err}")

            try: TEXT_EDIT()
            except: print(f"TEXT_EDIT{err}")

            try: TOOL_BOX()
            except: print(f"TOOL_BOX{err}")

            try: TREE_WIDGET()
            except: print(f"TREE_WIDGET{err}")
        _func_try()

        # Lancement des fonctions de MEF global
        In_classe(ui=self)
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


        # Demo lw
        for i in range(60):
            self.lw_demo_th.addItem(f"je suis l'item : {i}")
            self.lw_demo_tr.addItem(f"je suis l'item : {i}")
    def IN_CONNECTIONS(self):
        ## Menu_top
        self.pb_mt_option.clicked.connect(lambda: Option(fen=fen).MAIN())
        self.pb_mt_reduire.clicked.connect(lambda: self.reduire())
        self.pb_mt_agrandir.clicked.connect(lambda: self.agrandir())
        self.pb_mt_quitter.clicked.connect(lambda: self.cacher())
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


    #####################
    ##     ACTIONS     ##
    #####################

    #####################
    ##    /ACTIONS     ##
    #####################


    #######################
    ##     FONCTIONS     ##
    #######################

    #######################
    ##    /FONCTIONS     ##
    #######################


    ###################
    ##     EVENT     ##
    ###################
    # fenetre
    def _resize(self):
        if config.resize:
            self.setMinimumWidth(config.widht)
            self.setMinimumHeight(config.height)
        else:
            self.setFixedWidth(config.widht)
            self.setFixedHeight(config.height)
    def _centreFen(self):
        center = QtGui.QScreen.availableGeometry(QtWidgets.QApplication.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        self.move(geo.topLeft())
    # intéraction des boutons
    def agrandir(self):
        if self.windowState() == QtCore.Qt.WindowMaximized:
            self.win_state = QtCore.Qt.WindowNoState
            self._centreFen()
            self._resize()
        else:
            self.win_state = QtCore.Qt.WindowMaximized

        self.setWindowState(self.win_state)
    def reduire(self):
        self.setWindowState(QtCore.Qt.WindowMinimized)
    def cacher(self):
        if config.auto_close: return self.quitter()
        self.hide()
        self._centreFen()
    def quitter(self):
        rep = Rep().QUITTER()

        if rep:
            app.quit()
            quit()
    # event
    def mousePressEvent(self, event):
        cur = QtGui.QCursor()
        verifHeight = cur.pos().y() - self.pos().y()
        if event.buttons() == QtCore.Qt.LeftButton and verifHeight < P_dim().h9() and self.windowState() != QtCore.Qt.WindowMaximized:
            self.dragPos = event.globalPosition().toPoint()
            event.accept()
    def mouseDoubleClickEvent(self, event):
        cur = QtGui.QCursor()
        height_verif = cur.pos().y() - self.pos().y()
        if height_verif < P_dim().h9():
            self.agrandir()
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
            self.agrandir()
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
    ###################
    ##    /EVENT     ##
    ###################


ICO_MAIN = f"{P_img().main()}th3.svg"
app = QtWidgets.QApplication(sys.argv)
splash = QtWidgets.QSplashScreen(QtGui.QPixmap(ICO_MAIN).scaledToHeight(500), QtCore.Qt.WindowStaysOnTopHint)
splash.show()
app.processEvents()

fen = main()
splash.finish(fen)
fen.show()

sys.exit(app.exec())
