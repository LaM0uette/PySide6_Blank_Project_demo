# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rgb.ui'
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
    QLabel, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_Rgb(object):
    def setupUi(self, Rgb):
        if not Rgb.objectName():
            Rgb.setObjectName(u"Rgb")
        Rgb.resize(773, 388)
        self.glay_dlg = QGridLayout(Rgb)
        self.glay_dlg.setSpacing(0)
        self.glay_dlg.setObjectName(u"glay_dlg")
        self.glay_dlg.setContentsMargins(0, 0, 0, 0)
        self.fr_main = QFrame(Rgb)
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

        self.vlay_rgb_body = QVBoxLayout()
        self.vlay_rgb_body.setSpacing(0)
        self.vlay_rgb_body.setObjectName(u"vlay_rgb_body")
        self.vlay_rgb_body.setContentsMargins(20, -1, 20, -1)
        self.glay_rgb = QGridLayout()
        self.glay_rgb.setObjectName(u"glay_rgb")
        self.glay_rgb.setHorizontalSpacing(20)
        self.glay_rgb.setVerticalSpacing(0)
        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.glay_rgb.addItem(self.verticalSpacer_14, 0, 0, 1, 4)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.glay_rgb.addItem(self.horizontalSpacer_10, 1, 1, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.glay_rgb.addItem(self.verticalSpacer_11, 9, 0, 1, 4)

        self.sb_rgb_blue = QSpinBox(self.fr_main)
        self.sb_rgb_blue.setObjectName(u"sb_rgb_blue")

        self.glay_rgb.addWidget(self.sb_rgb_blue, 7, 2, 1, 1)

        self.lb_rgb_blue = QLabel(self.fr_main)
        self.lb_rgb_blue.setObjectName(u"lb_rgb_blue")

        self.glay_rgb.addWidget(self.lb_rgb_blue, 7, 0, 1, 1)

        self.sb_rgb_green = QSpinBox(self.fr_main)
        self.sb_rgb_green.setObjectName(u"sb_rgb_green")

        self.glay_rgb.addWidget(self.sb_rgb_green, 4, 2, 1, 1)

        self.lb_rgb_red = QLabel(self.fr_main)
        self.lb_rgb_red.setObjectName(u"lb_rgb_red")

        self.glay_rgb.addWidget(self.lb_rgb_red, 1, 0, 1, 1)

        self.lb_rgb_green = QLabel(self.fr_main)
        self.lb_rgb_green.setObjectName(u"lb_rgb_green")

        self.glay_rgb.addWidget(self.lb_rgb_green, 4, 0, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.glay_rgb.addItem(self.horizontalSpacer_12, 7, 1, 1, 1)

        self.sd_rgb_red = QSlider(self.fr_main)
        self.sd_rgb_red.setObjectName(u"sd_rgb_red")
        self.sd_rgb_red.setOrientation(Qt.Horizontal)

        self.glay_rgb.addWidget(self.sd_rgb_red, 2, 0, 1, 3)

        self.sd_rgb_green = QSlider(self.fr_main)
        self.sd_rgb_green.setObjectName(u"sd_rgb_green")
        self.sd_rgb_green.setOrientation(Qt.Horizontal)

        self.glay_rgb.addWidget(self.sd_rgb_green, 5, 0, 1, 3)

        self.sb_rgb_red = QSpinBox(self.fr_main)
        self.sb_rgb_red.setObjectName(u"sb_rgb_red")

        self.glay_rgb.addWidget(self.sb_rgb_red, 1, 2, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.glay_rgb.addItem(self.verticalSpacer_12, 6, 0, 1, 3)

        self.sd_rgb_blue = QSlider(self.fr_main)
        self.sd_rgb_blue.setObjectName(u"sd_rgb_blue")
        self.sd_rgb_blue.setOrientation(Qt.Horizontal)

        self.glay_rgb.addWidget(self.sd_rgb_blue, 8, 0, 1, 3)

        self.verticalSpacer_13 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.glay_rgb.addItem(self.verticalSpacer_13, 3, 0, 1, 3)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.glay_rgb.addItem(self.horizontalSpacer_11, 4, 1, 1, 1)

        self.fr_rgb_colors = QFrame(self.fr_main)
        self.fr_rgb_colors.setObjectName(u"fr_rgb_colors")
        self.fr_rgb_colors.setMinimumSize(QSize(20, 0))
        self.fr_rgb_colors.setFrameShape(QFrame.StyledPanel)
        self.fr_rgb_colors.setFrameShadow(QFrame.Raised)

        self.glay_rgb.addWidget(self.fr_rgb_colors, 1, 3, 8, 1)


        self.vlay_rgb_body.addLayout(self.glay_rgb)


        self.vlay_fr_main.addLayout(self.vlay_rgb_body)

        self.fr_rgb_bottom = QFrame(self.fr_main)
        self.fr_rgb_bottom.setObjectName(u"fr_rgb_bottom")
        self.hlay_rgb_bottom = QHBoxLayout(self.fr_rgb_bottom)
        self.hlay_rgb_bottom.setSpacing(2)
        self.hlay_rgb_bottom.setObjectName(u"hlay_rgb_bottom")
        self.hlay_rgb_bottom.setContentsMargins(0, 2, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_rgb_bottom.addItem(self.horizontalSpacer)

        self.pb_rgb_ok = QPushButton(self.fr_rgb_bottom)
        self.pb_rgb_ok.setObjectName(u"pb_rgb_ok")

        self.hlay_rgb_bottom.addWidget(self.pb_rgb_ok)

        self.pb_rgb_annuler = QPushButton(self.fr_rgb_bottom)
        self.pb_rgb_annuler.setObjectName(u"pb_rgb_annuler")

        self.hlay_rgb_bottom.addWidget(self.pb_rgb_annuler)


        self.vlay_fr_main.addWidget(self.fr_rgb_bottom)


        self.glay_dlg.addWidget(self.fr_main, 1, 0, 1, 1)


        self.retranslateUi(Rgb)

        QMetaObject.connectSlotsByName(Rgb)
    # setupUi

    def retranslateUi(self, Rgb):
        pass
    # retranslateUi

