from PySide6 import QtGui

from . import P_cur


class Fct:
    def __init__(self, **kwargs):

        self.kwargs = kwargs

    def CUR(self):
        cur = P_cur().RTN_CUR(self.kwargs.get("cur"))
        return QtGui.QCursor(QtGui.QPixmap(cur[0]), cur[1], cur[2])
