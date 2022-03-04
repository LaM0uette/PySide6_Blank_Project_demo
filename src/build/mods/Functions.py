from PySide6 import QtCore, QtGui


class Functions:

    def SET_DIM(self, *args, width=None, height=None):
        for wg in args:
            if width is not None: wg.setFixedWidth(width)
            if height is not None: wg.setFixedHeight(height)

    def ADD_QACTION(self, tray, ico=None, ico_rgb=None, txt="", status_tip="", height=None, fct=None, sht_1=None, sht_2=None, sht_3=None):
        if height is None: height=12

        shortcut = int()
        if sht_1 is not None: shortcut += sht_1
        if sht_2 is not None: shortcut += sht_2
        if sht_3 is not None: shortcut += sht_3

        action = QtGui.QAction(self)
        action.setIcon(QtGui.QPixmap(f"{ico}{ico_rgb}.svg").scaledToHeight(height))
        action.setText(txt)
        action.setShortcut("Ctrl+Shift+A")
        action.setStatusTip(status_tip)
        action.triggered.connect(fct)

        tray.addAction(action)
        QtGui.QShortcut(QtGui.QKeySequence(shortcut), self).activated.connect(fct)
