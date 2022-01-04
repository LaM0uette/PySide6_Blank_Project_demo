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
from PySide6.QtWidgets import (QApplication, QFontComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QStackedWidget, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Dlg(object):
    def setupUi(self, Dlg):
        if not Dlg.objectName():
            Dlg.setObjectName(u"Dlg")
        Dlg.resize(1133, 567)
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
        self.pg_dlg_option = QWidget()
        self.pg_dlg_option.setObjectName(u"pg_dlg_option")
        self.glay_stk_option = QGridLayout(self.pg_dlg_option)
        self.glay_stk_option.setSpacing(0)
        self.glay_stk_option.setObjectName(u"glay_stk_option")
        self.glay_stk_option.setContentsMargins(0, 0, 0, 0)
        self.fr_pg_dlg_option = QFrame(self.pg_dlg_option)
        self.fr_pg_dlg_option.setObjectName(u"fr_pg_dlg_option")
        self.hlay_pg_dlg_option = QHBoxLayout(self.fr_pg_dlg_option)
        self.hlay_pg_dlg_option.setSpacing(2)
        self.hlay_pg_dlg_option.setObjectName(u"hlay_pg_dlg_option")
        self.hlay_pg_dlg_option.setContentsMargins(0, 2, 0, 2)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_pg_dlg_option.addItem(self.horizontalSpacer_5)

        self.pb_dlg_option_appliquer = QPushButton(self.fr_pg_dlg_option)
        self.pb_dlg_option_appliquer.setObjectName(u"pb_dlg_option_appliquer")

        self.hlay_pg_dlg_option.addWidget(self.pb_dlg_option_appliquer)

        self.pb_dlg_option_ok = QPushButton(self.fr_pg_dlg_option)
        self.pb_dlg_option_ok.setObjectName(u"pb_dlg_option_ok")

        self.hlay_pg_dlg_option.addWidget(self.pb_dlg_option_ok)

        self.pb_dlg_option_annuler = QPushButton(self.fr_pg_dlg_option)
        self.pb_dlg_option_annuler.setObjectName(u"pb_dlg_option_annuler")

        self.hlay_pg_dlg_option.addWidget(self.pb_dlg_option_annuler)


        self.glay_stk_option.addWidget(self.fr_pg_dlg_option, 1, 0, 1, 3)

        self.hlay_option = QHBoxLayout()
        self.hlay_option.setSpacing(5)
        self.hlay_option.setObjectName(u"hlay_option")
        self.hlay_option.setContentsMargins(5, 5, 5, 5)
        self.trw_option = QTreeWidget(self.pg_dlg_option)
        self.trw_option.headerItem().setText(0, "")
        __qtreewidgetitem = QTreeWidgetItem(self.trw_option)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        __qtreewidgetitem1 = QTreeWidgetItem(self.trw_option)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(self.trw_option)
        self.trw_option.setObjectName(u"trw_option")

        self.hlay_option.addWidget(self.trw_option)

        self.scrollArea = QScrollArea(self.pg_dlg_option)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 556, 503))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stk_option = QStackedWidget(self.scrollAreaWidgetContents)
        self.stk_option.setObjectName(u"stk_option")
        self.pg_opt_menu = QWidget()
        self.pg_opt_menu.setObjectName(u"pg_opt_menu")
        self.stk_option.addWidget(self.pg_opt_menu)
        self.pg_opt_gen = QWidget()
        self.pg_opt_gen.setObjectName(u"pg_opt_gen")
        self.vlay_pg_opt_gen = QVBoxLayout(self.pg_opt_gen)
        self.vlay_pg_opt_gen.setSpacing(10)
        self.vlay_pg_opt_gen.setObjectName(u"vlay_pg_opt_gen")
        self.vlay_pg_opt_gen.setContentsMargins(10, 20, 10, 10)
        self.pb_opt_gen_font = QPushButton(self.pg_opt_gen)
        self.pb_opt_gen_font.setObjectName(u"pb_opt_gen_font")

        self.vlay_pg_opt_gen.addWidget(self.pb_opt_gen_font)

        self.pb_opt_gen_config = QPushButton(self.pg_opt_gen)
        self.pb_opt_gen_config.setObjectName(u"pb_opt_gen_config")

        self.vlay_pg_opt_gen.addWidget(self.pb_opt_gen_config)

        self.pb_opt_gen_cur = QPushButton(self.pg_opt_gen)
        self.pb_opt_gen_cur.setObjectName(u"pb_opt_gen_cur")

        self.vlay_pg_opt_gen.addWidget(self.pb_opt_gen_cur)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vlay_pg_opt_gen.addItem(self.verticalSpacer_6)

        self.stk_option.addWidget(self.pg_opt_gen)
        self.pg_opt_font = QWidget()
        self.pg_opt_font.setObjectName(u"pg_opt_font")
        self.vlay_pg_opt_font = QVBoxLayout(self.pg_opt_font)
        self.vlay_pg_opt_font.setSpacing(10)
        self.vlay_pg_opt_font.setObjectName(u"vlay_pg_opt_font")
        self.vlay_pg_opt_font.setContentsMargins(10, 20, 10, 10)
        self.fcb_opt_ft_font = QFontComboBox(self.pg_opt_font)
        self.fcb_opt_ft_font.setObjectName(u"fcb_opt_ft_font")

        self.vlay_pg_opt_font.addWidget(self.fcb_opt_ft_font)

        self.verticalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vlay_pg_opt_font.addItem(self.verticalSpacer_8)

        self.fr_opt_ft_h1 = QFrame(self.pg_opt_font)
        self.fr_opt_ft_h1.setObjectName(u"fr_opt_ft_h1")
        self.hlay_opt_ft_h1 = QHBoxLayout(self.fr_opt_ft_h1)
        self.hlay_opt_ft_h1.setSpacing(10)
        self.hlay_opt_ft_h1.setObjectName(u"hlay_opt_ft_h1")
        self.hlay_opt_ft_h1.setContentsMargins(5, 5, 5, 5)
        self.lb_opt_ft_h1 = QLabel(self.fr_opt_ft_h1)
        self.lb_opt_ft_h1.setObjectName(u"lb_opt_ft_h1")

        self.hlay_opt_ft_h1.addWidget(self.lb_opt_ft_h1)

        self.sb_opt_ft_h1 = QSpinBox(self.fr_opt_ft_h1)
        self.sb_opt_ft_h1.setObjectName(u"sb_opt_ft_h1")

        self.hlay_opt_ft_h1.addWidget(self.sb_opt_ft_h1)

        self.le_opt_ft_texte_h1 = QLineEdit(self.fr_opt_ft_h1)
        self.le_opt_ft_texte_h1.setObjectName(u"le_opt_ft_texte_h1")

        self.hlay_opt_ft_h1.addWidget(self.le_opt_ft_texte_h1)


        self.vlay_pg_opt_font.addWidget(self.fr_opt_ft_h1)

        self.fr_opt_ft_h2 = QFrame(self.pg_opt_font)
        self.fr_opt_ft_h2.setObjectName(u"fr_opt_ft_h2")
        self.hlay_opt_ft_h2 = QHBoxLayout(self.fr_opt_ft_h2)
        self.hlay_opt_ft_h2.setSpacing(10)
        self.hlay_opt_ft_h2.setObjectName(u"hlay_opt_ft_h2")
        self.hlay_opt_ft_h2.setContentsMargins(5, 5, 5, 5)
        self.lb_opt_ft_h2 = QLabel(self.fr_opt_ft_h2)
        self.lb_opt_ft_h2.setObjectName(u"lb_opt_ft_h2")

        self.hlay_opt_ft_h2.addWidget(self.lb_opt_ft_h2)

        self.sb_opt_ft_h2 = QSpinBox(self.fr_opt_ft_h2)
        self.sb_opt_ft_h2.setObjectName(u"sb_opt_ft_h2")

        self.hlay_opt_ft_h2.addWidget(self.sb_opt_ft_h2)

        self.le_opt_ft_texte_h2 = QLineEdit(self.fr_opt_ft_h2)
        self.le_opt_ft_texte_h2.setObjectName(u"le_opt_ft_texte_h2")

        self.hlay_opt_ft_h2.addWidget(self.le_opt_ft_texte_h2)


        self.vlay_pg_opt_font.addWidget(self.fr_opt_ft_h2)

        self.fr_opt_ft_h3 = QFrame(self.pg_opt_font)
        self.fr_opt_ft_h3.setObjectName(u"fr_opt_ft_h3")
        self.hlay_opt_ft_h3 = QHBoxLayout(self.fr_opt_ft_h3)
        self.hlay_opt_ft_h3.setSpacing(10)
        self.hlay_opt_ft_h3.setObjectName(u"hlay_opt_ft_h3")
        self.hlay_opt_ft_h3.setContentsMargins(5, 5, 5, 5)
        self.lb_opt_ft_h3 = QLabel(self.fr_opt_ft_h3)
        self.lb_opt_ft_h3.setObjectName(u"lb_opt_ft_h3")

        self.hlay_opt_ft_h3.addWidget(self.lb_opt_ft_h3)

        self.sb_opt_ft_h3 = QSpinBox(self.fr_opt_ft_h3)
        self.sb_opt_ft_h3.setObjectName(u"sb_opt_ft_h3")

        self.hlay_opt_ft_h3.addWidget(self.sb_opt_ft_h3)

        self.le_opt_ft_texte_h3 = QLineEdit(self.fr_opt_ft_h3)
        self.le_opt_ft_texte_h3.setObjectName(u"le_opt_ft_texte_h3")

        self.hlay_opt_ft_h3.addWidget(self.le_opt_ft_texte_h3)


        self.vlay_pg_opt_font.addWidget(self.fr_opt_ft_h3)

        self.fr_opt_ft_h4 = QFrame(self.pg_opt_font)
        self.fr_opt_ft_h4.setObjectName(u"fr_opt_ft_h4")
        self.hlay_opt_ft_h4 = QHBoxLayout(self.fr_opt_ft_h4)
        self.hlay_opt_ft_h4.setSpacing(10)
        self.hlay_opt_ft_h4.setObjectName(u"hlay_opt_ft_h4")
        self.hlay_opt_ft_h4.setContentsMargins(5, 5, 5, 5)
        self.lb_opt_ft_h4 = QLabel(self.fr_opt_ft_h4)
        self.lb_opt_ft_h4.setObjectName(u"lb_opt_ft_h4")

        self.hlay_opt_ft_h4.addWidget(self.lb_opt_ft_h4)

        self.sb_opt_ft_h4 = QSpinBox(self.fr_opt_ft_h4)
        self.sb_opt_ft_h4.setObjectName(u"sb_opt_ft_h4")

        self.hlay_opt_ft_h4.addWidget(self.sb_opt_ft_h4)

        self.le_opt_ft_texte_h4 = QLineEdit(self.fr_opt_ft_h4)
        self.le_opt_ft_texte_h4.setObjectName(u"le_opt_ft_texte_h4")

        self.hlay_opt_ft_h4.addWidget(self.le_opt_ft_texte_h4)


        self.vlay_pg_opt_font.addWidget(self.fr_opt_ft_h4)

        self.fr_opt_ft_h5 = QFrame(self.pg_opt_font)
        self.fr_opt_ft_h5.setObjectName(u"fr_opt_ft_h5")
        self.hlay_opt_ft_h5 = QHBoxLayout(self.fr_opt_ft_h5)
        self.hlay_opt_ft_h5.setSpacing(10)
        self.hlay_opt_ft_h5.setObjectName(u"hlay_opt_ft_h5")
        self.hlay_opt_ft_h5.setContentsMargins(5, 5, 5, 5)
        self.lb_opt_ft_h5 = QLabel(self.fr_opt_ft_h5)
        self.lb_opt_ft_h5.setObjectName(u"lb_opt_ft_h5")

        self.hlay_opt_ft_h5.addWidget(self.lb_opt_ft_h5)

        self.sb_opt_ft_h5 = QSpinBox(self.fr_opt_ft_h5)
        self.sb_opt_ft_h5.setObjectName(u"sb_opt_ft_h5")

        self.hlay_opt_ft_h5.addWidget(self.sb_opt_ft_h5)

        self.le_opt_ft_texte_h5 = QLineEdit(self.fr_opt_ft_h5)
        self.le_opt_ft_texte_h5.setObjectName(u"le_opt_ft_texte_h5")

        self.hlay_opt_ft_h5.addWidget(self.le_opt_ft_texte_h5)


        self.vlay_pg_opt_font.addWidget(self.fr_opt_ft_h5)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vlay_pg_opt_font.addItem(self.verticalSpacer_7)

        self.stk_option.addWidget(self.pg_opt_font)
        self.pg_opt_configs = QWidget()
        self.pg_opt_configs.setObjectName(u"pg_opt_configs")
        self.stk_option.addWidget(self.pg_opt_configs)
        self.pg_opt_cur = QWidget()
        self.pg_opt_cur.setObjectName(u"pg_opt_cur")
        self.stk_option.addWidget(self.pg_opt_cur)
        self.pg_opt_themes = QWidget()
        self.pg_opt_themes.setObjectName(u"pg_opt_themes")
        self.vlay_pg_opt_themes = QVBoxLayout(self.pg_opt_themes)
        self.vlay_pg_opt_themes.setSpacing(10)
        self.vlay_pg_opt_themes.setObjectName(u"vlay_pg_opt_themes")
        self.vlay_pg_opt_themes.setContentsMargins(10, 20, 10, 10)
        self.pb_opt_theme_colors = QPushButton(self.pg_opt_themes)
        self.pb_opt_theme_colors.setObjectName(u"pb_opt_theme_colors")

        self.vlay_pg_opt_themes.addWidget(self.pb_opt_theme_colors)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vlay_pg_opt_themes.addItem(self.verticalSpacer_4)

        self.stk_option.addWidget(self.pg_opt_themes)
        self.pg_opt_tcolors = QWidget()
        self.pg_opt_tcolors.setObjectName(u"pg_opt_tcolors")
        self.stk_option.addWidget(self.pg_opt_tcolors)
        self.pg_opt_infos = QWidget()
        self.pg_opt_infos.setObjectName(u"pg_opt_infos")
        self.vlay_pg_opt_infos = QVBoxLayout(self.pg_opt_infos)
        self.vlay_pg_opt_infos.setSpacing(0)
        self.vlay_pg_opt_infos.setObjectName(u"vlay_pg_opt_infos")
        self.vlay_pg_opt_infos.setContentsMargins(10, 20, 10, 10)
        self.lb_opt_info_nom = QLabel(self.pg_opt_infos)
        self.lb_opt_info_nom.setObjectName(u"lb_opt_info_nom")

        self.vlay_pg_opt_infos.addWidget(self.lb_opt_info_nom)

        self.verticalSpacer_5 = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vlay_pg_opt_infos.addItem(self.verticalSpacer_5)

        self.lb_opt_info_desc = QLabel(self.pg_opt_infos)
        self.lb_opt_info_desc.setObjectName(u"lb_opt_info_desc")

        self.vlay_pg_opt_infos.addWidget(self.lb_opt_info_desc)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vlay_pg_opt_infos.addItem(self.verticalSpacer_3)

        self.lb_opt_info_auteur = QLabel(self.pg_opt_infos)
        self.lb_opt_info_auteur.setObjectName(u"lb_opt_info_auteur")

        self.vlay_pg_opt_infos.addWidget(self.lb_opt_info_auteur)

        self.lb_opt_info_version = QLabel(self.pg_opt_infos)
        self.lb_opt_info_version.setObjectName(u"lb_opt_info_version")

        self.vlay_pg_opt_infos.addWidget(self.lb_opt_info_version)

        self.stk_option.addWidget(self.pg_opt_infos)

        self.verticalLayout.addWidget(self.stk_option)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.hlay_option.addWidget(self.scrollArea)


        self.glay_stk_option.addLayout(self.hlay_option, 0, 1, 1, 1)

        self.stk_dlg.addWidget(self.pg_dlg_option)

        self.vlay_fr_main.addWidget(self.stk_dlg)


        self.glay_dlg.addWidget(self.fr_main, 1, 0, 1, 1)


        self.retranslateUi(Dlg)

        self.stk_dlg.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Dlg)
    # setupUi

    def retranslateUi(self, Dlg):
        self.le_input.setPlaceholderText(QCoreApplication.translate("Dlg", u"...", None))

        __sortingEnabled = self.trw_option.isSortingEnabled()
        self.trw_option.setSortingEnabled(False)
        ___qtreewidgetitem = self.trw_option.topLevelItem(0)
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Dlg", u"G\u00e9n\u00e9ral", None));
        ___qtreewidgetitem1 = ___qtreewidgetitem.child(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Dlg", u"Polices", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem.child(1)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("Dlg", u"Configs", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem.child(2)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("Dlg", u"Curseurs", None));
        ___qtreewidgetitem4 = self.trw_option.topLevelItem(1)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("Dlg", u"Th\u00e8mes", None));
        ___qtreewidgetitem5 = ___qtreewidgetitem4.child(0)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("Dlg", u"T-Colors", None));
        ___qtreewidgetitem6 = self.trw_option.topLevelItem(2)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("Dlg", u"Infos", None));
        self.trw_option.setSortingEnabled(__sortingEnabled)

        self.pb_opt_gen_font.setText(QCoreApplication.translate("Dlg", u"Police", None))
        self.pb_opt_gen_config.setText(QCoreApplication.translate("Dlg", u"Configs", None))
        self.pb_opt_gen_cur.setText(QCoreApplication.translate("Dlg", u"Curseurs", None))
        self.lb_opt_ft_h1.setText(QCoreApplication.translate("Dlg", u"Taille H1: ", None))
        self.le_opt_ft_texte_h1.setText(QCoreApplication.translate("Dlg", u"TEST De la Police :)", None))
        self.lb_opt_ft_h2.setText(QCoreApplication.translate("Dlg", u"Taille H2: ", None))
        self.le_opt_ft_texte_h2.setText(QCoreApplication.translate("Dlg", u"TEST De la Police :)", None))
        self.lb_opt_ft_h3.setText(QCoreApplication.translate("Dlg", u"Taille H3: ", None))
        self.le_opt_ft_texte_h3.setText(QCoreApplication.translate("Dlg", u"TEST De la Police :)", None))
        self.lb_opt_ft_h4.setText(QCoreApplication.translate("Dlg", u"Taille H4: ", None))
        self.le_opt_ft_texte_h4.setText(QCoreApplication.translate("Dlg", u"TEST De la Police :)", None))
        self.lb_opt_ft_h5.setText(QCoreApplication.translate("Dlg", u"Taille H5: ", None))
        self.le_opt_ft_texte_h5.setText(QCoreApplication.translate("Dlg", u"TEST De la Police :)", None))
        self.pb_opt_theme_colors.setText(QCoreApplication.translate("Dlg", u"Couleurs", None))
        pass
    # retranslateUi

