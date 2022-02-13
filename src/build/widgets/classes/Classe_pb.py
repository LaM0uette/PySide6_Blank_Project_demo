from PySide6 import QtCore

from ....build import *


class Classe_pb:
    def __init__(self, **kwargs):

        self.kwargs = kwargs

        self.wg = self.kwargs.get("wg")
        self.dim_ico = self.kwargs.get("dim_ico")
        self.DIM_ICO = self.kwargs.get("DIM_ICO")
        self.img = self.kwargs.get("img")
        self.img_check = self.kwargs.get("img_check")
        self.tm = self.kwargs.get("tm")
        self.tm_hover = self.kwargs.get("tm_hover")
        self.tm_check = self.kwargs.get("tm_check")


    def MP_CHECK(self, event):
        if event.buttons() and QtCore.Qt.LeftButton and self.wg.isEnabled():
            if self.wg.isChecked():
                self.wg.setChecked(False)
                Fct(wg=self.wg, img=self.img + self.tm, dim=self.dim_ico).ICON()
            elif not self.wg.isChecked():
                self.wg.setChecked(True)
                Fct(wg=self.wg, img=self.img_check + self.tm, dim=self.dim_ico).ICON()

    def ENT_ICO(self, event):
        if not self.wg.isChecked() and self.wg.isEnabled():
            Fct(wg=self.wg, img=self.img + self.tm_hover, dim=self.dim_ico).ICON()
    def LVE_ICO(self, event):
        if not self.wg.isChecked() and self.wg.isEnabled():
            Fct(wg=self.wg, img=self.img + self.tm, dim=self.dim_ico).ICON()
    def MP_ICO(self, event):
        if event.buttons() and QtCore.Qt.LeftButton and self.wg.isEnabled():
            if self.wg.isChecked():
                self.wg.setChecked(False)
                Fct(wg=self.wg, img=self.img + self.tm, dim=self.dim_ico).ICON()
            elif not self.wg.isChecked():
                self.wg.setChecked(True)
                Fct(wg=self.wg, img=self.img + self.tm_hover, dim=self.dim_ico).ICON()

    def ENT_ZOOM(self, event):
        if not self.wg.isChecked() and self.wg.isEnabled():
            self.wg.setIconSize(QtCore.QSize(self.DIM_ICO, self.DIM_ICO))
    def LVE_ZOOM(self, event):
        if not self.wg.isChecked() and self.wg.isEnabled():
            self.wg.setIconSize(QtCore.QSize(self.dim_ico, self.dim_ico))