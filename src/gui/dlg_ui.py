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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFontComboBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QStackedWidget, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Dlg(object):
    def setupUi(self, Dlg):
        if not Dlg.objectName():
            Dlg.setObjectName(u"Dlg")
        Dlg.resize(909, 757)
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
        self.pg_dlg_option = QWidget()
        self.pg_dlg_option.setObjectName(u"pg_dlg_option")
        self.glay_stk_option = QGridLayout(self.pg_dlg_option)
        self.glay_stk_option.setSpacing(0)
        self.glay_stk_option.setObjectName(u"glay_stk_option")
        self.glay_stk_option.setContentsMargins(0, 0, 0, 0)
        self.fr_pg_dlg_option = QFrame(self.pg_dlg_option)
        self.fr_pg_dlg_option.setObjectName(u"fr_pg_dlg_option")
        self.glay_fr_pg_dlg_option = QGridLayout(self.fr_pg_dlg_option)
        self.glay_fr_pg_dlg_option.setObjectName(u"glay_fr_pg_dlg_option")
        self.glay_fr_pg_dlg_option.setHorizontalSpacing(2)
        self.glay_fr_pg_dlg_option.setVerticalSpacing(0)
        self.glay_fr_pg_dlg_option.setContentsMargins(0, 2, 0, 0)
        self.pb_dlg_option_ok = QPushButton(self.fr_pg_dlg_option)
        self.pb_dlg_option_ok.setObjectName(u"pb_dlg_option_ok")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_dlg_option_ok.sizePolicy().hasHeightForWidth())
        self.pb_dlg_option_ok.setSizePolicy(sizePolicy)

        self.glay_fr_pg_dlg_option.addWidget(self.pb_dlg_option_ok, 0, 2, 1, 1)

        self.pb_dlg_option_appliquer = QPushButton(self.fr_pg_dlg_option)
        self.pb_dlg_option_appliquer.setObjectName(u"pb_dlg_option_appliquer")
        sizePolicy.setHeightForWidth(self.pb_dlg_option_appliquer.sizePolicy().hasHeightForWidth())
        self.pb_dlg_option_appliquer.setSizePolicy(sizePolicy)

        self.glay_fr_pg_dlg_option.addWidget(self.pb_dlg_option_appliquer, 0, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.glay_fr_pg_dlg_option.addItem(self.horizontalSpacer_5, 0, 0, 1, 1)


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

        self.sca_option = QScrollArea(self.pg_dlg_option)
        self.sca_option.setObjectName(u"sca_option")
        self.sca_option.setWidgetResizable(True)
        self.sca_area_option = QWidget()
        self.sca_area_option.setObjectName(u"sca_area_option")
        self.sca_area_option.setGeometry(QRect(0, 0, 444, 354))
        self.vlay_sca_option = QVBoxLayout(self.sca_area_option)
        self.vlay_sca_option.setSpacing(0)
        self.vlay_sca_option.setObjectName(u"vlay_sca_option")
        self.vlay_sca_option.setContentsMargins(0, 0, 0, 0)
        self.stk_option = QStackedWidget(self.sca_area_option)
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
        self.vlay_pg_opt_configs = QVBoxLayout(self.pg_opt_configs)
        self.vlay_pg_opt_configs.setSpacing(10)
        self.vlay_pg_opt_configs.setObjectName(u"vlay_pg_opt_configs")
        self.vlay_pg_opt_configs.setContentsMargins(10, 20, 10, 10)
        self.fr_opt_cfg_opacity = QFrame(self.pg_opt_configs)
        self.fr_opt_cfg_opacity.setObjectName(u"fr_opt_cfg_opacity")
        self.hlay_opt_fr_opt_cfg_opacity = QHBoxLayout(self.fr_opt_cfg_opacity)
        self.hlay_opt_fr_opt_cfg_opacity.setSpacing(10)
        self.hlay_opt_fr_opt_cfg_opacity.setObjectName(u"hlay_opt_fr_opt_cfg_opacity")
        self.hlay_opt_fr_opt_cfg_opacity.setContentsMargins(5, 5, 5, 5)
        self.lb_opt_cfg_opacity = QLabel(self.fr_opt_cfg_opacity)
        self.lb_opt_cfg_opacity.setObjectName(u"lb_opt_cfg_opacity")

        self.hlay_opt_fr_opt_cfg_opacity.addWidget(self.lb_opt_cfg_opacity)

        self.sb_opt_cfg_opacity = QSpinBox(self.fr_opt_cfg_opacity)
        self.sb_opt_cfg_opacity.setObjectName(u"sb_opt_cfg_opacity")

        self.hlay_opt_fr_opt_cfg_opacity.addWidget(self.sb_opt_cfg_opacity)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_opt_fr_opt_cfg_opacity.addItem(self.horizontalSpacer_6)


        self.vlay_pg_opt_configs.addWidget(self.fr_opt_cfg_opacity)

        self.fr_opt_cfg_autoclose = QFrame(self.pg_opt_configs)
        self.fr_opt_cfg_autoclose.setObjectName(u"fr_opt_cfg_autoclose")
        self.gridLayout = QGridLayout(self.fr_opt_cfg_autoclose)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.ck_opt_cfg_autoclose = QCheckBox(self.fr_opt_cfg_autoclose)
        self.ck_opt_cfg_autoclose.setObjectName(u"ck_opt_cfg_autoclose")

        self.gridLayout.addWidget(self.ck_opt_cfg_autoclose, 1, 1, 1, 1)

        self.lb_opt_cfg_autoclose = QLabel(self.fr_opt_cfg_autoclose)
        self.lb_opt_cfg_autoclose.setObjectName(u"lb_opt_cfg_autoclose")

        self.gridLayout.addWidget(self.lb_opt_cfg_autoclose, 1, 0, 1, 1)

        self.lb_opt_cfg_autoreload = QLabel(self.fr_opt_cfg_autoclose)
        self.lb_opt_cfg_autoreload.setObjectName(u"lb_opt_cfg_autoreload")

        self.gridLayout.addWidget(self.lb_opt_cfg_autoreload, 0, 0, 1, 1)

        self.ck_opt_cfg_autoreload = QCheckBox(self.fr_opt_cfg_autoclose)
        self.ck_opt_cfg_autoreload.setObjectName(u"ck_opt_cfg_autoreload")

        self.gridLayout.addWidget(self.ck_opt_cfg_autoreload, 0, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 0, 2, 2, 1)


        self.vlay_pg_opt_configs.addWidget(self.fr_opt_cfg_autoclose)

        self.fr_opt_cfg_resize = QFrame(self.pg_opt_configs)
        self.fr_opt_cfg_resize.setObjectName(u"fr_opt_cfg_resize")
        self.glay_fr_opt_cfg_resize = QGridLayout(self.fr_opt_cfg_resize)
        self.glay_fr_opt_cfg_resize.setSpacing(5)
        self.glay_fr_opt_cfg_resize.setObjectName(u"glay_fr_opt_cfg_resize")
        self.glay_fr_opt_cfg_resize.setContentsMargins(5, 5, 5, 5)
        self.lb_opt_cfg_resize = QLabel(self.fr_opt_cfg_resize)
        self.lb_opt_cfg_resize.setObjectName(u"lb_opt_cfg_resize")

        self.glay_fr_opt_cfg_resize.addWidget(self.lb_opt_cfg_resize, 0, 0, 1, 1)

        self.ck_opt_cfg_resize = QCheckBox(self.fr_opt_cfg_resize)
        self.ck_opt_cfg_resize.setObjectName(u"ck_opt_cfg_resize")

        self.glay_fr_opt_cfg_resize.addWidget(self.ck_opt_cfg_resize, 0, 1, 1, 1)

        self.lb_opt_cfg_resize_width = QLabel(self.fr_opt_cfg_resize)
        self.lb_opt_cfg_resize_width.setObjectName(u"lb_opt_cfg_resize_width")

        self.glay_fr_opt_cfg_resize.addWidget(self.lb_opt_cfg_resize_width, 1, 0, 1, 1)

        self.lb_opt_cfg_resize_height = QLabel(self.fr_opt_cfg_resize)
        self.lb_opt_cfg_resize_height.setObjectName(u"lb_opt_cfg_resize_height")

        self.glay_fr_opt_cfg_resize.addWidget(self.lb_opt_cfg_resize_height, 2, 0, 1, 1)

        self.sb_opt_cfg_resize_width = QSpinBox(self.fr_opt_cfg_resize)
        self.sb_opt_cfg_resize_width.setObjectName(u"sb_opt_cfg_resize_width")

        self.glay_fr_opt_cfg_resize.addWidget(self.sb_opt_cfg_resize_width, 1, 1, 1, 1)

        self.sb_opt_cfg_resize_height = QSpinBox(self.fr_opt_cfg_resize)
        self.sb_opt_cfg_resize_height.setObjectName(u"sb_opt_cfg_resize_height")

        self.glay_fr_opt_cfg_resize.addWidget(self.sb_opt_cfg_resize_height, 2, 1, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.glay_fr_opt_cfg_resize.addItem(self.horizontalSpacer_9, 0, 2, 3, 1)


        self.vlay_pg_opt_configs.addWidget(self.fr_opt_cfg_resize)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vlay_pg_opt_configs.addItem(self.verticalSpacer_9)

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
        self.cb_opt_tm_theme = QComboBox(self.pg_opt_themes)
        self.cb_opt_tm_theme.setObjectName(u"cb_opt_tm_theme")

        self.vlay_pg_opt_themes.addWidget(self.cb_opt_tm_theme)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vlay_pg_opt_themes.addItem(self.verticalSpacer_4)

        self.hlay_opt_tm_colors = QHBoxLayout()
        self.hlay_opt_tm_colors.setSpacing(0)
        self.hlay_opt_tm_colors.setObjectName(u"hlay_opt_tm_colors")
        self.pb_opt_tm_th1 = QPushButton(self.pg_opt_themes)
        self.pb_opt_tm_th1.setObjectName(u"pb_opt_tm_th1")

        self.hlay_opt_tm_colors.addWidget(self.pb_opt_tm_th1)

        self.pb_opt_tm_th2 = QPushButton(self.pg_opt_themes)
        self.pb_opt_tm_th2.setObjectName(u"pb_opt_tm_th2")

        self.hlay_opt_tm_colors.addWidget(self.pb_opt_tm_th2)

        self.pb_opt_tm_th3 = QPushButton(self.pg_opt_themes)
        self.pb_opt_tm_th3.setObjectName(u"pb_opt_tm_th3")

        self.hlay_opt_tm_colors.addWidget(self.pb_opt_tm_th3)

        self.pb_opt_tm_bn1 = QPushButton(self.pg_opt_themes)
        self.pb_opt_tm_bn1.setObjectName(u"pb_opt_tm_bn1")

        self.hlay_opt_tm_colors.addWidget(self.pb_opt_tm_bn1)

        self.pb_opt_tm_bn2 = QPushButton(self.pg_opt_themes)
        self.pb_opt_tm_bn2.setObjectName(u"pb_opt_tm_bn2")

        self.hlay_opt_tm_colors.addWidget(self.pb_opt_tm_bn2)


        self.vlay_pg_opt_themes.addLayout(self.hlay_opt_tm_colors)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vlay_pg_opt_themes.addItem(self.verticalSpacer_10)

        self.pb_opt_tm_colors = QPushButton(self.pg_opt_themes)
        self.pb_opt_tm_colors.setObjectName(u"pb_opt_tm_colors")

        self.vlay_pg_opt_themes.addWidget(self.pb_opt_tm_colors)

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

        self.verticalSpacer_5 = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Fixed)

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

        self.vlay_sca_option.addWidget(self.stk_option)

        self.sca_option.setWidget(self.sca_area_option)

        self.hlay_option.addWidget(self.sca_option)


        self.glay_stk_option.addLayout(self.hlay_option, 0, 1, 1, 1)

        self.stk_dlg.addWidget(self.pg_dlg_option)
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
        self.hlay_pg_dlg_msg.setContentsMargins(0, 2, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_pg_dlg_msg.addItem(self.horizontalSpacer)

        self.pb_dlg_msg_ok = QPushButton(self.fr_pg_dlg_msg)
        self.pb_dlg_msg_ok.setObjectName(u"pb_dlg_msg_ok")
        sizePolicy.setHeightForWidth(self.pb_dlg_msg_ok.sizePolicy().hasHeightForWidth())
        self.pb_dlg_msg_ok.setSizePolicy(sizePolicy)

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
        self.hlay_pg_dlg_rep.setContentsMargins(0, 0, 2, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_pg_dlg_rep.addItem(self.horizontalSpacer_3)

        self.pb_dlg_rep_ok = QPushButton(self.fr_pg_dlg_rep)
        self.pb_dlg_rep_ok.setObjectName(u"pb_dlg_rep_ok")
        sizePolicy.setHeightForWidth(self.pb_dlg_rep_ok.sizePolicy().hasHeightForWidth())
        self.pb_dlg_rep_ok.setSizePolicy(sizePolicy)

        self.hlay_pg_dlg_rep.addWidget(self.pb_dlg_rep_ok)

        self.pb_dlg_rep_annuler = QPushButton(self.fr_pg_dlg_rep)
        self.pb_dlg_rep_annuler.setObjectName(u"pb_dlg_rep_annuler")
        sizePolicy.setHeightForWidth(self.pb_dlg_rep_annuler.sizePolicy().hasHeightForWidth())
        self.pb_dlg_rep_annuler.setSizePolicy(sizePolicy)

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
        self.hlay_pg_dlg_input.setContentsMargins(0, 2, 0, 0)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_pg_dlg_input.addItem(self.horizontalSpacer_4)

        self.pb_dlg_input_ok = QPushButton(self.fr_pg_dlg_input)
        self.pb_dlg_input_ok.setObjectName(u"pb_dlg_input_ok")
        sizePolicy.setHeightForWidth(self.pb_dlg_input_ok.sizePolicy().hasHeightForWidth())
        self.pb_dlg_input_ok.setSizePolicy(sizePolicy)

        self.hlay_pg_dlg_input.addWidget(self.pb_dlg_input_ok)

        self.pb_dlg_input_annuler = QPushButton(self.fr_pg_dlg_input)
        self.pb_dlg_input_annuler.setObjectName(u"pb_dlg_input_annuler")
        sizePolicy.setHeightForWidth(self.pb_dlg_input_annuler.sizePolicy().hasHeightForWidth())
        self.pb_dlg_input_annuler.setSizePolicy(sizePolicy)

        self.hlay_pg_dlg_input.addWidget(self.pb_dlg_input_annuler)


        self.vlay_pg_dlg_input.addWidget(self.fr_pg_dlg_input)

        self.stk_dlg.addWidget(self.pg_dlg_input)
        self.pg_dlg_colors = QWidget()
        self.pg_dlg_colors.setObjectName(u"pg_dlg_colors")
        self.vlay_pg_dlg_colors = QVBoxLayout(self.pg_dlg_colors)
        self.vlay_pg_dlg_colors.setSpacing(0)
        self.vlay_pg_dlg_colors.setObjectName(u"vlay_pg_dlg_colors")
        self.vlay_pg_dlg_colors.setContentsMargins(0, 0, 0, 0)
        self.sca_colors = QScrollArea(self.pg_dlg_colors)
        self.sca_colors.setObjectName(u"sca_colors")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sca_colors.sizePolicy().hasHeightForWidth())
        self.sca_colors.setSizePolicy(sizePolicy1)
        self.sca_colors.setWidgetResizable(True)
        self.sca_area_colors = QWidget()
        self.sca_area_colors.setObjectName(u"sca_area_colors")
        self.sca_area_colors.setGeometry(QRect(0, 0, 905, 226))
        self.hlay_sca_area_colors = QHBoxLayout(self.sca_area_colors)
        self.hlay_sca_area_colors.setSpacing(10)
        self.hlay_sca_area_colors.setObjectName(u"hlay_sca_area_colors")
        self.hlay_sca_area_colors.setContentsMargins(10, 10, 10, 0)
        self.glay_sca_area_colors = QGridLayout()
        self.glay_sca_area_colors.setSpacing(0)
        self.glay_sca_area_colors.setObjectName(u"glay_sca_area_colors")
        self.sb_opt_rgb_green = QSpinBox(self.sca_area_colors)
        self.sb_opt_rgb_green.setObjectName(u"sb_opt_rgb_green")

        self.glay_sca_area_colors.addWidget(self.sb_opt_rgb_green, 4, 2, 1, 1)

        self.lb_opt_rgb_green = QLabel(self.sca_area_colors)
        self.lb_opt_rgb_green.setObjectName(u"lb_opt_rgb_green")

        self.glay_sca_area_colors.addWidget(self.lb_opt_rgb_green, 4, 0, 1, 1)

        self.lb_opt_rgb_blue = QLabel(self.sca_area_colors)
        self.lb_opt_rgb_blue.setObjectName(u"lb_opt_rgb_blue")

        self.glay_sca_area_colors.addWidget(self.lb_opt_rgb_blue, 7, 0, 1, 1)

        self.sb_opt_rgb_blue = QSpinBox(self.sca_area_colors)
        self.sb_opt_rgb_blue.setObjectName(u"sb_opt_rgb_blue")

        self.glay_sca_area_colors.addWidget(self.sb_opt_rgb_blue, 7, 2, 1, 1)

        self.lb_opt_rgb_red = QLabel(self.sca_area_colors)
        self.lb_opt_rgb_red.setObjectName(u"lb_opt_rgb_red")

        self.glay_sca_area_colors.addWidget(self.lb_opt_rgb_red, 0, 0, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.glay_sca_area_colors.addItem(self.horizontalSpacer_12, 7, 1, 1, 1)

        self.sd_opt_rgb_red = QSlider(self.sca_area_colors)
        self.sd_opt_rgb_red.setObjectName(u"sd_opt_rgb_red")
        self.sd_opt_rgb_red.setOrientation(Qt.Horizontal)

        self.glay_sca_area_colors.addWidget(self.sd_opt_rgb_red, 1, 0, 1, 3)

        self.sd_opt_rgb_green = QSlider(self.sca_area_colors)
        self.sd_opt_rgb_green.setObjectName(u"sd_opt_rgb_green")
        self.sd_opt_rgb_green.setOrientation(Qt.Horizontal)

        self.glay_sca_area_colors.addWidget(self.sd_opt_rgb_green, 5, 0, 1, 3)

        self.sb_opt_rgb_red = QSpinBox(self.sca_area_colors)
        self.sb_opt_rgb_red.setObjectName(u"sb_opt_rgb_red")

        self.glay_sca_area_colors.addWidget(self.sb_opt_rgb_red, 0, 2, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.glay_sca_area_colors.addItem(self.verticalSpacer_12, 6, 0, 1, 3)

        self.sd_opt_rgb_blue = QSlider(self.sca_area_colors)
        self.sd_opt_rgb_blue.setObjectName(u"sd_opt_rgb_blue")
        self.sd_opt_rgb_blue.setOrientation(Qt.Horizontal)

        self.glay_sca_area_colors.addWidget(self.sd_opt_rgb_blue, 8, 0, 1, 3)

        self.verticalSpacer_13 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.glay_sca_area_colors.addItem(self.verticalSpacer_13, 2, 0, 1, 3)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.glay_sca_area_colors.addItem(self.horizontalSpacer_11, 4, 1, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.glay_sca_area_colors.addItem(self.verticalSpacer_11, 9, 0, 1, 3)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.glay_sca_area_colors.addItem(self.horizontalSpacer_10, 0, 1, 1, 1)


        self.hlay_sca_area_colors.addLayout(self.glay_sca_area_colors)

        self.frame = QFrame(self.sca_area_colors)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.hlay_sca_area_colors.addWidget(self.frame)

        self.sca_colors.setWidget(self.sca_area_colors)

        self.vlay_pg_dlg_colors.addWidget(self.sca_colors)

        self.fr_pg_dlg_colors = QFrame(self.pg_dlg_colors)
        self.fr_pg_dlg_colors.setObjectName(u"fr_pg_dlg_colors")
        self.hlay_fr_pg_dlg_colors = QHBoxLayout(self.fr_pg_dlg_colors)
        self.hlay_fr_pg_dlg_colors.setSpacing(2)
        self.hlay_fr_pg_dlg_colors.setObjectName(u"hlay_fr_pg_dlg_colors")
        self.hlay_fr_pg_dlg_colors.setContentsMargins(0, 2, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_fr_pg_dlg_colors.addItem(self.horizontalSpacer_7)

        self.pb_dlg_colors_ok = QPushButton(self.fr_pg_dlg_colors)
        self.pb_dlg_colors_ok.setObjectName(u"pb_dlg_colors_ok")
        sizePolicy.setHeightForWidth(self.pb_dlg_colors_ok.sizePolicy().hasHeightForWidth())
        self.pb_dlg_colors_ok.setSizePolicy(sizePolicy)

        self.hlay_fr_pg_dlg_colors.addWidget(self.pb_dlg_colors_ok)


        self.vlay_pg_dlg_colors.addWidget(self.fr_pg_dlg_colors)

        self.stk_dlg.addWidget(self.pg_dlg_colors)

        self.vlay_fr_main.addWidget(self.stk_dlg)


        self.glay_dlg.addWidget(self.fr_main, 1, 0, 1, 1)


        self.retranslateUi(Dlg)

        self.stk_dlg.setCurrentIndex(4)
        self.stk_option.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Dlg)
    # setupUi

    def retranslateUi(self, Dlg):

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
        self.le_opt_ft_texte_h1.setText(QCoreApplication.translate("Dlg", u"TEST De la Police", None))
        self.lb_opt_ft_h2.setText(QCoreApplication.translate("Dlg", u"Taille H2: ", None))
        self.le_opt_ft_texte_h2.setText(QCoreApplication.translate("Dlg", u"TEST De la Police", None))
        self.lb_opt_ft_h3.setText(QCoreApplication.translate("Dlg", u"Taille H3: ", None))
        self.le_opt_ft_texte_h3.setText(QCoreApplication.translate("Dlg", u"TEST De la Police", None))
        self.lb_opt_ft_h4.setText(QCoreApplication.translate("Dlg", u"Taille H4: ", None))
        self.le_opt_ft_texte_h4.setText(QCoreApplication.translate("Dlg", u"TEST De la Police", None))
        self.lb_opt_ft_h5.setText(QCoreApplication.translate("Dlg", u"Taille H5: ", None))
        self.le_opt_ft_texte_h5.setText(QCoreApplication.translate("Dlg", u"TEST De la Police", None))
        self.lb_opt_cfg_opacity.setText(QCoreApplication.translate("Dlg", u"Opacit\u00e9 ", None))
        self.lb_opt_cfg_autoclose.setText(QCoreApplication.translate("Dlg", u"Auto close : ", None))
        self.lb_opt_cfg_autoreload.setText(QCoreApplication.translate("Dlg", u"Auto reload : ", None))
        self.lb_opt_cfg_resize.setText(QCoreApplication.translate("Dlg", u"Manuel : ", None))
        self.lb_opt_cfg_resize_width.setText(QCoreApplication.translate("Dlg", u"Largeur : ", None))
        self.lb_opt_cfg_resize_height.setText(QCoreApplication.translate("Dlg", u"Hauteur : ", None))
        self.pb_opt_tm_th1.setText(QCoreApplication.translate("Dlg", u"TH1", None))
        self.pb_opt_tm_th2.setText(QCoreApplication.translate("Dlg", u"TH2", None))
        self.pb_opt_tm_th3.setText(QCoreApplication.translate("Dlg", u"TH3", None))
        self.pb_opt_tm_bn1.setText(QCoreApplication.translate("Dlg", u"BN1", None))
        self.pb_opt_tm_bn2.setText(QCoreApplication.translate("Dlg", u"BN2", None))
        self.pb_opt_tm_colors.setText(QCoreApplication.translate("Dlg", u"Couleurs", None))
        self.le_input.setPlaceholderText(QCoreApplication.translate("Dlg", u"...", None))
        self.lb_opt_rgb_green.setText(QCoreApplication.translate("Dlg", u"GREEN", None))
        self.lb_opt_rgb_blue.setText(QCoreApplication.translate("Dlg", u"BLUE", None))
        self.lb_opt_rgb_red.setText(QCoreApplication.translate("Dlg", u"RED", None))
        pass
    # retranslateUi

