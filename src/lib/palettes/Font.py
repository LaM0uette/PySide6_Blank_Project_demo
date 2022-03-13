from PySide6 import QtGui

from src.config import config


class Font:
    def h1(self): return 32    # A SUPPRIMER
    def h2(self): return 24    # A SUPPRIMER
    def h3(self): return 16    # A SUPPRIMER
    def h4(self): return 12    # A SUPPRIMER
    def h5(self): return 8    # A SUPPRIMER

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
