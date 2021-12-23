"""
_TITRE: Définition des palettes

_DESC: Dictionnaires des palettes qui servent à configurer des thèmes pour les widgets.
    Il suffit dans le dictionnaires des classes de faire appel à ces palettes.
    Voici comment les configurer:

A0: "pal": {"nom_palette": {"c1": couleur_th1 _type:(), "c2": couleur_th2 _type:(), "c3": couleur_th3 _type:(), "bn": couleur_bn _type:()}}
    _ex: "th": {"c1": (20, 20, 20), "c2": (80, 80, 80), "c3": (150, 150, 150), "bn": (255, 0, 0)}
    _acp: None

A0: "dim": {"nom_dim": {"w": largeur _type:int, "h": hauteur _type:int}
    _ex: "all_w": {"w": None, "h": 30} | "all_h": {"w": 150, "h": None} | "all": {"w": None, "h": None}
    _acp: None
"""

from . import dct_gen
from .config import colors

wg = dct_gen.dct_size.get("wg")
dim = dct_gen.dct_dim


dct_pal = {
    "pal": {
        # Palettes de bases ___________________________________________________________
        "th1": {"c1": colors.th1, "c2": colors.th2, "c3": colors.th3, "bn": colors.bn1},
        "th2": {"c1": colors.th2, "c2": colors.th1, "c3": colors.th4, "bn": colors.bn1},
        "th3": {"c1": colors.th3, "c2": colors.th4, "c3": colors.th1, "bn": colors.bn1},
        "th4": {"c1": colors.th4, "c2": colors.th3, "c3": colors.th2, "bn": colors.bn1},
        "u1": {"c1": colors.th1},
        "u2": {"c1": colors.th2},
        "u3": {"c1": colors.th3},
        "u4": {"c1": colors.th4},

        # Palettes valider / annuler _______________________________________________________
        "vert": {"c1": colors.th1, "c2": colors.th2, "c3": colors.vert, "bn": colors.bn1},
        "rouge": {"c1": colors.th1, "c2": colors.th2, "c3": colors.rouge, "bn": colors.bn1}
    },
    "dim": {
        # Base ______________________
        "all": {"w": None, "h": None},
        "aw_h4": {"w": None, "h": wg.get("h4")},
        "c_h4": {"w": wg.get("h4"), "h": wg.get("h4")},

        # Menu top
        "aw_menu_top": {"w": None, "h": dim.get("h_menu_top")},
        "r_menu_top": {"w": dim.get("h_menu_top")*1.5, "h": dim.get("h_menu_top")},
        "c_menu_top": {"w": dim.get("h_menu_top"), "h": dim.get("h_menu_top")},
    }
}
