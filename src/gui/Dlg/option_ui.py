# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'option.ui'
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

class Ui_Option(object):
    def setupUi(self, Option):
        if not Option.objectName():
            Option.setObjectName(u"Option")
        Option.resize(773, 261)
        self.glay_dlg = QGridLayout(Option)
        self.glay_dlg.setSpacing(0)
        self.glay_dlg.setObjectName(u"glay_dlg")
        self.glay_dlg.setContentsMargins(0, 0, 0, 0)
        self.fr_main = QFrame(Option)
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

        self.vlay_opt_body = QVBoxLayout()
        self.vlay_opt_body.setSpacing(0)
        self.vlay_opt_body.setObjectName(u"vlay_opt_body")
        self.vlay_opt_body.setContentsMargins(20, -1, 20, -1)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vlay_opt_body.addItem(self.verticalSpacer_2)

        self.lb_opt_text = QLabel(self.fr_main)
        self.lb_opt_text.setObjectName(u"lb_opt_text")

        self.vlay_opt_body.addWidget(self.lb_opt_text)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vlay_opt_body.addItem(self.verticalSpacer)


        self.vlay_fr_main.addLayout(self.vlay_opt_body)

        self.fr_opt_bottom = QFrame(self.fr_main)
        self.fr_opt_bottom.setObjectName(u"fr_opt_bottom")
        self.hlay_opt_bottom = QHBoxLayout(self.fr_opt_bottom)
        self.hlay_opt_bottom.setSpacing(2)
        self.hlay_opt_bottom.setObjectName(u"hlay_opt_bottom")
        self.hlay_opt_bottom.setContentsMargins(0, 2, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_opt_bottom.addItem(self.horizontalSpacer)

        self.pb_opt_appliquer = QPushButton(self.fr_opt_bottom)
        self.pb_opt_appliquer.setObjectName(u"pb_opt_appliquer")

        self.hlay_opt_bottom.addWidget(self.pb_opt_appliquer)

        self.pb_opt_ok = QPushButton(self.fr_opt_bottom)
        self.pb_opt_ok.setObjectName(u"pb_opt_ok")

        self.hlay_opt_bottom.addWidget(self.pb_opt_ok)


        self.vlay_fr_main.addWidget(self.fr_opt_bottom)


        self.glay_dlg.addWidget(self.fr_main, 1, 0, 1, 1)


        self.retranslateUi(Option)

        QMetaObject.connectSlotsByName(Option)
    # setupUi

    def retranslateUi(self, Option):
        pass
    # retranslateUi

