from src.lib.palettes import *


#####################
##     QWidget     ##
#####################
# SizePolicy
SIZE_POLICY_H = SizePolicy().prefered()
SIZE_POLICY_V = SizePolicy().prefered()

# Dimensions
WIDTH = None
HEIGHT = None
WG_WIDTH = None
WG_HEIGHT = Dim.H9

# Font
FONT = Font().base()

# Cursor
CUR = Cur().souris()
CUR_ACTION = Cur().main()

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
POPUP_MODE = PopupMode().delayed_popup()
TOOL_BUTTON_STYLE = ToolButtonStyle().icon_only()
ARROW_TYPE = ArrowType.NO
#############################
##    /QAbstractButton     ##
#############################


###################
##     STYLE     ##
###################

###  BACKGROUND  ###
BG = Rgb().th3()
BG_ALTERNATE = Rgb().th2()
BG_HOVER = Rgb().th3()
BG_CHECKED = Rgb().th1()
BG_CHECKED_HOVER = Rgb().th1()
BG_INDETERMINATE = Rgb().th2()
BG_INDETERMINATE_HOVER = Rgb().th2()
BG_PRESSED = Rgb().th3()
BG_CHECKED_PRESSED = Rgb().th1()
BG_INDETERMINATE_PRESSED = Rgb().th1()
BG_SELECTION = Rgb().th1()
    # Background item
BG_ITEM = Rgb().th3()
BG_ITEM_HOVER = Rgb().th3()
BG_ITEM_CHECKED = Rgb().th1()
BG_ITEM_CHECKED_HOVER = Rgb().th1()
    # Background other
BG_CHUNK = Rgb().th2()
BG_CHUNK_HOVER = Rgb().bn1()
BG_GROOVE = Rgb().th3()
BG_GROOVE_HOVER = Rgb().th3()
BG_GROOVE_PRESSED = Rgb().th3()
BG_HANDLE = Rgb().th2()
BG_HANDLE_HOVER = Rgb().th2()
BG_HANDLE_PRESSED = Rgb().bn1()
BG_SEPARATOR = Rgb().bn1()
### /BACKGROUND  ###


###  FOREGROUND  ###
FG = Rgb().th1()
FG_HOVER = Rgb().bn1()
FG_CHECKED = Rgb().th3()
FG_CHECKED_HOVER = Rgb().bn1()
FG_INDETERMINATE = Rgb().th3()
FG_INDETERMINATE_HOVER = Rgb().th1()
FG_PRESSED = Rgb().bn2()
FG_CHECKED_PRESSED = Rgb().bn2()
FG_INDETERMINATE_PRESSED = Rgb().bn2()
FG_SELECTION = Rgb().th3()
FG_PLACEHOLDER = Rgb().th2()
    # foreground item
FG_ITEM = Rgb().th1()
FG_ITEM_HOVER = Rgb().bn1()
FG_ITEM_CHECKED = Rgb().th3()
FG_ITEM_CHECKED_HOVER = Rgb().bn1()
### /FOREGROUND  ###


###  OTHER  ###
GRIDLINE = Rgb().th2()
### /OTHER  ###


###  IMAGES  ###
IMG_UNCHECK = Img().check0()
IMG_UNCHECK_HOVER = Img().check0()
IMG_CHECK = Img().check2()
IMG_CHECK_HOVER = Img().check2()
IMG_INDETERMINATE = Img().check1()
IMG_INDETERMINATE_HOVER = Img().check1()
IMG_UNROLL = Img().fleche_bottom()
IMG_UNROLL_HOVER = Img().fleche_bottom()
    # Arrows
IMG_UP = Img().plus()
IMG_DOWN = Img().moins()
IMG_RIGHT = Img().fleche_droite()
IMG_LEFT = Img().fleche_gauche()
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
BORDER_RGB = Rgb().tr()
### /BORDER  ###


###  RADIUS  ###
RADIUS_SIZE = 3
RADIUS = (RADIUS_SIZE,) * 4
### /RADIUS  ###


###  SCROLL  ###
SCROLL_BG = Rgb().th1()
SCROLL_WIDTH = 10
SCROLL_HEIGHT = 10
SCROLL_HANDLE_BG = Rgb().th3()
SCROLL_HANDLE_BG_HOVER = Rgb().th3()
SCROLL_HANDLE_FG = Rgb().th2()
SCROLL_HANDLE_FG_HOVER = Rgb().bn1()
SCROLL_HANDLE_MIN_WIDTH = 20
SCROLL_HANDLE_MIN_HEIGHT = 20
SCROLL_H = Scroll().need()
SCROLL_V = Scroll().need()
HEADER_H = True
HEADER_V = True
### /SCROLL  ###

###################
##    /STYLE     ##
###################
