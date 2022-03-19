from src.config import config
from src.lib.palettes import *


########################
##     DIMENSIONS     ##
########################
WIDTH = None
HEIGHT = Dim.H9

####################
##     POLICE     ##
####################
FONT = config.font
FONT_SIZE = Font.H4
FONT_SIZE_HD = Font.H3

########################
##     PARAMETRES     ##
########################
BUTTON_SYMBOLS = ButtonSymbols.PLUS_MINUS
DRAG_DROP_MODE = DragDropMode.NO
DROP_ACTION = DropAction.MOVE
EDIT = False
FOCUS_POLICY = FocusPolicy.STRONG
FLOW = Flow().TOP_TO_BOTTOM
FRAME_SHAPE = FrameShape.NO
FRAME_SHADOW = FrameShadow.PLAIN
INSERT_POLICY = InsertPolicy.BOTTOM
MAX_VISIBLE_ITEMS = 10
MAX_LENGTH = 32767
PROGRESS_FORMAT = ProgressFormat.PERCENTAGE
SELECTION_BEHAVIOR = SelectionBehavior.ROW
SELECTION_MODE = SelectionMode.SINGLE
TEXT_VISIBLE = True
VALUE_MIN = 0
VALUE_MAX = 100
VALUE_STEP = 1
PAGE_STEP = 10
TEXT_FORMAT = TextFormat.PLAIN
TICK_POSITION = TickPosition.NO
TICK_INTERVAL = 0
WORD_WRAP = True

#####################
##     CURSEUR     ##
#####################
CUR = Cur.SOURIS
CUR_MAIN = Cur.MAIN
CUR_VIEW = Cur.SOURIS_MAIN
CUR_VIEWPORT = Cur.CROIX
CUR_LE = Cur.IBEAM

######################
##     COULEURS     ##
######################
# BG
BG = Rgb().th3()
BG_ALTERNATE = Rgb.TH2
BG_HOVER = Rgb().th3()
BG_CHECKED = Rgb.TH1
BG_CHECKED_HOVER = Rgb.TH1
BG_INDETERMINATE = Rgb.TH2
BG_INDETERMINATE_HOVER = Rgb.TH2
BG_PRESSED = Rgb().th3()
BG_CHECKED_PRESSED = Rgb.TH1
BG_SELECTION = Rgb.TH1
# BG item
BG_ITEM = Rgb().th3()
BG_ITEM_HOVER = Rgb().th3()
BG_ITEM_CHECKED = Rgb.TH1
BG_ITEM_CHECKED_HOVER = Rgb.TH1
# BG Autres
BG_CHUNK = Rgb.TH2
BG_CHUNK_HOVER = Rgb().bn1()
BG_GROOVE = Rgb().th3()
BG_GROOVE_HOVER = Rgb().th3()
BG_GROOVE_PRESSED = Rgb().th3()
BG_HANDLE = Rgb.TH2
BG_HANDLE_HOVER = Rgb.TH2
BG_HANDLE_PRESSED = Rgb().bn1()
BG_SEPARATOR = Rgb().bn1()

# FG
FG = Rgb.TH1
FG_HOVER = Rgb().bn1()
FG_CHECKED = Rgb().th3()
FG_CHECKED_HOVER = Rgb().bn1()
FG_INDETERMINATE = Rgb().th3()
FG_INDETERMINATE_HOVER = Rgb.TH1
FG_PRESSED = Rgb().bn1()
FG_CHECKED_PRESSED = Rgb().bn2()
FG_SELECTION = Rgb().th3()
FG_PLACEHOLDER = Rgb.TH2
# FG item
FG_ITEM = Rgb.TH1
FG_ITEM_HOVER = Rgb().bn1()
FG_ITEM_CHECKED = Rgb().th3()
FG_ITEM_CHECKED_HOVER = Rgb().bn1()

# Autres
GRIDLINE = Rgb.TH2

####################
##     IMAGES     ##
####################
# Check
IMG_UNCHECK = Img.CHECK0
IMG_UNCHECK_HOVER = Img.CHECK0
IMG_CHECK = Img.CHECK2
IMG_CHECK_HOVER = Img.CHECK2
IMG_INDETERMINATE = Img.CHECK1
IMG_INDETERMINATE_HOVER = Img.CHECK1
IMG_UNROLL = Img.FLECHE_BOTTOM
IMG_UNROLL_HOVER = Img.FLECHE_BOTTOM
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
IMG_UP = Img.PLUS
IMG_DOWN = Img.MOINS
IMG_RIGHT = Img.FLECHE_RIGHT
IMG_LEFT = Img.FLECHE_LEFT
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
img_width = HEIGHT * StyleBase.x_ico
IMG_WIDTH = HEIGHT * StyleBase.X_ICO
img_height = HEIGHT * StyleBase.x_ico
IMG_HEIGHT = HEIGHT * StyleBase.X_ICO

#####################
##     BORDURE     ##
#####################
BORDER_WIDTH = (0,) * 4
BORDER_STYLE = "solid"
BORDER_RGB = Rgb().tr()

###################
##     RAYON     ##
###################
RADIUS_SIZE = 3
RADIUS = (RADIUS_SIZE,) * 4

####################
##     SCROLL     ##
####################
SCROLL_BG = Rgb.TH1
SCROLL_WIDTH = 10
SCROLL_HEIGHT = 10

SCROLL_HANDLE_BG = Rgb().th3()
SCROLL_HANDLE_BG_HOVER = Rgb().th3()
SCROLL_HANDLE_FG = Rgb.TH2
SCROLL_HANDLE_FG_HOVER = Rgb().bn1()
SCROLL_HANDLE_MIN_WIDTH = 20
SCROLL_HANDLE_MIN_HEIGHT = 20

SCROLL_H = Scroll.NEED
SCROLL_V = Scroll.NEED
HEADER_H = True
HEADER_V = True
