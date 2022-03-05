from PySide6 import QtCore, QtGui

from src import *


class Functions:

    def SET_DIM(self, *args, width=None, height=None):
        for wg in args:
            if width is not None: wg.setFixedWidth(width)
            if height is not None: wg.setFixedHeight(height)
    def SET_FONT(self, *args, font=config.font, font_size=Font().h5()):
        for wg in args:
            ft = QtGui.QFont()
            ft.setFamily(font)
            ft.setPointSize(font_size)
            wg.setFont(ft)

    def ADD_QACTION(self, tray, ico=None, ico_rgb=None, txt="", shortcut_txt="", status_tip="", size=None, fct=None, sht_1=None, sht_2=None, sht_3=None):
        if size is None: size=12

        shortcut = int()
        if sht_1 is not None: shortcut += sht_1
        if sht_2 is not None: shortcut += sht_2
        if sht_3 is not None: shortcut += sht_3

        action = QtGui.QAction(self)
        action.setIcon(QtGui.QPixmap(f"{ico}{ico_rgb}.svg").scaledToHeight(size))
        action.setText(txt)
        action.setShortcut(shortcut_txt)
        action.setStatusTip(status_tip)
        action.triggered.connect(fct)

        tray.addAction(action)
        QtGui.QShortcut(QtGui.QKeySequence(shortcut), self).activated.connect(fct)
