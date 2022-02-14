from PySide6 import QtCore

from ...build import *
from ...config import *


######################
##     COULEURS     ##
######################
COULEURS = P_rgb().p_th3()

# BG
COLORS_BG= Rgb().th3()
COLORS_BG_HOVER= Rgb().th3()
COLORS_BG_CHECKED= Rgb().th1()
COLORS_BG_CHECKED_HOVER= Rgb().th1()



_COLORS_BG= COULEURS.get("c1") + (255,)
_COLORS_BG_HOVER= COULEURS.get("c1") + (255,)
_COLORS_BG_CHECKED= COULEURS.get("c3") + (255,)
_COLORS_BG_CHECKED_HOVER= COULEURS.get("c3") + (255,)

COLORS_BG_PLACEHOLDER= COULEURS.get("bn1") + (255,)
COLORS_BG_BARRE= COULEURS.get("c3") + (255,)
COLORS_BG_BARRE_HOVER= COULEURS.get("c3") + (255,)
COLORS_BG_BARRE_PRESSED= COULEURS.get("c1") + (255,)
COLORS_BG_CUR= COULEURS.get("c1") + (255,)
COLORS_BG_CUR_HOVER= COULEURS.get("bn1") + (255,)
COLORS_BG_CUR_PRESSED= COULEURS.get("bn2") + (255,)
COLORS_BG_SELECTION=COULEURS.get("c3")
COLORS_BG_PRESSED=_COLORS_BG_HOVER
COLORS_BG_CHECKED_PRESSED=_COLORS_BG_CHECKED_HOVER
COLORS_BG_ITEM= COULEURS.get("c1") + (255,)
COLORS_BG_ITEM_HOVER= COULEURS.get("c1") + (255,)
COLORS_BG_ITEM_CHECKED= COULEURS.get("c3") + (255,)
COLORS_BG_ITEM_CHECKED_HOVER= COULEURS.get("c3") + (255,)

# FG
COLORS_FG=Rgb().th1()
COLORS_FG_HOVER= Rgb().bn1()
COLORS_FG_CHECKED= Rgb().th3()
COLORS_FG_CHECKED_HOVER= Rgb().bn1()



_COLORS_FG=COULEURS.get("c3")
_COLORS_FG_HOVER=COULEURS.get("bn1")
_COLORS_FG_CHECKED=COULEURS.get("c2")
_COLORS_FG_CHECKED_HOVER=COULEURS.get("bn1")

COLORS_FG_PLACEHOLDER=COULEURS.get("bn2")
COLORS_FG_SELECTION=COULEURS.get("c1")
COLORS_FG_PRESSED=COULEURS.get("bn2")
COLORS_FG_CHECKED_PRESSED=COULEURS.get("bn2")
COLORS_FG_ITEM=COULEURS.get("c3")
COLORS_FG_ITEM_HOVER=COULEURS.get("bn1")
COLORS_FG_ITEM_CHECKED= COULEURS.get("c2")
COLORS_FG_ITEM_CHECKED_HOVER= COULEURS.get("bn1")
COLORS_GRID=COULEURS.get("c3")


########################
##     DIMENSIONS     ##
########################
DIM_WIDTH = None
DIM_WG_WIDTH = None
DIM_HEIGHT = None
DIM_WG_HEIGHT = P_dim().h9()
SPACING = 10


####################
##     IMAGES     ##
####################
TM = "th2"
IMG_UNCHECK = P_img().check()
IMG_HOVER = P_img().check()
IMG_CHECK = P_img().valider()
IMG_CHECK_HOVER = P_img().valider()
IMG_DEROULANT = P_img().fleche_bottom()
IMG_DEROULANT_HOVER = P_img().fleche_bottom()
IMG_DROITE = P_img().fleche_droite()
IMG_GAUCHE = P_img().fleche_gauche()
IMG_UP = P_img().plus()
IMG_DOWN = P_img().moins()

TM_UNCHECK = "th2"
TM_HOVER = "bn1"
TM_CHECK = "th2"
TM_CHECK_HOVER = "th2"
TM_DROITE = "th3"
TM_GAUCHE = "th3"
TM_UP = "th2"
TM_DOWN = "th2"

IMG_WIDTH = P_dim().h9() * P_style().x_ico()
IMG_HEIGHT = P_dim().h9() * P_style().x_ico()


#####################
##     BORDURE     ##
#####################
BD_WIDTH = 0
BD_STYLE = "solid"
BD_COULEUR = COULEURS.get("bn1") + (0,)


###################
##     RAYON     ##
###################
RD_WG = 0


####################
##     SCROLL     ##
####################
SCROLL_BG = COULEURS.get("c1")
SCROLL_HANDLE_BG = COULEURS.get("c1")
SCROLL_HANDLE_FG = COULEURS.get("c3")
SCROLL_WIDTH = 20
SCROLL_HEIGHT = 20
SCROLL_HANDLE_MIN_WIDTH = 30
SCROLL_HANDLE_MIN_HEIGHT = 30
SCROLL_H = QtCore.Qt.ScrollBarAsNeeded
SCROLL_V = QtCore.Qt.ScrollBarAsNeeded
HEADER_H = True
HEADER_V = True


####################
##     POLICE     ##
####################
FONT = config.font
FONT_SIZE = P_font().h4()
HD_FONT_SIZE = P_font().h3()


########################
##     PARAMETRES     ##
########################
ALIGN = P_align().l().c()
EDIT = False
SB_BUTTONS_TYPE = P_pb_sb().pl_mi()
TEXT_VISIBLE = True
WORD_WRAP = True
NO_FOCUS = False
VAL_MIN = 0
VAL_MAX = 100
VAL_PAS = 1


#####################
##     CURSEUR     ##
#####################
CUR = P_cur().souris()
CUR_LE = P_cur().IBeam()
