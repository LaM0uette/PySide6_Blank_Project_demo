import sys

from PySide6 import QtCore, QtWidgets, QtGui

from src import *


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
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.e_resize_screen()
    def IN_SETUP_UI(self):
        ### Ui principal ###
        self.setupUi(self)
    def IN_CLASSE(self):
        ## QCheckBox ###
        CheckBox.Demo(self.ck_demo_th_1, self.ck_demo_th_2, self.ck_demo_th_3).th()
        CheckBox.Demo(self.ck_demo_tr_1, self.ck_demo_tr_2, self.ck_demo_tr_3).tr()
        ## /QCheckBox ###


        ### QComboBox ###
        ComboBox.Base(self.cb_demo_th).th()
        ComboBox.Base(self.cb_demo_tr).tr()
        ### /QComboBox ###


        ## QRadioButton ###
        RadioButton.Base(self.rb_demo_th_1, self.rb_demo_th_2, self.rb_demo_th_3).th()
        RadioButton.Base(self.rb_demo_tr_1, self.rb_demo_tr_2, self.rb_demo_tr_3).tr()
        ## /QRadioButton ###
    def IN_WG(self):
        ### Base ###
        self.setCursor(Functions().SET_CURSOR(Cur().souris()))


        ### Icone de l'app ###
        dim = Dim().h9()
        Functions().SET_DIM(self.lb_mt_ico, width=dim, height=dim)
        self.lb_mt_ico.setPixmap(QtGui.QPixmap(f"{Img().main()}th3.svg"))
        self.lb_mt_ico.setScaledContents(True)


        ### Nom de l'app ###
        self.lb_mt_nom.setText(config.nom)


        ### Widget blanc pour centrer le nom de l'app ###
        dim = Dim().h9() * 1.4
        Functions().SET_DIM(self.wg_mt_blank, width=dim * 3, height=dim)


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
    def IN_CONNECTIONS(self):
        ### Menu_top ###
        # self.pb_mt_option.clicked.connect(lambda: DLG_Option(fen=fen).MAIN())
        self.pb_mt_reduire.clicked.connect(lambda: self.evt.e_reduire())
        self.pb_mt_agrandir.clicked.connect(lambda: self.evt.e_agrandir())
        self.pb_mt_quitter.clicked.connect(lambda: self.evt.e_cacher())
    def IN_ACT(self):
        pass
    def IN_WG_BASE(self):
        pass
    def IN_TRAY(self):
        # TrayIcon.Main(self.tray_menu)

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
            fct[0]()
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
    def e_resize_screen(self):
        if config.resize:
            self.setMinimumWidth(config.widht)
            self.setMinimumHeight(config.height)
        else:
            self.setFixedWidth(config.widht)
            self.setFixedHeight(config.height)
    #####
    def traySingleClick(self):
        pass
        # screen = QtWidgets.QApplication.primaryScreen().availableGeometry()
        # widget = tray_ui.geometry()
        #
        # tray_ui.move(screen.width()-widget.width(), screen.height()-widget.height())
        # tray_ui.open()
        # tray_ui.activateWindow()
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
        elif config.auto_close:  # DLG_Rep().QUITTER()
            app.quit()
    def e_quitter_tray(self):
        self.show()
        fen.activateWindow()

        if fen.windowState() == QtCore.Qt.WindowMinimized:
            fen.setWindowState(QtCore.Qt.WindowActive)

        # if DLG_Rep().QUITTER():
        #     self.ui.app.quit()
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
    app.processEvents()

    fen = main()
    fen.show()

    sys.exit(app.exec())
