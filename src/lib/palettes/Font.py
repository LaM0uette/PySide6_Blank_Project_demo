from PySide6 import QtGui

from src.config import config


class Font:
    H1 = 32             # A SUPPRIMER
    H2 = 24             # A SUPPRIMER
    H3 = 16             # A SUPPRIMER
    H4 = 12             # A SUPPRIMER
    H5 = 8              # A SUPPRIMER

    font_size = {
        "h1": 33,
        "h2": 25,
        "h3": 17,
        "h4": 13,
        "h5": 9
    }

    def base(self):
        ft = QtGui.QFont()
        ft.setFamily(config.font)
        ft.setPointSize(self.font_size.get("h4"))
        return ft
    def titre(self):
        ft = QtGui.QFont()
        ft.setFamily(config.font)
        ft.setPointSize(self.font_size.get("h1"))
        return ft
    def texte(self):
        ft = QtGui.QFont()
        ft.setFamily(config.font)
        ft.setPointSize(self.font_size.get("h5"))
        return ft
