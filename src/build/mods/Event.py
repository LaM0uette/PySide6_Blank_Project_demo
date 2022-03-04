from PySide6 import QtCore, QtGui

from src.lib.globals import v_gb
from src.lib.palettes import *


class Event:

    def __init__(self, ui):
        self.ui = ui

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
            self.ui.e_agrandir()
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
            self.ui.e_agrandir()
            event.accept()
