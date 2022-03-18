from PySide6 import QtGui

from src.config import config


class FontSize:
    H1 = 32
    H2 = 24
    H3 = 16
    H4 = 12
    H5 = 8
class Font:

    @staticmethod
    def _gen_font(family=config.font, size=FontSize.H4):
        ft = QtGui.QFont()
        ft.setFamily(family)
        ft.setPointSize(size)
        return ft

    H1 = 32  # A SUPPRIMER
    H2 = 24  # A SUPPRIMER
    H3 = 16  # A SUPPRIMER
    H4 = 12  # A SUPPRIMER
    H5 = 8  # A SUPPRIMER

    BASE = _gen_font(size=FontSize.H4)
    TITRE = _gen_font(size=FontSize.H1)
    TEXTE = _gen_font(size=FontSize.H5)
