from PySide6 import QtGui

from src.config import config


class Cur:
    base = [9, 1]
    centre = [16, 16]

    def CUR(self, img): return f"src/assets/cursor/{config.cur}/{img}.cur"
    def ANI(self, img): return f"src/assets/cursor/{config.cur}/{img}.ani"

    def agrandir(self): return QtGui.QCursor(QtGui.QPixmap(self.CUR("agrandir")), self.base[0], self.base[1])
    def copier(self): return QtGui.QCursor(QtGui.QPixmap(self.CUR("copier")), self.base[0], self.base[1])
    def crayon(self): return QtGui.QCursor(QtGui.QPixmap(self.CUR("crayon")), 1, 32)
    def croix(self): return QtGui.QCursor(QtGui.QPixmap(self.CUR("croix")), self.centre[0], self.centre[1])
    def fleche_nesw(self): return QtGui.QCursor(QtGui.QPixmap(self.CUR("fleche_nesw")), self.centre[0], self.centre[1])
    def fleche_ns(self): return QtGui.QCursor(QtGui.QPixmap(self.CUR("fleche_ns")), self.centre[0], self.centre[1])
    def fleche_nwse(self): return QtGui.QCursor(QtGui.QPixmap(self.CUR("fleche_nwse")), self.centre[0], self.centre[1])
    def fleche_top(self): return QtGui.QCursor(QtGui.QPixmap(self.CUR("fleche_top")), 16, 1)
    def fleche_tout(self): return QtGui.QCursor(QtGui.QPixmap(self.CUR("fleche_tout")), self.centre[0], self.centre[1])
    def fleche_we(self): return QtGui.QCursor(QtGui.QPixmap(self.CUR("fleche_we")), self.centre[0], self.centre[1])
    def ibeam(self): return QtGui.QCursor(QtGui.QPixmap(self.CUR("ibeam")), self.centre[0], self.centre[1])
    def infos(self): return QtGui.QCursor(QtGui.QPixmap(self.CUR("infos")), self.base[0], self.base[1])
    def main(self): return QtGui.QCursor(QtGui.QPixmap(self.CUR("main")), self.base[0], self.base[1])
    def non(self): return QtGui.QCursor(QtGui.QPixmap(self.CUR("non")), self.centre[0], self.centre[1])
    def retour(self): return QtGui.QCursor(QtGui.QPixmap(self.CUR("retour")), self.base[0], self.base[1])
    def souris(self): return QtGui.QCursor(QtGui.QPixmap(self.CUR("souris")), self.base[0], self.base[1])
    def souris_main(self): return QtGui.QCursor(QtGui.QPixmap(self.CUR("souris_main")), self.base[0], self.base[1])
    def souris_non(self): return QtGui.QCursor(QtGui.QPixmap(self.CUR("souris_non")), self.base[0], self.base[1])
    def wait(self): return QtGui.QCursor(QtGui.QPixmap(self.CUR("wait")), self.centre[0], self.centre[1])
