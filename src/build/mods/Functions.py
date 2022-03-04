from PySide6 import QtCore, QtGui


class Functions:

    def SET_DIM(self, *args, width=None, height=None):
        for wg in args:
            if width is not None: wg.setFixedWidth(width)
            if height is not None: wg.setFixedHeight(height)

    def ADD_QACTION(self, tray=None, ico=None, ico_rgb=None, txt=None, fct=None, height=None):
        if height is None : height=12

        action = QtGui.QAction()
        action.setIcon(QtGui.QPixmap(f"{ico}{ico_rgb}.svg").scaledToHeight(height))
        action.setText(txt)
        action.setShortcut("t")

        tray.addAction(action)
    def ADD_QSHORTCUT(self, slf, sht_1, sht_2, sht_3, fct):
        shortcut = int()
        if sht_1 is not None: shortcut += sht_1
        if sht_2 is not None: shortcut += sht_2
        if sht_3 is not None: shortcut += sht_3

        QtGui.QShortcut(QtGui.QKeySequence(shortcut), slf).activated.connect(fct)
