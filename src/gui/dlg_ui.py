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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

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
        self.pg_dlg_rep = QWidget()
        self.pg_dlg_rep.setObjectName(u"pg_dlg_rep")
        self.vlay_pg_dlg_rep = QVBoxLayout(self.pg_dlg_rep)
        self.vlay_pg_dlg_rep.setSpacing(0)
        self.vlay_pg_dlg_rep.setObjectName(u"vlay_pg_dlg_rep")
        self.vlay_pg_dlg_rep.setContentsMargins(0, 0, 0, 0)
        self.lb_rep_texte = QLabel(self.pg_dlg_rep)
        self.lb_rep_texte.setObjectName(u"lb_rep_texte")

        self.vlay_pg_dlg_rep.addWidget(self.lb_rep_texte)

        self.fr_pg_dlg_rep = QFrame(self.pg_dlg_rep)
        self.fr_pg_dlg_rep.setObjectName(u"fr_pg_dlg_rep")
        self.hlay_pg_dlg_rep = QHBoxLayout(self.fr_pg_dlg_rep)
        self.hlay_pg_dlg_rep.setSpacing(2)
        self.hlay_pg_dlg_rep.setObjectName(u"hlay_pg_dlg_rep")
        self.hlay_pg_dlg_rep.setContentsMargins(0, 2, 0, 2)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_pg_dlg_rep.addItem(self.horizontalSpacer_3)

        self.pb_dlg_rep_ok = QPushButton(self.fr_pg_dlg_rep)
        self.pb_dlg_rep_ok.setObjectName(u"pb_dlg_rep_ok")

        self.hlay_pg_dlg_rep.addWidget(self.pb_dlg_rep_ok)

        self.pb_dlg_rep_annuler = QPushButton(self.fr_pg_dlg_rep)
        self.pb_dlg_rep_annuler.setObjectName(u"pb_dlg_rep_annuler")

        self.hlay_pg_dlg_rep.addWidget(self.pb_dlg_rep_annuler)


        self.vlay_pg_dlg_rep.addWidget(self.fr_pg_dlg_rep)

        self.stk_dlg.addWidget(self.pg_dlg_rep)
        self.pg_dlg_input = QWidget()
        self.pg_dlg_input.setObjectName(u"pg_dlg_input")
        self.vlay_pg_dlg_input = QVBoxLayout(self.pg_dlg_input)
        self.vlay_pg_dlg_input.setSpacing(0)
        self.vlay_pg_dlg_input.setObjectName(u"vlay_pg_dlg_input")
        self.vlay_pg_dlg_input.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vlay_pg_dlg_input.addItem(self.verticalSpacer)

        self.vlay_dlg_input = QVBoxLayout()
        self.vlay_dlg_input.setSpacing(10)
        self.vlay_dlg_input.setObjectName(u"vlay_dlg_input")
        self.vlay_dlg_input.setContentsMargins(20, -1, 20, -1)
        self.lb_input_texte = QLabel(self.pg_dlg_input)
        self.lb_input_texte.setObjectName(u"lb_input_texte")

        self.vlay_dlg_input.addWidget(self.lb_input_texte)

        self.le_input = QLineEdit(self.pg_dlg_input)
        self.le_input.setObjectName(u"le_input")

        self.vlay_dlg_input.addWidget(self.le_input)


        self.vlay_pg_dlg_input.addLayout(self.vlay_dlg_input)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vlay_pg_dlg_input.addItem(self.verticalSpacer_2)

        self.fr_pg_dlg_input = QFrame(self.pg_dlg_input)
        self.fr_pg_dlg_input.setObjectName(u"fr_pg_dlg_input")
        self.hlay_pg_dlg_input = QHBoxLayout(self.fr_pg_dlg_input)
        self.hlay_pg_dlg_input.setSpacing(2)
        self.hlay_pg_dlg_input.setObjectName(u"hlay_pg_dlg_input")
        self.hlay_pg_dlg_input.setContentsMargins(0, 2, 0, 2)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_pg_dlg_input.addItem(self.horizontalSpacer_4)

        self.pb_dlg_input_ok = QPushButton(self.fr_pg_dlg_input)
        self.pb_dlg_input_ok.setObjectName(u"pb_dlg_input_ok")

        self.hlay_pg_dlg_input.addWidget(self.pb_dlg_input_ok)

        self.pb_dlg_input_annuler = QPushButton(self.fr_pg_dlg_input)
        self.pb_dlg_input_annuler.setObjectName(u"pb_dlg_input_annuler")

        self.hlay_pg_dlg_input.addWidget(self.pb_dlg_input_annuler)


        self.vlay_pg_dlg_input.addWidget(self.fr_pg_dlg_input)

        self.stk_dlg.addWidget(self.pg_dlg_input)

        self.vlay_fr_main.addWidget(self.stk_dlg)


        self.glay_dlg.addWidget(self.fr_main, 1, 0, 1, 1)


        self.retranslateUi(Dlg)

        self.stk_dlg.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Dlg)
    # setupUi

    def retranslateUi(self, Dlg):
        self.le_input.setPlaceholderText(QCoreApplication.translate("Dlg", u"...", None))
        pass
    # retranslateUi

