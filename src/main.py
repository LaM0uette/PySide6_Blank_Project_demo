import sys

from PySide6 import QtCore, QtWidgets, QtGui

from .build import cursor, functions
from .config import config, colors
from .dct_gen import dct_dim, dct_img
from .dct_pal import dct_pal
from .ui_classe import STYLE_WG
from .option import option
from .gui.main_ui import Ui_main


class main(Ui_main, QtWidgets.QWidget):
    """
    _TITRE: Titre de la fonctions/module/actions/classe:...
    _DESC: Déscription de la fonction, module, action, classe, ...

    _acp: Valeurs possibles
    _ex: Exemples
    _fct = Fonctions
    _info: Informations
    _lien: Lien avec une fonction, module, action, classe, ...
    _type: () tuple, [] list, {} dict, 1 int, "" str, bool
    _val: Valeures (arguments, variables, ...)

    AA = AUTOMATIQUE
    A0 = OBLIGATOIRE
    A1 = FORTEMENT CONSEILLE
    A2 = AU CHOIX
    """
    dragPos: QtCore.QPoint

    def __init__(self):
        super(main, self).__init__()

        ### INIT UI ______
        self.setupUi(self)

        ### CREATION DES CURSEURS
        self.dct_cur = {
            "agrandir": QtGui.QCursor(QtGui.QPixmap(cursor.cur_agrandir[0]), cursor.cur_agrandir[1], cursor.cur_agrandir[2]),
            "copier": QtGui.QCursor(QtGui.QPixmap(cursor.cur_copier[0]), cursor.cur_copier[1], cursor.cur_copier[2]),
            "crayon": QtGui.QCursor(QtGui.QPixmap(cursor.cur_crayon[0]), cursor.cur_crayon[1], cursor.cur_crayon[2]),
            "croix": QtGui.QCursor(QtGui.QPixmap(cursor.cur_croix[0]), cursor.cur_croix[1], cursor.cur_croix[2]),
            "fleche_nesw": QtGui.QCursor(QtGui.QPixmap(cursor.cur_fleche_nesw[0]), cursor.cur_fleche_nesw[1], cursor.cur_fleche_nesw[2]),
            "fleche_ns": QtGui.QCursor(QtGui.QPixmap(cursor.cur_fleche_ns[0]), cursor.cur_fleche_ns[1], cursor.cur_fleche_ns[2]),
            "fleche_nwse": QtGui.QCursor(QtGui.QPixmap(cursor.cur_fleche_nwse[0]), cursor.cur_fleche_nwse[1], cursor.cur_fleche_nwse[2]),
            "fleche_top": QtGui.QCursor(QtGui.QPixmap(cursor.cur_fleche_top[0]), cursor.cur_fleche_top[1], cursor.cur_fleche_top[2]),
            "fleche_tout": QtGui.QCursor(QtGui.QPixmap(cursor.cur_fleche_tout[0]), cursor.cur_fleche_tout[1], cursor.cur_fleche_tout[2]),
            "fleche_we": QtGui.QCursor(QtGui.QPixmap(cursor.cur_fleche_we[0]), cursor.cur_fleche_we[1], cursor.cur_fleche_we[2]),
            "IBeam": QtGui.QCursor(QtGui.QPixmap(cursor.cur_IBeam[0]), cursor.cur_IBeam[1], cursor.cur_IBeam[2]),
            "infos": QtGui.QCursor(QtGui.QPixmap(cursor.cur_infos[0]), cursor.cur_infos[1], cursor.cur_infos[2]),
            "main": QtGui.QCursor(QtGui.QPixmap(cursor.cur_main[0]), cursor.cur_main[1], cursor.cur_main[2]),
            "non": QtGui.QCursor(QtGui.QPixmap(cursor.cur_non[0]), cursor.cur_non[1], cursor.cur_non[2]),
            "retour": QtGui.QCursor(QtGui.QPixmap(cursor.cur_retour[0]), cursor.cur_retour[1], cursor.cur_retour[2]),
            "souris": QtGui.QCursor(QtGui.QPixmap(cursor.cur_souris[0]), cursor.cur_souris[1], cursor.cur_souris[2]),
            "souris_main": QtGui.QCursor(QtGui.QPixmap(cursor.cur_souris_main[0]), cursor.cur_souris_main[1], cursor.cur_souris_main[2]),
            "souris_non": QtGui.QCursor(QtGui.QPixmap(cursor.cur_souris_non[0]), cursor.cur_souris_non[1], cursor.cur_souris_non[2])
        }

        ### INIT _____
        self.IN_INIT()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.activateWindow()

    ### INIT ___________
    def cr_lst_wg(self):
        return {
            "txt": {},
            "cb": {},
            "de": {},
            "fr": {
                "menu_top": [self.fr_menu_top]
            },
            "lb": {
                "menu_top": [self.lb_mt_version, self.lb_mt_nom]
            },
            "lw": {},
            "pb": {
                "menu_top": [self.pb_mt_option, self.pb_mt_reduire, self.pb_mt_agrandir, self.pb_mt_quitter]
            },
            "ckb": {},
            "rb": {},
            "pg": {},
            "sca": {},
            "sb": {},
            "tw": {}
        }
    def cr_ln(self):
        return {}

    def IN_BASE(self):
        ## Fenetre _______________________
        self.setFixedWidth(config.widht)
        self.setFixedHeight(config.height)
        self.setWindowOpacity(config.opacity)
        self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(PXM)))
        self.setWindowTitle(config.nom)

        self.setCursor(self.dct_cur.get("souris"))
        self.setStyleSheet(f"background-color: rgb{colors.th1};")
    def IN_CLASSE(self):
        """ _TITRE: Stylise les widgets

            _DESC: Permet de récuperer les dictionnaires des wg pour les mettres en formes.
                les arguments possibles sont:

            _FCT - STYLE_WG:
            AA  _ex: type_wg = "lb"
                _info: Correspond au type de widget.
                _lien: FCT: cr_lst_wg

            AA  _ex: wg_name = self.label
                _info: Correspond au widget.
                _lien: FCT: cr_lst_wg

            AA  _ex: wg = self.label
                _info: Correspond au nom du widget.
                _lien: FCT: cr_lst_wg
        """

        # ln ________________
        lst_ln = self.cr_ln()
        for dct_lst in lst_ln:
            for ln in lst_ln[dct_lst]:
                ln.setFrameShadow(QtWidgets.QFrame.Plain)
                ln.setLineWidth(2)
                ln.setStyleSheet(f"color: rgb{colors.bn1};")

        # wg ______________________
        lsts_wgs = self.cr_lst_wg()
        for dct_lsts in lsts_wgs:
            type_wg = dct_lsts

            for lst_wgs in lsts_wgs[dct_lsts]:
                for wg in lsts_wgs[dct_lsts][lst_wgs]:
                    STYLE_WG(type_wg=type_wg, wg_name=wg.objectName(), wg=wg)
    def IN_WG(self):
        # Frame ________________________________________________
        self.fr_menu_top.setFixedHeight(dct_dim.get("h_menu_top"))

        # Icone de l'app ______________________________
        self.lb_mt_version.setText(str(config.version))

        # Icone de l'app ___________________________
        dim = dct_pal.get("dim").get("c_menu_top")
        functions.DIM(wg=self.lb_mt_ico, w=dim.get("w"), h=dim.get("h"))
        self.lb_mt_ico.setPixmap(QtGui.QPixmap(PXM))
        self.lb_mt_ico.setScaledContents(True)
        self.lb_mt_nom.setText(config.nom)

        # Widget blanc pour centrer le nom de l'app ________________________
        functions.DIM(wg=self.wg_mt_blank, w=dim.get("w")*3, h=dim.get("h"))
    def IN_WG_BASE(self):
        pass
    def IN_CONNECTIONS(self):
        # Menu top _________________________________________________
        self.pb_mt_option.clicked.connect(lambda: self.FCT_OPTION())
        self.pb_mt_reduire.clicked.connect(lambda: self.EVT_REDUIRE_GDT())
        self.pb_mt_agrandir.clicked.connect(lambda: self.EVT_AGRANDIR_GDT())
        self.pb_mt_quitter.clicked.connect(lambda: self.EVT_REDUIRE_HIDE_GDT())
    def IN_ACT(self):
        pass
    def IN_INIT(self):
        self.IN_BASE()
        self.IN_CLASSE()
        self.IN_WG()
        self.IN_WG_BASE()
        self.IN_CONNECTIONS()
        self.IN_ACT()


    ### FONCTIONS _______
    def FCT_OPTION(self):
        fen_option = option(fen)
        fen_option.show()


    ### EVENT _______________
    def EVT_CENTRE_FEN(self):
        center = QtGui.QScreen.availableGeometry(QtWidgets.QApplication.primaryScreen()).center()
        geo = fen.frameGeometry()
        geo.moveCenter(center)
        fen.move(geo.topLeft())

        self.setFixedWidth(config.widht)
        self.setFixedHeight(config.height)
    def EVT_AGRANDIR_GDT(self):
        if fen.windowState() == QtCore.Qt.WindowMaximized:
            fen.setWindowState(QtCore.Qt.WindowNoState)
            self.EVT_CENTRE_FEN()
        else:
            fen.setWindowState(QtCore.Qt.WindowMaximized)
    def EVT_REDUIRE_GDT(self):
        fen.setWindowState(QtCore.Qt.WindowNoState)
        self.EVT_CENTRE_FEN()
        fen.setWindowState(QtCore.Qt.WindowMinimized)
    def EVT_REDUIRE_HIDE_GDT(self):
        if config.auto_close: return self.EVT_QUITTER()
        self.hide()
        self.EVT_CENTRE_FEN()
    def EVT_QUITTER(self):
        dlg = functions.DLG(msg="Voulez vous vraiment quitter l'application ? ")
        rep = dlg.VERIF_CHOIX(titre="Quitter", msg_verif="Quitter", ico=dct_img.get("quitter") + "th1")

        if rep == QtWidgets.QMessageBox.Ok:
            app.quit()
            quit()
    def mousePressEvent(self, event):
        cur = QtGui.QCursor()
        verifHeight = cur.pos().y() - self.pos().y()
        if event.buttons() == QtCore.Qt.LeftButton and verifHeight < dct_dim.get("h_menu_top") and fen.windowState() != QtCore.Qt.WindowMaximized:
            self.dragPos = event.globalPosition().toPoint()
            event.accept()
    def mouseMoveEvent(self, event):
        cur = QtGui.QCursor()
        height_verif = cur.pos().y() - self.pos().y()

        if event.buttons() == QtCore.Qt.LeftButton and height_verif < dct_dim.get("h_menu_top") and fen.windowState() != QtCore.Qt.WindowMaximized and cur.pos().y() <= 0:
            self.setCursor(self.dct_cur.get("agrandir"))
        else:
            self.setCursor(self.dct_cur.get("souris"))

        try:
            if event.buttons() == QtCore.Qt.LeftButton and height_verif < dct_dim.get("h_menu_top") and fen.windowState() != QtCore.Qt.WindowMaximized:
                self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
                self.dragPos = event.globalPosition().toPoint()
                event.accept()

            if event.buttons() == QtCore.Qt.LeftButton and height_verif < dct_dim.get("h_menu_top") and fen.windowState() == QtCore.Qt.WindowMaximized:
                fen.setWindowState(QtCore.Qt.WindowNoState)
                self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
                self.dragPos = event.globalPosition().toPoint()
                event.accept()

        except AttributeError:
            pass
    def mouseReleaseEvent(self, event):
        cur = QtGui.QCursor()
        height_verif = cur.pos().y() - self.pos().y()
        if height_verif < dct_dim.get("h_menu_top") and fen.windowState() != QtCore.Qt.WindowMaximized and cur.pos().y() <= 0:
            self.setCursor(self.dct_cur.get("souris"))
            self.EVT_AGRANDIR_GDT()
            event.accept()
    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        event.accept()
        app.quit()


PXM = dct_img.get("main") + "th1" + ".svg"
app = QtWidgets.QApplication(sys.argv)
splash = QtWidgets.QSplashScreen(QtGui.QPixmap(PXM).scaledToHeight(500), QtCore.Qt.WindowStaysOnTopHint)
splash.show()
app.processEvents()

fen = main()
splash.finish(fen)
fen.show()

sys.exit(app.exec())
