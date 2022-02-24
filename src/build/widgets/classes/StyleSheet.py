from PySide6 import QtGui

from ....build import *
from ....build.widgets import p_base
from ....build.widgets.classes import Classe_pb


class StyleSheet:
    def __init__(
            self,

            # Couleurs BG
            bg_gen=None,
            bg=p_base.BG,
            bg_hover=p_base.BG_HOVER,
            bg_checked=p_base.BG_CHECKED,
            bg_checked_hover=p_base.BG_CHECKED_HOVER,
            bg_pressed=p_base.BG_PRESSED,
            bg_checked_pressed=p_base.BG_CHECKED_PRESSED,
            bg_selection=p_base.BG_SELECTION,
            bg_item_gen=None,
            bg_item=p_base.BG_ITEM,
            bg_item_hover=p_base.BG_ITEM_HOVER,
            bg_item_checked=p_base.BG_ITEM_CHECKED,
            bg_item_checked_hover=p_base.BG_ITEM_CHECKED_HOVER,
            bg_chunk=p_base.BG_CHUNK,
            bg_chunk_hover=p_base.BG_CHUNK_HOVER,
            bg_header=Rgb().th2(),
            # Couleurs FG
            fg_gen=None,
            fg=p_base.FG,
            fg_hover=p_base.FG_HOVER,
            fg_checked=p_base.FG_CHECKED,
            fg_checked_hover=p_base.FG_CHECKED_HOVER,
            fg_pressed=p_base.FG_PRESSED,
            fg_checked_pressed=p_base.FG_CHECKED_PRESSED,
            fg_selection=p_base.FG_SELECTION,
            fg_placeholder=p_base.FG_PLACEHOLDER,
            fg_item_gen=None,
            fg_item=p_base.FG_ITEM,
            fg_item_hover=p_base.FG_ITEM_HOVER,
            fg_item_checked=p_base.FG_ITEM_CHECKED,
            fg_item_checked_hover=p_base.FG_ITEM_CHECKED_HOVER,
            fg_header=Rgb().th1(),

            # Dimensions WG
            height=p_base.WG_HEIGHT,

            # Positions WG
            padding_top=0,
            padding_bottom=0,
            padding_right=0,
            padding_left=0,

            # Images
            img_uncheck=p_base.IMG_UNCHECK,
            img_uncheck_hover=p_base.IMG_UNCHECK_HOVER,
            img_check=p_base.IMG_CHECK,
            img_check_hover=p_base.IMG_CHECK_HOVER,
            img_all=None,
            img=p_base.IMG_UNROLL,
            img_hover=p_base.IMG_UNROLL_HOVER,
            img_up=p_base.IMG_UP,
            img_down=p_base.IMG_DOWN,
            # Images RGB
            img_uncheck_rgb=p_base.IMG_UNCHECK_RGB,
            img_uncheck_hover_rgb=p_base.IMG_UNCHECK_HOVER_RGB,
            img_check_rgb=p_base.IMG_CHECK_RGB,
            img_check_hover_rgb=p_base.IMG_CHECK_HOVER_RGB,
            img_all_rgb=None,
            img_rgb=p_base.IMG_UNROLL_RGB,
            img_hover_rgb=p_base.IMG_UNROLL_HOVER_RGB,
            img_up_rgb=p_base.IMG_UP_RGB,
            img_down_rgb=p_base.IMG_DOWN_RGB,
            # Images DIM
            img_width=p_base.img_width,
            img_height=p_base.img_height,
            IMG_HEIGHT=p_base.IMG_HEIGHT,
            img_up_width=10,
            img_up_height=10,
            img_down_width=10,
            img_down_height=10,

            # Images positions
            img_up_top=2,
            img_up_bottom=0,
            img_up_right=2,
            img_up_left=0,
            img_down_top=0,
            img_down_bottom=2,
            img_down_right=2,
            img_down_left=0,

            # Bordures GEN
            border_gen_all=None,
            border_gen_style=None,
            border_gen_rgb=None,
            border_gen_top=None, border_gen_bottom=None, border_gen_right=None, border_gen_left=None,
            # Bordures
            border_all=None,
            border_style=p_base.WG_BORDER_STYLE,
            border_rgb=p_base.WG_BORDER_RGB,
            border_top=p_base.WG_BORDER_WIDTH, border_bottom=p_base.WG_BORDER_WIDTH, border_right=p_base.WG_BORDER_WIDTH, border_left=p_base.WG_BORDER_WIDTH,
            # Bordures hover
            border_all_hover=None,
            border_style_hover=p_base.WG_BORDER_STYLE,
            border_rgb_hover=p_base.WG_BORDER_RGB,
            border_top_hover=p_base.WG_BORDER_WIDTH, border_bottom_hover=p_base.WG_BORDER_WIDTH, border_right_hover=p_base.WG_BORDER_WIDTH, border_left_hover=p_base.WG_BORDER_WIDTH,
            # Bordures checked
            border_all_checked=None,
            border_style_checked=p_base.WG_BORDER_STYLE,
            border_rgb_checked=p_base.WG_BORDER_RGB,
            border_top_checked=p_base.WG_BORDER_WIDTH, border_bottom_checked=p_base.WG_BORDER_WIDTH, border_right_checked=p_base.WG_BORDER_WIDTH, border_left_checked=p_base.WG_BORDER_WIDTH,
            # Bordures checked hover
            border_all_checked_hover=None,
            border_style_checked_hover=p_base.WG_BORDER_STYLE,
            border_rgb_checked_hover=p_base.WG_BORDER_RGB,
            border_top_checked_hover=p_base.WG_BORDER_WIDTH, border_bottom_checked_hover=p_base.WG_BORDER_WIDTH, border_right_checked_hover=p_base.WG_BORDER_WIDTH, border_left_checked_hover=p_base.WG_BORDER_WIDTH,

            # Bordures HD GEN
            border_hd_gen_all=None,
            border_hd_gen_style=None,
            border_hd_gen_rgb=None,
            border_hd_gen_top=None, border_hd_gen_bottom=None, border_hd_gen_right=None, border_hd_gen_left=None,
            # Bordures HD
            border_hd_all=None,
            border_hd_style=p_base.WG_BORDER_STYLE,
            border_hd_rgb=p_base.WG_BORDER_RGB,
            border_hd_top=p_base.WG_BORDER_WIDTH, border_hd_bottom=p_base.WG_BORDER_WIDTH, border_hd_right=p_base.WG_BORDER_WIDTH, border_hd_left=p_base.WG_BORDER_WIDTH,
            # Bordures HD hover
            border_hd_all_hover=None,
            border_hd_style_hover=p_base.WG_BORDER_STYLE,
            border_hd_rgb_hover=p_base.WG_BORDER_RGB,
            border_hd_top_hover=p_base.WG_BORDER_WIDTH, border_hd_bottom_hover=p_base.WG_BORDER_WIDTH, border_hd_right_hover=p_base.WG_BORDER_WIDTH, border_hd_left_hover=p_base.WG_BORDER_WIDTH,
            # Bordures HD checked
            border_hd_all_checked=None,
            border_hd_style_checked=p_base.WG_BORDER_STYLE,
            border_hd_rgb_checked=p_base.WG_BORDER_RGB,
            border_hd_top_checked=p_base.WG_BORDER_WIDTH, border_hd_bottom_checked=p_base.WG_BORDER_WIDTH, border_hd_right_checked=p_base.WG_BORDER_WIDTH, border_hd_left_checked=p_base.WG_BORDER_WIDTH,
            # Bordures HD checked hover
            border_hd_all_checked_hover=None,
            border_hd_style_checked_hover=p_base.WG_BORDER_STYLE,
            border_hd_rgb_checked_hover=p_base.WG_BORDER_RGB,
            border_hd_top_checked_hover=p_base.WG_BORDER_WIDTH, border_hd_bottom_checked_hover=p_base.WG_BORDER_WIDTH, border_hd_right_checked_hover=p_base.WG_BORDER_WIDTH, border_hd_left_checked_hover=p_base.WG_BORDER_WIDTH,

            # Bordures item GEN
            border_item_gen_all=None,
            border_item_gen_style=None,
            border_item_gen_rgb=None,
            border_item_gen_top=None, border_item_gen_bottom=None, border_item_gen_right=None, border_item_gen_left=None,
            # Bordures item
            border_item_all=None,
            border_item_style=p_base.WG_BORDER_STYLE,
            border_item_rgb=p_base.WG_BORDER_RGB,
            border_item_top=p_base.WG_BORDER_WIDTH, border_item_bottom=p_base.WG_BORDER_WIDTH, border_item_right=p_base.WG_BORDER_WIDTH, border_item_left=p_base.WG_BORDER_WIDTH,
            # Bordures item hover
            border_item_all_hover=None,
            border_item_style_hover=p_base.WG_BORDER_STYLE,
            border_item_rgb_hover=p_base.WG_BORDER_RGB,
            border_item_top_hover=p_base.WG_BORDER_WIDTH, border_item_bottom_hover=p_base.WG_BORDER_WIDTH, border_item_right_hover=p_base.WG_BORDER_WIDTH, border_item_left_hover=p_base.WG_BORDER_WIDTH,
            # Bordures item checked
            border_item_all_checked=None,
            border_item_style_checked=p_base.WG_BORDER_STYLE,
            border_item_rgb_checked=p_base.WG_BORDER_RGB,
            border_item_top_checked=p_base.WG_BORDER_WIDTH, border_item_bottom_checked=p_base.WG_BORDER_WIDTH, border_item_right_checked=p_base.WG_BORDER_WIDTH, border_item_left_checked=p_base.WG_BORDER_WIDTH,
            # Bordures item checked hover
            border_item_all_checked_hover=None,
            border_item_style_checked_hover=p_base.WG_BORDER_STYLE,
            border_item_rgb_checked_hover=p_base.WG_BORDER_RGB,
            border_item_top_checked_hover=p_base.WG_BORDER_WIDTH, border_item_bottom_checked_hover=p_base.WG_BORDER_WIDTH, border_item_right_checked_hover=p_base.WG_BORDER_WIDTH, border_item_left_checked_hover=p_base.WG_BORDER_WIDTH,
    ):
        try:
            # BG / FG
            if not bg_gen is None:
                bg = bg_gen
                bg_hover = bg_gen
                bg_checked = bg_gen
                bg_checked_hover = bg_gen
                bg_pressed = bg_gen
                bg_checked_pressed = bg_gen
            if not fg_gen is None:
                fg = fg_gen
                fg_hover = fg_gen
                fg_checked = fg_gen
                fg_checked_hover = fg_gen
                fg_pressed = fg_gen
                fg_checked_pressed = fg_gen
            if not bg_item_gen is None:
                bg_item = bg_item_gen
                bg_item_hover = bg_item_gen
                bg_item_checked = bg_item_gen
                bg_item_checked_hover = bg_item_gen
            if not fg_item_gen is None:
                fg_item = fg_item_gen
                fg_item_hover = fg_item_gen
                fg_item_checked = fg_item_gen
                fg_item_checked_hover = fg_item_gen

            # IMG
            if not img_all is None:
                img = img_all
                img_hover = img_all
            if not img_all_rgb is None:
                img_rgb = img_all_rgb
                img_hover_rgb = img_all_rgb

            # Bordure GEN
            if not border_gen_all is None:
                border_top = border_gen_all
                border_bottom = border_gen_all
                border_right = border_gen_all
                border_left = border_gen_all
                border_top_hover = border_gen_all
                border_bottom_hover = border_gen_all
                border_right_hover = border_gen_all
                border_left_hover = border_gen_all
                border_top_checked = border_gen_all
                border_bottom_checked = border_gen_all
                border_right_checked = border_gen_all
                border_left_checked = border_gen_all
                border_top_checked_hover = border_gen_all
                border_bottom_checked_hover = border_gen_all
                border_right_checked_hover = border_gen_all
                border_left_checked_hover = border_gen_all
            elif border_gen_all is None:
                if not border_all is None:
                    border_top = border_all
                    border_bottom = border_all
                    border_right = border_all
                    border_left = border_all
                if not border_all_hover is None:
                    border_top_hover = border_all_hover
                    border_bottom_hover = border_all_hover
                    border_right_hover = border_all_hover
                    border_left_hover = border_all_hover
                if not border_all_checked is None:
                    border_top_checked = border_all_checked
                    border_bottom_checked = border_all_checked
                    border_right_checked = border_all_checked
                    border_left_checked = border_all_checked
                if not border_all_checked_hover is None:
                    border_top_checked_hover = border_all_checked_hover
                    border_bottom_checked_hover = border_all_checked_hover
                    border_right_checked_hover = border_all_checked_hover
                    border_left_checked_hover = border_all_checked_hover

                if not border_gen_top is None:
                    border_top = border_gen_top
                    border_top_hover = border_gen_top
                    border_top_checked = border_gen_top
                    border_top_checked_hover = border_gen_top
                if not border_gen_bottom is None:
                    border_bottom = border_gen_bottom
                    border_bottom_hover = border_gen_bottom
                    border_bottom_checked = border_gen_bottom
                    border_bottom_checked_hover = border_gen_bottom
                if not border_gen_right is None:
                    border_right = border_gen_right
                    border_right_hover = border_gen_right
                    border_right_checked = border_gen_right
                    border_right_checked_hover = border_gen_right
                if not border_gen_left is None:
                    border_left = border_gen_left
                    border_left_hover = border_gen_left
                    border_left_checked = border_gen_left
                    border_left_checked_hover = border_gen_left
            if not border_gen_style is None:
                border_style = border_gen_style
                border_style_hover = border_gen_style
                border_style_checked = border_gen_style
                border_style_checked_hover = border_gen_style
            if not border_gen_rgb is None:
                border_rgb = border_gen_rgb
                border_rgb_hover = border_gen_rgb
                border_rgb_checked = border_gen_rgb
                border_rgb_checked_hover = border_gen_rgb

            # Bordure hd GEN
            if not border_hd_gen_all is None:
                border_hd_top = border_hd_gen_all
                border_hd_bottom = border_hd_gen_all
                border_hd_right = border_hd_gen_all
                border_hd_left = border_hd_gen_all
                border_hd_top_hover = border_hd_gen_all
                border_hd_bottom_hover = border_hd_gen_all
                border_hd_right_hover = border_hd_gen_all
                border_hd_left_hover = border_hd_gen_all
                border_hd_top_checked = border_hd_gen_all
                border_hd_bottom_checked = border_hd_gen_all
                border_hd_right_checked = border_hd_gen_all
                border_hd_left_checked = border_hd_gen_all
                border_hd_top_checked_hover = border_hd_gen_all
                border_hd_bottom_checked_hover = border_hd_gen_all
                border_hd_right_checked_hover = border_hd_gen_all
                border_hd_left_checked_hover = border_hd_gen_all
            elif border_hd_gen_all is None:
                if not border_hd_all is None:
                    border_hd_top = border_hd_all
                    border_hd_bottom = border_hd_all
                    border_hd_right = border_hd_all
                    border_hd_left = border_hd_all
                if not border_hd_all_hover is None:
                    border_hd_top_hover = border_hd_all_hover
                    border_hd_bottom_hover = border_hd_all_hover
                    border_hd_right_hover = border_hd_all_hover
                    border_hd_left_hover = border_hd_all_hover
                if not border_hd_all_checked is None:
                    border_hd_top_checked = border_hd_all_checked
                    border_hd_bottom_checked = border_hd_all_checked
                    border_hd_right_checked = border_hd_all_checked
                    border_hd_left_checked = border_hd_all_checked
                if not border_hd_all_checked_hover is None:
                    border_hd_top_checked_hover = border_hd_all_checked_hover
                    border_hd_bottom_checked_hover = border_hd_all_checked_hover
                    border_hd_right_checked_hover = border_hd_all_checked_hover
                    border_hd_left_checked_hover = border_hd_all_checked_hover

                if not border_hd_gen_top is None:
                    border_hd_top = border_hd_gen_top
                    border_hd_top_hover = border_hd_gen_top
                    border_hd_top_checked = border_hd_gen_top
                    border_hd_top_checked_hover = border_hd_gen_top
                if not border_hd_gen_bottom is None:
                    border_hd_bottom = border_hd_gen_bottom
                    border_hd_bottom_hover = border_hd_gen_bottom
                    border_hd_bottom_checked = border_hd_gen_bottom
                    border_hd_bottom_checked_hover = border_hd_gen_bottom
                if not border_hd_gen_right is None:
                    border_hd_right = border_hd_gen_right
                    border_hd_right_hover = border_hd_gen_right
                    border_hd_right_checked = border_hd_gen_right
                    border_hd_right_checked_hover = border_hd_gen_right
                if not border_hd_gen_left is None:
                    border_hd_left = border_hd_gen_left
                    border_hd_left_hover = border_hd_gen_left
                    border_hd_left_checked = border_hd_gen_left
                    border_hd_left_checked_hover = border_hd_gen_left
            if not border_hd_gen_style is None:
                border_hd_style = border_hd_gen_style
                border_hd_style_hover = border_hd_gen_style
                border_hd_style_checked = border_hd_gen_style
                border_hd_style_checked_hover = border_hd_gen_style
            if not border_hd_gen_rgb is None:
                border_hd_rgb = border_hd_gen_rgb
                border_hd_rgb_hover = border_hd_gen_rgb
                border_hd_rgb_checked = border_hd_gen_rgb
                border_hd_rgb_checked_hover = border_hd_gen_rgb

            # Bordure item GEN
            if not border_item_gen_all is None:
                border_item_top = border_item_gen_all
                border_item_bottom = border_item_gen_all
                border_item_right = border_item_gen_all
                border_item_left = border_item_gen_all
                border_item_top_hover = border_item_gen_all
                border_item_bottom_hover = border_item_gen_all
                border_item_right_hover = border_item_gen_all
                border_item_left_hover = border_item_gen_all
                border_item_top_checked = border_item_gen_all
                border_item_bottom_checked = border_item_gen_all
                border_item_right_checked = border_item_gen_all
                border_item_left_checked = border_item_gen_all
                border_item_top_checked_hover = border_item_gen_all
                border_item_bottom_checked_hover = border_item_gen_all
                border_item_right_checked_hover = border_item_gen_all
                border_item_left_checked_hover = border_item_gen_all
            elif border_item_gen_all is None:
                if not border_item_all is None:
                    border_item_top = border_item_all
                    border_item_bottom = border_item_all
                    border_item_right = border_item_all
                    border_item_left = border_item_all
                if not border_item_all_hover is None:
                    border_item_top_hover = border_item_all_hover
                    border_item_bottom_hover = border_item_all_hover
                    border_item_right_hover = border_item_all_hover
                    border_item_left_hover = border_item_all_hover
                if not border_item_all_checked is None:
                    border_item_top_checked = border_item_all_checked
                    border_item_bottom_checked = border_item_all_checked
                    border_item_right_checked = border_item_all_checked
                    border_item_left_checked = border_item_all_checked
                if not border_item_all_checked_hover is None:
                    border_item_top_checked_hover = border_item_all_checked_hover
                    border_item_bottom_checked_hover = border_item_all_checked_hover
                    border_item_right_checked_hover = border_item_all_checked_hover
                    border_item_left_checked_hover = border_item_all_checked_hover

                if not border_item_gen_top is None:
                    border_item_top = border_item_gen_top
                    border_item_top_hover = border_item_gen_top
                    border_item_top_checked = border_item_gen_top
                    border_item_top_checked_hover = border_item_gen_top
                if not border_item_gen_bottom is None:
                    border_item_bottom = border_item_gen_bottom
                    border_item_bottom_hover = border_item_gen_bottom
                    border_item_bottom_checked = border_item_gen_bottom
                    border_item_bottom_checked_hover = border_item_gen_bottom
                if not border_item_gen_right is None:
                    border_item_right = border_item_gen_right
                    border_item_right_hover = border_item_gen_right
                    border_item_right_checked = border_item_gen_right
                    border_item_right_checked_hover = border_item_gen_right
                if not border_item_gen_left is None:
                    border_item_left = border_item_gen_left
                    border_item_left_hover = border_item_gen_left
                    border_item_left_checked = border_item_gen_left
                    border_item_left_checked_hover = border_item_gen_left
            if not border_item_gen_style is None:
                border_item_style = border_item_gen_style
                border_item_style_hover = border_item_gen_style
                border_item_style_checked = border_item_gen_style
                border_item_style_checked_hover = border_item_gen_style
            if not border_item_gen_rgb is None:
                border_item_rgb = border_item_gen_rgb
                border_item_rgb_hover = border_item_gen_rgb
                border_item_rgb_checked = border_item_gen_rgb
                border_item_rgb_checked_hover = border_item_gen_rgb
        except: pass

        self.style = f"""
/**************************
**       QComboBox       **
***************************/
                QComboBox, QFontComboBox {{
                background-color: rgba{bg};
                color: rgba{fg};
                selection-background-color: rgba{bg_selection};
                selection-color: rgba{fg_selection};
                }}
                QComboBox:hover, QFontComboBox:hover {{
                background-color: rgba{bg_hover};
                color: rgba{fg_hover};
                }}

                /* BOUTON DE DEROULEMENT */
                QComboBox::drop-down, QFontComboBox::drop-down {{
                width: {height}px;
                border: none;
                }}

                /* IMAGE DU BOUTON DE DEROULEMENT */
                QComboBox::down-arrow, QFontComboBox::down-arrow {{
                image: url({f"{img}{img_rgb}.svg"});
                width: {img_width}px;
                height: {img_height}px;
                }}
                QComboBox::down-arrow:hover, QFontComboBox::down-arrow:hover {{
                image: url({f"{img_hover}{img_hover_rgb}.svg"});
                width: {img_width}px;
                height: {img_height}px;
                }}

                /* ELEMENTS DEROULEMENT */
                QComboBox QAbstractItemView::item, QFontComboBox QAbstractItemView::item {{
                background-color: rgba{bg_item};
                color: rgba{fg_item};
                }}
                QComboBox QAbstractItemView::item:hover, QFontComboBox QAbstractItemView::item:hover {{
                background-color: rgba{bg_item_hover};
                color: rgba{fg_item_hover};
                }}

                /* BORDURES */
                .QComboBox, .QFontComboBox {{
                border-top: {border_top}px {border_style} rgba{border_rgb};
                border-bottom: {border_bottom}px {border_style} rgba{border_rgb};
                border-right: {border_right}px {border_style} rgba{border_rgb};
                border-left: {border_left}px {border_style} rgba{border_rgb};
                }}
                .QComboBox:hover, .QFontComboBox:hover {{
                border-top: {border_top_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-bottom: {border_bottom_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-right: {border_right_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-left: {border_left_hover}px {border_style_hover} rgba{border_rgb_hover};
                }}
/**************************
**      /QComboBox       **
***************************/
                
  
                
/***********************
**       QLabel       **
************************/
                .QLabel {{
                background-color: rgba{bg};
                color: rgba{fg};
                }}
                .QLabel:hover {{
                background-color: rgba{bg_hover};
                color: rgba{fg_hover};
                }}
        
                /* BORDURES */
                .QLabel {{
                border-top: {border_top}px {border_style} rgba{border_rgb};
                border-bottom: {border_bottom}px {border_style} rgba{border_rgb};
                border-right: {border_right}px {border_style} rgba{border_rgb};
                border-left: {border_left}px {border_style} rgba{border_rgb};
                }}
                .QLabel:hover {{
                border-top: {border_top_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-bottom: {border_bottom_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-right: {border_right_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-left: {border_left_hover}px {border_style_hover} rgba{border_rgb_hover};
                }}
/***********************
**      /QLabel       **
************************/     
     
                
                
/*****************************
**       QProgressBar       **
******************************/      
                QProgressBar {{
                background-color: rgba{bg};
                color: rgba{fg};
                }}
        
                /* PROGRESS */
                QProgressBar::chunk {{
                background-color: rgba{bg_chunk};
                }}
                QProgressBar::chunk:hover {{
                background-color: rgba{bg_chunk_hover};
                }}
        
                /* BORDURES */
                .QProgressBar {{
                border-top: {border_top}px {border_style} rgba{border_rgb};
                border-bottom: {border_bottom}px {border_style} rgba{border_rgb};
                border-right: {border_right}px {border_style} rgba{border_rgb};
                border-left: {border_left}px {border_style} rgba{border_rgb};
                padding-top={padding_top}px;
                padding-bottom={padding_bottom}px;
                padding-right={padding_right}px;
                padding-left={padding_left}px;
                }}
                .QProgressBar:hover {{
                border-top: {border_top_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-bottom: {border_bottom_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-right: {border_right_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-left: {border_left_hover}px {border_style_hover} rgba{border_rgb_hover};
                }}
/*****************************
**      /QProgressBar       **
******************************/     



/****************************
**       QPushButton       **
*****************************/
                QPushButton {{
                background-color: rgba{bg};
                color: rgba{fg};
                }}
        
                QPushButton:hover {{
                background-color: rgba{bg_hover};
                color: rgba{fg_hover};
                }}
        
                QPushButton:checked {{
                background-color: rgba{bg_checked};
                color: rgba{fg_checked};
                }}
        
                QPushButton:checked:hover {{
                background-color: rgba{bg_checked_hover};
                color: rgba{fg_checked_hover};
                }}
        
                QPushButton:pressed {{
                background-color: rgba{bg_pressed};
                color: rgba{fg_pressed};
                }}
        
                QPushButton:checked:pressed {{
                background-color: rgba{bg_checked_pressed};
                color: rgba{fg_checked_pressed};
                }}
        
                /* BORDURES */
                .QPushButton {{
                border-top: {border_top}px {border_style} rgba{border_rgb};
                border-bottom: {border_bottom}px {border_style} rgba{border_rgb};
                border-right: {border_right}px {border_style} rgba{border_rgb};
                border-left: {border_left}px {border_style} rgba{border_rgb};
                }}
                .QPushButton:hover {{
                border-top: {border_top_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-bottom: {border_bottom_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-right: {border_right_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-left: {border_left_hover}px {border_style_hover} rgba{border_rgb_hover};
                }}
                .QPushButton:checked {{
                border-top: {border_top_checked}px {border_style_checked} rgba{border_rgb_checked};
                border-bottom: {border_bottom_checked}px {border_style_checked} rgba{border_rgb_checked};
                border-right: {border_right_checked}px {border_style_checked} rgba{border_rgb_checked};
                border-left: {border_left_checked}px {border_style_checked} rgba{border_rgb_checked};
                }}
                .QPushButton:checked:hover {{
                border-top: {border_top_checked_hover}px {border_style_checked_hover} rgba{border_rgb_checked_hover};
                border-bottom: {border_bottom_checked_hover}px {border_style_checked_hover} rgba{border_rgb_checked_hover};
                border-right: {border_right_checked_hover}px {border_style_checked_hover} rgba{border_rgb_checked_hover};
                border-left: {border_left_checked_hover}px {border_style_checked_hover} rgba{border_rgb_checked_hover};
                }}
/****************************
**      /QPushButton       **
*****************************/



/****************************
**       QScrollArea       **
*****************************/
                .QScrollArea .QWidget {{
                background-color: rgba{bg};
                }}
        
                /* BORDURES */
                .QScrollArea {{
                border-top: {border_top}px {border_style} rgba{border_rgb};
                border-bottom: {border_bottom}px {border_style} rgba{border_rgb};
                border-right: {border_right}px {border_style} rgba{border_rgb};
                border-left: {border_left}px {border_style} rgba{border_rgb};
                }}
                .QScrollArea:hover {{
                border-top: {border_top_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-bottom: {border_bottom_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-right: {border_right_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-left: {border_left_hover}px {border_style_hover} rgba{border_rgb_hover};
                }}
/****************************
**      /QScrollArea       **
*****************************/



/*************************
**      /QSpinBox       **
**************************/
                QSpinBox, QDoubleSpinBox {{
                background-color: rgba{bg};
                color: rgba{fg};
                selection-background-color: rgba{bg_selection};
                selection-color: rgba{fg_selection}
                }}
        
                QSpinBox::up-button, QDoubleSpinBox::up-button  {{
                subcontrol-position: top right;
                top: {img_up_top}px;
                bottom: {img_up_bottom}px;
                right: {img_up_right}px;
                left: {img_up_left}px;
                image: url({f"{img_up}{img_up_rgb}.svg"});
                width: {img_up_width}px;
                height: {img_up_height}px;
                }}
        
                QSpinBox::down-button, QDoubleSpinBox::down-button  {{
                subcontrol-position: bottom right;
                top: {img_down_top}px;
                bottom: {img_down_bottom}px;
                right: {img_down_right}px;
                left: {img_down_left}px;
                image: url({f"{img_down}{img_down_rgb}.svg"});
                width: {img_down_width}px;
                height: {img_down_height}px;
                }}
        
                /* BORDURES */
                .QSpinBox, .QDoubleSpinBox {{
                border-top: {border_top}px {border_style} rgba{border_rgb};
                border-bottom: {border_bottom}px {border_style} rgba{border_rgb};
                border-right: {border_right}px {border_style} rgba{border_rgb};
                border-left: {border_left}px {border_style} rgba{border_rgb};
                }}
                .QSpinBox:hover, .QDoubleSpinBox:hover {{
                border-top: {border_top_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-bottom: {border_bottom_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-right: {border_right_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-left: {border_left_hover}px {border_style_hover} rgba{border_rgb_hover};
                }}
/*************************
**       QSpinBox       **
**************************/



/***********************************************************
**       QLineEdit  |  QPlainTextEdit  |  QTextEdit       **
************************************************************/
                .QLineEdit, .QPlainTextEdit, .QTextEdit {{
                background-color: rgba{bg};
                selection-background-color: rgba{bg_selection};
                selection-color: rgba{fg_selection};
                }}
        
                /* BORDURES */
                .QLineEdit, .QPlainTextEdit, .QTextEdit {{
                border-top: {border_top}px {border_style} rgba{border_rgb};
                border-bottom: {border_bottom}px {border_style} rgba{border_rgb};
                border-right: {border_right}px {border_style} rgba{border_rgb};
                border-left: {border_left}px {border_style} rgba{border_rgb};
                }}
                .QLineEdit:hover, .QPlainTextEdit:hover, .QTextEdit:hover {{
                border-top: {border_top_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-bottom: {border_bottom_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-right: {border_right_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-left: {border_left_hover}px {border_style_hover} rgba{border_rgb_hover};
                }}
/*********************************************************
**      /QLineEdit | /QPlainTextEdit | /QTextEdit       **
**********************************************************/


/*************************
**       QToolBox       **
**************************/
                QToolBox::tab {{
                background-color: rgba{bg};
                color: rgba{fg};
                border-top: {border_hd_top}px {border_hd_style} rgba{border_hd_rgb};
                border-bottom: {border_hd_bottom}px {border_hd_style} rgba{border_hd_rgb};
                border-right: {border_hd_right}px {border_hd_style} rgba{border_hd_rgb};
                border-left: {border_hd_left}px {border_hd_style} rgba{border_hd_rgb};
                }}
        
                QToolBox::tab:hover {{
                background-color: rgba{bg_hover};
                color: rgba{fg_hover};
                border-top: {border_hd_top_hover}px {border_hd_style_hover} rgba{border_hd_rgb_hover};
                border-bottom: {border_hd_bottom_hover}px {border_hd_style_hover} rgba{border_hd_rgb_hover};
                border-right: {border_hd_right_hover}px {border_hd_style_hover} rgba{border_hd_rgb_hover};
                border-left: {border_hd_left_hover}px {border_hd_style_hover} rgba{border_hd_rgb_hover};
                }}
        
                QToolBox::tab:selected {{
                background-color: rgba{bg_checked};
                color: rgba{fg_checked};
                border-top: {border_hd_top_checked}px {border_hd_style_checked} rgba{border_hd_rgb_checked};
                border-bottom: {border_hd_bottom_checked}px {border_hd_style_checked} rgba{border_hd_rgb_checked};
                border-right: {border_hd_right_checked}px {border_hd_style_checked} rgba{border_hd_rgb_checked};
                border-left: {border_hd_left_checked}px {border_hd_style_checked} rgba{border_hd_rgb_checked};
                }}
        
                QToolBox::tab:selected:hover {{
                background-color: rgba{bg_checked_hover};
                color: rgba{fg_checked_hover};
                border-top: {border_hd_top_checked_hover}px {border_hd_style_checked_hover} rgba{border_hd_rgb_checked_hover};
                border-bottom: {border_hd_bottom_checked_hover}px {border_hd_style_checked_hover} rgba{border_hd_rgb_checked_hover};
                border-right: {border_hd_right_checked_hover}px {border_hd_style_checked_hover} rgba{border_hd_rgb_checked_hover};
                border-left: {border_hd_left_checked_hover}px {border_hd_style_checked_hover} rgba{border_hd_rgb_checked_hover};
                }}
        
                /* BORDURES */
                .QToolBox {{
                border-top: {border_top}px {border_style} rgba{border_rgb};
                border-bottom: {border_bottom}px {border_style} rgba{border_rgb};
                border-right: {border_right}px {border_style} rgba{border_rgb};
                border-left: {border_left}px {border_style} rgba{border_rgb};
                }}
                .QToolBox:hover {{
                border-top: {border_top_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-bottom: {border_bottom_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-right: {border_right_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-left: {border_left_hover}px {border_style_hover} rgba{border_rgb_hover};
                }}
/*************************
**      /QToolBox       **
**************************/



/*******************************************
**       QTreeWidget  |   QTreeView       **
********************************************/
                QHeaderView::section {{
                background-color: rgba{bg_header};
                color: rgba{fg_header};
                border-top: {border_hd_top}px {border_hd_style} rgba{border_hd_rgb};
                border-bottom: {border_hd_bottom}px {border_hd_style} rgba{border_hd_rgb};
                border-right: {border_hd_right}px {border_hd_style} rgba{border_hd_rgb};
                border-left: {border_hd_left}px {border_hd_style} rgba{border_hd_rgb};
                }}
        
                QTreeWidget, QTreeView {{
                background-color: rgba{bg};
                color: rgba{fg};
                }}
        
                QTreeWidget::item, QTreeView::item {{
                background-color: rgba{bg_item};
                color: rgba{fg_item};
                border-top: {border_item_top}px {border_item_style} rgba{border_item_rgb};
                border-bottom: {border_item_bottom}px {border_item_style} rgba{border_item_rgb};
                border-right: {border_item_right}px {border_item_style} rgba{border_item_rgb};
                border-left: {border_item_left}px {border_item_style} rgba{border_item_rgb};
                }}
        
                QTreeWidget::item:hover, QTreeView::item:hover {{
                background-color: rgba{bg_item_hover};
                color: rgba{fg_item_hover};
                border-top: {border_item_top_hover}px {border_item_style_hover} rgba{border_item_rgb_hover};
                border-bottom: {border_item_bottom_hover}px {border_item_style_hover} rgba{border_item_rgb_hover};
                border-right: {border_item_right_hover}px {border_item_style_hover} rgba{border_item_rgb_hover};
                border-left: {border_item_left_hover}px {border_item_style_hover} rgba{border_item_rgb_hover};
                }}
        
                QTreeWidget::item:selected, QTreeView::item:selected {{
                background-color: rgba{bg_item_checked};
                color: rgba{fg_item_checked};
                border-top: {border_item_top_checked}px {border_item_style_checked} rgba{border_item_rgb_checked};
                border-bottom: {border_item_bottom_checked}px {border_item_style_checked} rgba{border_item_rgb_checked};
                border-right: {border_item_right_checked}px {border_item_style_checked} rgba{border_item_rgb_checked};
                border-left: {border_item_left_checked}px {border_item_style_checked} rgba{border_item_rgb_checked};
                }}
        
                QTreeWidget::item:selected:hover, QTreeView::item:selected:hover {{
                background-color: rgba{bg_item_checked_hover};
                color: rgba{fg_item_checked_hover};
                border-top: {border_item_top_checked_hover}px {border_item_style_checked_hover} rgba{border_item_rgb_checked_hover};
                border-bottom: {border_item_bottom_checked_hover}px {border_item_style_checked_hover} rgba{border_item_rgb_checked_hover};
                border-right: {border_item_right_checked_hover}px {border_item_style_checked_hover} rgba{border_item_rgb_checked_hover};
                border-left: {border_item_left_checked_hover}px {border_item_style_checked_hover} rgba{border_item_rgb_checked_hover};
                }}
        
                /* BORDURES */
                .QTreeWidget, .QTreeView {{
                border-top: {border_top}px {border_style} rgba{border_rgb};
                border-bottom: {border_bottom}px {border_style} rgba{border_rgb};
                border-right: {border_right}px {border_style} rgba{border_rgb};
                border-left: {border_left}px {border_style} rgba{border_rgb};
                }}
                .QTreeWidget:hover, .QTreeView:hover {{
                border-top: {border_top_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-bottom: {border_bottom_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-right: {border_right_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-left: {border_left_hover}px {border_style_hover} rgba{border_rgb_hover};
                }}
/*******************************************
**      /QTreeWidget  |  /QTreeView       **
********************************************/
"""

        self.fg = fg
        self.fg_placeholder = fg_placeholder

        self.img_height = img_height
        self.IMG_HEIGHT = IMG_HEIGHT
        self.img = img
        self.img_hover = img_hover
        self.img_uncheck = img_uncheck
        self.img_uncheck_hover = img_uncheck_hover
        self.img_check = img_check
        self.img_check_hover = img_check_hover
        self.img_rgb = img_rgb
        self.img_hover_rgb = img_hover_rgb
        self.img_uncheck_rgb = img_uncheck_rgb
        self.img_uncheck_hover_rgb = img_uncheck_hover_rgb
        self.img_check_rgb = img_check_rgb
        self.img_check_hover_rgb = img_check_hover_rgb


    def get(self): return self.style
    def get_txt_palette(self):
        palette_txt = QtGui.QPalette()
        palette_txt.setColor(QtGui.QPalette.Text, QtGui.QColor(*self.fg))
        palette_txt.setColor(QtGui.QPalette.PlaceholderText, QtGui.QColor(*self.fg_placeholder))
        return palette_txt
    def get_cls_pb(self, wg, wg_type):
        if wg_type is not None:
            if wg_type == "check":
                Fct(wg=wg, img=f"{self.img_uncheck}{self.img_uncheck_rgb}", dim=self.img_height).ICON()
            else:
                Fct(wg=wg, img=f"{self.img}{self.img_rgb}", dim=self.img_height).ICON()

            return Classe_pb.Classe_pb(
                wg=wg,
                dim_ico=self.img_height,
                DIM_ICO=self.IMG_HEIGHT,
                img=self.img,
                img_hover=self.img_hover,
                img_uncheck=self.img_uncheck,
                img_uncheck_hover=self.img_uncheck_hover,
                img_check=self.img_check,
                img_check_hover=self.img_check_hover,
                img_rgb=self.img_rgb,
                img_hover_rgb=self.img_hover_rgb,
                img_uncheck_rgb=self.img_uncheck_rgb,
                img_uncheck_hover_rgb=self.img_uncheck_hover_rgb,
                img_check_rgb=self.img_check_rgb,
                img_check_hover_rgb=self.img_check_hover_rgb,
            )

