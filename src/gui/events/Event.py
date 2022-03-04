from PySide6 import QtCore, QtWidgets, QtGui

from src.config import config
from src.lib.globals import v_gb
from src.lib.palettes import *


class Event:
    def __init__(self, ui):
        self.ui = ui


    def _e_center_screen(self):
        center = QtGui.QScreen.availableGeometry(QtWidgets.QApplication.primaryScreen()).center()
        geo = self.ui.frameGeometry()
        geo.moveCenter(center)
        self.ui.move(geo.topLeft())

    #####

    def e_agrandir(self):
        if self.ui.windowState() == QtCore.Qt.WindowMaximized:
            self.ui.win_state = QtCore.Qt.WindowNoState
            self._e_center_screen()
            self.ui.e_resize_screen()
        else:
            self.ui.win_state = QtCore.Qt.WindowMaximized

        self.ui.setWindowState(self.ui.win_state)
    def e_reduire(self):
        self.ui.setWindowState(QtCore.Qt.WindowMinimized)
    def e_cacher(self):
        if config.debug: return self.e_quitter()
        self.ui.hide()
        self._e_center_screen()
    def e_quitter(self):
        if not config.auto_close:
            self.ui.hide()
        elif config.auto_close:  # DLG_Rep().QUITTER()
            self.ui.app.quit()

    #####

    def mousePressEvent(self, event):
        cur = QtGui.QCursor()
        verif_height = cur.pos().y() - self.ui.pos().y()
        if event.buttons() == QtCore.Qt.LeftButton and v_gb.BD_LIMIT < verif_height < Dim().h9()+v_gb.BD_LIMIT and self.ui.windowState() != QtCore.Qt.WindowMaximized:
            self.ui.dragPos = event.globalPosition().toPoint()
            event.accept()
    def mouseDoubleClickEvent(self, event):
        cur = QtGui.QCursor()
        verif_height = cur.pos().y() - self.ui.pos().y()
        if v_gb.BD_LIMIT < verif_height < Dim().h9()+v_gb.BD_LIMIT:
            self.e_agrandir()
            event.accept()
    def mouseMoveEvent(self, event):
        def act_move(event):
            self.ui.move(self.ui.pos() + event.globalPosition().toPoint() - self.ui.dragPos)
            self.ui.dragPos = event.globalPosition().toPoint()
            event.accept()

        cur = QtGui.QCursor()
        verif_height = cur.pos().y() - self.ui.pos().y()
        if event.buttons() == QtCore.Qt.LeftButton and v_gb.BD_LIMIT < verif_height < Dim().h9()+v_gb.BD_LIMIT and self.ui.windowState() != QtCore.Qt.WindowMaximized and cur.pos().y() <= 0:
            self.ui.setCursor(Cur().agrandir())
        else:
            self.ui.setCursor(Cur().souris())

        try:
            if event.buttons() == QtCore.Qt.LeftButton and v_gb.BD_LIMIT < verif_height < Dim().h9()+v_gb.BD_LIMIT and self.ui.windowState() != QtCore.Qt.WindowMaximized:
                act_move(event)
            if event.buttons() == QtCore.Qt.LeftButton and v_gb.BD_LIMIT < verif_height < Dim().h9()+v_gb.BD_LIMIT and self.ui.windowState() == QtCore.Qt.WindowMaximized:
                self.ui.setWindowState(QtCore.Qt.WindowNoState)
                self.ui.win_state = QtCore.Qt.WindowNoState
                act_move(event)
        except AttributeError: pass
    def mouseReleaseEvent(self, event):
        cur = QtGui.QCursor()
        verif_height = cur.pos().y() - self.ui.pos().y()
        if v_gb.BD_LIMIT < verif_height < Dim().h9()+v_gb.BD_LIMIT and self.ui.windowState() != QtCore.Qt.WindowMaximized and cur.pos().y() <= 0:
            self.ui.setCursor(Cur().souris())
            self.e_agrandir()
            event.accept()
