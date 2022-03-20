from src.lib.palettes import *

#####################
##     QWidget     ##
#####################
# PaSizePolicy
SIZE_POLICY = DcSizePolicy.Base

# Dimensions
WIDTH = None
HEIGHT = None
WG_WIDTH = None
WG_HEIGHT = PaDim.H9
DIM = DcDim.Base
DIM_WG = DcDim.Base(fixed_height=PaDim.H9)

# PaFont
FONT = PaFont.BASE

# Cursor
CUR = PaCur.SOURIS
CUR_ACTION = PaCur.MAIN

# PaFocusPolicy
FOCUS_POLICY = PaFocusPolicy.NO

# PaLayoutDirection
LAYOUT_DIRECTION = PaLayoutDirection.LEFT_TO_RIGHT
#####################
##    /QWidget     ##
#####################


#############################
##     QAbstractButton     ##
#############################
# Txt
TXT = None

# ico
ICO = DcIco.Base

# Actions
AUTO_ACTIONS = DcAutoActions.Base
#############################
##    /QAbstractButton     ##
#############################


#############################
##     QToolButton     ##
#############################
POPUP_MODE = PaPopupMode.DELAYED
TOOL_BUTTON_STYLE = PaToolButtonStyle.ICON_ONLY
ARROW_TYPE = PaArrowType.NO
#############################
##    /QAbstractButton     ##
#############################


###################
##     STYLE     ##
###################

###  BACKGROUND  ###
BG = PaRgb.TH3
BG_ALTERNATE = PaRgb.TH2
BG_HOVER = PaRgb.TH3
BG_CHECKED = PaRgb.TH1
BG_CHECKED_HOVER = PaRgb.TH1
BG_INDETERMINATE = PaRgb.TH2
BG_INDETERMINATE_HOVER = PaRgb.TH2
BG_PRESSED = PaRgb.TH3
BG_CHECKED_PRESSED = PaRgb.TH1
BG_INDETERMINATE_PRESSED = PaRgb.TH1
BG_SELECTION = PaRgb.TH1
    # Background item
BG_ITEM = PaRgb.TH3
BG_ITEM_HOVER = PaRgb.TH3
BG_ITEM_CHECKED = PaRgb.TH1
BG_ITEM_CHECKED_HOVER = PaRgb.TH1
    # Background other
BG_CHUNK = PaRgb.TH2
BG_CHUNK_HOVER = PaRgb.BN1
BG_GROOVE = PaRgb.TH3
BG_GROOVE_HOVER = PaRgb.TH3
BG_GROOVE_PRESSED = PaRgb.TH3
BG_HANDLE = PaRgb.TH2
BG_HANDLE_HOVER = PaRgb.TH2
BG_HANDLE_PRESSED = PaRgb.BN1
BG_SEPARATOR = PaRgb.BN1
### /BACKGROUND  ###


###  FOREGROUND  ###
FG = PaRgb.TH1
FG_HOVER = PaRgb.BN1
FG_CHECKED = PaRgb.TH3
FG_CHECKED_HOVER = PaRgb.BN1
FG_INDETERMINATE = PaRgb.TH3
FG_INDETERMINATE_HOVER = PaRgb.TH1
FG_PRESSED = PaRgb.BN2
FG_CHECKED_PRESSED = PaRgb.BN2
FG_INDETERMINATE_PRESSED = PaRgb.BN2
FG_SELECTION = PaRgb.TH3
FG_PLACEHOLDER = PaRgb.TH2
    # foreground item
FG_ITEM = PaRgb.TH1
FG_ITEM_HOVER = PaRgb.BN1
FG_ITEM_CHECKED = PaRgb.TH3
FG_ITEM_CHECKED_HOVER = PaRgb.BN1
### /FOREGROUND  ###


###  OTHER  ###
GRIDLINE = PaRgb.TH2
### /OTHER  ###


###  IMAGES  ###
IMG_UNCHECK = PaImg.CHECK0
IMG_UNCHECK_HOVER = PaImg.CHECK0
IMG_CHECK = PaImg.CHECK2
IMG_CHECK_HOVER = PaImg.CHECK2
IMG_INDETERMINATE = PaImg.CHECK1
IMG_INDETERMINATE_HOVER = PaImg.CHECK1
IMG_UNROLL = PaImg.FLECHE_BOTTOM
IMG_UNROLL_HOVER = PaImg.FLECHE_BOTTOM
    # Arrows
IMG_UP = PaImg.PLUS
IMG_DOWN = PaImg.MOINS
IMG_RIGHT = PaImg.FLECHE_RIGHT
IMG_LEFT = PaImg.FLECHE_LEFT
### /IMAGES  ###


###  IMAGES RGB  ###
IMG_UNCHECK_RGB = "th2"
IMG_UNCHECK_HOVER_RGB = "bn1"
IMG_CHECK_RGB = "th2"
IMG_CHECK_HOVER_RGB = "bn1"
IMG_INDETERMINATE_RGB = "th3"
IMG_INDETERMINATE_HOVER_RGB = "th1"
IMG_UNROLL_RGB = "th2"
IMG_UNROLL_HOVER_RGB = "bn1"
    # Arrows RGB
IMG_UP_RGB = "th2"
IMG_UP_HOVER_RGB = "bn1"
IMG_DOWN_RGB = "th2"
IMG_DOWN_HOVER_RGB = "bn1"
IMG_RIGHT_RGB = "th3"
IMG_RIGHT_HOVER_RGB = "bn1"
IMG_LEFT_RGB = "th3"
IMG_LEFT_HOVER_RGB = "bn1"
### /IMAGES RGB  ###


###  BORDER  ###
BORDER_WIDTH = (0,)*4
BORDER_STYLE = "solid"
BORDER_RGB = PaRgb.TR
### /BORDER  ###


###  RADIUS  ###
RADIUS_SIZE = 3
RADIUS = (RADIUS_SIZE,) * 4
### /RADIUS  ###


###  SCROLL  ###
SCROLL_BG = PaRgb.TH1
SCROLL_WIDTH = 10
SCROLL_HEIGHT = 10
SCROLL_HANDLE_BG = PaRgb.TH3
SCROLL_HANDLE_BG_HOVER = PaRgb.TH3
SCROLL_HANDLE_FG = PaRgb.TH2
SCROLL_HANDLE_FG_HOVER = PaRgb.BN1
SCROLL_HANDLE_MIN_WIDTH = 20
SCROLL_HANDLE_MIN_HEIGHT = 20
SCROLL_H = PaScroll.NEED
SCROLL_V = PaScroll.NEED
HEADER_H = True
HEADER_V = True
### /SCROLL  ###

###################
##    /STYLE     ##
###################
