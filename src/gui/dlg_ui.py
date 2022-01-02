# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlg.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_Dlg(object):
    def setupUi(self, Dlg):
        if not Dlg.objectName():
            Dlg.setObjectName(u"Dlg")
        Dlg.resize(600, 165)
        self.glay_dlg = QGridLayout(Dlg)
        self.glay_dlg.setSpacing(0)
        self.glay_dlg.setObjectName(u"glay_dlg")
        self.glay_dlg.setContentsMargins(0, 0, 0, 0)
        self.fr_main = QFrame(Dlg)
        self.fr_main.setObjectName(u"fr_main")
        self.fr_main.setFrameShape(QFrame.StyledPanel)
        self.fr_main.setFrameShadow(QFrame.Raised)
        self.vlay_fr_main = QVBoxLayout(self.fr_main)
        self.vlay_fr_main.setSpacing(0)
        self.vlay_fr_main.setObjectName(u"vlay_fr_main")
        self.vlay_fr_main.setContentsMargins(0, 0, 0, 0)
        self.fr_menu_top = QFrame(self.fr_main)
        self.fr_menu_top.setObjectName(u"fr_menu_top")
        self.hlay_menu_top = QHBoxLayout(self.fr_menu_top)
        self.hlay_menu_top.setSpacing(0)
        self.hlay_menu_top.setObjectName(u"hlay_menu_top")
        self.hlay_menu_top.setContentsMargins(0, 0, 0, 0)
        self.lb_mt_ico = QLabel(self.fr_menu_top)
        self.lb_mt_ico.setObjectName(u"lb_mt_ico")

        self.hlay_menu_top.addWidget(self.lb_mt_ico)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_menu_top.addItem(self.horizontalSpacer_2)

        self.lb_mt_nom = QLabel(self.fr_menu_top)
        self.lb_mt_nom.setObjectName(u"lb_mt_nom")

        self.hlay_menu_top.addWidget(self.lb_mt_nom)

        self.horizontalSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_menu_top.addItem(self.horizontalSpacer_1)

        self.pb_mt_quitter = QPushButton(self.fr_menu_top)
        self.pb_mt_quitter.setObjectName(u"pb_mt_quitter")

        self.hlay_menu_top.addWidget(self.pb_mt_quitter)


        self.vlay_fr_main.addWidget(self.fr_menu_top)

        self.stk_dlg = QStackedWidget(self.fr_main)
        self.stk_dlg.setObjectName(u"stk_dlg")
        self.pg_dlg_msg = QWidget()
        self.pg_dlg_msg.setObjectName(u"pg_dlg_msg")
        self.vlay_pg_dlg_info = QVBoxLayout(self.pg_dlg_msg)
        self.vlay_pg_dlg_info.setSpacing(0)
        self.vlay_pg_dlg_info.setObjectName(u"vlay_pg_dlg_info")
        self.vlay_pg_dlg_info.setContentsMargins(0, 0, 0, 0)
        self.lb_msg_texte = QLabel(self.pg_dlg_msg)
        self.lb_msg_texte.setObjectName(u"lb_msg_texte")

        self.vlay_pg_dlg_info.addWidget(self.lb_msg_texte)

        self.fr_pg_dlg_msg = QFrame(self.pg_dlg_msg)
        self.fr_pg_dlg_msg.setObjectName(u"fr_pg_dlg_msg")
        self.hlay_pg_dlg_msg = QHBoxLayout(self.fr_pg_dlg_msg)
        self.hlay_pg_dlg_msg.setSpacing(2)
        self.hlay_pg_dlg_msg.setObjectName(u"hlay_pg_dlg_msg")
        self.hlay_pg_dlg_msg.setContentsMargins(0, 2, 0, 2)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_pg_dlg_msg.addItem(self.horizontalSpacer)

        self.pb_dlg_msg_ok = QPushButton(self.fr_pg_dlg_msg)
        self.pb_dlg_msg_ok.setObjectName(u"pb_dlg_msg_ok")

        self.hlay_pg_dlg_msg.addWidget(self.pb_dlg_msg_ok)


        self.vlay_pg_dlg_info.addWidget(self.fr_pg_dlg_msg)

        self.stk_dlg.addWidget(self.pg_dlg_msg)
        self.pg_dlg_alerte = QWidget()
        self.pg_dlg_alerte.setObjectName(u"pg_dlg_alerte")
        self.verticalLayout = QVBoxLayout(self.pg_dlg_alerte)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lb_alerte_texte = QLabel(self.pg_dlg_alerte)
        self.lb_alerte_texte.setObjectName(u"lb_alerte_texte")

        self.verticalLayout.addWidget(self.lb_alerte_texte)

        self.fr_pg_dlg_alerte = QFrame(self.pg_dlg_alerte)
        self.fr_pg_dlg_alerte.setObjectName(u"fr_pg_dlg_alerte")
        self.hlay_pg_dlg_info_2 = QHBoxLayout(self.fr_pg_dlg_alerte)
        self.hlay_pg_dlg_info_2.setSpacing(2)
        self.hlay_pg_dlg_info_2.setObjectName(u"hlay_pg_dlg_info_2")
        self.hlay_pg_dlg_info_2.setContentsMargins(0, 2, 0, 2)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_pg_dlg_info_2.addItem(self.horizontalSpacer_3)

        self.pb_dlg_alerte_ok = QPushButton(self.fr_pg_dlg_alerte)
        self.pb_dlg_alerte_ok.setObjectName(u"pb_dlg_alerte_ok")

        self.hlay_pg_dlg_info_2.addWidget(self.pb_dlg_alerte_ok)


        self.verticalLayout.addWidget(self.fr_pg_dlg_alerte)

        self.stk_dlg.addWidget(self.pg_dlg_alerte)

        self.vlay_fr_main.addWidget(self.stk_dlg)


        self.glay_dlg.addWidget(self.fr_main, 1, 0, 1, 1)


        self.retranslateUi(Dlg)

        self.stk_dlg.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Dlg)
    # setupUi

    def retranslateUi(self, Dlg):
        pass
    # retranslateUi

