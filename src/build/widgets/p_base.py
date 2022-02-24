from PySide6 import QtCore

from ...build import *
from ...config import *


######################
##     COULEURS     ##
######################
# BG
BG = Rgb().th3()
BG_HOVER = Rgb().th3()
BG_CHECKED = Rgb().th1()
BG_CHECKED_HOVER = Rgb().th1()
BG_PRESSED = Rgb().th3()
BG_CHECKED_PRESSED = Rgb().th1()
BG_SELECTION = Rgb().th1()
# BG item
BG_ITEM = Rgb().th3()
BG_ITEM_HOVER = Rgb().th3()
BG_ITEM_CHECKED = Rgb().th1()
BG_ITEM_CHECKED_HOVER = Rgb().th1()
# BG Autres
BG_CHUNK = Rgb().th2()
BG_CHUNK_HOVER = Rgb().bn1()
BG_GROOVE = Rgb().th3()
BG_GROOVE_HOVER = Rgb().th3()
BG_GROOVE_PRESSED = Rgb().th3()
BG_HANDLE = Rgb().th2()
BG_HANDLE_HOVER = Rgb().th2()
BG_HANDLE_PRESSED = Rgb().bn1()

# FG
FG = Rgb().th1()
FG_HOVER = Rgb().bn1()
FG_CHECKED = Rgb().th3()
FG_CHECKED_HOVER = Rgb().bn1()
FG_PRESSED = Rgb().bn1()
FG_CHECKED_PRESSED = Rgb().bn2()
FG_SELECTION = Rgb().th3()
FG_PLACEHOLDER = Rgb().th2()
# FG item
FG_ITEM = Rgb().th1()
FG_ITEM_HOVER = Rgb().bn1()
FG_ITEM_CHECKED = Rgb().th3()
FG_ITEM_CHECKED_HOVER = Rgb().bn1()

# Autres
GRIDLINE = Rgb().th2()


########################
##     DIMENSIONS     ##
########################
WIDTH = None
HEIGHT = None
WG_WIDTH = None
WG_HEIGHT = P_dim().h9()


####################
##     IMAGES     ##
####################
# Check
IMG_UNCHECK = P_img().check()
IMG_UNCHECK_HOVER = P_img().check()
IMG_CHECK = P_img().valider()
IMG_CHECK_HOVER = P_img().valider()
IMG_UNROLL = P_img().fleche_bottom()
IMG_UNROLL_HOVER = P_img().fleche_bottom()
# Check RGB
IMG_UNCHECK_RGB = "th2"
IMG_UNCHECK_HOVER_RGB = "bn1"
IMG_CHECK_RGB = "th2"
IMG_CHECK_HOVER_RGB = "bn1"
IMG_UNROLL_RGB = "th2"
IMG_UNROLL_HOVER_RGB = "bn1"

# Fleches
IMG_UP = P_img().plus()
IMG_DOWN = P_img().moins()
IMG_RIGHT = P_img().fleche_droite()
IMG_LEFT = P_img().fleche_gauche()
# Fleches RGB
IMG_UP_RGB = "th2"
IMG_DOWN_RGB = "th2"
IMG_RIGHT_RGB = "th3"
IMG_LEFT_RGB = "th3"

# img dim
img_width = WG_HEIGHT * P_style().x_ico()
IMG_WIDTH = WG_HEIGHT * P_style().X_ICO()
img_height = WG_HEIGHT * P_style().x_ico()
IMG_HEIGHT = WG_HEIGHT * P_style().X_ICO()


#####################
##     BORDURE     ##
#####################
BORDER_WIDTH = ((0, )*4)
BORDER_STYLE = "solid"
BORDER_RGB = Rgb().tr()
WG_BORDER_WIDTH = ((0, )*4)
WG_BORDER_STYLE = "solid"
WG_BORDER_RGB = Rgb().tr()


###################
##     RAYON     ##
###################
RADIUS = ((0, )*4)
WG_RADIUS = ((0, )*4)


####################
##     SCROLL     ##
####################
SCROLL_BG = Rgb().th1()
SCROLL_WIDTH = 20
SCROLL_HEIGHT = 20

SCROLL_HANDLE_BG = Rgb().th3()
SCROLL_HANDLE_BG_HOVER = Rgb().th3()
SCROLL_HANDLE_FG = Rgb().th2()
SCROLL_HANDLE_FG_HOVER = Rgb().bn1()
SCROLL_HANDLE_MIN_WIDTH = 20
SCROLL_HANDLE_MIN_HEIGHT = 20

SCROLL_H = QtCore.Qt.ScrollBarAsNeeded
SCROLL_V = QtCore.Qt.ScrollBarAsNeeded
HEADER_H = True
HEADER_V = True


####################
##     POLICE     ##
####################
FONT = config.font
FONT_SIZE = P_font().h4()
FONT_SIZE_HD = P_font().h3()


########################
##     PARAMETRES     ##
########################
EDIT = False
NO_FOCUS = False
SB_BUTTONS_TYPE = P_pb_sb().plus_minus()
TEXT_VISIBLE = True
VAL_MIN = 0
VAL_MAX = 100
VAL_STEP = 1
WORD_WRAP = True


#####################
##     CURSEUR     ##
#####################
CUR = Cur().souris()
CUR_LE = Cur().IBeam()
