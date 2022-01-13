import glob
import os
import time

from PySide6 import QtCore, QtWidgets, QtGui

from .gui import *
from .build import *
from .config import *
from .In_classe import In_classe


class Dialog(dlg_ui.Ui_Dlg, QtWidgets.QDialog):
    sgn_rep = QtCore.Signal(bool)
    sgn_txt = QtCore.Signal(str)
    sgn_rgb = QtCore.Signal(list)
    sgn_reload = QtCore.Signal()

    def __init__(self, **kwargs):
        super(Dialog, self).__init__()

        self.kwargs = kwargs
        self.reload = False

        self.titre = self.kwargs.get("titre")
        if self.titre is None:
            self.titre = "Information"

        self.msg = self.kwargs.get("msg")
        if self.msg is None:
            self.msg = ":)"

        self.ico = self.kwargs.get("ico")
        if self.ico is None:
            self.ico = P_img().main()

        self.txt_pb_ok = self.kwargs.get("txt_pb_ok")
        if self.txt_pb_ok is None:
            self.txt_pb_ok = "Ok"

        self.txt_pb_appliquer = self.kwargs.get("txt_pb_appliquer")
        if self.txt_pb_appliquer is None:
            self.txt_pb_appliquer = "Appliquer"

        self.txt_pb_annuler = self.kwargs.get("txt_pb_annuler")
        if self.txt_pb_annuler is None:
            self.txt_pb_annuler = "Annuler"


        self.width = self.kwargs.get("width")
        if self.width is None: self.width = config.widht / 2

        self.height = self.kwargs.get("height")
        if self.height is None: self.height = config.height / 4

        self.opacity = self.kwargs.get("opacity")
        if self.opacity is None: self.opacity = 1

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setupUi(self)
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
            Combo_box.base(self.fcb_opt_ft_font, self.cb_opt_tm_theme).tr()
        def CHECK_BOX():
            Check_box.base(self.ck_opt_cfg_autoreload, self.ck_opt_cfg_autoclose, self.ck_opt_cfg_resize).tr()
        def FRAME():
            Frame.menu_bottom_dlg(self.fr_pg_dlg_msg, self.fr_pg_dlg_rep, self.fr_pg_dlg_input, self.fr_pg_dlg_option, self.fr_pg_dlg_colors).th()
            Frame.base(self.fr_opt_ft_h1, self.fr_opt_ft_h2, self.fr_opt_ft_h3, self.fr_opt_ft_h4, self.fr_opt_ft_h5,
                       self.fr_opt_cfg_opacity, self.fr_opt_cfg_autoclose, self.fr_opt_cfg_resize).cadre_th3()
        def LABEL():
            Label.h1(self.lb_opt_info_nom).tr()
            Label.base(self.lb_msg_texte, self.lb_rep_texte, self.lb_input_texte, self.lb_opt_info_desc, self.lb_opt_info_auteur,
                       self.lb_opt_info_version, self.lb_opt_ft_h1, self.lb_opt_ft_h2, self.lb_opt_ft_h3, self.lb_opt_ft_h4, self.lb_opt_ft_h5,
                       self.lb_opt_cfg_opacity, self.lb_opt_cfg_autoreload, self.lb_opt_cfg_autoclose, self.lb_opt_cfg_resize,
                       self.lb_opt_cfg_resize_width, self.lb_opt_cfg_resize_height).tr()
        def PUSH_BUTTON():
            Push_button.dlg_ok(self.pb_dlg_msg_ok, self.pb_dlg_rep_ok, self.pb_dlg_input_ok, self.pb_dlg_option_ok, self.pb_dlg_colors_ok).txt()
            Push_button.dlg_ok(self.pb_dlg_option_appliquer).txt_inv()
            Push_button.dlg_nok(self.pb_dlg_rep_annuler, self.pb_dlg_input_annuler).txt_inv()

            Push_button.base_txt(self.pb_opt_gen_font, self.pb_opt_gen_config, self.pb_opt_gen_cur, self.pb_opt_tm_colors).txt()

            Push_button.base(self.pb_opt_tm_th1).plein_th1()
            Push_button.base(self.pb_opt_tm_th2).plein_th2()
            Push_button.base(self.pb_opt_tm_th3).plein_th3()
            Push_button.base(self.pb_opt_tm_bn1).plein_bn1()
            Push_button.base(self.pb_opt_tm_bn2).plein_bn2()
        def SCROLL_BOX_AREA():
            Scroll_box_area.base(self.sca_option, self.sca_colors).invisible()
        def SLIDER():
            Slider.base(self.sd_opt_rgb_red, self.sd_opt_rgb_green, self.sd_opt_rgb_blue).rond()
        def SPIN_BOX():
            Spin_box.plus_minus(self.sb_opt_ft_h1, self.sb_opt_ft_h2, self.sb_opt_ft_h3, self.sb_opt_ft_h4, self.sb_opt_ft_h5, self.sb_opt_cfg_opacity).bd_th3()
            Spin_box.plus_minus_infini(self.sb_opt_cfg_resize_width, self.sb_opt_cfg_resize_height).bd_th3()
            Spin_box.rgb(self.spinBox).bd_th3()
        def TEXT_EDIT():
            Text_edit.h1(self.le_opt_ft_texte_h1).tr()
            Text_edit.h2(self.le_opt_ft_texte_h2).tr()
            Text_edit.h3(self.le_opt_ft_texte_h3).tr()
            Text_edit.h4(self.le_opt_ft_texte_h4).tr()
            Text_edit.h5(self.le_opt_ft_texte_h5).tr()


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

            try: SCROLL_BOX_AREA()
            except: print(f"SCROLL_BOX_AREA{err}")

            try: SLIDER()
            except: print(f"SLIDER{err}")

            try: SPIN_BOX()
            except: print(f"SPIN_BOX{err}")

            try: TEXT_EDIT()
            except: print(f"TEXT_EDIT{err}")
        _func_try()


        In_classe(ui=self)


        # QTreeWidget
        with C_trw() as C_:
            C_.option(self.trw_option)
    def IN_WG(self):
        # Base
        self.setCursor(Fct(cur=P_cur().souris()).CUR())
        self.setStyleSheet(f"background-color: rgb{P_rgb().th1()};")

        # Frame menu_top
        self.fr_menu_top.setFixedHeight(P_dim().h9())

        # Icone de l'app
        dim = P_dim().carr().h9()
        Fct(wg=self.lb_mt_ico, w=dim.get("w"), h=dim.get("h")).DIM()
        self.lb_mt_ico.setPixmap(QtGui.QPixmap(f"{self.ico}th3.svg"))
        self.lb_mt_ico.setScaledContents(True)
        self.lb_mt_nom.setText(self.titre)


        ### OPTION
        ""#info
        self.lb_opt_info_nom.setText(config.nom)
        self.lb_opt_info_desc.setText(config.description)
        self.lb_opt_info_auteur.setText(f"Auteur : {config.auteur}")
        self.lb_opt_info_version.setText(f"Version : {config.version}")
    def IN_WG_BASE(self):
        # Option
        self.pb_dlg_option_appliquer.setVisible(False)
        self.stk_option.setCurrentWidget(self.pg_opt_menu)
    def IN_CONNECTIONS(self):
        ## Menu_top
        self.pb_mt_quitter.clicked.connect(lambda: self.close())
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
    def _set_dlg(self, pg, ico=None):
        self.stk_dlg.setCurrentWidget(pg)

        if ico is None: ico = self.ico

        self.lb_mt_ico.setPixmap(QtGui.QPixmap(f"{ico}th3.svg"))
        self.lb_mt_ico.setScaledContents(True)
    def _close(self): self.close()
    def _rep(self):
        self.sgn_rep.emit(True)
        self.close()
    def _reload(self):
        self.setCursor(QtCore.Qt.WaitCursor)

        importlib.reload(config)

        Fct().GEN_SVG()
        time.sleep(0.5)

        self.IN_WG()
        self.IN_CLASSE()

        self.sgn_reload.emit()
        self.setCursor(Fct(cur=P_cur().souris()).CUR())

        if self.reload:
            dlg = Dialog(msg="Modifications appliquées !\nCertains paramètres peuvent nécessiter un redémarrage de l'application.")
            dlg.MSG(ico=P_img().info())
            dlg.exec()

            self.reload = False


    ### FONCTIONS
    def OPTION(self):
        def __set_opt(item):
            self.stk_option.setCurrentWidget(dct_pg.get(item.text(0))[0])
        def __val_change_appliquer(val=""):
            if not self.pb_dlg_option_appliquer.isVisible():
                self.pb_dlg_option_appliquer.setVisible(True)
            if val == "true":
                self.reload = True
        def __appliquer():
            self.pb_dlg_option_appliquer.setVisible(False)

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
        def __ok():
            if self .pb_dlg_option_appliquer.isVisible():
                __appliquer()
                self._close()
            else: self._close()

        def __maj_cb_theme():
            self.cb_opt_tm_theme.clear()
            for i, js in enumerate(glob.glob(f"{vrb.DO_THEME}*.json")):
                tm = os.path.basename(js).split(".")[0]
                self.cb_opt_tm_theme.addItem(tm)
                if tm == config.theme:
                    self.cb_opt_tm_theme.setCurrentIndex(i)


        dct_pg = {
            "Général": [self.pg_opt_gen],
            "Polices": [self.pg_opt_font],
            "Configs": [self.pg_opt_configs],
            "Curseurs": [self.pg_opt_cur],
            "Thèmes": [self.pg_opt_themes],
            "T-Colors": [self.pg_opt_tcolors],
            "Infos": [self.pg_opt_infos],
        }

        self._set_dlg(pg=self.pg_dlg_option)
        __maj_cb_theme()

        # Données
        self.pb_dlg_option_ok.setText(self.txt_pb_ok)
        self.pb_dlg_option_appliquer.setText(self.txt_pb_appliquer)

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


        self.pb_dlg_option_ok.setDefault(True)
        # Connection
        self.trw_option.itemClicked.connect(__set_opt)
        self.pb_opt_gen_font.clicked.connect(lambda: self.stk_option.setCurrentWidget(dct_pg.get("Polices")[0]))
        self.pb_opt_gen_config.clicked.connect(lambda: self.stk_option.setCurrentWidget(dct_pg.get("Configs")[0]))
        self.pb_opt_gen_cur.clicked.connect(lambda: self.stk_option.setCurrentWidget(dct_pg.get("Curseurs")[0]))
        self.pb_opt_tm_colors.clicked.connect(lambda: self.stk_option.setCurrentWidget(dct_pg.get("T-Colors")[0]))

        self.pb_dlg_option_ok.clicked.connect(__ok)
        self.pb_dlg_option_appliquer.clicked.connect(__appliquer)

        # Connection value change
        self.fcb_opt_ft_font.currentTextChanged.connect(__val_change_appliquer)
        self.sb_opt_ft_h1.valueChanged.connect(__val_change_appliquer)
        self.sb_opt_ft_h2.valueChanged.connect(__val_change_appliquer)
        self.sb_opt_ft_h3.valueChanged.connect(__val_change_appliquer)
        self.sb_opt_ft_h4.valueChanged.connect(__val_change_appliquer)
        self.sb_opt_ft_h5.valueChanged.connect(__val_change_appliquer)

        self.sb_opt_cfg_opacity.valueChanged.connect(__val_change_appliquer)
        self.sb_opt_cfg_resize_width.valueChanged.connect(lambda: __val_change_appliquer(val="true"))
        self.sb_opt_cfg_resize_height.valueChanged.connect(lambda: __val_change_appliquer(val="true"))
        self.ck_opt_cfg_autoreload.stateChanged.connect(__val_change_appliquer)
        self.ck_opt_cfg_autoclose.stateChanged.connect(__val_change_appliquer)
        self.ck_opt_cfg_resize.stateChanged.connect(lambda: __val_change_appliquer(val="true"))

        self.cb_opt_tm_theme.currentTextChanged.connect(__val_change_appliquer)
    def MSG(self, ico):
        self._set_dlg(pg=self.pg_dlg_msg, ico=ico)

        # Données
        self.lb_msg_texte.setText(self.msg)
        self.pb_dlg_msg_ok.setText(self.txt_pb_ok)

        # Connection
        self.pb_dlg_msg_ok.clicked.connect(self._close)
        self.pb_dlg_msg_ok.setDefault(True)
    def REP(self):
        self._set_dlg(pg=self.pg_dlg_rep)

        # Données
        self.lb_rep_texte.setText(self.msg)
        self.pb_dlg_rep_ok.setText(self.txt_pb_ok)
        self.pb_dlg_rep_annuler.setText(self.txt_pb_annuler)

        # Connection
        self.pb_dlg_rep_ok.clicked.connect(self._rep)
        self.pb_dlg_rep_annuler.clicked.connect(self._close)
        self.pb_dlg_rep_ok.setDefault(True)
    def INPUT(self):
        def __input():
            self.sgn_txt.emit(self.le_input.text())
            self.close()

        self._set_dlg(pg=self.pg_dlg_input)

        # Données
        self.lb_input_texte.setText(self.msg)
        self.pb_dlg_input_ok.setText(self.txt_pb_ok)
        self.pb_dlg_input_annuler.setText(self.txt_pb_annuler)

        # Connection
        self.pb_dlg_input_ok.clicked.connect(__input)
        self.pb_dlg_input_annuler.clicked.connect(self._close)
        self.pb_dlg_input_ok.setDefault(True)
    def COLORS(self):
        def __input():
            self.sgn_rgb.emit([0, 0, 0])
            self.close()

        self._set_dlg(pg=self.pg_dlg_colors)

        # Données
        self.pb_dlg_colors_ok.setText(self.txt_pb_ok)

        # Connection
        self.pb_dlg_colors_ok.clicked.connect(__input)
        self.pb_dlg_colors_ok.setDefault(True)




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
