import sys
import time

from PySide6 import QtCore, QtWidgets, QtGui

from src import *
from src.gui import *


class main(Ui_main, QtWidgets.QWidget):
    dragPos: QtCore.QPoint

    def __init__(self):
        super(main, self).__init__()

        ### AJOUTS DE BASE ###
            # size_grip
        self.size_grip = QtWidgets.QSizeGrip(self)
            # tray
        self.tray = QtWidgets.QSystemTrayIcon(QtGui.QPixmap(f"{Img().main()}th3.svg"), self)
        self.tray.activated.connect(self.trayActivate)
        self.timer_double_click = QtCore.QTimer(self)
        self.timer_double_click.setSingleShot(True)
        self.timer_double_click.timeout.connect(self.traySingleClick)
            # tray_menu
        self.tray_menu = QtWidgets.QMenu()
        self.tray_menu.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ### VARIABLES DE BASES ###
        self.win_state = QtCore.Qt.WindowNoState

        ### FONCTIONS AU LANCEMENT ###
        self.INIT(
            [self.IN_BASE, "Configuration des éléments principaux"],
            [self.IN_SETUP_UI, "Setup de l'interface graphique"],
            [self.IN_CLASSE, "Initialisation des Widgets"],
            [self.IN_WG, "Configuration de base des Widgets"],
            [self.IN_CONNECTIONS, "Ajout des connexions"],
            [self.IN_ACT, "Fonctions de base"],
            [self.IN_WG_BASE, "Etat de base des Widgets"],
            [self.IN_TRAY, "Finalisation de la configuration"]
        )

        splash_screen.close()

        ### CREATION DES EVENT ###
        self.evt = Event(self)
        self.mousePressEvent = self.evt.mousePressEvent
        self.mouseDoubleClickEvent = self.evt.mouseDoubleClickEvent
        self.mouseMoveEvent = self.evt.mouseMoveEvent
        self.mouseReleaseEvent = self.evt.mouseReleaseEvent

    ############################
    ##     INITIALISATION     ##
    ############################
    def IN_BASE(self):
        ### Fenetre principal ###
        self.setWindowTitle(config.nom)
        self.setWindowIcon(QtGui.QPixmap(f"{Img().main()}th3.svg"))
        self.setWindowOpacity(config.opacity)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setGraphicsEffect(Shadow().ombre_portee(self))

        self.e_resize_screen()
    def IN_SETUP_UI(self):
        ### Ui principal ###
        self.setupUi(self)
        self.vlay_main.setContentsMargins(v_gb.MARGIN_APP, v_gb.MARGIN_APP, v_gb.MARGIN_APP, v_gb.MARGIN_APP)
    def IN_CLASSE(self):
        ### QLineEdit ###
        LineEdit.Base(self.le_demo_th).th()
        LineEdit.Base(self.le_demo_tr).tr()
        ### /QLineEdit ###


        ### QTextEdit ###
        TextEdit.Demo(self.te_demo_th).th()
        TextEdit.Demo(self.te_demo_tr).tr()
        ### /QTextEdit ###


        ### QPlainTextEdit ###
        PlainTextEdit.Demo(self.pte_demo_th).th()
        PlainTextEdit.Demo(self.pte_demo_tr).tr()
        ### /QPlainTextEdit ###


        ### QScrollBoxArea ###
        ScrollArea.Base(self.sca_main).th()
        ### /QScrollBoxArea ###


        ## QCheckBox ###
        CheckBox.Demo(self.ck_demo_th_1, self.ck_demo_th_2, self.ck_demo_th_3).th()
        CheckBox.Demo(self.ck_demo_tr_1, self.ck_demo_tr_2, self.ck_demo_tr_3).tr()
        ## /QCheckBox ###


        ### QComboBox ###
        ComboBox.Base(self.cb_demo_th).th()
        ComboBox.Base(self.cb_demo_tr).tr()
        ### /QComboBox ###


        ### QDateEdit ###
        DateEdit.Base(self.de_demo_th).th()
        DateEdit.Base(self.de_demo_tr).tr()
        ### /QDateEdit ###


        ### QFrame ###
        Frame.Menu(self.fr_menu_top).top()
        Frame.Cadre(self.fr_main).th2()
        Frame.Base(self.fr_body).tr()
        Frame.Base(self.fr_demo_th, self.fr_tb_demo_th_1, self.fr_tb_demo_th_2).th()
        Frame.Base(self.fr_tb_demo_tr_1, self.fr_tb_demo_tr_2).th()
        Frame.Cadre(
            self.fr_cb, self.fr_de, self.fr_lw, self.fr_pb, self.fr_ck,
            self.fr_rb, self.fr_pg, self.fr_sb, self.fr_tw, self.fr_le,
            self.fr_te, self.fr_pte, self.fr_tb, self.fr_trw, self.fr_sd,
            self.fr_demo_cadre, self.fr_fr, self.fr_lb, border=(StyleBase().border(), )*4
        ).bn1()
        Frame.Menu(self.fr_menu_bottom).bottom()
        Frame.Demo_hover(self.fr_demo_cadre_hover)
        ### /QFrame ###


        ### QLabel ###
        Label.Base(self.lb_mt_ico).ico_main()
        Label.Demo(self.lb_lb_demo_th).th()
        Label.Base(self.lb_mt_nom, font_size=Font().h3()).tr()
        Label.Base(self.lb_mb_version).tr()
        Label.Demo(self.lb_lb_demo_tr).tr()
        Label.Demo(
            self.lb_cb_demo, self.lb_de_demo, self.lb_lw_demo, self.lb_pb_demo, self.lb_ck_demo,
            self.lb_rb_demo, self.lb_pg_demo, self.lb_sb_demo, self.lb_tw_demo, self.lb_le_demo,
            self.lb_te_demo, self.lb_pte_demo, self.lb_tb_demo, self.lb_trw_demo, self.lb_sd_demo,
            self.lb_fr_demo, self.lb_lb_demo
        ).wg_categorie()
        ### /QLabel ###


        ### QListWidget ###
        ListWidget.Demo(self.lv_demo_th, self.lw_demo_th).th()
        ListWidget.Demo(self.lv_demo_tr, self.lw_demo_tr).tr()
        ### /QListWidget ###


        ### QProgressBar ###
        ProgressBar.Demo(self.pg_demo_th).th()
        ProgressBar.Demo(self.pg_demo_tr).tr()
        ### /QProgressBar ###


        ### QPushButton ###
        PushButton.Base(self.pb_demo_th, self.pb_demo_ck).th()
        PushButton.Base(self.pb_demo_tr).tr()

        PushButton.menu_top(self.pb_mt_option).option()
        PushButton.menu_top(self.pb_mt_reduire).reduire()
        PushButton.menu_top(self.pb_mt_agrandir).agrandir()
        PushButton.menu_top(self.pb_mt_quitter).quitter()

        PushButton.Txt(self.pb_demo_txt).txt()
        PushButton.Txt(self.pb_demo_txt_inv).inv()

        PushButton.ck_ico(self.pb_demo_ck_ico, self.pb_demo_ico_ck)
        PushButton.zoom(self.pb_demo_zoom)
        ### /QPushButton ###


        ## QRadioButton ###
        RadioButton.Base(self.rb_demo_th_1, self.rb_demo_th_2, self.rb_demo_th_3).th()
        RadioButton.Base(self.rb_demo_tr_1, self.rb_demo_tr_2, self.rb_demo_tr_3).tr()
        ## /QRadioButton ###


        ## QRadioButton ###
        TrayIcon.Main(self.tray_menu)
        ## /QRadioButton ###


        ### QSlider ###
        Slider.Base(self.hsd_demo).th()
        Slider.Base(self.vsd_demo).rond()
        ### /QSlider ###


        ### QSpinBox ###
        SpinBox.PlusMinus(self.sb_demo).th()
        SpinBox.PlusMinus(self.sb_demo_3).tr()
        SpinBox.UpDown(self.sb_demo_2).th()
        SpinBox.UpDown(self.dsb_demo).tr()
        ### /QSpinBox ###


        ### QTableWidget ###
        TableWidget.Demo(self.tv_demo_th, self.tw_demo_th).th()
        TableWidget.Demo(self.tv_demo_tr, self.tw_demo_tr).tr()
        ### /QTableWidget ###


        ### QToolBox ###
        ToolBox.Demo(self.tb_demo_th).th()
        ToolBox.Demo(self.tb_demo_tr).tr()
        ### /QToolBox ###


        ### QTreeWidget ###
        TreeWidget.Base(self.trv_demo_th, self.trw_demo_th).th()
        TreeWidget.Base(self.trv_demo_tr, self.trw_demo_tr).tr()
        ### /QTreeWidget ###
    def IN_WG(self):
        ### Base ###
        self.setCursor(Functions().SET_CURSOR(Cur().souris()))


        ### Nom de l'app ###
        self.lb_mt_nom.setText(config.nom)


        ### Widget blanc pour centrer le nom de l'app ###
        dim = Dim().h9() * 1.4
        Functions().SET_DIM(self.wg_mt_blank, width=dim*3, height=dim)


        ### Version de l'app ###
        self.lb_mb_version.setText(f" Version : {config.version}")


        ### size_grip ###
        if config.resize:
            self.size_grip.setCursor(Functions().SET_CURSOR(Cur().fleche_nwse()))
            self.size_grip.setStyleSheet(
                f"""
                QSizeGrip {{
                image: url({Img().resize()}th3.svg);
                width: {Dim().h10()}px;
                height: {Dim().h10()}px;
                }}
                """
            )
            self.hlay_menu_bottom.addWidget(self.size_grip)




        # Demo lw
        model = QtGui.QStandardItemModel(60, 1)
        for i in range(60):
            self.lw_demo_th.addItem(f"je suis l'item : {i}")
            self.lw_demo_tr.addItem(f"je suis l'item : {i}")
            model.setItem(i, 0, QtGui.QStandardItem(f"je suis l'item : {i}"))
        self.lv_demo_th.setModel(model)
        self.lv_demo_tr.setModel(model)

        # Demo tv
        model = QtGui.QStandardItemModel(20, 100)
        for ic in range(100):
            for ir in range(20):
                model.setItem(ir, ic, QtGui.QStandardItem(f"item:{ic + ir}"))
        self.tv_demo_th.setModel(model)
        self.tv_demo_tr.setModel(model)

        model = QtWidgets.QFileSystemModel()
        model.setRootPath('')
        self.trv_demo_th.setModel(model)
        self.trv_demo_tr.setModel(model)

        # PB
        self.pb_demo_ck.setCheckable(True)
    def IN_CONNECTIONS(self):
        ### Menu_top ###
        self.pb_mt_option.clicked.connect(lambda: OptionBox(fen_main=fen).MAIN())
        self.pb_demo_th.clicked.connect(lambda: self.test())
        self.pb_mt_reduire.clicked.connect(lambda: self.evt.e_reduire())
        self.pb_mt_agrandir.clicked.connect(lambda: self.evt.e_agrandir())
        self.pb_mt_quitter.clicked.connect(lambda: self.evt.e_cacher())
    def IN_ACT(self):
        pass
    def IN_WG_BASE(self):
        pass
    def IN_TRAY(self):
        ### Actions ###
        Functions.ADD_QACTION(
            self,
            tray=self.tray_menu,
            ico=Img().quitter(),
            ico_rgb="bn2",
            txt="Quitter",
            shortcut_txt="Shift+Esc",
            status_tip="Quitter",
            fct=self.e_quitter_tray,
            sht_1=Keys().shift(),
            sht_2=Keys().escape()
        )

        # self.tray_menu.addSeparator()

        self.tray.setContextMenu(self.tray_menu)
        self.tray.show()
    def INIT(self, *args):
        for fct in args:
            splash_screen.lb_chargement.setText(fct[1])
            splash_screen.pg_chargement.setValue(splash_screen.pg_chargement.value() + 100 / len(args))
            fct[0]()

        splash_screen.lb_chargement.setText("Lancement de l'application")
        splash_screen.pg_chargement.setValue(100)
        time.sleep(0)
    ############################
    ##    /INITIALISATION     ##
    ############################


    #####################
    ##     ACTIONS     ##
    #####################
    def test(self):
        print(RgbBox().GET())
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
    def e_resize_screen(self):
        if config.resize:
            self.setMinimumWidth(config.widht)
            self.setMinimumHeight(config.height)
        else:
            self.setFixedWidth(config.widht)
            self.setFixedHeight(config.height)
    #####
    def traySingleClick(self):
        screen = QtWidgets.QApplication.primaryScreen().availableGeometry()
        widget = toolBox.geometry()

        toolBox.open()
        toolBox.show()
        toolBox.activateWindow()

        toolBox.move(screen.width()-widget.width(), screen.height()-widget.height())
    def trayDoubleClick(self):
        self.timer_double_click.stop()
        self.show()
        fen.activateWindow()

        if fen.windowState() == QtCore.Qt.WindowMinimized:
            fen.setWindowState(QtCore.Qt.WindowActive)
    def trayActivate(self, reason):
        if reason == QtWidgets.QSystemTrayIcon.Trigger:
            self.timer_double_click.start(app.doubleClickInterval())

        elif reason == QtWidgets.QSystemTrayIcon.DoubleClick:
            self.trayDoubleClick()
    def e_quitter(self):
        """Permet de quitter l'application"""
        if not config.auto_close:
            self.hide()
        elif ResponseBox().QUITTER():
            app.quit()
    def e_quitter_tray(self):
        self.show()
        fen.activateWindow()

        if fen.windowState() == QtCore.Qt.WindowMinimized:
            fen.setWindowState(QtCore.Qt.WindowActive)

        if ResponseBox().QUITTER():
            app.quit()
    #####
    def closeEvent(self, event):
        event.accept()
        app.quit()
    ###################
    ##    /EVENT     ##
    ###################


if __name__ == "__main__":
    Functions().GEN_SVG()

    app = QtWidgets.QApplication(sys.argv)
    splash_screen = SplashScreen()
    splash_screen.open()
    toolBox = ToolBoxUi()
    app.processEvents()

    fen = main()
    fen.show()

    sys.exit(app.exec())
