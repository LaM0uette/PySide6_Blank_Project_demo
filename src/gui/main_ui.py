# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
    QVBoxLayout, QWidget)

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(756, 490)
        self.glay_main = QGridLayout(main)
        self.glay_main.setSpacing(0)
        self.glay_main.setObjectName(u"glay_main")
        self.glay_main.setContentsMargins(0, 0, 0, 0)
        self.fr_menu_top = QFrame(main)
        self.fr_menu_top.setObjectName(u"fr_menu_top")
        self.fr_menu_top.setFrameShape(QFrame.StyledPanel)
        self.fr_menu_top.setFrameShadow(QFrame.Raised)
        self.hlay_menu_top = QHBoxLayout(self.fr_menu_top)
        self.hlay_menu_top.setSpacing(0)
        self.hlay_menu_top.setObjectName(u"hlay_menu_top")
        self.hlay_menu_top.setContentsMargins(0, 0, 0, 0)
        self.lb_mt_ico = QLabel(self.fr_menu_top)
        self.lb_mt_ico.setObjectName(u"lb_mt_ico")

        self.hlay_menu_top.addWidget(self.lb_mt_ico)

        self.lb_mt_version = QLabel(self.fr_menu_top)
        self.lb_mt_version.setObjectName(u"lb_mt_version")

        self.hlay_menu_top.addWidget(self.lb_mt_version)

        self.wg_mt_blank = QWidget(self.fr_menu_top)
        self.wg_mt_blank.setObjectName(u"wg_mt_blank")

        self.hlay_menu_top.addWidget(self.wg_mt_blank)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_menu_top.addItem(self.horizontalSpacer_2)

        self.lb_mt_nom = QLabel(self.fr_menu_top)
        self.lb_mt_nom.setObjectName(u"lb_mt_nom")

        self.hlay_menu_top.addWidget(self.lb_mt_nom)

        self.horizontalSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_menu_top.addItem(self.horizontalSpacer_1)

        self.pb_mt_option = QPushButton(self.fr_menu_top)
        self.pb_mt_option.setObjectName(u"pb_mt_option")

        self.hlay_menu_top.addWidget(self.pb_mt_option)

        self.pb_mt_reduire = QPushButton(self.fr_menu_top)
        self.pb_mt_reduire.setObjectName(u"pb_mt_reduire")

        self.hlay_menu_top.addWidget(self.pb_mt_reduire)

        self.pb_mt_agrandir = QPushButton(self.fr_menu_top)
        self.pb_mt_agrandir.setObjectName(u"pb_mt_agrandir")

        self.hlay_menu_top.addWidget(self.pb_mt_agrandir)

        self.pb_mt_quitter = QPushButton(self.fr_menu_top)
        self.pb_mt_quitter.setObjectName(u"pb_mt_quitter")

        self.hlay_menu_top.addWidget(self.pb_mt_quitter)


        self.glay_main.addWidget(self.fr_menu_top, 0, 0, 1, 1)

        self.vlay_wg = QVBoxLayout()
        self.vlay_wg.setSpacing(20)
        self.vlay_wg.setObjectName(u"vlay_wg")
        self.vlay_wg.setContentsMargins(50, 20, 50, 20)
        self.vlay_pb = QVBoxLayout()
        self.vlay_pb.setSpacing(10)
        self.vlay_pb.setObjectName(u"vlay_pb")
        self.vlay_pb.setContentsMargins(0, -1, 0, -1)
        self.lb_pb_demo = QLabel(main)
        self.lb_pb_demo.setObjectName(u"lb_pb_demo")

        self.vlay_pb.addWidget(self.lb_pb_demo)

        self.line = QFrame(main)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.vlay_pb.addWidget(self.line)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vlay_pb.addItem(self.verticalSpacer_2)

        self.pb_demo_txt = QPushButton(main)
        self.pb_demo_txt.setObjectName(u"pb_demo_txt")

        self.vlay_pb.addWidget(self.pb_demo_txt)

        self.pb_demo_txt_inv = QPushButton(main)
        self.pb_demo_txt_inv.setObjectName(u"pb_demo_txt_inv")

        self.vlay_pb.addWidget(self.pb_demo_txt_inv)

        self.pb_demo_tr = QPushButton(main)
        self.pb_demo_tr.setObjectName(u"pb_demo_tr")

        self.vlay_pb.addWidget(self.pb_demo_tr)

        self.pb_demo_ck = QPushButton(main)
        self.pb_demo_ck.setObjectName(u"pb_demo_ck")
        self.pb_demo_ck.setCheckable(True)

        self.vlay_pb.addWidget(self.pb_demo_ck)

        self.pb_demo_ck_ico = QPushButton(main)
        self.pb_demo_ck_ico.setObjectName(u"pb_demo_ck_ico")
        self.pb_demo_ck_ico.setCheckable(True)

        self.vlay_pb.addWidget(self.pb_demo_ck_ico)

        self.pb_demo_ico_ck = QPushButton(main)
        self.pb_demo_ico_ck.setObjectName(u"pb_demo_ico_ck")
        self.pb_demo_ico_ck.setCheckable(True)

        self.vlay_pb.addWidget(self.pb_demo_ico_ck)


        self.vlay_wg.addLayout(self.vlay_pb)


        self.glay_main.addLayout(self.vlay_wg, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.glay_main.addItem(self.verticalSpacer, 4, 0, 1, 1)


        self.retranslateUi(main)

        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"Form", None))
        self.lb_pb_demo.setText(QCoreApplication.translate("main", u"QPushButton :", None))
        self.pb_demo_txt.setText(QCoreApplication.translate("main", u"PushButton text", None))
        self.pb_demo_txt_inv.setText(QCoreApplication.translate("main", u"PushButton text invers\u00e9", None))
        self.pb_demo_tr.setText(QCoreApplication.translate("main", u"PushButton transparent", None))
        self.pb_demo_ck.setText(QCoreApplication.translate("main", u"PushButton checkable", None))
        self.pb_demo_ck_ico.setText(QCoreApplication.translate("main", u"PushButton checkable avec icone", None))
        self.pb_demo_ico_ck.setText(QCoreApplication.translate("main", u"PushButton icone checkable", None))
    # retranslateUi

