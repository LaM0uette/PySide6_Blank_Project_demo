from ...build import *


######################
##     COULEURS     ##
######################
COLORS = P_rgb().p_th1()


########################
##     DIMENSIONS     ##
########################
DIM_WIDTH = None
DIM_HEIGHT = P_dim().h9()
SPACING = 10


####################
##     IMAGES     ##
####################
TM = "th3"
IMG_UNCHECK = P_img().check()
IMG_HOVER = P_img().check()
IMG_CHECK = P_img().valider()
IMG_CHECK_HOVER = P_img().valider()
TM_UNCHECK = "th2"
TM_HOVER = "th2"
TM_CHECK = "th2"
TM_CHECK_HOVER = "th2"

IMG_WIDTH = P_dim().h9() * P_style().x_ico()
IMG_HEIGHT = P_dim().h9() * P_style().x_ico()


#####################
##     BORDURE     ##
#####################
BD_WIDTH = P_style().bd()
BD_STYLE = "solid"
BD_COULEUR = COLORS.get("bn1") + (0, )


###################
##     RAYON     ##
###################
RD = 10


####################
##     POLICE     ##
####################
FONT = P_font().h4()
HD_FONT = P_font().h3()


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
