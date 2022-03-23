from src.lib.palettes import *


#####################
##     QWidget     ##
#####################

###  SIZE POLICY  ###
SIZE_POLICY = DcSizePolicy.Base
### /SIZE POLICY  ###

###  DIMENSIONS  ###
DIM = DcDim.Base
DIM_WG = DcDim.Base(fixed_height=PaDim.H9)
### /DIMENSIONS  ###

###  FONT  ###
FONT = PaFont.BASE
### /FONT  ###

###  CURSOR  ###
CUR = PaCur.SOURIS
CUR_ACTION = PaCur.MAIN
### /CURSOR  ###

###  FOCUS POLICY  ###
FOCUS_POLICY = PaFocusPolicy.NO
### /FOCUS POLICY  ###

###  LAYOUT DIRECTION  ###
LAYOUT_DIRECTION = PaLayoutDirection.LEFT_TO_RIGHT
### /LAYOUT DIRECTION  ###

#####################
##    /QWidget     ##
#####################


#############################
##     QAbstractButton     ##
#############################
###  TEXTE  ###
TXT = None
### /TEXTE  ###

###  ICO  ###
ICO = DcIco.Base
###  /ICO  ###

###  ACTIONS  ###
AUTO_ACTIONS = DcAutoActions.Base
AUTO_ACTIONS_EXCLUSIVE = DcAutoActions.Base(auto_exclusive=True)
### /ACTIONS  ###

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

###  RGB  ###
BACKGROUND = DcRgbBg.Base
FOREGROUND = DcRgbFg.Base
BACKGROUND_ITEM = DcRgbBg.Base
FOREGROUND_ITEM = DcRgbFg.Base
### /RGB  ###

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
