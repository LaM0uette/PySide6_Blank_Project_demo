import glob
import os
import random
import time

from PySide6 import QtCore, QtWidgets, QtGui
import pyperclip

from ... import option_ui
from ..Msg import Msg
from ..Rgb import Rgb
from .....build import *
from .....config import *
from .....In_classe import In_classe


class Dlg_option(option_ui.Ui_Option, QtWidgets.QDialog):
    dragPos: QtCore.QPoint

    def __init__(self,
                 fen,
                 titre,
                 msg,
                 ico,
                 tm,
                 txt_pb_appliquer,
                 txt_pb_ok,
                 width,
                 height,
                 opacity,
    ):
        super(Dlg_option, self).__init__()

        self.fen = fen
        self.titre = titre
        self.msg = msg
        self.ico = ico
        self.tm = tm
        self.txt_pb_ok = txt_pb_ok
        self.txt_pb_appliquer = txt_pb_appliquer
        self.width = width
        self.height = height
        self.opacity = opacity

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setupUi(self)

        # Global
        self.reload = False
        self.dct_pg = {
            "Général": [self.pg_opt_gen],
            "Polices": [self.pg_opt_font],
            "Configs": [self.pg_opt_configs],
            "Thèmes": [self.pg_opt_themes],
            "T-Colors": [self.pg_opt_tcolors],
            "Infos": [self.pg_opt_infos],
        }

        self.INIT()


    ### INITIALISATION
    def IN_BASE(self):
        ## Fenetre
        self.setWindowTitle(self.titre)
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)
        self.setWindowOpacity(self.opacity)
    def IN_CLASSE(self):
        def COMBO_BOX():
            Combo_box.base(self.fcb_opt_ft_font, self.cb_opt_tm_theme, self.cb_opt_tcolors_mode).tr()
        def CHECK_BOX():
            Check_box.base(self.ck_opt_cfg_autoreload, self.ck_opt_cfg_autoclose, self.ck_opt_cfg_resize).tr()
        def FRAME():
            Frame.base(self.fr_main).cadre_th3()
            Frame.menu_bottom_dlg(self.fr_opt_bottom).th()
            Frame.base(self.fr_opt_ft_h1, self.fr_opt_ft_h2, self.fr_opt_ft_h3, self.fr_opt_ft_h4, self.fr_opt_ft_h5,
                       self.fr_opt_cfg_opacity, self.fr_opt_cfg_autoclose, self.fr_opt_cfg_resize).cadre_th3()
            Frame.base(self.fr_opt_tcolors_th1, self.fr_opt_tcolors_th2, self.fr_opt_tcolors_th3, self.fr_opt_tcolors_bn1, self.fr_opt_tcolors_bn2, dim=P_dim().aw().h5()).th()
        def LABEL():
            Label.h1(self.lb_opt_info_nom).tr()
            Label.base(self.lb_opt_info_desc, self.lb_opt_info_auteur, self.lb_opt_info_version, self.lb_opt_ft_h1,
                       self.lb_opt_ft_h2, self.lb_opt_ft_h3, self.lb_opt_ft_h4, self.lb_opt_ft_h5, self.lb_opt_cfg_opacity,
                       self.lb_opt_cfg_autoreload, self.lb_opt_cfg_autoclose, self.lb_opt_cfg_resize, self.lb_opt_cfg_resize_width,
                       self.lb_opt_cfg_resize_height).tr()
        def PUSH_BUTTON():
            Push_button.dlg_ok(self.pb_opt_appliquer).txt()
            Push_button.dlg_ok(self.pb_opt_ok).txt_inv()
            Push_button.base_txt(self.pb_opt_gen_font, self.pb_opt_gen_config, self.pb_opt_tm_colors, self.pb_opt_tcolors_save).txt()
            Push_button.base(self.pb_opt_tm_th1).plein_th1()
            Push_button.base(self.pb_opt_tm_th2).plein_th2()
            Push_button.base(self.pb_opt_tm_th3).plein_th3()
            Push_button.base(self.pb_opt_tm_bn1).plein_bn1()
            Push_button.base(self.pb_opt_tm_bn2).plein_bn2()

            Push_button.rgb(self.pb_opt_tcolors_th1_cophex, self.pb_opt_tcolors_th2_cophex, self.pb_opt_tcolors_th3_cophex,
                                 self.pb_opt_tcolors_bn1_cophex, self.pb_opt_tcolors_bn2_cophex, dim=P_dim().carr().h8()).copier()
        def SPIN_BOX():
            Spin_box.plus_minus(self.sb_opt_ft_h1, self.sb_opt_ft_h2, self.sb_opt_ft_h3, self.sb_opt_ft_h4, self.sb_opt_ft_h5, self.sb_opt_cfg_opacity).bd_th3()
            Spin_box.plus_minus_infini(self.sb_opt_cfg_resize_width, self.sb_opt_cfg_resize_height).bd_th3()
        def TEXT_EDIT():
            Text_edit.h1(self.le_opt_ft_texte_h1).tr()
            Text_edit.h2(self.le_opt_ft_texte_h2).tr()
            Text_edit.h3(self.le_opt_ft_texte_h3).tr()
            Text_edit.h4(self.le_opt_ft_texte_h4).tr()
            Text_edit.h5(self.le_opt_ft_texte_h5).tr()
        def TREE_WIDGET():
            Tree_widget.base(self.trw_option).option()

        def _func_try():
            err = f"[ {self.objectName()} ] ne fonctionne pas !"

            try: COMBO_BOX()
            except: print(f"COMBO_BOX{err}")

            try: CHECK_BOX()
            except: print(f"CHECK_BOX{err}")

            try: FRAME()
            except: print(f"FRAME{err}")

            try: LABEL()
            except: print(f"LABEL{err}")

            try: PUSH_BUTTON()
            except: print(f"PUSH_BUTTON{err}")

            try: SPIN_BOX()
            except: print(f"SPIN_BOX{err}")

            try: TEXT_EDIT()
            except: print(f"TEXT_EDIT{err}")

            try: TREE_WIDGET()
            except: print(f"TREE_WIDGET{err}")
        _func_try()

        In_classe(ui=self)
    def IN_WG(self):
        # Base
        self.setCursor(Fct(cur=P_cur().souris()).CUR())
        self.setStyleSheet(f"background-color: rgb{P_rgb().th1()};")

        # Frame menu_top
        self.fr_menu_top.setFixedHeight(P_dim().h9())

        # Menu_top
        dim = P_dim().carr().h9()
        Fct(wg=self.lb_mt_ico, w=dim.get("w"), h=dim.get("h")).DIM()
        self.lb_mt_ico.setPixmap(QtGui.QPixmap(f"{self.ico}th3.svg"))
        self.lb_mt_ico.setScaledContents(True)
        self.lb_mt_nom.setText(self.titre)
        self.lb_mt_ico.setPixmap(QtGui.QPixmap(f"{self.ico}{self.tm}.svg"))
        self.lb_mt_ico.setScaledContents(True)

        # Configs
        try:
            self.fcb_opt_ft_font.setCurrentText(config.font)
            self.sb_opt_ft_h1.setValue(P_font().h1())
            self.sb_opt_ft_h2.setValue(P_font().h2())
            self.sb_opt_ft_h3.setValue(P_font().h3())
            self.sb_opt_ft_h4.setValue(P_font().h4())
            self.sb_opt_ft_h5.setValue(P_font().h5())

            self.sb_opt_cfg_opacity.setValue(config.opacity*100)
            self.ck_opt_cfg_autoreload.setChecked(True) if config.auto_reload == True else self.ck_opt_cfg_autoreload.setChecked(False)
            self.ck_opt_cfg_autoclose.setChecked(True) if config.auto_close == True else self.ck_opt_cfg_autoclose.setChecked(False)
            self.ck_opt_cfg_resize.setChecked(True) if config.resize == True else self.ck_opt_cfg_resize.setChecked(False)

            self.sb_opt_cfg_resize_width.setValue(config.widht)
            self.sb_opt_cfg_resize_height.setValue(config.height)
        except: pass
        self.pb_opt_ok.setDefault(True)

        # infos
        self.lb_opt_info_nom.setText(config.nom)
        self.lb_opt_info_desc.setText(config.description)
        self.lb_opt_info_auteur.setText(f"Auteur : {config.auteur}")
        self.lb_opt_info_version.setText(f"Version : {config.version}")

        # pb ok / appliquer
        self.pb_opt_ok.setText(self.txt_pb_ok)
        self.pb_opt_appliquer.setText(self.txt_pb_appliquer)
        self.pb_opt_appliquer.setDefault(True)
    def IN_CONNECTIONS(self):
        # Menu_top
        self.pb_mt_quitter.clicked.connect(lambda: self.close())

        self.trw_option.itemClicked.connect(self._set_opt)
        self.pb_opt_gen_font.clicked.connect(lambda: self.stk_option.setCurrentWidget(self.dct_pg.get("Polices")[0]))
        self.pb_opt_gen_config.clicked.connect(lambda: self.stk_option.setCurrentWidget(self.dct_pg.get("Configs")[0]))
        self.pb_opt_tm_colors.clicked.connect(lambda: self.stk_option.setCurrentWidget(self.dct_pg.get("T-Colors")[0]))

        # Connection value change
        self.fcb_opt_ft_font.currentTextChanged.connect(self._val_change_appliquer)
        self.sb_opt_ft_h1.valueChanged.connect(self._val_change_appliquer)
        self.sb_opt_ft_h2.valueChanged.connect(self._val_change_appliquer)
        self.sb_opt_ft_h3.valueChanged.connect(self._val_change_appliquer)
        self.sb_opt_ft_h4.valueChanged.connect(self._val_change_appliquer)
        self.sb_opt_ft_h5.valueChanged.connect(self._val_change_appliquer)

        self.sb_opt_cfg_opacity.valueChanged.connect(self._val_change_appliquer)
        self.sb_opt_cfg_resize_width.valueChanged.connect(lambda: self._val_change_appliquer(val="true"))
        self.sb_opt_cfg_resize_height.valueChanged.connect(lambda: self._val_change_appliquer(val="true"))
        self.ck_opt_cfg_autoreload.stateChanged.connect(self._val_change_appliquer)
        self.ck_opt_cfg_autoclose.stateChanged.connect(self._val_change_appliquer)
        self.ck_opt_cfg_resize.stateChanged.connect(lambda: self._val_change_appliquer(val="true"))

        self.cb_opt_tm_theme.currentTextChanged.connect(self._val_change_appliquer)

        # pb tm
        self.pb_opt_tm_th1.clicked.connect(lambda: self._pb_tm_maj(tm="th1"))
        self.pb_opt_tm_th2.clicked.connect(lambda: self._pb_tm_maj(tm="th2"))
        self.pb_opt_tm_th3.clicked.connect(lambda: self._pb_tm_maj(tm="th3"))
        self.pb_opt_tm_bn1.clicked.connect(lambda: self._pb_tm_maj(tm="bn1"))
        self.pb_opt_tm_bn2.clicked.connect(lambda: self._pb_tm_maj(tm="bn2"))

        self._space = QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Space), self)
        self._space.activated.connect(self._tm_random)

        self.pb_opt_tcolors_hex1.clicked.connect(lambda: pyperclip.copy(self.pb_opt_tcolors_hex1.text()))
        self.pb_opt_tcolors_hex2.clicked.connect(lambda: pyperclip.copy(self.pb_opt_tcolors_hex2.text()))
        self.pb_opt_tcolors_hex3.clicked.connect(lambda: pyperclip.copy(self.pb_opt_tcolors_hex3.text()))
        self.pb_opt_tcolors_hex4.clicked.connect(lambda: pyperclip.copy(self.pb_opt_tcolors_hex4.text()))
        self.pb_opt_tcolors_hex5.clicked.connect(lambda: pyperclip.copy(self.pb_opt_tcolors_hex5.text()))
        self.pb_opt_tcolors_hex6.clicked.connect(lambda: pyperclip.copy(self.pb_opt_tcolors_hex6.text()))
        self.pb_opt_tcolors_hex7.clicked.connect(lambda: pyperclip.copy(self.pb_opt_tcolors_hex7.text()))
        self.pb_opt_tcolors_hex8.clicked.connect(lambda: pyperclip.copy(self.pb_opt_tcolors_hex8.text()))
        self.pb_opt_tcolors_hex9.clicked.connect(lambda: pyperclip.copy(self.pb_opt_tcolors_hex9.text()))
        self.pb_opt_tcolors_hex10.clicked.connect(lambda: pyperclip.copy(self.pb_opt_tcolors_hex10.text()))
        self.pb_opt_tcolors_hex11.clicked.connect(lambda: pyperclip.copy(self.pb_opt_tcolors_hex11.text()))
        self.pb_opt_tcolors_hex12.clicked.connect(lambda: pyperclip.copy(self.pb_opt_tcolors_hex12.text()))
        self.pb_opt_tcolors_hex13.clicked.connect(lambda: pyperclip.copy(self.pb_opt_tcolors_hex13.text()))
        self.pb_opt_tcolors_hex14.clicked.connect(lambda: pyperclip.copy(self.pb_opt_tcolors_hex14.text()))
        self.pb_opt_tcolors_hex15.clicked.connect(lambda: pyperclip.copy(self.pb_opt_tcolors_hex15.text()))

        self.pb_opt_tcolors_th1_cophex.clicked.connect(lambda: self._tm_frame(fr=self.fr_opt_tcolors_th1))
        self.pb_opt_tcolors_th2_cophex.clicked.connect(lambda: self._tm_frame(fr=self.fr_opt_tcolors_th2))
        self.pb_opt_tcolors_th3_cophex.clicked.connect(lambda: self._tm_frame(fr=self.fr_opt_tcolors_th3))
        self.pb_opt_tcolors_bn1_cophex.clicked.connect(lambda: self._tm_frame(fr=self.fr_opt_tcolors_bn1))
        self.pb_opt_tcolors_bn2_cophex.clicked.connect(lambda: self._tm_frame(fr=self.fr_opt_tcolors_bn2))

        # pb ok
        self.pb_opt_ok.clicked.connect(lambda: self.FCT_OK())
        self.pb_opt_appliquer.clicked.connect(self._appliquer)
    def IN_WG_BASE(self):
        # stk
        self.stk_option.setCurrentWidget(self.pg_opt_menu)

        # pb appliquer
        self.pb_opt_appliquer.setVisible(False)
    def IN_ACT(self):
        self._maj_cb_theme()
        self._tm_random()
    def INIT(self):
        self.IN_BASE()
        self.IN_CLASSE()
        self.IN_WG()
        self.IN_CONNECTIONS()
        self.IN_WG_BASE()
        self.IN_ACT()


    ### ACTIONS
    def _reload(self):
        self.setCursor(QtCore.Qt.WaitCursor)

        importlib.reload(config)
        importlib.reload(rld)

        Fct().GEN_SVG()
        time.sleep(0.5)

        self.IN_WG()
        self.IN_CLASSE()

        self.fen.IN_BASE()
        self.fen.IN_CLASSE()

        # self.sgn_reload.emit()
        self.setCursor(Fct(cur=P_cur().souris()).CUR())

        if self.reload:
            Msg().INFO(msg="Modifications appliquées !\nCertains paramètres peuvent nécessiter un redémarrage de l'application.")
            self.reload = False

    def _maj_cb_theme(self):
        self.cb_opt_tm_theme.clear()
        for i, js in enumerate(glob.glob(f"{vrb.DO_THEME}*.json")):
            tm = os.path.basename(js).split(".")[0]
            self.cb_opt_tm_theme.addItem(tm)
            if tm == config.theme:
                self.cb_opt_tm_theme.setCurrentIndex(i)
    def _set_opt(self, item):
        self.stk_option.setCurrentWidget(self.dct_pg.get(item.text(0))[0])
    def _val_change_appliquer(self, val=""):
        if not self.pb_opt_appliquer.isVisible():
            self.pb_opt_appliquer.setVisible(True)
        if val == "true":
            self.reload = True
    def _appliquer(self):
        self.pb_opt_appliquer.setVisible(False)

        config_ini = Ini(lien_ini=vrb.INI_CONFIG)
        config = config_ini.OPEN_INI()
        config["config"]["theme"] = self.cb_opt_tm_theme.currentText()
        config["config"]["font"] = self.fcb_opt_ft_font.currentText()
        config["config"]["widht"] = f"{self.sb_opt_cfg_resize_width.value()}"
        config["config"]["height"] = f"{self.sb_opt_cfg_resize_height.value()}"
        config["config"]["opacity"] = f"{self.sb_opt_cfg_opacity.value() / 100}"
        config["var"]["autoreload"] = "true" if self.ck_opt_cfg_autoreload.isChecked() == True else "false"
        config["var"]["autoclose"] = "true" if self.ck_opt_cfg_autoclose.isChecked() == True else "false"
        config["var"]["resize"] = "true" if self.ck_opt_cfg_resize.isChecked() == True else "false"
        config_ini.WRITE_INI(ini=config)

        dct = {
            "h1": self.sb_opt_ft_h1.value(),
            "h2": self.sb_opt_ft_h2.value(),
            "h3": self.sb_opt_ft_h3.value(),
            "h4": self.sb_opt_ft_h4.value(),
            "h5": self.sb_opt_ft_h5.value(),
        }
        Json(lien_json=vrb.JS_FONT).UPDATE(dct)

        self._reload()

    def _pb_tm_maj(self, tm):
        dct_colors = {
            "th1": P_rgb().p_u1().get("c1"),
            "th2": P_rgb().p_u2().get("c1"),
            "th3": P_rgb().p_u3().get("c1"),
            "bn1": P_rgb().p_u_bn1().get("c1"),
            "bn2": P_rgb().p_u_bn2().get("c1")
        }
        rep, colors = Rgb().GET(rgb=dct_colors.get(tm))
        if rep:
            self._val_change_appliquer()

            dct = {
                f"{tm}": list(colors),
            }
            Json(lien_json=f"{vrb.DO_THEME}{config.theme}.json").UPDATE(dct)

            self._reload()
    def _tm_random(self):
        def __rgb_random(*args):
            for pb in args:
                colors = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
                Push_button.rgb(pb, colors={"c1": colors, "bn1": P_rgb().p_u_bn1()}, dim=P_dim().aw().h7()).uni()
                pb.setText(str(colors))

        __rgb_random(self.pb_opt_tcolors_hex1, self.pb_opt_tcolors_hex2, self.pb_opt_tcolors_hex3, self.pb_opt_tcolors_hex4, self.pb_opt_tcolors_hex5,
                     self.pb_opt_tcolors_hex6, self.pb_opt_tcolors_hex7, self.pb_opt_tcolors_hex8, self.pb_opt_tcolors_hex9, self.pb_opt_tcolors_hex10,
                     self.pb_opt_tcolors_hex11, self.pb_opt_tcolors_hex12, self.pb_opt_tcolors_hex13, self.pb_opt_tcolors_hex14, self.pb_opt_tcolors_hex15)
    def _tm_frame(self, fr):
        try:
            rgb = (int(pyperclip.paste()[1:-1].split(", ")[0]), int(pyperclip.paste()[1:-1].split(", ")[1]), int(pyperclip.paste()[1:-1].split(", ")[2]))
            Frame.base(fr, colors={"c1": rgb}, dim=P_dim().aw().h5()).th()

            Push_button.rgb(self.pb_opt_tcolors_th1_cophex, self.pb_opt_tcolors_th2_cophex, self.pb_opt_tcolors_th3_cophex,
                            self.pb_opt_tcolors_bn1_cophex, self.pb_opt_tcolors_bn2_cophex, dim=P_dim().carr().h8()).copier()
        except: return


    ### FONCTIONS
    def FCT_OK(self):
        if self.pb_opt_appliquer.isVisible():
            self._appliquer()
            self.close()
        else: self.close()


    ### EVENT
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

        try:
            if event.buttons() == QtCore.Qt.LeftButton and height_verif < P_dim().h9() and self.windowState() != QtCore.Qt.WindowMaximized:
                act_move(event)
            if event.buttons() == QtCore.Qt.LeftButton and height_verif < P_dim().h9() and self.windowState() == QtCore.Qt.WindowMaximized:
                self.setWindowState(QtCore.Qt.WindowNoState)
                act_move(event)
        except AttributeError: pass
