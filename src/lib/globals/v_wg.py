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
IMG = DcImg.Base
### /IMAGES RGB  ###

###  BORDER  ###
BORDER = DcBorder.Base
### /BORDER  ###

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
