from ...build import *


### TYPE
TYPE = None


### COULEURS
COLORS_TYPE = "th"
COLORS = None
C1, C2, C3, BN1, BN2 = None, None, None, None, None


### DIMENSIONS
DIM = {"w": None, "h": None}


### IMAGES
TH = ""
TH_HOVER = "bn1"
TH_CHECK = "bn2"


### FONT
FONT = P_font().h4()


### RADIUS
RD_MAT = "0000"
RD_PX = None
RD = {"mat": RD_MAT, "px": RD_PX}


### BORDURES
BD_MAT = "0000"
BD_PX = P_style().bd()
BD_TH = P_rgb().bn1()
BD = {"mat": BD_MAT, "px": BD_PX, "th": BD_TH}
BD_RGBA = (0, 0, 0, 0)


### CURSOR
CUR = P_cur().souris()


### PARAMETRES
ALIGN = P_align().c().c()
EDIT = False
WORD_WRAP = False
SCROLL = P_scroll().n_n()
HEADER = {"h": True, "v": True}
PB_SB = P_pb_sb().no()
PAD = 0
PB_SIDE = "tb"
MIN = 0
MAX = 99
STEP = 1
