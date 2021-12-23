# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'option.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QToolBox, QVBoxLayout, QWidget)

from src.classe_wg import PB_ZOOM

class Ui_option(object):
    def setupUi(self, option):
        if not option.objectName():
            option.setObjectName(u"option")
        option.resize(674, 629)
        self.vlay_dlg = QVBoxLayout(option)
        self.vlay_dlg.setSpacing(0)
        self.vlay_dlg.setObjectName(u"vlay_dlg")
        self.vlay_dlg.setContentsMargins(0, 0, 0, 0)
        self.fr_bg_dlg = QFrame(option)
        self.fr_bg_dlg.setObjectName(u"fr_bg_dlg")
        self.fr_bg_dlg.setFrameShape(QFrame.StyledPanel)
        self.fr_bg_dlg.setFrameShadow(QFrame.Raised)
        self.vlay_bg_dlg = QVBoxLayout(self.fr_bg_dlg)
        self.vlay_bg_dlg.setSpacing(0)
        self.vlay_bg_dlg.setObjectName(u"vlay_bg_dlg")
        self.vlay_bg_dlg.setContentsMargins(0, 0, 0, 0)
        self.fr_menu_top = QFrame(self.fr_bg_dlg)
        self.fr_menu_top.setObjectName(u"fr_menu_top")
        self.fr_menu_top.setFrameShape(QFrame.StyledPanel)
        self.fr_menu_top.setFrameShadow(QFrame.Raised)
        self.hlay_menu_top = QHBoxLayout(self.fr_menu_top)
        self.hlay_menu_top.setSpacing(0)
        self.hlay_menu_top.setObjectName(u"hlay_menu_top")
        self.hlay_menu_top.setContentsMargins(0, 0, 0, 0)
        self.wg_mt_blank = QWidget(self.fr_menu_top)
        self.wg_mt_blank.setObjectName(u"wg_mt_blank")

        self.hlay_menu_top.addWidget(self.wg_mt_blank)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_menu_top.addItem(self.horizontalSpacer_2)

        self.lb_mt_nom = QLabel(self.fr_menu_top)
        self.lb_mt_nom.setObjectName(u"lb_mt_nom")

        self.hlay_menu_top.addWidget(self.lb_mt_nom)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_menu_top.addItem(self.horizontalSpacer)

        self.pb_mt_quitter = PB_ZOOM(self.fr_menu_top)
        self.pb_mt_quitter.setObjectName(u"pb_mt_quitter")

        self.hlay_menu_top.addWidget(self.pb_mt_quitter)


        self.vlay_bg_dlg.addWidget(self.fr_menu_top)

        self.glay_main = QGridLayout()
        self.glay_main.setSpacing(0)
        self.glay_main.setObjectName(u"glay_main")
        self.glay_main.setContentsMargins(5, -1, 5, 5)
        self.hlay_valider_annuler = QHBoxLayout()
        self.hlay_valider_annuler.setSpacing(5)
        self.hlay_valider_annuler.setObjectName(u"hlay_valider_annuler")
        self.pb_appliquer = QPushButton(self.fr_bg_dlg)
        self.pb_appliquer.setObjectName(u"pb_appliquer")

        self.hlay_valider_annuler.addWidget(self.pb_appliquer)

        self.pb_ok = QPushButton(self.fr_bg_dlg)
        self.pb_ok.setObjectName(u"pb_ok")

        self.hlay_valider_annuler.addWidget(self.pb_ok)


        self.glay_main.addLayout(self.hlay_valider_annuler, 8, 0, 1, 1)

        self.tb_option = QToolBox(self.fr_bg_dlg)
        self.tb_option.setObjectName(u"tb_option")
        self.pg_opt_theme = QWidget()
        self.pg_opt_theme.setObjectName(u"pg_opt_theme")
        self.pg_opt_theme.setGeometry(QRect(0, 0, 662, 481))
        self.vlay_pg_opt_theme = QVBoxLayout(self.pg_opt_theme)
        self.vlay_pg_opt_theme.setSpacing(0)
        self.vlay_pg_opt_theme.setObjectName(u"vlay_pg_opt_theme")
        self.vlay_pg_opt_theme.setContentsMargins(0, 0, 0, 0)
        self.fr_opt_theme = QFrame(self.pg_opt_theme)
        self.fr_opt_theme.setObjectName(u"fr_opt_theme")
        self.fr_opt_theme.setFrameShape(QFrame.StyledPanel)
        self.fr_opt_theme.setFrameShadow(QFrame.Raised)
        self.glay_tb_pg_theme = QGridLayout(self.fr_opt_theme)
        self.glay_tb_pg_theme.setSpacing(0)
        self.glay_tb_pg_theme.setObjectName(u"glay_tb_pg_theme")
        self.glay_tb_pg_theme.setContentsMargins(5, 0, 5, 5)
        self.hlay_nom_theme = QHBoxLayout()
        self.hlay_nom_theme.setSpacing(10)
        self.hlay_nom_theme.setObjectName(u"hlay_nom_theme")
        self.lb_nom_theme = QLabel(self.fr_opt_theme)
        self.lb_nom_theme.setObjectName(u"lb_nom_theme")

        self.hlay_nom_theme.addWidget(self.lb_nom_theme)

        self.le_nom_theme = QLineEdit(self.fr_opt_theme)
        self.le_nom_theme.setObjectName(u"le_nom_theme")
        self.le_nom_theme.setMinimumSize(QSize(200, 0))

        self.hlay_nom_theme.addWidget(self.le_nom_theme)


        self.glay_tb_pg_theme.addLayout(self.hlay_nom_theme, 2, 4, 1, 1)

        self.pb_creer_theme = QPushButton(self.fr_opt_theme)
        self.pb_creer_theme.setObjectName(u"pb_creer_theme")

        self.glay_tb_pg_theme.addWidget(self.pb_creer_theme, 6, 0, 1, 7)

        self.glay_gestion_theme = QGridLayout()
        self.glay_gestion_theme.setObjectName(u"glay_gestion_theme")
        self.glay_gestion_theme.setHorizontalSpacing(5)
        self.glay_gestion_theme.setVerticalSpacing(20)
        self.glay_gestion_theme.setContentsMargins(0, 0, 0, 0)
        self.pb_bn1 = QPushButton(self.fr_opt_theme)
        self.pb_bn1.setObjectName(u"pb_bn1")

        self.glay_gestion_theme.addWidget(self.pb_bn1, 0, 8, 1, 1)

        self.pb_bn2 = QPushButton(self.fr_opt_theme)
        self.pb_bn2.setObjectName(u"pb_bn2")

        self.glay_gestion_theme.addWidget(self.pb_bn2, 1, 8, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.glay_gestion_theme.addItem(self.horizontalSpacer_7, 0, 9, 2, 1)

        self.lb_th4 = QLabel(self.fr_opt_theme)
        self.lb_th4.setObjectName(u"lb_th4")

        self.glay_gestion_theme.addWidget(self.lb_th4, 1, 4, 1, 1)

        self.lb_th3 = QLabel(self.fr_opt_theme)
        self.lb_th3.setObjectName(u"lb_th3")

        self.glay_gestion_theme.addWidget(self.lb_th3, 0, 4, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.glay_gestion_theme.addItem(self.horizontalSpacer_9, 0, 6, 2, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.glay_gestion_theme.addItem(self.horizontalSpacer_6, 0, 0, 2, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.glay_gestion_theme.addItem(self.horizontalSpacer_8, 0, 3, 2, 1)

        self.pb_th1 = QPushButton(self.fr_opt_theme)
        self.pb_th1.setObjectName(u"pb_th1")

        self.glay_gestion_theme.addWidget(self.pb_th1, 0, 2, 1, 1)

        self.pb_th2 = QPushButton(self.fr_opt_theme)
        self.pb_th2.setObjectName(u"pb_th2")

        self.glay_gestion_theme.addWidget(self.pb_th2, 1, 2, 1, 1)

        self.pb_th4 = QPushButton(self.fr_opt_theme)
        self.pb_th4.setObjectName(u"pb_th4")

        self.glay_gestion_theme.addWidget(self.pb_th4, 1, 5, 1, 1)

        self.pb_th3 = QPushButton(self.fr_opt_theme)
        self.pb_th3.setObjectName(u"pb_th3")

        self.glay_gestion_theme.addWidget(self.pb_th3, 0, 5, 1, 1)

        self.lb_bn2 = QLabel(self.fr_opt_theme)
        self.lb_bn2.setObjectName(u"lb_bn2")

        self.glay_gestion_theme.addWidget(self.lb_bn2, 1, 7, 1, 1)

        self.lb_bn1 = QLabel(self.fr_opt_theme)
        self.lb_bn1.setObjectName(u"lb_bn1")

        self.glay_gestion_theme.addWidget(self.lb_bn1, 0, 7, 1, 1)

        self.lb_th1 = QLabel(self.fr_opt_theme)
        self.lb_th1.setObjectName(u"lb_th1")

        self.glay_gestion_theme.addWidget(self.lb_th1, 0, 1, 1, 1)

        self.lb_th2 = QLabel(self.fr_opt_theme)
        self.lb_th2.setObjectName(u"lb_th2")

        self.glay_gestion_theme.addWidget(self.lb_th2, 1, 1, 1, 1)


        self.glay_tb_pg_theme.addLayout(self.glay_gestion_theme, 4, 0, 1, 7)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.glay_tb_pg_theme.addItem(self.verticalSpacer, 0, 0, 1, 7)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.glay_tb_pg_theme.addItem(self.horizontalSpacer_11, 2, 6, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.glay_tb_pg_theme.addItem(self.verticalSpacer_7, 3, 0, 1, 7)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.glay_tb_pg_theme.addItem(self.verticalSpacer_2, 5, 0, 1, 7)

        self.pb_modif_theme = QPushButton(self.fr_opt_theme)
        self.pb_modif_theme.setObjectName(u"pb_modif_theme")

        self.glay_tb_pg_theme.addWidget(self.pb_modif_theme, 8, 0, 1, 7)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.glay_tb_pg_theme.addItem(self.horizontalSpacer_12, 2, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.glay_tb_pg_theme.addItem(self.verticalSpacer_5, 9, 0, 1, 7)

        self.pb_supp_theme = QPushButton(self.fr_opt_theme)
        self.pb_supp_theme.setObjectName(u"pb_supp_theme")

        self.glay_tb_pg_theme.addWidget(self.pb_supp_theme, 10, 0, 1, 7)

        self.verticalSpacer_14 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.glay_tb_pg_theme.addItem(self.verticalSpacer_14, 7, 0, 1, 7)


        self.vlay_pg_opt_theme.addWidget(self.fr_opt_theme)

        self.tb_option.addItem(self.pg_opt_theme, u"> GESTION DES TH\u00c8MES")
        self.pg_opt_affichages = QWidget()
        self.pg_opt_affichages.setObjectName(u"pg_opt_affichages")
        self.pg_opt_affichages.setGeometry(QRect(0, 0, 662, 481))
        self.vlay_pg_opt_affichages = QVBoxLayout(self.pg_opt_affichages)
        self.vlay_pg_opt_affichages.setSpacing(0)
        self.vlay_pg_opt_affichages.setObjectName(u"vlay_pg_opt_affichages")
        self.vlay_pg_opt_affichages.setContentsMargins(0, 0, 0, 0)
        self.fr_opt_affichages = QFrame(self.pg_opt_affichages)
        self.fr_opt_affichages.setObjectName(u"fr_opt_affichages")
        self.fr_opt_affichages.setFrameShape(QFrame.StyledPanel)
        self.fr_opt_affichages.setFrameShadow(QFrame.Raised)
        self.glay_pg_options = QGridLayout(self.fr_opt_affichages)
        self.glay_pg_options.setSpacing(0)
        self.glay_pg_options.setObjectName(u"glay_pg_options")
        self.glay_pg_options.setContentsMargins(0, 0, 0, 0)
        self.lb_parametre_titre = QLabel(self.fr_opt_affichages)
        self.lb_parametre_titre.setObjectName(u"lb_parametre_titre")

        self.glay_pg_options.addWidget(self.lb_parametre_titre, 6, 1, 1, 3)

        self.verticalSpacer_10 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.glay_pg_options.addItem(self.verticalSpacer_10, 11, 1, 1, 3)

        self.verticalSpacer_13 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.glay_pg_options.addItem(self.verticalSpacer_13, 8, 1, 1, 3)

        self.lb_auto_close = QLabel(self.fr_opt_affichages)
        self.lb_auto_close.setObjectName(u"lb_auto_close")

        self.glay_pg_options.addWidget(self.lb_auto_close, 13, 1, 1, 1)

        self.ckb_auto_close = QCheckBox(self.fr_opt_affichages)
        self.ckb_auto_close.setObjectName(u"ckb_auto_close")

        self.glay_pg_options.addWidget(self.ckb_auto_close, 13, 3, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.glay_pg_options.addItem(self.verticalSpacer_12, 3, 1, 1, 3)

        self.lb_auto_reload = QLabel(self.fr_opt_affichages)
        self.lb_auto_reload.setObjectName(u"lb_auto_reload")

        self.glay_pg_options.addWidget(self.lb_auto_reload, 10, 1, 1, 1)

        self.ckb_auto_reload = QCheckBox(self.fr_opt_affichages)
        self.ckb_auto_reload.setObjectName(u"ckb_auto_reload")

        self.glay_pg_options.addWidget(self.ckb_auto_reload, 10, 3, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.glay_pg_options.addItem(self.verticalSpacer_8, 14, 1, 1, 3)

        self.lb_opacity = QLabel(self.fr_opt_affichages)
        self.lb_opacity.setObjectName(u"lb_opacity")

        self.glay_pg_options.addWidget(self.lb_opacity, 4, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.glay_pg_options.addItem(self.horizontalSpacer_5, 4, 2, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.glay_pg_options.addItem(self.verticalSpacer_9, 5, 1, 1, 3)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.glay_pg_options.addItem(self.verticalSpacer_11, 0, 1, 1, 3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.glay_pg_options.addItem(self.horizontalSpacer_3, 0, 4, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.glay_pg_options.addItem(self.horizontalSpacer_4, 0, 0, 1, 1)

        self.lb_opacity_titre = QLabel(self.fr_opt_affichages)
        self.lb_opacity_titre.setObjectName(u"lb_opacity_titre")

        self.glay_pg_options.addWidget(self.lb_opacity_titre, 1, 1, 1, 3)

        self.line = QFrame(self.fr_opt_affichages)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.glay_pg_options.addWidget(self.line, 2, 1, 1, 3)

        self.line_2 = QFrame(self.fr_opt_affichages)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.glay_pg_options.addWidget(self.line_2, 7, 1, 1, 3)

        self.sp_opacity = QSpinBox(self.fr_opt_affichages)
        self.sp_opacity.setObjectName(u"sp_opacity")
        self.sp_opacity.setMaximum(100)

        self.glay_pg_options.addWidget(self.sp_opacity, 4, 3, 1, 1)


        self.vlay_pg_opt_affichages.addWidget(self.fr_opt_affichages)

        self.tb_option.addItem(self.pg_opt_affichages, u"> OPTIONS D'AFFICHAGES")

        self.glay_main.addWidget(self.tb_option, 4, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.glay_main.addItem(self.verticalSpacer_6, 7, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.glay_main.addItem(self.verticalSpacer_3, 3, 0, 1, 1)

        self.lb_choix_theme = QLabel(self.fr_bg_dlg)
        self.lb_choix_theme.setObjectName(u"lb_choix_theme")

        self.glay_main.addWidget(self.lb_choix_theme, 0, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.glay_main.addItem(self.verticalSpacer_4, 1, 0, 1, 1)

        self.cb_choix_theme = QComboBox(self.fr_bg_dlg)
        self.cb_choix_theme.setObjectName(u"cb_choix_theme")

        self.glay_main.addWidget(self.cb_choix_theme, 2, 0, 1, 1)


        self.vlay_bg_dlg.addLayout(self.glay_main)


        self.vlay_dlg.addWidget(self.fr_bg_dlg)


        self.retranslateUi(option)

        self.tb_option.layout().setSpacing(0)


        QMetaObject.connectSlotsByName(option)
    # setupUi

    def retranslateUi(self, option):
        option.setWindowTitle(QCoreApplication.translate("option", u"Dialog", None))
        self.pb_appliquer.setText(QCoreApplication.translate("option", u"APPLIQUER", None))
        self.pb_ok.setText(QCoreApplication.translate("option", u"OK", None))
        self.lb_nom_theme.setText(QCoreApplication.translate("option", u"Nom du th\u00e8me :", None))
        self.le_nom_theme.setPlaceholderText(QCoreApplication.translate("option", u"Nom du th\u00e8me...", None))
        self.pb_creer_theme.setText(QCoreApplication.translate("option", u"CREER UN THEME", None))
        self.pb_bn1.setText(QCoreApplication.translate("option", u"200_20_20", None))
        self.pb_bn2.setText(QCoreApplication.translate("option", u"20_200_20", None))
        self.lb_th4.setText(QCoreApplication.translate("option", u"TH4 :", None))
        self.lb_th3.setText(QCoreApplication.translate("option", u"TH3 :", None))
        self.pb_th1.setText(QCoreApplication.translate("option", u"20_20_20", None))
        self.pb_th2.setText(QCoreApplication.translate("option", u"50_50_50", None))
        self.pb_th4.setText(QCoreApplication.translate("option", u"120_120_120", None))
        self.pb_th3.setText(QCoreApplication.translate("option", u"80_80_80", None))
        self.lb_bn2.setText(QCoreApplication.translate("option", u"BN2 :", None))
        self.lb_bn1.setText(QCoreApplication.translate("option", u"BN1 :", None))
        self.lb_th1.setText(QCoreApplication.translate("option", u"TH1 :", None))
        self.lb_th2.setText(QCoreApplication.translate("option", u"TH2 :", None))
        self.pb_modif_theme.setText(QCoreApplication.translate("option", u"MODIFIER LE THEME", None))
        self.pb_supp_theme.setText(QCoreApplication.translate("option", u"SUPPRIMER CE THEME", None))
        self.tb_option.setItemText(self.tb_option.indexOf(self.pg_opt_theme), QCoreApplication.translate("option", u"> GESTION DES TH\u00c8MES", None))
        self.lb_parametre_titre.setText(QCoreApplication.translate("option", u"PARAMETRE :", None))
        self.lb_auto_close.setText(QCoreApplication.translate("option", u"Auto close :", None))
        self.lb_auto_reload.setText(QCoreApplication.translate("option", u"Auto reload :", None))
        self.lb_opacity.setText(QCoreApplication.translate("option", u"Opacit\u00e9 :", None))
        self.lb_opacity_titre.setText(QCoreApplication.translate("option", u"AFFICHAGE :", None))
        self.tb_option.setItemText(self.tb_option.indexOf(self.pg_opt_affichages), QCoreApplication.translate("option", u"> OPTIONS D'AFFICHAGES", None))
        self.lb_choix_theme.setText(QCoreApplication.translate("option", u"Choix du th\u00e8me :", None))
    # retranslateUi

