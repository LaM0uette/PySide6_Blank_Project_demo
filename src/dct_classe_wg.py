"""
_TITRE: Définition des classes de widgets

_DESC: Les classes de widgets peuvent être utilisée à l'identique dans le dictionnaire des widgets.
    mais si un même type de widgets est présent plusieurs fois, alors if suffit de faire appelle à sa classe juste ici.

_info: "colors": {"type": "type", "pal": "pal"}
_info: "dim":  dim.get("nom_dim")  #fait appelle à la classe des dimensions. _acp: dim.get("all_w_h1") == {"w": int, "h": int}
_info: "img": img.get("nom_image")
_info: "img_check": img.get("nom_image") # si check
_info: "th": "couleur_image"
_info: "th_hover": "couleur_image" # au survol
_info: "th_check": "couleur_image" # si check
_info: "font":  police.get("nom_police")  #fait appelle au dictionnaire des tailles de polices. _acp: police.get("h1") == int
_info: "rd": {"mat": "mat", "px": "px"}
_info: "bd": {"mat": "mat", "px": "px", "th": couleur}
_info: "cur" "nom_curseur"
_info: "align":  QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter  #le type d'alignement avec QtCore
_info: "edit": Bool  #Vraix ou faux
_info: "scroll": {"h": QtCore.Qt.ScrollBarAsNeeded, "v": QtCore.Qt.ScrollBarAsNeeded}  #le type de ScrollBar avec QtCore
_info: "header": {"h": Bool, "v": Bool}  #affiche ou non le header
_info: "pb_sb": QtWidgets.QAbstractSpinBox.NoButtons  #boutons des QSpinBox et QDoubleSpinBox

_info: "type":
        txt = theme pour du texte.
        txt_inv = theme pour du texte mais les couleurs sont inversées.
        th = theme normal.
        tr = theme transparent.
        zoom = icone qui zoom au survol.
        rd = ajoute un rayon sur le widget.
        bd = Bordure uniquement.
        uni = couleurs unique
_info: "pal":  pal.get("nom_palette")}  #fait appelle à la classe des palettes. _acp: pal.get("th1") == pal.get("u1") == "c1": colors.th1 == "c1": (0, 0, 0)
_info: "mat": "0011"  # matrice ou 0=None et 1=True. dans l'ordre:HG, HD, BG, BD  |  H, D, B, G _acp: None
_info: "px": 15  # taille en pixel d'un élément _acp: None
_info: "scroll":
        QtCore.Qt.ScrollBarAsNeeded = affichée si besoin
        ScrollBarAlwaysOff = jamais affichée
        ScrollBarAlwaysOn = toujours affichée
_info: "pb_sb":
        QtWidgets.QAbstractSpinBox.NoButtons = pas de boutons
        QtWidgets.QAbstractSpinBox.PlusMinus = boutons + et -
        QtWidgets.QAbstractSpinBox.UpDownArrows = boutons avec des flèches haut bas


_TITRE: QComboBox
"nom": {
A1: "colors": {"pal": %}, _acp: None
A1: "dim": dim.get("all_w_menu_top"), _acp: None
A2: "font": %, _acp: None
A2: "cur": %, _acp: None
A2: "edit": %} _acp: None

_TITRE: QDateEdit
"nom": {
A1: "colors": {"pal": %}, _acp: None
A1: "dim": dim.get("all_w_menu_top"), _acp: None
A2: "font": %, _acp: None
A2: "align": %, _acp: None
A2: "cur": %} _acp: None

_TITRE: QFrame
"nom": {
A1: "colors": {"pal": %}, _acp: None
A1: "dim": dim.get("all_w_menu_top"), _acp: None
A2: "bd": {"mat": %, "px": %, "th": %} _acp: None

_TITRE: QLabel
"nom": {
A1: "colors": {"type": %, "pal": %}, _acp: None
A1: "dim": %, _acp: None
A1: "font": %, _acp: None
A2: "align": %} _acp: None

_TITRE: QListWidget
"nom": {
A1: "colors": {"pal": %}, _acp: None
A1: "dim": dim.get("all_w_menu_top"), _acp: None
A2: "font": %, _acp: None
A2: "cur": %, _acp: None
A2: "scroll": {"h": %, "v": %}} _acp: None

_TITRE: QPushButton
"nom": {
A1: "colors": {"type": %, "pal": %}, _acp: None  _val: type - txt, txt_inv, th, tr, zoom, rd, uni
A1: "dim": %, _acp: None
A1: "img": %, _acp: None
A2: "img_check": %,
A1: "th": %, _acp: None
A2: "th_hover": %,
A2: "th_check": %, _acp: None
A1: "font": %, _acp: None
A2: "rd": {"mat": %, "px": %}, _acp: None
A2: "cur": %} _acp: None

_TITRE: QCheckBox
"nom": {
A1: "colors": {"type": %, "pal": %}, _acp: None  _val: type - th, tr, rd
A1: "dim": %, _acp: None
A1: "img": %, _acp: None
A2: "img_check": %,
A1: "th": %, _acp: None
A2: "th_check": %, _acp: None
A1: "font": %, _acp: None
A2: "rd": {"mat": %, "px": %}, _acp: None
A2: "cur": %} _acp: None

_TITRE: QRadioButton
"nom": {
A1: "colors": {"type": %, "pal": %}, _acp: None  _val: type - th, tr, rd
A1: "dim": %, _acp: None
A1: "img": %, _acp: None
A2: "img_check": %,
A1: "th": %, _acp: None
A2: "th_check": %, _acp: None
A1: "font": %, _acp: None
A2: "rd": {"mat": %, "px": %}, _acp: None
A2: "cur": %} _acp: None

_TITRE: QProgressBar
"nom": {
A1: "colors": {"type": %, "pal": %}, _acp: None
A1: "dim": %, _acp: None
A1: "font": %, _acp: None
A2: "align": %} _acp: None

_TITRE: QScrollArea
"nom": {
A1: "colors": {"type": %, "pal": %}, _acp: None
A1: "dim": %, _acp: None
A2: "scroll": {"h": %, "v": %}} _acp: None

_TITRE: QSpinBox, QDoubleSpinBox
"nom": {
A1: "colors": {"type": %, "pal": %}, _acp: None
A1: "dim": %, _acp: None
A1: "font": %, _acp: None
A2: "align": %, _acp: None
A2: "pb_sb": %} _acp: None

_TITRE: QToolBox
"nom": {
A1: "colors": {"type": %, "pal": %}, _acp: None  _val: type - th, bd, rd
A1: "dim": dim.get("all_w_menu_top"), _acp: None
A2: "font": %, _acp: None
A2: "rd": {"mat": %, "px": %}, _acp: None
A2: "cur": %} _acp: None

_TITRE: QTableWidget
"nom": {
A1: "colors": {"pal": %}, _acp: None
A1: "dim": dim.get("all_w_menu_top"), _acp: None
A2: "font": %, _acp: None
A2: "cur": %, _acp: None
A2: "scroll": {"h": %, "v": %}, _acp: None
A2: "header": {"h": %, "v": %}} _acp: None

_TITRE: QLineEdit, QTextEdit, QPlainTextEdit
"nom": {
A1: "colors": {"type": %, "pal": %}, _acp: None
A1: "dim": %, _acp: None
A1: "font": %, _acp: None
A2: "align": %, _acp: None
A2: "scroll": {"h": %, "v": %}} _acp: None
"""

