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
