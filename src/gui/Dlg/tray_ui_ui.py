# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tray_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_TrayUi(object):
    def setupUi(self, TrayUi):
        if not TrayUi.objectName():
            TrayUi.setObjectName(u"TrayUi")
        TrayUi.resize(446, 791)
        self.verticalLayout = QVBoxLayout(TrayUi)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.fr_main = QFrame(TrayUi)
        self.fr_main.setObjectName(u"fr_main")
        self.fr_main.setFrameShape(QFrame.StyledPanel)
        self.fr_main.setFrameShadow(QFrame.Raised)
        self.vlay_fr_main = QVBoxLayout(self.fr_main)
        self.vlay_fr_main.setSpacing(0)
        self.vlay_fr_main.setObjectName(u"vlay_fr_main")
        self.vlay_fr_main.setContentsMargins(5, 5, 5, 5)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vlay_fr_main.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.fr_main)


        self.retranslateUi(TrayUi)

        QMetaObject.connectSlotsByName(TrayUi)
    # setupUi

    def retranslateUi(self, TrayUi):
        pass
    # retranslateUi

