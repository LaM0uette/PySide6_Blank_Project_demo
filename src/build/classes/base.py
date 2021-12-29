from ...build import *


### COULEURS
COLORS = None
C1, C2, C3, C4 = None, None, None, None


### DIMENSIONS
DIM = {"w": None, "h": None}


### IMAGES
TH = ""
TH_HOVER = "bn1"
TH_CHECK = "bn2"


### FONT
FONT = P_police().p()


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
ALIGN = P_align().c_c()
EDIT = False
SCROLL = P_scroll().n_n()
HEADER = {"h": True, "v": True}
PB_SB = P_pb_sb().no()