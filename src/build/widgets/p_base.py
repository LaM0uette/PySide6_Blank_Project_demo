from ...build import *


### TYPE
PB_TYPE = None


### COULEURS
COLORS_TYPE = "th"
COLORS = None
GRADIENT_COLORS = {"c1": (0, 0, 0), "c2": (255, 255, 255)}
C1, C2, C3, BN1, BN2 = None, None, None, None, None


### DIMENSIONS
DIM = {"w": None, "h": None}


### IMAGES
TM = ""
TM_HOVER = "bn1"
TM_CHECK = "bn2"


### FONT
FONT = P_font().h4()
HD_FONT = P_font().h3()


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


### CURSOR
CUR = P_cur().souris()


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
