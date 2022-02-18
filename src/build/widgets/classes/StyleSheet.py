from PySide6 import QtGui

from ....build import *
from ....build.widgets import p_base


class StyleSheet:
    def __init__(
            self,

            # Couleurs BG
            bg_gen=None,
            bg=p_base.BG,
            bg_hover=p_base.BG_HOVER,
            bg_checked=p_base.BG_CHECKED,
            bg_checked_hover=p_base.BG_CHECKED_HOVER,
            bg_selection=p_base.BG_SELECTION,
            bg_item_gen=None,
            bg_item=p_base.BG_ITEM,
            bg_item_hover=p_base.BG_ITEM_HOVER,
            bg_item_checked=p_base.BG_ITEM_CHECKED,
            bg_item_checked_hover=p_base.BG_ITEM_CHECKED_HOVER,
            bg_chunk=p_base.BG_CHUNK,
            bg_chunk_hover=p_base.BG_CHUNK_HOVER,
            bg_corner=p_base.BG,
            bg_header=Rgb().th2(),
            bg_header_hover=Rgb().th2(),
            bg_header_checked=Rgb().th3(),
            bg_header_checked_hover=Rgb().th3(),
            bg_mois=Rgb().th2(),
            # Couleurs FG
            fg_gen=None,
            fg=p_base.FG,
            fg_hover=p_base.FG_HOVER,
            fg_checked=p_base.FG_CHECKED,
            fg_checked_hover=p_base.FG_CHECKED_HOVER,
            fg_selection=p_base.FG_SELECTION,
            fg_placeholder=p_base.FG_PLACEHOLDER,
            fg_item_gen=None,
            fg_item=p_base.FG_ITEM,
            fg_item_hover=p_base.FG_ITEM_HOVER,
            fg_item_checked=p_base.FG_ITEM_CHECKED,
            fg_item_checked_hover=p_base.FG_ITEM_CHECKED_HOVER,
            fg_header=Rgb().th1(),
            fg_header_hover=Rgb().bn1(),
            fg_header_checked=Rgb().bn1(),
            fg_header_checked_hover=Rgb().bn2(),
            fg_mois=Rgb().th1(),
            # couleurs autres
            gridline=p_base.GRIDLINE,

            # Dimensions WG
            width=p_base.WG_WIDTH,
            height=p_base.WG_HEIGHT,
            spacing=10,
            padding_top=0,
            padding_bottom=0,
            padding_right=0,
            padding_left=0,

            # Police
            font=p_base.FONT,
            font_size=p_base.FONT_SIZE,

            # Images
            img_uncheck=p_base.IMG_UNCHECK,
            img_uncheck_hover=p_base.IMG_UNCHECK_HOVER,
            img_check=p_base.IMG_CHECK,
            img_check_hover=p_base.IMG_CHECK_HOVER,
            img_all=None,
            img=p_base.IMG_UNROLL,
            img_hover=p_base.IMG_UNROLL_HOVER,
            img_right=p_base.IMG_RIGHT,
            img_left=p_base.IMG_LEFT,
            # Images RGB
            img_uncheck_rgb=p_base.IMG_UNCHECK_RGB,
            img_uncheck_hover_rgb=p_base.IMG_UNCHECK_HOVER_RGB,
            img_check_rgb=p_base.IMG_CHECK_RGB,
            img_check_hover_rgb=p_base.IMG_CHECK_HOVER_RGB,
            img_all_rgb=None,
            img_rgb=p_base.IMG_UNROLL_RGB,
            img_hover_rgb=p_base.IMG_UNROLL_HOVER_RGB,
            img_right_rgb=p_base.IMG_RIGHT_RGB,
            img_left_rgb=p_base.IMG_LEFT_RGB,
            # Images DIM
            img_width=p_base.IMG_WIDTH,
            img_height=p_base.IMG_HEIGHT,
            # Images margin
            img_margin_top=0,
            img_margin_bottom=0,
            img_margin_right=0,
            img_margin_left=0,

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

            # Bordures jours
            border_day_size=P_style().bd(),
            border_day_style=p_base.WG_BORDER_STYLE,
            border_day_rgb=p_base.FG_ITEM_HOVER,

            # Rayons
            radius_all=None,
            radius_top_right=p_base.WG_RADIUS,
            radius_top_left=p_base.WG_RADIUS,
            radius_bottom_right=p_base.WG_RADIUS,
            radius_bottom_left=p_base.WG_RADIUS,

            # Scroll
            scroll_bg=p_base.SCROLL_BG,
            scroll_width=p_base.SCROLL_WIDTH,
            scroll_height=p_base.SCROLL_HEIGHT,
            scroll_handle_bg=p_base.SCROLL_HANDLE_BG,
            scroll_handle_bg_hover=p_base.SCROLL_HANDLE_BG_HOVER,
            scroll_handle_fg=p_base.SCROLL_HANDLE_FG,
            scroll_handle_fg_hover=p_base.SCROLL_HANDLE_FG_HOVER,
            scroll_handle_min_width=p_base.SCROLL_HANDLE_MIN_WIDTH,
            scroll_handle_min_height=p_base.SCROLL_HANDLE_MIN_HEIGHT,
    ):
        # Style all generation
        try:
            # BG / FG
            if not bg_gen is None:
                bg = bg_gen
                bg_hover = bg_gen
                bg_checked = bg_gen
                bg_checked_hover = bg_gen
            if not fg_gen is None:
                fg = fg_gen
                fg_hover = fg_gen
                fg_checked = fg_gen
                fg_checked_hover = fg_gen
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

            # Radius
            if not radius_all is None:
                radius_top_right = radius_all
                radius_top_left = radius_all
                radius_bottom_right = radius_all
                radius_bottom_left = radius_all
        except: pass

        self.style = f"""
/******************************************
**       QCheckBox  |  QRadioButton      **
*******************************************/
                QCheckBox, QRadioButton {{
                background-color: rgba{bg};
                color: rgba{fg};
                spacing: {spacing}px;
                }}
                QCheckBox:hover, QRadioButton:hover {{
                background-color: rgba{bg_hover};
                color: rgba{fg_hover};
                }}
                QCheckBox:checked, QRadioButton:checked {{
                background-color: rgba{bg_checked};
                color: rgba{fg_checked};
                }}
                QCheckBox:checked:hover, QRadioButton:checked:hover {{
                background-color: rgba{bg_checked_hover};
                color: rgba{fg_checked_hover};
                }}

                /* IMG */
                QCheckBox::indicator, QRadioButton::indicator {{
                margin-top: {img_margin_top}px;
                margin-bottom: {img_margin_bottom}px;
                margin-right: {img_margin_right}px;
                margin-left: {img_margin_left}px;
                width: {img_width}px;
                height: {img_height}px;
                }}
                QCheckBox::indicator:unchecked, QRadioButton::indicator:unchecked {{
                image: url({f"{img_uncheck}{img_uncheck_rgb}.svg"});
                }}
                QCheckBox::indicator:hover, QRadioButton::indicator:hover {{
                image: url({f"{img_uncheck_hover}{img_uncheck_hover_rgb}.svg"});
                }}
                QCheckBox::indicator:checked, QRadioButton::indicator:checked {{
                image: url({f"{img_check}{img_check_rgb}.svg"});
                }}
                QCheckBox::indicator:checked:hover, QRadioButton::indicator:checked:hover {{
                image: url({f"{img_check_hover}{img_check_hover_rgb}.svg"});
                }}

                /* BORDURES */
                .QCheckBox, .QRadioButton {{
                border-top: {border_top}px {border_style} rgba{border_rgb};
                border-bottom: {border_bottom}px {border_style} rgba{border_rgb};
                border-right: {border_right}px {border_style} rgba{border_rgb};
                border-left: {border_left}px {border_style} rgba{border_rgb};
                }}
                .QCheckBox:hover, QRadioButton:hover {{
                border-top: {border_top_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-bottom: {border_bottom_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-right: {border_right_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-left: {border_left_hover}px {border_style_hover} rgba{border_rgb_hover};
                }}
                .QCheckBox:checked, .QRadioButton:checked {{
                border-top: {border_top_checked}px {border_style_checked} rgba{border_rgb_checked};
                border-bottom: {border_bottom_checked}px {border_style_checked} rgba{border_rgb_checked};
                border-right: {border_right_checked}px {border_style_checked} rgba{border_rgb_checked};
                border-left: {border_left_checked}px {border_style_checked} rgba{border_rgb_checked};
                }}
                .QCheckBox:checked:hover, .QRadioButton:checked:hover {{
                border-top: {border_top_checked_hover}px {border_style_checked_hover} rgba{border_rgb_checked_hover};
                border-bottom: {border_bottom_checked_hover}px {border_style_checked_hover} rgba{border_rgb_checked_hover};
                border-right: {border_right_checked_hover}px {border_style_checked_hover} rgba{border_rgb_checked_hover};
                border-left: {border_left_checked_hover}px {border_style_checked_hover} rgba{border_rgb_checked_hover};
                }}
/******************************************
**      /QCheckBox | /QRadioButton       **
*******************************************/
        
        
        
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
                
                
                
/**************************
**       QDateEdit       **
***************************/
                QDateEdit {{
                background-color: rgba{bg};
                color: rgba{fg};
                selection-background-color: rgba{bg_selection};
                selection-color: rgba{fg_selection};
                }}
                QDateEdit:hover {{
                background-color: rgba{bg_hover};
                color: rgba{fg_hover};
                }}

                /* IMG CALENDRIER */
                QDateEdit::drop-down {{
                image: url({f"{img}{img_rgb}.svg"});
                width: {img_width}px;
                height: {img_height}px;
                margin-top: {img_margin_top}px;
                margin-bottom: {img_margin_bottom}px;
                margin-right: {img_margin_right}px;
                margin-left: {img_margin_left}px;
                }}
                QDateEdit::drop-down:hover {{
                image: url({f"{img_hover}{img_hover_rgb}.svg"});
                }}

                /* WIDGETS */
                QCalendarWidget QWidget {{
                alternate-background-color: rgba{bg_mois};
                color: rgb{fg_mois};
                }}

                /* TOOL BUTTON */
                QCalendarWidget QToolButton {{
                font-size: {font_size}px;
                background-color: rgba{bg_header};
                color: rgba{fg_header};
                }}
                QCalendarWidget QToolButton:hover {{
                background-color: rgba{bg_header_hover};
                color: rgba{fg_header_hover};
                }}

                /* FLECHE GAUCHE DROITE */
                QToolButton#qt_calendar_nextmonth  {{
                qproperty-icon: url({f"{img_right}{img_right_rgb}.svg"});
                icon-size: {font_size}px, {font_size}px;
                }}
                QToolButton#qt_calendar_prevmonth {{
                qproperty-icon: url({f"{img_left}{img_left_rgb}.svg"});
                icon-size: {font_size}px, {font_size}px;
                }}

                /* MENU DEROULANT */
                QCalendarWidget QMenu {{
                width: 150px;
                font-size: {font_size}px;
                font-family: {font};
                background-color: rgba{bg_header};
                color: rgba{fg_header};
                }}

                /* SPIN BOX */
                QCalendarWidget QSpinBox {{
                width: 60px;
                font-size: {font_size}px;
                font-family: {font};
                background-color: rgba{bg_header};
                color: rgba{fg_header};
                selection-background-color: rgba{bg_selection};
                selection-color: rgba{fg_selection};
                }}

                /* JOURS */
                QCalendarWidget QAbstractItemView {{
                font-size: {font_size}px;
                font-family: {font};
                font-weight: 30;
                outline: 0px;
                }}
                QCalendarWidget QAbstractItemView:enabled {{
                background-color: rgba{bg_item};
                color: rgba{fg_item};
                selection-background-color: rgba{fg_item};
                selection-color: rgba{bg_item};
                }}
                QCalendarWidget QWidget:item:hover, QCalendarWidget QWidget:item:selected {{
                background-color: rgba{bg_item_hover};
                color: rgba{fg_item_hover};
                border: {border_day_size}px {border_day_style} rgba{border_day_rgb};
                }}

                /* BARRE HAUT */
                QCalendarWidget QWidget#qt_calendar_navigationbar {{
                background-color: rgba{bg_header};
                }}

                /* BORDURES */
                .QDateEdit {{
                border-top: {border_top}px {border_style} rgba{border_rgb};
                border-bottom: {border_bottom}px {border_style} rgba{border_rgb};
                border-right: {border_right}px {border_style} rgba{border_rgb};
                border-left: {border_left}px {border_style} rgba{border_rgb};
                }}
                .QDateEdit:hover {{
                border-top: {border_top_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-bottom: {border_bottom_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-right: {border_right_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-left: {border_left_hover}px {border_style_hover} rgba{border_rgb_hover};
                }}
/**************************
**      /QDateEdit       **
***************************/
                
                
                
/***********************
**       QFrame       **
************************/
                .QFrame {{
                background-color: rgba{bg};
                }}
        
                /* BORDURES */
                .QFrame {{
                border-top: {border_top}px {border_style} rgba{border_rgb};
                border-bottom: {border_bottom}px {border_style} rgba{border_rgb};
                border-right: {border_right}px {border_style} rgba{border_rgb};
                border-left: {border_left}px {border_style} rgba{border_rgb};
                }}
                .QFrame:hover {{
                border-top: {border_top_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-bottom: {border_bottom_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-right: {border_right_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-left: {border_left_hover}px {border_style_hover} rgba{border_rgb_hover};
                }}
/***********************
**      /QFrame       **
************************/
                
                
                
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
                
                
                
/****************************
**       QListWidget       **
*****************************/
                .QListWidget, .QListView {{
                background-color: rgba{bg};
                color: rgba{fg};
                }}
        
                /* ITEM */
                .QListWidget::item, .QListView::item {{
                background-color: rgba{bg_item};
                color: rgba{fg_item};
                border-top: {border_item_top}px {border_item_style} rgba{border_item_rgb};
                border-bottom: {border_item_bottom}px {border_item_style} rgba{border_item_rgb};
                border-right: {border_item_right}px {border_item_style} rgba{border_item_rgb};
                border-left: {border_item_left}px {border_item_style} rgba{border_item_rgb};
                }}
                .QListWidget::item:hover, .QListView::item:hover {{
                background-color: rgba{bg_item_hover};
                color: rgba{fg_item_hover};
                border-top: {border_item_top_hover}px {border_item_style_hover} rgba{border_item_rgb_hover};
                border-bottom: {border_item_bottom_hover}px {border_item_style_hover} rgba{border_item_rgb_hover};
                border-right: {border_item_right_hover}px {border_item_style_hover} rgba{border_item_rgb_hover};
                border-left: {border_item_left_hover}px {border_item_style_hover} rgba{border_item_rgb_hover};
                }}
                .QListWidget::item:selected, .QListView::item:selected {{
                background-color: rgba{bg_item_checked};
                color: rgba{fg_item_checked};
                border-top: {border_item_top_checked}px {border_item_style_checked} rgba{border_item_rgb_checked};
                border-bottom: {border_item_bottom_checked}px {border_item_style_checked} rgba{border_item_rgb_checked};
                border-right: {border_item_right_checked}px {border_item_style_checked} rgba{border_item_rgb_checked};
                border-left: {border_item_left_checked}px {border_item_style_checked} rgba{border_item_rgb_checked};
                }}
                .QListWidget::item:selected:hover, .QListView::item:selected:hover {{
                background-color: rgba{bg_item_checked_hover};
                color: rgba{fg_item_checked_hover};
                border-top: {border_item_top_checked_hover}px {border_item_style_checked_hover} rgba{border_item_rgb_checked_hover};
                border-bottom: {border_item_bottom_checked_hover}px {border_item_style_checked_hover} rgba{border_item_rgb_checked_hover};
                border-right: {border_item_right_checked_hover}px {border_item_style_checked_hover} rgba{border_item_rgb_checked_hover};
                border-left: {border_item_left_checked_hover}px {border_item_style_checked_hover} rgba{border_item_rgb_checked_hover};
                }}
        
                /* BORDURES */
                .QListWidget, .QListView {{
                border-top: {border_top}px {border_style} rgba{border_rgb};
                border-bottom: {border_bottom}px {border_style} rgba{border_rgb};
                border-right: {border_right}px {border_style} rgba{border_rgb};
                border-left: {border_left}px {border_style} rgba{border_rgb};
                }}
                .QListWidget:hover, .QListView:hover {{
                border-top: {border_top_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-bottom: {border_bottom_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-right: {border_right_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-left: {border_left_hover}px {border_style_hover} rgba{border_rgb_hover};
                }}
/****************************
**      /QListWidget       **
*****************************/
     
     
                
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


/************************
**       QSlider       **
*************************/
/************************
**      /QSlider       **
*************************/



/*************************
**      /QSpinBox       **
**************************/
/*************************
**       QSpinBox       **
**************************/



/*****************************
**      /QTableWidget       **
******************************/
                /* CORNER */
                QTableCornerButton::section {{
                background-color: rgba{bg_corner};
                }}
        
                /* TABLE_WIDGET */
                QTableWidget, QTableView {{
                background-color: rgba{bg};
                gridline-color: rgba{gridline};
                color: rgba{fg};
                }}
        
                /* ITEM */
                QTableWidget::item, QTableView::item {{
                background-color: rgba{bg_item};
                color: rgba{fg_item};
                border-top: {border_item_top}px {border_item_style} rgba{border_item_rgb};
                border-bottom: {border_item_bottom}px {border_item_style} rgba{border_item_rgb};
                border-right: {border_item_right}px {border_item_style} rgba{border_item_rgb};
                border-left: {border_item_left}px {border_item_style} rgba{border_item_rgb};
                }}
                QTableWidget::item:hover, QTableView::item:hover {{
                background-color: rgba{bg_item_hover};
                color: rgba{fg_item_hover};
                border-top: {border_item_top_hover}px {border_item_style_hover} rgba{border_item_rgb_hover};
                border-bottom: {border_item_bottom_hover}px {border_item_style_hover} rgba{border_item_rgb_hover};
                border-right: {border_item_right_hover}px {border_item_style_hover} rgba{border_item_rgb_hover};
                border-left: {border_item_left_hover}px {border_item_style_hover} rgba{border_item_rgb_hover};
                }}
                QTableWidget::item:selected, QTableView::item:selected {{
                background-color: rgba{bg_item_checked};
                color: rgba{fg_item_checked};
                border-top: {border_item_top_checked}px {border_item_style_checked} rgba{border_item_rgb_checked};
                border-bottom: {border_item_bottom_checked}px {border_item_style_checked} rgba{border_item_rgb_checked};
                border-right: {border_item_right_checked}px {border_item_style_checked} rgba{border_item_rgb_checked};
                border-left: {border_item_left_checked}px {border_item_style_checked} rgba{border_item_rgb_checked};
                }}
                QTableWidget::item:selected:hover, QTableView::item:selected:hover {{
                background-color: rgba{bg_item_checked_hover};
                color: rgba{fg_item_checked_hover};
                border-top: {border_item_top_checked_hover}px {border_item_style_checked_hover} rgba{border_item_rgb_checked_hover};
                border-bottom: {border_item_bottom_checked_hover}px {border_item_style_checked_hover} rgba{border_item_rgb_checked_hover};
                border-right: {border_item_right_checked_hover}px {border_item_style_checked_hover} rgba{border_item_rgb_checked_hover};
                border-left: {border_item_left_checked_hover}px {border_item_style_checked_hover} rgba{border_item_rgb_checked_hover};
                }}
        
                /* BORDURES */
                .QTableWidget, .QTableView {{
                border-top: {border_top}px {border_style} rgba{border_rgb};
                border-bottom: {border_bottom}px {border_style} rgba{border_rgb};
                border-right: {border_right}px {border_style} rgba{border_rgb};
                border-left: {border_left}px {border_style} rgba{border_rgb};
                }}
                .QTableWidget:hover, .QTableView:hover {{
                border-top: {border_top_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-bottom: {border_bottom_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-right: {border_right_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-left: {border_left_hover}px {border_style_hover} rgba{border_rgb_hover};
                }}
                
                QHeaderView::section {{
                background-color: rgba{bg_header};
                color: rgba{fg_header};
                border-top: {border_hd_top}px {border_hd_style} rgba{border_hd_rgb};
                border-bottom: {border_hd_bottom}px {border_hd_style} rgba{border_hd_rgb};
                border-right: {border_hd_right}px {border_hd_style} rgba{border_hd_rgb};
                border-left: {border_hd_left}px {border_hd_style} rgba{border_hd_rgb};
                }}
                QHeaderView::section:hover {{
                background-color: rgba{bg_header_hover};
                color: rgba{fg_header_hover};
                border-top: {border_hd_top_hover}px {border_hd_style_hover} rgba{border_hd_rgb_hover};
                border-bottom: {border_hd_bottom_hover}px {border_hd_style_hover} rgba{border_hd_rgb_hover};
                border-right: {border_hd_right_hover}px {border_hd_style_hover} rgba{border_hd_rgb_hover};
                border-left: {border_hd_left_hover}px {border_hd_style_hover} rgba{border_hd_rgb_hover};
                }}
                QHeaderView::section:checked {{
                background-color: rgba{bg_header_checked};
                color: rgba{fg_header_checked};
                border-top: {border_hd_top_checked}px {border_hd_style_checked} rgba{border_hd_rgb_checked};
                border-bottom: {border_hd_bottom_checked}px {border_hd_style_checked} rgba{border_hd_rgb_checked};
                border-right: {border_hd_right_checked}px {border_hd_style_checked} rgba{border_hd_rgb_checked};
                border-left: {border_hd_left_checked}px {border_hd_style_checked} rgba{border_hd_rgb_checked};
                }}
                QHeaderView::section:checked:hover {{
                background-color: rgba{bg_header_checked_hover};
                color: rgba{fg_header_checked_hover};
                border-top: {border_hd_top_checked_hover}px {border_hd_style_checked_hover} rgba{border_hd_rgb_checked_hover};
                border-bottom: {border_hd_bottom_checked_hover}px {border_hd_style_checked_hover} rgba{border_hd_rgb_checked_hover};
                border-right: {border_hd_right_checked_hover}px {border_hd_style_checked_hover} rgba{border_hd_rgb_checked_hover};
                border-left: {border_hd_left_checked_hover}px {border_hd_style_checked_hover} rgba{border_hd_rgb_checked_hover};
                }}
/*****************************
**       QTableWidget       **
******************************/



/***********************************************************
**       QLineEdit  |  QPlainTextEdit  |  QTextEdit       **
************************************************************/
                .QLineEdit, .QPlainTextEdit, .QTextEdit {{
                background-color: rgba{bg};
                color: rgba{fg};
                selection-background-color: rgb{bg_selection};
                selection-color: rgb{fg_selection};
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
















/***********************
**       RAYONS       **
************************/
                QWidget {{
                border-top-right-radius: {radius_top_right}px;
                border-top-left-radius: {radius_top_left}px;
                border-bottom-right-radius: {radius_bottom_right}px;
                border-bottom-left-radius: {radius_bottom_left}px;
                }}
/***********************
**       RAYONS       **
************************/
                
/***************************
**       QScrollBar       **
****************************/
                QScrollBar {{
                background-color: rgba{scroll_bg};
                width: {scroll_width}px;
                height: {scroll_height}px;
                }}
                QScrollBar::handle:horizontal {{
                min-width: {scroll_handle_min_width}px;
                }}
                QScrollBar::handle:vertical {{
                min-height: {scroll_handle_min_height}px;
                }}
                QScrollBar::handle {{
                background-color: rgba{scroll_handle_fg};
                }}
                QScrollBar::handle:hover {{
                background-color: rgba{scroll_handle_fg_hover};
                }}
                
                QScrollBar::add-page, QScrollBar::sub-page {{
                background-color: rgba{scroll_handle_bg};
                border: none;
                }}
                QScrollBar::add-page:hover, QScrollBar::sub-page:hover {{
                background-color: rgba{scroll_handle_bg_hover};
                border: none;
                }}
/***************************
**      /QScrollBar       **
****************************/
"""

        self.palette_txt = QtGui.QPalette()
        self.palette_txt.setColor(QtGui.QPalette.Text, QtGui.QColor(*fg))
        self.palette_txt.setColor(QtGui.QPalette.PlaceholderText, QtGui.QColor(*fg_placeholder))


    def get(self): return self.style
    def get_txt_palette(self): return self.palette_txt