from PySide6 import QtCore, QtWidgets

from . import dct_gen, dct_pal
from .config import colors


police = dct_gen.dct_size.get("police")
img = dct_gen.dct_img

pal = dct_pal.dct_pal.get("pal")
dim = dct_pal.dct_pal.get("dim")

dct_classe = {
    "txt": {
        # Option ___________
        "option_line": {
            "colors": {"type": "bd", "pal": pal.get("th1")},
            "dim": dim.get("aw_menu_top"),
            "font": police.get("h3"),
            "cur": "IBeam",
            "align": QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        },
    },
    "cb": {
        # Option __
        "option": {
            "colors": {"pal": pal.get("th1")},
            "dim": dim.get("aw_h4"),
            "edit": False
        },
    },
    "de": {},
    "fr": {
        # Menu Top _____
        "aw_menu_top": {
            "colors": {"pal": pal.get("u1")},
            "dim": dim.get("aw_menu_top")
        },

        # tb __
        "tb": {
            "colors": {"type": "bd", "pal": pal.get("th1")},
            "dim": dim.get("all"),
            "bd": {"mat": "0111"}
        }
    },
    "lb": {
        # Menu Top _
        "nom_app": {
            "colors": {"type": "tr", "pal": pal.get("u3")},
            "dim": dim.get("aw_menu_top"),
            "font": police.get("h3")
        },
        "version": {
            "colors": {"type": "tr", "pal": pal.get("u2")},
            "dim": dim.get("rect_menu_top"),
            "font": police.get("h4"),
            "align": QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        },

        # Options __
        "option": {
            "colors": {"type": "tr", "pal": pal.get("u3")},
            "dim": dim.get("aw_h4"),
            "font": police.get("h4"),
            "align": QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom
        },
        "option_titre": {
            "colors": {"type": "tr", "pal": pal.get("u3")},
            "dim": dim.get("aw_h4"),
            "font": police.get("h3"),
            "align": QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom
        },
    },
    "lw": {},
    "pb": {
        # Menu Top ___
        "mt_option": {
            "colors": {"type": "zoom", "pal": pal.get("th1")},
            "dim": dim.get("r_menu_top"),
            "img": img.get("option"),
            "th": "th2",
            "cur": "souris_main"
        },
        "mt_reduire": {
            "colors": {"type": "zoom", "pal": pal.get("th1")},
            "dim": dim.get("r_menu_top"),
            "img": img.get("reduire"),
            "th": "bn1",
            "cur": "souris_main"
        },
        "mt_agrandir": {
            "colors": {"type": "zoom", "pal": pal.get("th1")},
            "dim": dim.get("r_menu_top"),
            "img": img.get("agrandir"),
            "th": "th3",
            "cur": "souris_main"
        },
        "mt_quitter": {
            "colors": {"type": "zoom", "pal": pal.get("th1")},
            "dim": dim.get("r_menu_top"),
            "img": img.get("quitter"),
            "th": "bn2",
            "cur": "souris_main"
        },

        # Option ______
        "option_txt": {
            "colors": {"type": "txt", "pal": pal.get("th1")},
            "dim": dim.get("aw_h4")
        },
        "appliquer": {
            "colors": {"type": "txt_inv", "pal": pal.get("vert")},
            "dim": dim.get("aw_h4")
        },
        "valider": {
            "colors": {"type": "txt", "pal": pal.get("vert")},
            "dim": dim.get("aw_h4")
        },
        "annuler": {
            "colors": {"type": "txt", "pal": pal.get("rouge")},
            "dim": dim.get("aw_h4")
        },
        "uni": {
            "colors": {"type": "uni", "pal": {"c1": colors.th2}},
            "dim": dim.get("c_h4")
        },
    },
    "ckb": {
        # Option __
        "option": {
            "colors": {"type": "tr", "pal": pal.get("th1")},
            "dim": dim.get("c_h4"),
            "img": img.get("check"),
            "img_check": img.get("valider"),
            "th": "th2",
            "th_check": "th2"
        },
    },
    "rb": {},
    "pg": {},
    "sca": {},
    "sb": {
        # Option __
        "option": {
            "colors": {"type": "th", "pal": pal.get("th1")},
            "dim": dim.get("aw_menu_top"),
            "font": police.get("h3"),
            "pb_sb": QtWidgets.QAbstractSpinBox.PlusMinus
        },
    },
    "tb": {
        "option": {
            "colors": {"type": "bd", "pal": pal.get("th1")},
            "dim": dim.get("all"),
            "font": police.get("h3"),
            "cur": "souris_main"
        }
    },
    "tw": {},
}
