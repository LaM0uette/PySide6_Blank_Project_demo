from PySide6 import QtCore, QtWidgets, QtGui

from .gui import *
from .build import *
from .config import *
from .In_classe import In_classe


class Dialog(dlg_ui.Ui_Dlg, QtWidgets.QDialog):
    sgn_rep = QtCore.Signal(bool)
    sgn_txt = QtCore.Signal(str)

    def __init__(self, **kwargs):
        super(Dialog, self).__init__()

        self.kwargs = kwargs

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
        # QLineEdit | QTextEdit | QPlainTextEdit
        with C_txt() as C_:
            C_.tr(self.le_input)
            C_.tr_h1(self.le_opt_ft_texte_h1)
            C_.tr_h2(self.le_opt_ft_texte_h2)
            C_.tr_h3(self.le_opt_ft_texte_h3)
            C_.tr_h4(self.le_opt_ft_texte_h4)
            C_.tr_h5(self.le_opt_ft_texte_h5)

        # QScrollBoxArea
        with C_sca() as C_:
            C_.invisible(self.sca_option)

        In_classe(ui=self)

        # QComboBox
        with C_cb() as C_:
            C_.font(self.fcb_opt_ft_font)

        # QFrame
        with C_fr() as C_:
            C_.menu_bottom_dlg(self.fr_pg_dlg_msg, self.fr_pg_dlg_rep, self.fr_pg_dlg_input, self.fr_pg_dlg_option)
            C_.option_font(self.fr_opt_ft_h1, self.fr_opt_ft_h2, self.fr_opt_ft_h3, self.fr_opt_ft_h4, self.fr_opt_ft_h5)

        # QLabel
        with C_lb() as C_:
            C_.h1(self.lb_opt_info_nom)
            C_.p(self.lb_msg_texte, self.lb_rep_texte, self.lb_input_texte, self.lb_opt_info_desc, self.lb_opt_info_auteur, self.lb_opt_info_version,
                 self.lb_opt_ft_h1, self.lb_opt_ft_h2, self.lb_opt_ft_h3, self.lb_opt_ft_h4, self.lb_opt_ft_h5)

        # QPushButton
        with C_pb() as C_:
            C_.ok(self.pb_dlg_msg_ok, self.pb_dlg_rep_ok, self.pb_dlg_input_ok, self.pb_dlg_option_ok)
            C_.appliquer(self.pb_dlg_option_appliquer)
            C_.annuler(self.pb_dlg_rep_annuler, self.pb_dlg_input_annuler, self.pb_dlg_option_annuler)
            C_.txt_h9(self.pb_opt_gen_font, self.pb_opt_gen_config, self.pb_opt_gen_cur, self.pb_opt_theme_colors)

        # QSpinBox | QDoubleSpinBox
        with C_sb() as C_:
            C_.th1(self.sb_opt_ft_h1, self.sb_opt_ft_h2, self.sb_opt_ft_h3, self.sb_opt_ft_h4, self.sb_opt_ft_h5)

        # QTreeWidget
        with C_trw() as C_:
            C_.option(self.trw_option)
    def IN_WG(self):
        # Base
        self.setCursor(Fct(cur="souris").CUR())
        self.setStyleSheet(f"background-color: rgb{P_rgb().th1()};")

        # Frame menu_top
        self.fr_menu_top.setFixedHeight(P_dim().h_mt())

        # Icone de l'app
        dim = P_dim().p_c_mt()
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
        self.pb_dlg_option_appliquer.setVisible(True)
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


    ### FONCTIONS
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

    def OPTION(self):
        def __set_opt(item):

            self.stk_option.setCurrentWidget(dct_pg.get(item.text(0))[0])
        def __appliquer():
            self.pb_dlg_option_appliquer.setVisible(False)

            self.config_ini = functions.INI(lien_ini=vrb.ini_cfg)
            self.cfg = self.config_ini.OPEN_INI()
            self.cfg["config"]["theme"] = self.cb_choix_theme.currentText()

            self.config_ini.WRITE_INI(ini=self.cfg)

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

        # Données
        self.pb_dlg_option_ok.setText(self.txt_pb_ok)
        self.pb_dlg_option_appliquer.setText(self.txt_pb_appliquer)
        self.pb_dlg_option_annuler.setText(self.txt_pb_annuler)

        try:
            self.fcb_opt_ft_font.setCurrentText(config.font)
            self.sb_opt_ft_h1.setValue(P_font().h1())
            self.sb_opt_ft_h2.setValue(P_font().h2())
            self.sb_opt_ft_h3.setValue(P_font().h3())
            self.sb_opt_ft_h4.setValue(P_font().h4())
            self.sb_opt_ft_h5.setValue(P_font().h5())
        except: pass


        # Connection
        self.pb_dlg_option_ok.setDefault(True)
        self.trw_option.itemClicked.connect(__set_opt)
        self.pb_dlg_option_ok.clicked.connect(self._rep)
        self.pb_dlg_option_appliquer.clicked.connect(__appliquer)
        self.pb_dlg_option_annuler.clicked.connect(self._close)
        self.pb_opt_gen_font.clicked.connect(lambda: self.stk_option.setCurrentWidget(dct_pg.get("Polices")[0]))
        self.pb_opt_gen_config.clicked.connect(lambda: self.stk_option.setCurrentWidget(dct_pg.get("Configs")[0]))
        self.pb_opt_gen_cur.clicked.connect(lambda: self.stk_option.setCurrentWidget(dct_pg.get("Curseurs")[0]))
        self.pb_opt_theme_colors.clicked.connect(lambda: self.stk_option.setCurrentWidget(dct_pg.get("T-Colors")[0]))


    ### EVENT
    def mousePressEvent(self, event):
        cur = QtGui.QCursor()
        verifHeight = cur.pos().y() - self.pos().y()
        if event.buttons() == QtCore.Qt.LeftButton and verifHeight < P_dim().h_mt() and self.windowState() != QtCore.Qt.WindowMaximized:
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
            if event.buttons() == QtCore.Qt.LeftButton and height_verif < P_dim().h_mt() and self.windowState() != QtCore.Qt.WindowMaximized:
                act_move(event)
            if event.buttons() == QtCore.Qt.LeftButton and height_verif < P_dim().h_mt() and self.windowState() == QtCore.Qt.WindowMaximized:
                self.setWindowState(QtCore.Qt.WindowNoState)
                act_move(event)
        except AttributeError: pass
