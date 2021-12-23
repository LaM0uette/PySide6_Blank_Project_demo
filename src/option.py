import glob
import importlib
import os.path
import time

from PySide6 import QtCore, QtWidgets, QtGui

from . import vrb
from .worker import worker
from .build import cursor, functions
from .config import config, colors
from .dct_gen import dct_dim, dct_img
from .dct_pal import dct_pal
from .ui_classe import STYLE_WG
from .gui.option_ui import Ui_option


class option(Ui_option, QtWidgets.QWidget):
    dragPos: QtCore.QPoint

    def __init__(self, fen):
        super(option, self).__init__()

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

        ### VARIABLES GLOBALES ________
        self.fen = fen # Fenêtres main
            #thread
        self.thread = QtCore.QThreadPool()
            #theme
        self.config_ini = functions.INI(lien_ini=vrb.ini_cfg)
        self.cfg = self.config_ini.OPEN_INI()
        self.theme_actuel = self.cfg["config"]["theme"]
        self.appliquer = False

        ### INIT _____
        self.IN_INIT()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.activateWindow()

    ### INIT ___________
    def cr_lst_wg(self):
        return {
            "txt": {
                "option": [self.le_nom_theme]
            },
            "cb": {
                "option": [self.cb_choix_theme]
            },
            "fr": {
                "menu_top": [self.fr_menu_top],
                "option": [self.fr_opt_theme, self.fr_opt_affichages]
            },
            "lb": {
                "menu_top": [self.lb_mt_nom],
                "option": [self.lb_choix_theme, self.lb_nom_theme, self.lb_th1, self.lb_th2, self.lb_th3, self.lb_th4, self.lb_bn1, self.lb_bn2,
                           self.lb_opacity_titre, self.lb_opacity, self.lb_parametre_titre, self.lb_auto_reload, self.lb_auto_close]
            },
            "pb": {
                "menu_top": [self.pb_mt_quitter],
                "option": [self.pb_creer_theme, self.pb_modif_theme, self.pb_supp_theme, self.pb_appliquer, self.pb_ok],
                "option_pb_theme_colors": [self.pb_th1, self.pb_th2, self.pb_th3, self.pb_th4, self.pb_bn1, self.pb_bn2]
            },
            "ckb": {
                "option": [self.ckb_auto_reload, self.ckb_auto_close]
            },
            "sb": {
                "option": [self.sp_opacity]
            },

            "tb": {
                "option": [self.tb_option]
            }
        }
    def cr_ln(self):
        return {
            "demo": [self.line, self.line_2]
        }

    def IN_BASE(self):
        ## Fenetre _______________________
        self.setFixedWidth(config.widht/1.8)
        self.setFixedHeight(config.height/1.4)
        self.setWindowOpacity(1)
        self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(dct_img.get("option") + "th1" + ".svg")))
        self.setWindowTitle("Options")

        self.setCursor(self.dct_cur.get("souris"))
        self.setStyleSheet(f"background-color: rgb{colors.th1};")
        self.fr_bg_dlg.setStyleSheet("QFrame#fr_bg_dlg {"
                                     f"border: 2px solid rgb{colors.th3};"
                                     "}")
    def IN_CLASSE(self):
        # ln ________________
        lst_ln = self.cr_ln()
        for dct_lst in lst_ln:
            for ln in lst_ln[dct_lst]:
                ln.setFrameShadow(QtWidgets.QFrame.Plain)
                ln.setLineWidth(2)
                ln.setStyleSheet(f"color: rgb{colors.bn1};")

        # WG ______________________
        lsts_wgs = self.cr_lst_wg()
        for dct_lsts in lsts_wgs:
            type_wg = dct_lsts

            for lst_wgs in lsts_wgs[dct_lsts]:
                for wg in lsts_wgs[dct_lsts][lst_wgs]:
                    STYLE_WG(type_wg=type_wg, wg_name=wg.objectName(), wg=wg)
    def IN_WG(self):
        # Frame ________________________________________________
        self.fr_menu_top.setFixedHeight(dct_dim.get("h_menu_top"))

        # Icone de l'app ________________
        self.lb_mt_nom.setText("Options")

        # Widget blanc pour centrer le nom de l'app
        dim = dct_pal.get("dim").get("c_menu_top")
        functions.DIM(wg=self.wg_mt_blank, w=dim.get("w"), h=dim.get("h"))
    def IN_WG_BASE(self):
        self.tb_option.setCurrentIndex(1)
    def IN_CONNECTIONS(self):
        # Menut top __________________________________________________
        self.pb_mt_quitter.clicked.connect(lambda: self.close())

        self.pb_th1.clicked.connect(lambda: self.FCT_CHANGE_COLOR(wg=self.pb_th1))
        self.pb_th2.clicked.connect(lambda: self.FCT_CHANGE_COLOR(wg=self.pb_th2))
        self.pb_th3.clicked.connect(lambda: self.FCT_CHANGE_COLOR(wg=self.pb_th3))
        self.pb_th4.clicked.connect(lambda: self.FCT_CHANGE_COLOR(wg=self.pb_th4))
        self.pb_bn1.clicked.connect(lambda: self.FCT_CHANGE_COLOR(wg=self.pb_bn1))
        self.pb_bn2.clicked.connect(lambda: self.FCT_CHANGE_COLOR(wg=self.pb_bn2))

        self.pb_creer_theme.clicked.connect(lambda: self.FCT_ADD_THEME())
        self.pb_modif_theme.clicked.connect(lambda: self.FCT_MODIF_THEME())
        self.pb_supp_theme.clicked.connect(lambda: self.FCT_REMOVE_THEME())

        self.cb_choix_theme.currentIndexChanged.connect(lambda: self.act_reset_appliquer())
        self.sp_opacity.valueChanged.connect(lambda: self.act_reset_appliquer())
        self.ckb_auto_reload.clicked.connect(lambda: self.act_reset_appliquer())
        self.ckb_auto_close.clicked.connect(lambda: self.act_reset_appliquer())

        self.pb_appliquer.clicked.connect(lambda: self.FCT_APPLIQUER())
        self.pb_ok.clicked.connect(lambda: self.FCT_OK())
    def IN_ACT(self):
        self.act_maj_options()
        self.act_set_colors()
    def IN_INIT(self):
        self.IN_BASE()
        self.IN_CLASSE()
        self.IN_WG()
        self.IN_WG_BASE()
        self.IN_CONNECTIONS()
        self.IN_ACT()


    ### ACTIONS _________
    def act_set_colors(self):
        lst_wg = self.cr_lst_wg().get("pb").get("option_pb_theme_colors")

        lst = [colors.th1, colors.th2, colors.th3, colors.th4, colors.bn1, colors.bn2]
        for i, wg in enumerate(lst_wg):
            wg.setStyleSheet("QPushButton {"
                             f"background-color: rgb{lst[i]};"
                             f"color: rgb{lst[i]};"
                             "}"
                             "QPushButton:flat {"
                             "border: 1px solid rgb(216, 216, 216);"
                             "}")
            wg.setText(f"{lst[i][0]}_{lst[i][1]}_{lst[i][2]}")
    def act_get_colors(self):
        col = QtWidgets.QColorDialog.getColor().getRgb()
        return [col[i] for i in range(3)]
    def act_theme_get_colors(self):
        return {
            "th1": [int(self.pb_th1.text().split("_")[i]) for i in range(len(self.pb_th1.text().split("_")))],
            "th2": [int(self.pb_th2.text().split("_")[i]) for i in range(len(self.pb_th2.text().split("_")))],
            "th3": [int(self.pb_th3.text().split("_")[i]) for i in range(len(self.pb_th3.text().split("_")))],
            "th4": [int(self.pb_th4.text().split("_")[i]) for i in range(len(self.pb_th4.text().split("_")))],
            "bn1": [int(self.pb_bn1.text().split("_")[i]) for i in range(len(self.pb_bn1.text().split("_")))],
            "bn2": [int(self.pb_bn2.text().split("_")[i]) for i in range(len(self.pb_bn2.text().split("_")))]
        }

    def act_maj_config(self):
        autoreload = "true" if self.ckb_auto_reload.isChecked() else "false"
        autoclose = "true" if self.ckb_auto_close.isChecked() else "false"

        self.cfg["config"]["theme"] = self.cb_choix_theme.currentText()
        self.cfg["config"]["opacity"] = str(self.sp_opacity.value() / 100)
        self.cfg["var"]["autoreload"] = autoreload
        self.cfg["var"]["autoclose"] = autoclose

        self.config_ini.WRITE_INI(ini=self.cfg)

        self.theme_actuel = self.cb_choix_theme.currentText()
    def act_reload_modules(self):
        importlib.reload(config)
        importlib.reload(colors)

        functions.GEN_SVG()

        from . import dct_pal as pal
        importlib.reload(pal)
        del pal

        from . import dct_classe_wg as classe
        importlib.reload(classe)
        del classe

        from . import dct_wg as wg
        importlib.reload(wg)
        del wg
    def act_maj_options(self):
        # Theme ___________________
        self.cb_choix_theme.clear()
        for i, js in enumerate(glob.glob(vrb.lien_json + "*.json")):
            tm = os.path.basename(js).split(".")[0]
            self.cb_choix_theme.addItem(tm)
            if tm == self.theme_actuel:
                self.cb_choix_theme.setCurrentIndex(i)

        # Affichage
        self.sp_opacity.setValue(int(round(config.opacity*100)))
        self.ckb_auto_reload.setChecked(True) if config.auto_reload == True else self.ckb_auto_reload.setChecked(False)
        self.ckb_auto_close.setChecked(True) if config.auto_close == True else self.ckb_auto_close.setChecked(False)
    def act_maj_affichage_ui(self):
        self.act_maj_options()

        self.IN_BASE()
        self.IN_CLASSE()

        self.fen.IN_BASE()
        self.fen.IN_CLASSE()
        self.act_set_colors()

        self.appliquer = True
    def act_reset_appliquer(self):
        self.appliquer = False
        self.le_nom_theme.setText(self.cb_choix_theme.currentText())


    ### FONCTIONS ____________
    def FCT_CHANGE_COLOR(self, wg):
        col = self.act_get_colors()

        wg.setStyleSheet("QPushButton {"
                        f"background-color: rgb{tuple(col)};"
                        f"color: rgb{tuple(col)};"
                        "}"
                        "QPushButton:flat {"
                        "border: none;"
                        "}")
        wg.setText(f"{col[0]}_{col[1]}_{col[2]}")
    def FCT_ADD_THEME(self):
        nom_theme = self.le_nom_theme.text()
        if os.path.exists(vrb.lien_json + f"{nom_theme}.json"):
            functions.DLG(msg="Ce thème existe déjà").MSG_ERREUR()
            return
        js = functions.JSON(vrb.lien_json + f"{nom_theme}.json")
        js.WRITE(data=self.act_theme_get_colors())

        self.act_maj_config()
        self.act_maj_options()

        for i in range(self.cb_choix_theme.count()):
            if self.cb_choix_theme.itemText(i) == nom_theme:
                self.cb_choix_theme.setCurrentIndex(i)
    def FCT_MODIF_THEME(self):
        nom_theme = self.le_nom_theme.text()
        if self.cb_choix_theme.currentText() in ("claire", "moderne", "sombre"):
            functions.DLG(msg="Impossible de modifier ce thème").MSG_ERREUR()
            return

        if os.path.exists(vrb.lien_json + f"{self.cb_choix_theme.currentText()}.json"):
            os.rename(vrb.lien_json + f"{self.cb_choix_theme.currentText()}.json", vrb.lien_json + f"{nom_theme}.json")

            js = functions.JSON(vrb.lien_json + f"{nom_theme}.json")
            js.WRITE(data=self.act_theme_get_colors())

            self.act_maj_config()
            self.act_maj_options()

            for i in range(self.cb_choix_theme.count()):
                if self.cb_choix_theme.itemText(i) == nom_theme:
                    self.cb_choix_theme.setCurrentIndex(i)
    def FCT_REMOVE_THEME(self):
        if self.cb_choix_theme.currentText() in ("claire", "moderne", "sombre"):
            functions.DLG(msg="Vous ne pouvez pas supprimer ce thème").MSG_ERREUR()
            return
        dlg = functions.DLG(msg="Voulez vous vraiment supprimer ce thème ?")
        rep = dlg.VERIF_CHOIX(titre="Suppresion thème", msg_verif="Supprimer", ico=dct_img.get("quitter") + "th1")

        fichier = vrb.lien_json + self.cb_choix_theme.currentText() + ".json"
        if rep == QtWidgets.QMessageBox.Ok:
            os.remove(fichier)
            self.act_maj_options()
            self.act_maj_config()

    def FCT_APPLIQUER(self):
        self.act_maj_config()
        time.sleep(0.2)

        wk = worker(func=self.act_reload_modules)
        wk.signals.finished.connect(self.act_maj_affichage_ui)
        self.thread.start(wk)
    def FCT_OK(self):
        if not self.appliquer:
            dlg = functions.DLG(msg="Vous n'avez pas appliqué les modifications.\nVoulez les appliquer ?")
            rep = dlg.VERIF_CHOIX(titre="Modifications", msg_verif="Appliquer", ico=dct_img.get("quitter") + "th1")

            if rep == QtWidgets.QMessageBox.Ok:
                self.FCT_APPLIQUER()
        self.close()


    ### EVENT ____________
    def mousePressEvent(self, event):
        cur = QtGui.QCursor()
        verifHeight = cur.pos().y() - self.pos().y()
        if event.buttons() == QtCore.Qt.LeftButton and verifHeight < dct_dim.get("h_menu_top") and self.windowState() != QtCore.Qt.WindowMaximized:
            self.dragPos = event.globalPosition().toPoint()
            event.accept()
    def mouseMoveEvent(self, event):
        cur = QtGui.QCursor()
        height_verif = cur.pos().y() - self.pos().y()

        if event.buttons() == QtCore.Qt.LeftButton and height_verif < dct_dim.get("h_menu_top") and self.windowState() != QtCore.Qt.WindowMaximized and cur.pos().y() <= 0:
            self.setCursor(self.dct_cur.get("agrandir"))
        else:
            self.setCursor(self.dct_cur.get("souris"))

        try:
            if event.buttons() == QtCore.Qt.LeftButton and height_verif < dct_dim.get("h_menu_top") and self.windowState() != QtCore.Qt.WindowMaximized:
                self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
                self.dragPos = event.globalPosition().toPoint()
                event.accept()

            if event.buttons() == QtCore.Qt.LeftButton and height_verif < dct_dim.get("h_menu_top") and self.windowState() == QtCore.Qt.WindowMaximized:
                self.setWindowState(QtCore.Qt.WindowNoState)
                self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
                self.dragPos = event.globalPosition().toPoint()
                event.accept()

        except AttributeError:
            pass
    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        event.accept()
        self.close()
