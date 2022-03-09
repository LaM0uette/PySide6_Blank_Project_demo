import glob
import importlib
import os
import time

from PySide6 import QtCore, QtWidgets

from src import *
from src.gui.dlg.Msg.DLG_Msg import DLG_Msg
from src.gui.dlg.Rgb.DLG_Rgb import DLG_Rgb
from src.gui.ui import option_ui
from src.gui.events.Event import Event


class Option(option_ui.Ui_Option, QtWidgets.QDialog):
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
        super(Option, self).__init__()

        self.fen = fen
        self.titre = titre
        self.msg = msg
        self.ico = ico
        self.ico_rgb = tm
        self.txt_pb_ok = txt_pb_ok
        self.txt_pb_appliquer = txt_pb_appliquer
        self.width = width
        self.height = height
        self.opacity = opacity

        # Global
        self.reload = False

        self.INIT()

        self.dct_pg = {
            "Configs": [self.pg_opt_configs],
            "Thèmes": [self.pg_opt_themes],
            "Infos": [self.pg_opt_infos],
        }

        ### CREATION DES EVENT ###
        self.evt = Event(self)
        self.mousePressEvent = self.evt.mousePressEvent
        self.mouseMoveEvent = self.evt.mouseMoveEvent

    ############################
    ##     INITIALISATION     ##
    ############################
    def IN_BASE(self):
        ### Fenetre ###
        self.setWindowTitle(self.titre)
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)
        self.setWindowOpacity(self.opacity)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setGraphicsEffect(Shadow().ombre_portee(self))
        self.setWindowModality(QtCore.Qt.ApplicationModal)
    def IN_SETUP_UI(self):
        ### Ui ###
        self.setupUi(self)
        self.glay_main.setContentsMargins(v_gb.MARGIN_APP, v_gb.MARGIN_APP, v_gb.MARGIN_APP, v_gb.MARGIN_APP)
    def IN_CLASSE(self):
        ### QCheckBox ###
        CheckBox.Base(self.ck_opt_cfg_debug, self.ck_opt_cfg_autoclose, self.ck_opt_cfg_resize, self.ck_opt_cfg_ui_pin).tr()
        ### /QCheckBox ###


        ### QComboBox ###
        ComboBox.Base(self.fcb_opt_ft_font, self.cb_opt_tm_theme).th()
        ### /QComboBox ###


        ### QFrame ###
        Frame.Menu(self.fr_menu_top).top()
        Frame.Cadre(self.fr_main).th2()
        Frame.Cadre(
            self.fr_opt_cfg_opacity, self.fr_opt_cfg_autoclose, self.fr_opt_cfg_resize
        ).th3()
        Frame.Base(self.fr_body).th(rgb=Rgb().th1())
        Frame.Menu(self.fr_opt_bottom).bottom_dlg()
        ### /QFrame ###


        ### QLabel ###
        Label.Base(self.lb_mt_ico).ico_main()
        Label.Base(self.lb_mt_nom, font_size=Font().h3()).tr()
        Label.Base(self.lb_opt_info_nom).titre()
        Label.Base(
            self.lb_opt_info_desc, self.lb_opt_info_auteur, self.lb_opt_info_version, self.lb_opt_cfg_opacity,
            self.lb_opt_cfg_debug, self.lb_opt_cfg_autoclose, self.lb_opt_cfg_resize, self.lb_opt_cfg_ui_pin, self.lb_opt_cfg_resize_width,
            self.lb_opt_cfg_resize_height
        ).tr()
        ### /QLabel ###


        ### QPushButton ###
        PushButton.Dlg(self.pb_opt_appliquer).ok()
        PushButton.Dlg(self.pb_opt_ok).nok_inv()
        PushButton.menu_top(self.pb_mt_quitter).quitter()

        PushButton.plein(self.pb_opt_tm_th1).th1()
        PushButton.plein(self.pb_opt_tm_th2).th2()
        PushButton.plein(self.pb_opt_tm_th3).th3()
        PushButton.plein(self.pb_opt_tm_bn1).bn1()
        PushButton.plein(self.pb_opt_tm_bn2).bn2()
        ### /QPushButton ###


        ### QSpinBox ###
        SpinBox.Border(self.sb_opt_cfg_opacity).th()
        SpinBox.Border(self.sb_opt_cfg_resize_width, self.sb_opt_cfg_resize_height).inf()
        ### /QSpinBox ###


        ### QTreeWidget ###
        TreeWidget.Base(self.trw_option).option()
        ### /QTreeWidget ###
    def IN_WG(self):
        # Base
        self.setCursor(Functions().SET_CURSOR(cur=Cur().souris()))

        # Frame menu_top
        self.fr_menu_top.setFixedHeight(Dim().h9())

        # Menu_top
        self.lb_mt_nom.setText(self.titre)

        # Configs
        try:
            self.fcb_opt_ft_font.setCurrentText(config.font)

            self.sb_opt_cfg_opacity.setValue(config.opacity*100)
            self.ck_opt_cfg_debug.setChecked(True) if config.debug == True else self.ck_opt_cfg_debug.setChecked(False)
            self.ck_opt_cfg_autoclose.setChecked(True) if config.auto_close == True else self.ck_opt_cfg_autoclose.setChecked(False)
            self.ck_opt_cfg_resize.setChecked(True) if config.resize == True else self.ck_opt_cfg_resize.setChecked(False)
            self.ck_opt_cfg_ui_pin.setChecked(True) if config.toolbox_pin == True else self.ck_opt_cfg_ui_pin.setChecked(False)

            self.sb_opt_cfg_resize_width.setValue(config.widht)
            self.sb_opt_cfg_resize_height.setValue(config.height)
        except: pass

        # infos
        self.lb_opt_info_nom.setText(config.nom)
        self.lb_opt_info_desc.setText(config.description)
        self.lb_opt_info_auteur.setText(f"Auteur : {config.auteur}")
        self.lb_opt_info_version.setText(f"Version : {config.version}")

        # pb dlg
        self.pb_opt_ok.setText(self.txt_pb_ok)
        self.pb_opt_ok.setDefault(True)
        self.pb_opt_appliquer.setText(self.txt_pb_appliquer)
        self.pb_opt_appliquer.setDefault(True)
    def IN_CONNECTIONS(self):
        # Menu_top
        self.pb_mt_quitter.clicked.connect(lambda: self.close())
        self.trw_option.itemClicked.connect(self._set_opt)

        # Connection value change #
        ## font combo box
        self.fcb_opt_ft_font.currentTextChanged.connect(self._val_change_appliquer)

        ## slider
        self.sb_opt_cfg_opacity.valueChanged.connect(self._val_change_appliquer)
        self.sb_opt_cfg_resize_width.valueChanged.connect(lambda: self._val_change_appliquer(val="true"))
        self.sb_opt_cfg_resize_height.valueChanged.connect(lambda: self._val_change_appliquer(val="true"))
        self.ck_opt_cfg_debug.stateChanged.connect(self._val_change_appliquer)
        self.ck_opt_cfg_autoclose.stateChanged.connect(self._val_change_appliquer)
        self.ck_opt_cfg_resize.stateChanged.connect(lambda: self._val_change_appliquer(val="true"))
        self.ck_opt_cfg_ui_pin.stateChanged.connect(lambda: self._val_change_appliquer(val="true"))
        ## combo box theme
        self.cb_opt_tm_theme.currentTextChanged.connect(self._val_change_appliquer)

        # pb tm
        self.pb_opt_tm_th1.clicked.connect(lambda: self._pb_tm_maj(rgb="th1"))
        self.pb_opt_tm_th2.clicked.connect(lambda: self._pb_tm_maj(rgb="th2"))
        self.pb_opt_tm_th3.clicked.connect(lambda: self._pb_tm_maj(rgb="th3"))
        self.pb_opt_tm_bn1.clicked.connect(lambda: self._pb_tm_maj(rgb="bn1"))
        self.pb_opt_tm_bn2.clicked.connect(lambda: self._pb_tm_maj(rgb="bn2"))

        # pb dlg
        self.pb_opt_ok.clicked.connect(lambda: self.OK())
        self.pb_opt_appliquer.clicked.connect(self._appliquer)
    def IN_ACT(self):
        # MAJ de la liste des thèmes
        self._maj_cb_theme()
    def IN_WG_BASE(self):
        # pb appliquer
        self.pb_opt_appliquer.setVisible(False)
    def INIT(self):
        self.IN_BASE()
        self.IN_SETUP_UI()
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
    def __reload(self):
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)

        importlib.reload(config)

        Functions().GEN_SVG()
        time.sleep(0.5)

        # importlib.reload(rld)

        self.IN_WG()
        self.IN_CLASSE()

        self.fen.IN_BASE()
        self.fen.IN_CLASSE()

        QtWidgets.QApplication.restoreOverrideCursor()

        if self.reload:
            DLG_Msg().INFO(msg="Modifications appliquées !\nCertains paramètres peuvent nécessiter un redémarrage de l'application.")
            self.reload = False
    ## configuration
    def _maj_cb_theme(self):
        self.cb_opt_tm_theme.clear()

        for i, js in enumerate(glob.glob(f"src/theme/*.json")):
            tm = os.path.basename(js).split(".")[0]
            self.cb_opt_tm_theme.addItem(tm)
            if tm == config.theme:
                self.cb_opt_tm_theme.setCurrentIndex(i)
    def _set_opt(self, item):
        self.stk_option.setCurrentWidget(self.dct_pg.get(item.text(0))[0])
    def _pb_tm_maj(self, rgb):
        dct_colors = {
            "th1": Rgb().th1(),
            "th2": Rgb().th2(),
            "th3": Rgb().th3(),
            "bn1": Rgb().bn1(),
            "bn2": Rgb().bn2(),
        }
        rep, colors = DLG_Rgb().GET(rgb=dct_colors.get(rgb))
        if rep:
            self._val_change_appliquer()

            dct = {
                f"{rgb}": list(colors),
            }
            Json(lien_json=f"src/theme/{config.theme}.json").UPDATE(dct)

            self.__reload()

    # application des modifs
    def _val_change_appliquer(self, val=""):
        if not self.pb_opt_appliquer.isVisible():
            self.pb_opt_appliquer.setVisible(True)
        if val == "true":
            self.reload = True
    def _appliquer(self):
        self.pb_opt_appliquer.setVisible(False)

        dct = {
            "config": {
                "theme": self.cb_opt_tm_theme.currentText(),
                "font": self.fcb_opt_ft_font.currentText(),
                "widht": f"{self.sb_opt_cfg_resize_width.value()}",
                "height": f"{self.sb_opt_cfg_resize_height.value()}",
                "opacity": f"{self.sb_opt_cfg_opacity.value() / 100}"
            },

            "var": {
                "debug": True if self.ck_opt_cfg_debug.isChecked() else False,
                "resize": True if self.ck_opt_cfg_resize.isChecked() else False,
                "auto_close": True if self.ck_opt_cfg_autoclose.isChecked() else False,
                "toolbox_pin": True if self.ck_opt_cfg_ui_pin.isChecked() else False
            },
        }
        Json(lien_json=f"src/config/config.json").UPDATE(dct)

        self.__reload()
    #####################
    ##    /ACTIONS     ##
    #####################


    #######################
    ##     FONCTIONS     ##
    #######################
    def OK(self):
        if self.pb_opt_appliquer.isVisible():
            self._appliquer()
        self.close()
    #######################
    ##    /FONCTIONS     ##
    #######################
