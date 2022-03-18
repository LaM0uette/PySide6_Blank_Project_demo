from PySide6 import QtGui

from src.config import config


class Font:
    H1 = 32             # A SUPPRIMER
    H2 = 24             # A SUPPRIMER
    H3 = 16             # A SUPPRIMER
    H4 = 12             # A SUPPRIMER
    H5 = 8              # A SUPPRIMER

    def base(self):
        ft = QtGui.QFont()
        ft.setFamily(config.font)
        ft.setPointSize(self.H4)
        return ft
    def titre(self):
        ft = QtGui.QFont()
        ft.setFamily(config.font)
        ft.setPointSize(self.H1)
        return ft
    def texte(self):
        ft = QtGui.QFont()
        ft.setFamily(config.font)
        ft.setPointSize(self.H5)
        return ft
