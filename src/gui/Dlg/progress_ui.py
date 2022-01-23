# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'progress.ui'
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
    QLabel, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Progress(object):
    def setupUi(self, Progress):
        if not Progress.objectName():
            Progress.setObjectName(u"Progress")
        Progress.resize(773, 261)
        self.glay_dlg = QGridLayout(Progress)
        self.glay_dlg.setSpacing(0)
        self.glay_dlg.setObjectName(u"glay_dlg")
        self.glay_dlg.setContentsMargins(0, 0, 0, 0)
        self.fr_main = QFrame(Progress)
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

        self.vlay_pg_body = QVBoxLayout()
        self.vlay_pg_body.setSpacing(2)
        self.vlay_pg_body.setObjectName(u"vlay_pg_body")
        self.vlay_pg_body.setContentsMargins(20, -1, 20, -1)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vlay_pg_body.addItem(self.verticalSpacer_2)

        self.pg_pg_progress = QProgressBar(self.fr_main)
        self.pg_pg_progress.setObjectName(u"pg_pg_progress")

        self.vlay_pg_body.addWidget(self.pg_pg_progress)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vlay_pg_body.addItem(self.verticalSpacer)


        self.vlay_fr_main.addLayout(self.vlay_pg_body)

        self.fr_pg_bottom = QFrame(self.fr_main)
        self.fr_pg_bottom.setObjectName(u"fr_pg_bottom")
        self.hlay_pg_bottom = QHBoxLayout(self.fr_pg_bottom)
        self.hlay_pg_bottom.setSpacing(2)
        self.hlay_pg_bottom.setObjectName(u"hlay_pg_bottom")
        self.hlay_pg_bottom.setContentsMargins(0, 2, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_pg_bottom.addItem(self.horizontalSpacer)

        self.pb_pg_annuler = QPushButton(self.fr_pg_bottom)
        self.pb_pg_annuler.setObjectName(u"pb_pg_annuler")

        self.hlay_pg_bottom.addWidget(self.pb_pg_annuler)


        self.vlay_fr_main.addWidget(self.fr_pg_bottom)


        self.glay_dlg.addWidget(self.fr_main, 1, 0, 1, 1)


        self.retranslateUi(Progress)

        QMetaObject.connectSlotsByName(Progress)
    # setupUi

    def retranslateUi(self, Progress):
        pass
    # retranslateUi

