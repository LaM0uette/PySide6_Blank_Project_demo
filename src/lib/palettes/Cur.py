import json
import os

from PySide6 import QtGui

from src.config import config


class Cur:
    with open(f"{os.path.dirname(f'src/assets/cursor/{config.cur}/_data.json')}/_data.json", "r", encoding="utf-8") as fichier:
        cur = json.load(fichier)

    _souris = cur["_souris"]
    _centre = cur["_centre"]
    _crayon = cur["_crayon"]
    _fleche_top = cur["_fleche_top"]

    def CUR(self, img): return f"src/assets/cursor/{config.cur}/{img}.cur"
    def ANI(self, img): return f"src/assets/cursor/{config.cur}/{img}.ani"

    def agrandir(self): return QtGui.QCursor(QtGui.QPixmap(self.CUR("agrandir")), self._souris[0], self._souris[1])
    def copier(self): return QtGui.QCursor(QtGui.QPixmap(self.CUR("copier")), self._souris[0], self._souris[1])
    def crayon(self): return QtGui.QCursor(QtGui.QPixmap(self.CUR("crayon")), self._crayon[0], self._crayon[1])
    def croix(self): return QtGui.QCursor(QtGui.QPixmap(self.CUR("croix")), self._centre[0], self._centre[1])
    def fleche_nesw(self): return QtGui.QCursor(QtGui.QPixmap(self.CUR("fleche_nesw")), self._centre[0], self._centre[1])
    def fleche_ns(self): return QtGui.QCursor(QtGui.QPixmap(self.CUR("fleche_ns")), self._centre[0], self._centre[1])
    def fleche_nwse(self): return QtGui.QCursor(QtGui.QPixmap(self.CUR("fleche_nwse")), self._centre[0], self._centre[1])
    def fleche_top(self): return QtGui.QCursor(QtGui.QPixmap(self.CUR("fleche_top")), self._fleche_top[0], self._fleche_top[1])
    def fleche_tout(self): return QtGui.QCursor(QtGui.QPixmap(self.CUR("fleche_tout")), self._centre[0], self._centre[1])
    def fleche_we(self): return QtGui.QCursor(QtGui.QPixmap(self.CUR("fleche_we")), self._centre[0], self._centre[1])
    def ibeam(self): return QtGui.QCursor(QtGui.QPixmap(self.CUR("ibeam")), self._centre[0], self._centre[1])
    def infos(self): return QtGui.QCursor(QtGui.QPixmap(self.CUR("infos")), self._souris[0], self._souris[1])
    def main(self): return QtGui.QCursor(QtGui.QPixmap(self.CUR("main")), self._souris[0], self._souris[1])
    def non(self): return QtGui.QCursor(QtGui.QPixmap(self.CUR("non")), self._centre[0], self._centre[1])
    def retour(self): return QtGui.QCursor(QtGui.QPixmap(self.CUR("retour")), self._souris[0], self._souris[1])
    def souris(self): return QtGui.QCursor(QtGui.QPixmap(self.CUR("souris")), self._souris[0], self._souris[1])
    def souris_main(self): return QtGui.QCursor(QtGui.QPixmap(self.CUR("souris_main")), self._souris[0], self._souris[1])
    def souris_non(self): return QtGui.QCursor(QtGui.QPixmap(self.CUR("souris_non")), self._souris[0], self._souris[1])
    def wait(self): return QtGui.QCursor(QtGui.QPixmap(self.CUR("wait")), self._centre[0], self._centre[1])
