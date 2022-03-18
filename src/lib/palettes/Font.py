from PySide6 import QtGui

from src.config import config


class FontSize:
    H1 = 32
    H2 = 24
    H3 = 16
    H4 = 12
    H5 = 8


class Font:
    H1 = 32  # A SUPPRIMER
    H2 = 24  # A SUPPRIMER
    H3 = 16  # A SUPPRIMER
    H4 = 12  # A SUPPRIMER
    H5 = 8  # A SUPPRIMER

    @staticmethod
    def base():
        ft = QtGui.QFont()
        ft.setFamily(config.font)
        ft.setPointSize(FontSize.H4)
        return ft

    @staticmethod
    def titre():
        ft = QtGui.QFont()
        ft.setFamily(config.font)
        ft.setPointSize(FontSize.H1)
        return ft

    @staticmethod
    def texte():
        ft = QtGui.QFont()
        ft.setFamily(config.font)
        ft.setPointSize(FontSize.H5)
        return ft
