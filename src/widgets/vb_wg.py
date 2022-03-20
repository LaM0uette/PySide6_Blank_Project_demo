from src.config.config import Config
from src.lib.palettes import *


########################
##     DIMENSIONS     ##
########################
WIDTH = None
HEIGHT = PaDim.H9

####################
##     POLICE     ##
####################
FONT = Config.font
FONT_SIZE = PaFont.H4
FONT_SIZE_HD = PaFont.H3

########################
##     PARAMETRES     ##
########################
BUTTON_SYMBOLS = PaButtonSymbols.PLUS_MINUS
DRAG_DROP_MODE = PaDragDropMode.NO
DROP_ACTION = PaDropAction.MOVE
EDIT = False
FOCUS_POLICY = PaFocusPolicy.STRONG
FLOW = PaFlow().TOP_TO_BOTTOM
FRAME_SHAPE = PaFrameShape.NO
FRAME_SHADOW = PaFrameShadow.PLAIN
INSERT_POLICY = PaInsertPolicy.BOTTOM
MAX_VISIBLE_ITEMS = 10
MAX_LENGTH = 32767
PROGRESS_FORMAT = ProgressFormat.PERCENTAGE
SELECTION_BEHAVIOR = PaSelectionBehavior.ROW
SELECTION_MODE = PaSelectionMode.SINGLE
TEXT_VISIBLE = True
VALUE_MIN = 0
VALUE_MAX = 100
VALUE_STEP = 1
PAGE_STEP = 10
TEXT_FORMAT = PaTextFormat.PLAIN
TICK_POSITION = PaTickPosition.NO
TICK_INTERVAL = 0
WORD_WRAP = True

#####################
##     CURSEUR     ##
#####################
CUR = PaCur.SOURIS
CUR_MAIN = PaCur.MAIN
CUR_VIEW = PaCur.SOURIS_MAIN
CUR_VIEWPORT = PaCur.CROIX
CUR_LE = PaCur.IBEAM

######################
##     COULEURS     ##
######################
# BG
BG = PaRgb.TH3
BG_ALTERNATE = PaRgb.TH2
BG_HOVER = PaRgb.TH3
BG_CHECKED = PaRgb.TH1
BG_CHECKED_HOVER = PaRgb.TH1
BG_INDETERMINATE = PaRgb.TH2
BG_INDETERMINATE_HOVER = PaRgb.TH2
BG_PRESSED = PaRgb.TH3
BG_CHECKED_PRESSED = PaRgb.TH1
BG_SELECTION = PaRgb.TH1
# BG item
BG_ITEM = PaRgb.TH3
BG_ITEM_HOVER = PaRgb.TH3
BG_ITEM_CHECKED = PaRgb.TH1
BG_ITEM_CHECKED_HOVER = PaRgb.TH1
# BG Autres
BG_CHUNK = PaRgb.TH2
BG_CHUNK_HOVER = PaRgb.BN1
BG_GROOVE = PaRgb.TH3
BG_GROOVE_HOVER = PaRgb.TH3
BG_GROOVE_PRESSED = PaRgb.TH3
BG_HANDLE = PaRgb.TH2
BG_HANDLE_HOVER = PaRgb.TH2
BG_HANDLE_PRESSED = PaRgb.BN1
BG_SEPARATOR = PaRgb.BN1

# FG
FG = PaRgb.TH1
FG_HOVER = PaRgb.BN1
FG_CHECKED = PaRgb.TH3
FG_CHECKED_HOVER = PaRgb.BN1
FG_INDETERMINATE = PaRgb.TH3
FG_INDETERMINATE_HOVER = PaRgb.TH1
FG_PRESSED = PaRgb.BN1
FG_CHECKED_PRESSED = PaRgb.BN2
FG_SELECTION = PaRgb.TH3
FG_PLACEHOLDER = PaRgb.TH2
# FG item
FG_ITEM = PaRgb.TH1
FG_ITEM_HOVER = PaRgb.BN1
FG_ITEM_CHECKED = PaRgb.TH3
FG_ITEM_CHECKED_HOVER = PaRgb.BN1

# Autres
GRIDLINE = PaRgb.TH2

####################
##     IMAGES     ##
####################
# Check
IMG_UNCHECK = PaImg.CHECK0
IMG_UNCHECK_HOVER = PaImg.CHECK0
IMG_CHECK = PaImg.CHECK2
IMG_CHECK_HOVER = PaImg.CHECK2
IMG_INDETERMINATE = PaImg.CHECK1
IMG_INDETERMINATE_HOVER = PaImg.CHECK1
IMG_UNROLL = PaImg.FLECHE_BOTTOM
IMG_UNROLL_HOVER = PaImg.FLECHE_BOTTOM
# Check RGB
IMG_UNCHECK_RGB = "th2"
IMG_UNCHECK_HOVER_RGB = "bn1"
IMG_CHECK_RGB = "th2"
IMG_CHECK_HOVER_RGB = "bn1"
IMG_INDETERMINATE_RGB = "th3"
IMG_INDETERMINATE_HOVER_RGB = "th1"
IMG_UNROLL_RGB = "th2"
IMG_UNROLL_HOVER_RGB = "bn1"

# Fleches
IMG_UP = PaImg.PLUS
IMG_DOWN = PaImg.MOINS
IMG_RIGHT = PaImg.FLECHE_RIGHT
IMG_LEFT = PaImg.FLECHE_LEFT
# Fleches RGB
IMG_UP_RGB = "th2"
IMG_UP_HOVER_RGB = "bn1"
IMG_DOWN_RGB = "th2"
IMG_DOWN_HOVER_RGB = "bn1"
IMG_RIGHT_RGB = "th3"
IMG_RIGHT_HOVER_RGB = "bn1"
IMG_LEFT_RGB = "th3"
IMG_LEFT_HOVER_RGB = "bn1"

# img dim
img_width = HEIGHT * PaStyleBase.x_ico
IMG_WIDTH = HEIGHT * PaStyleBase.X_ICO
img_height = HEIGHT * PaStyleBase.x_ico
IMG_HEIGHT = HEIGHT * PaStyleBase.X_ICO

#####################
##     BORDURE     ##
#####################
BORDER_WIDTH = (0,) * 4
BORDER_STYLE = "solid"
BORDER_RGB = PaRgb.TR

###################
##     RAYON     ##
###################
RADIUS_SIZE = 3
RADIUS = (RADIUS_SIZE,) * 4

####################
##     SCROLL     ##
####################
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
