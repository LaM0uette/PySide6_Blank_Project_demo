from src.lib.palettes import *

#####################
##     QWidget     ##
#####################
# SizePolicy
SIZE_POLICY = dc_size_policy.Base

# Dimensions
WIDTH = None
HEIGHT = None
WG_WIDTH = None
WG_HEIGHT = Dim.H9
DIM = dc_dim.Base()
DIM_WG = dc_dim.Base(fixed_height=Dim.H9)

# Font
FONT = Font.BASE

# Cursor
CUR = Cur.SOURIS
CUR_ACTION = Cur.MAIN

# FocusPolicy
FOCUS_POLICY = FocusPolicy.NO

# LayoutDirection
LAYOUT_DIRECTION = LayoutDirection.LEFT_TO_RIGHT
#####################
##    /QWidget     ##
#####################


#############################
##     QAbstractButton     ##
#############################
# Txt
TXT = None

# Actions
AUTO_REPEAT_DELAY = 300
AUTO_REPEAT_INTERVAL = 100
#############################
##    /QAbstractButton     ##
#############################


#############################
##     QToolButton     ##
#############################
POPUP_MODE = PopupMode.DELAYED
TOOL_BUTTON_STYLE = ToolButtonStyle.ICON_ONLY
ARROW_TYPE = ArrowType.NO
#############################
##    /QAbstractButton     ##
#############################


###################
##     STYLE     ##
###################

###  BACKGROUND  ###
BG = Rgb.TH3
BG_ALTERNATE = Rgb.TH2
BG_HOVER = Rgb.TH3
BG_CHECKED = Rgb.TH1
BG_CHECKED_HOVER = Rgb.TH1
BG_INDETERMINATE = Rgb.TH2
BG_INDETERMINATE_HOVER = Rgb.TH2
BG_PRESSED = Rgb.TH3
BG_CHECKED_PRESSED = Rgb.TH1
BG_INDETERMINATE_PRESSED = Rgb.TH1
BG_SELECTION = Rgb.TH1
    # Background item
BG_ITEM = Rgb.TH3
BG_ITEM_HOVER = Rgb.TH3
BG_ITEM_CHECKED = Rgb.TH1
BG_ITEM_CHECKED_HOVER = Rgb.TH1
    # Background other
BG_CHUNK = Rgb.TH2
BG_CHUNK_HOVER = Rgb.BN1
BG_GROOVE = Rgb.TH3
BG_GROOVE_HOVER = Rgb.TH3
BG_GROOVE_PRESSED = Rgb.TH3
BG_HANDLE = Rgb.TH2
BG_HANDLE_HOVER = Rgb.TH2
BG_HANDLE_PRESSED = Rgb.BN1
BG_SEPARATOR = Rgb.BN1
### /BACKGROUND  ###


###  FOREGROUND  ###
FG = Rgb.TH1
FG_HOVER = Rgb.BN1
FG_CHECKED = Rgb.TH3
FG_CHECKED_HOVER = Rgb.BN1
FG_INDETERMINATE = Rgb.TH3
FG_INDETERMINATE_HOVER = Rgb.TH1
FG_PRESSED = Rgb.BN2
FG_CHECKED_PRESSED = Rgb.BN2
FG_INDETERMINATE_PRESSED = Rgb.BN2
FG_SELECTION = Rgb.TH3
FG_PLACEHOLDER = Rgb.TH2
    # foreground item
FG_ITEM = Rgb.TH1
FG_ITEM_HOVER = Rgb.BN1
FG_ITEM_CHECKED = Rgb.TH3
FG_ITEM_CHECKED_HOVER = Rgb.BN1
### /FOREGROUND  ###


###  OTHER  ###
GRIDLINE = Rgb.TH2
### /OTHER  ###


###  IMAGES  ###
IMG_UNCHECK = Img.CHECK0
IMG_UNCHECK_HOVER = Img.CHECK0
IMG_CHECK = Img.CHECK2
IMG_CHECK_HOVER = Img.CHECK2
IMG_INDETERMINATE = Img.CHECK1
IMG_INDETERMINATE_HOVER = Img.CHECK1
IMG_UNROLL = Img.FLECHE_BOTTOM
IMG_UNROLL_HOVER = Img.FLECHE_BOTTOM
    # Arrows
IMG_UP = Img.PLUS
IMG_DOWN = Img.MOINS
IMG_RIGHT = Img.FLECHE_RIGHT
IMG_LEFT = Img.FLECHE_LEFT
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
BORDER_RGB = Rgb.TR
### /BORDER  ###


###  RADIUS  ###
RADIUS_SIZE = 3
RADIUS = (RADIUS_SIZE,) * 4
### /RADIUS  ###


###  SCROLL  ###
SCROLL_BG = Rgb.TH1
SCROLL_WIDTH = 10
SCROLL_HEIGHT = 10
SCROLL_HANDLE_BG = Rgb.TH3
SCROLL_HANDLE_BG_HOVER = Rgb.TH3
SCROLL_HANDLE_FG = Rgb.TH2
SCROLL_HANDLE_FG_HOVER = Rgb.BN1
SCROLL_HANDLE_MIN_WIDTH = 20
SCROLL_HANDLE_MIN_HEIGHT = 20
SCROLL_H = Scroll.NEED
SCROLL_V = Scroll.NEED
HEADER_H = True
HEADER_V = True
### /SCROLL  ###

###################
##    /STYLE     ##
###################
