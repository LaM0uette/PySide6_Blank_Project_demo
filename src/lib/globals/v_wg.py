from src.config import config
from src.lib.palettes import *


#####################
##     QWidget     ##
#####################
# SizePolicy
SIZE_POLICY_H = SizePolicy().prefered()
SIZE_POLICY_V = SizePolicy().prefered()

# Font
FONT = Font().base()

# Cursor
CUR = Cur().souris()

# FocusPolicy
FOCUS_POLICY = FocusPolicy().no_focus()

# LayoutDirection
LAYOUT_DIRECTION = LayoutDirection().left_to_right()
#####################
##    /QWidget     ##
#####################


#############################
##     QAbstractButton     ##
#############################
# Txt
TXT = ""

# Actions
REPEAT_DELAY = 300
REPEAT_INTERVAL = 100
#############################
##    /QAbstractButton     ##
#############################


###################
##     STYLE     ##
###################
# Background
BG = Rgb().th3()
BG_ALTERNATE = Rgb().th2()
BG_HOVER = Rgb().th3()
BG_CHECKED = Rgb().th1()
BG_CHECKED_HOVER = Rgb().th1()
BG_INDETERMINATE = Rgb().th2()
BG_INDETERMINATE_HOVER = Rgb().th2()
BG_PRESSED = Rgb().th3()
BG_CHECKED_PRESSED = Rgb().th1()
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

# foreground
FG = Rgb().th1()
FG_HOVER = Rgb().bn1()
FG_CHECKED = Rgb().th3()
FG_CHECKED_HOVER = Rgb().bn1()
FG_INDETERMINATE = Rgb().th3()
FG_INDETERMINATE_HOVER = Rgb().th1()
FG_PRESSED = Rgb().bn1()
FG_CHECKED_PRESSED = Rgb().bn2()
FG_SELECTION = Rgb().th3()
FG_PLACEHOLDER = Rgb().th2()
    # foreground item
FG_ITEM = Rgb().th1()
FG_ITEM_HOVER = Rgb().bn1()
FG_ITEM_CHECKED = Rgb().th3()
FG_ITEM_CHECKED_HOVER = Rgb().bn1()

# Other
GRIDLINE = Rgb().th2()
###################
##    /STYLE     ##
###################