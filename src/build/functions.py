from PySide6 import QtGui

from . import P_cur


class Fct:
    def __init__(self, **kwargs):

        self.kwargs = kwargs

    def CUR(self):
        cur = self.kwargs.get("cur")
        if cur is None: cur = "souris"

        cursor = P_cur().RTN_CUR(cur)
        return QtGui.QCursor(QtGui.QPixmap(cursor[0]), cursor[1], cursor[2])
    def DIM(self):
        wg = self.kwargs.get("wg")
        if wg is None: return

        w, h = self.kwargs.get("w"), self.kwargs.get("h")

        wg.setFixedWidth(w) if w is not None else False
        wg.setFixedHeight(h) if h is not None else False
