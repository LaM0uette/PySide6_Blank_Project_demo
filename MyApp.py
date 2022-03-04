import sys

from PySide6 import QtCore, QtWidgets, QtGui

from src import *


class main(Ui_main, QtWidgets.QWidget):
    dragPos: QtCore.QPoint

    def __init__(self):
        super(main, self).__init__()

        ### AJOUTS DE BASE ###
        self.size_grip = QtWidgets.QSizeGrip(self)

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
        evt = Event(self)

        self.mousePressEvent = evt.mousePressEvent
        self.mouseDoubleClickEvent = evt.mouseDoubleClickEvent

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
        pass
    def IN_WG(self):
        ### Base ###
        self.setCursor(Cur().souris())


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
            self.size_grip.setCursor(Cur().fleche_nwse())
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
        self.pb_mt_reduire.clicked.connect(lambda: self.e_reduire())
        self.pb_mt_agrandir.clicked.connect(lambda: self.e_agrandir())
        self.pb_mt_quitter.clicked.connect(lambda: self.e_cacher())
    def IN_ACT(self):
        pass
    def IN_WG_BASE(self):
        pass
    def IN_TRAY(self):
        pass
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
    def _e_center_screen(self):
        center = QtGui.QScreen.availableGeometry(QtWidgets.QApplication.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        self.move(geo.topLeft())

    #####

    def e_resize_screen(self):
        if config.resize:
            self.setMinimumWidth(config.widht)
            self.setMinimumHeight(config.height)
        else:
            self.setFixedWidth(config.widht)
            self.setFixedHeight(config.height)
    def e_agrandir(self):
        if self.windowState() == QtCore.Qt.WindowMaximized:
            self.win_state = QtCore.Qt.WindowNoState
            self._e_center_screen()
            self.e_resize_screen()
        else:
            self.win_state = QtCore.Qt.WindowMaximized

        self.setWindowState(self.win_state)
    def e_reduire(self):
        self.setWindowState(QtCore.Qt.WindowMinimized)
    def e_cacher(self):
        if config.debug: return self.e_quitter()
        self.hide()
        self._e_center_screen()
    def e_quitter(self):
        if not config.auto_close:
            self.hide()
        elif config.auto_close:  # DLG_Rep().QUITTER()
            app.quit()

    #####


    def mouseMoveEvent(self, event):
        def act_move(event):
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
            self.dragPos = event.globalPosition().toPoint()
            event.accept()

        cur = QtGui.QCursor()
        verif_height = cur.pos().y() - self.pos().y()
        if event.buttons() == QtCore.Qt.LeftButton and v_gb.BD_LIMIT < verif_height < Dim().h9()+v_gb.BD_LIMIT and self.windowState() != QtCore.Qt.WindowMaximized and cur.pos().y() <= 0:
            self.setCursor(Cur().agrandir())
        else:
            self.setCursor(Cur().souris())

        try:
            if event.buttons() == QtCore.Qt.LeftButton and v_gb.BD_LIMIT < verif_height < Dim().h9()+v_gb.BD_LIMIT and self.windowState() != QtCore.Qt.WindowMaximized:
                act_move(event)
            if event.buttons() == QtCore.Qt.LeftButton and v_gb.BD_LIMIT < verif_height < Dim().h9()+v_gb.BD_LIMIT and self.windowState() == QtCore.Qt.WindowMaximized:
                self.setWindowState(QtCore.Qt.WindowNoState)
                self.win_state = QtCore.Qt.WindowNoState
                act_move(event)
        except AttributeError: pass
    def mouseReleaseEvent(self, event):
        cur = QtGui.QCursor()
        verif_height = cur.pos().y() - self.pos().y()
        if v_gb.BD_LIMIT < verif_height < Dim().h9()+v_gb.BD_LIMIT and self.windowState() != QtCore.Qt.WindowMaximized and cur.pos().y() <= 0:
            self.setCursor(Cur().souris())
            self.e_agrandir()
            event.accept()
    def closeEvent(self, event):
        event.accept()
        app.quit()
        # self.tray_menu.update()
        # self.tray_menu.close()
        # self.tray_menu.destroy()
    ###################
    ##    /EVENT     ##
    ###################


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.processEvents()

    fen = main()
    fen.show()

    sys.exit(app.exec())
