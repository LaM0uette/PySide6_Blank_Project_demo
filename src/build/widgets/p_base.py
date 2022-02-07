from ...build import *
from ...config import *

######################
##     COULEURS     ##
######################
COLORS = P_rgb().p_th3()

# BG
COULEUR_BG=COLORS.get("c1")+(255, )
COULEUR_BG_HOVER=COLORS.get("c1")+(255, )
COULEUR_BG_CHECKED=COLORS.get("c3")+(255, )
COULEUR_BG_CHECKED_HOVER=COLORS.get("c3")+(255, )

COULEUR_BG_SELECTION=COLORS.get("c3")

COULEUR_BG_ITEM=COLORS.get("c1")+(255, )
COULEUR_BG_ITEM_HOVER=COLORS.get("c1")+(255, )

# FG
COULEUR_FG=COLORS.get("c3")
COULEUR_FG_HOVER=COLORS.get("bn1")
COULEUR_FG_CHECKED=COLORS.get("c2")
COULEUR_FG_CHECKED_HOVER=COLORS.get("bn1")

COULEUR_FG_SELECTION=COLORS.get("c1")

COULEUR_FG_ITEM=COLORS.get("c3")
COULEUR_FG_ITEM_HOVER=COLORS.get("bn1")


########################
##     DIMENSIONS     ##
########################
DIM_WIDTH = None
DIM_HEIGHT = P_dim().h9()
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

TM_UNCHECK = "th2"
TM_HOVER = "bn1"
TM_CHECK = "th2"
TM_CHECK_HOVER = "th2"
TM_DROITE = "th2"
TM_GAUCHE = "th2"

IMG_WIDTH = P_dim().h9() * P_style().x_ico()
IMG_HEIGHT = P_dim().h9() * P_style().x_ico()


#####################
##     BORDURE     ##
#####################
BD_WIDTH = 0
BD_STYLE = "solid"
BD_COULEUR = COLORS.get("bn1") + (0, )


###################
##     RAYON     ##
###################
RD_WG = 0


####################
##     SCROLL     ##
####################
SCROLL_BG = COLORS.get("c1")
SCROLL_HANDLE_BG = COLORS.get("c1")
SCROLL_HANDLE_FG = COLORS.get("c3")
SCROLL_WIDTH = 20
SCROLL_HEIGHT = 20
SCROLL_HANDLE_MIN_WIDTH = 30
SCROLL_HANDLE_MIN_HEIGHT = 30


####################
##     POLICE     ##
####################
FONT = config.font
FONT_SIZE = P_font().h4()
HD_FONT_SIZE = P_font().h3()


#####################
##     CURSEUR     ##
#####################
CUR = P_cur().souris()




### TYPE
PB_TYPE = None


### COULEURS
COLORS_TYPE = "th"
GRADIENT_COLORS = {"c1": (0, 0, 0), "c2": (255, 255, 255)}
C1, C2, C3, BN1, BN2 = None, None, None, None, None


### DIMENSIONS
DIM = {"w": None, "h": None}


### RADIUS
RD_MAT = "0000"
RD_PX = None
RD = {"mat": RD_MAT, "px": RD_PX}


### BORDURES
BD_MAT = "0000"
BD_PX = 0
BD_TH = P_rgb().bn1()
BD = {"mat": BD_MAT, "px": BD_PX, "th": BD_TH}
BD_RGBA = (0, 0, 0, 0)





### PARAMETRES
ALIGN = P_align().c().c()
EDIT = False
WORD_WRAP = True
SCROLL = P_scroll().nd().nd()
HEADER = P_header().tt()
PB_SB = P_pb_sb().no()
PAD = 0
PB_SIDE = "tb"
NO_FOCUS = False
VAL_MIN = 0
VAL_MAX = 100
STEP = 1
