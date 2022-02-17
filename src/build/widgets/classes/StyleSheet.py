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
            bg_item=p_base.BG_ITEM,
            bg_item_hover=p_base.BG_ITEM_HOVER,
            # Couleurs FG
            fg_gen=None,
            fg=p_base.FG,
            fg_hover=p_base.FG_HOVER,
            fg_checked=p_base.FG_CHECKED,
            fg_checked_hover=p_base.FG_CHECKED_HOVER,
            fg_selection=p_base.FG_SELECTION,
            fg_item=p_base.FG_ITEM,
            fg_item_hover=p_base.FG_ITEM_HOVER,

            # Dimensions WG
            width=p_base.WG_WIDTH,
            height=p_base.WG_HEIGHT,
            spacing=10,

            # Police
            font=p_base.FONT,
            font_size=p_base.FONT_SIZE,

            # Images
            img_uncheck=p_base.IMG_UNCHECK,
            img_uncheck_hover=p_base.IMG_UNCHECK_HOVER,
            img_check=p_base.IMG_CHECK,
            img_check_hover=p_base.IMG_CHECK_HOVER,
            img_unroll=p_base.IMG_UNROLL,
            img_unroll_hover=p_base.IMG_UNROLL_HOVER,
            # Images RGB
            img_uncheck_rgb=p_base.IMG_UNCHECK_RGB,
            img_uncheck_hover_rgb=p_base.IMG_UNCHECK_HOVER_RGB,
            img_check_rgb=p_base.IMG_CHECK_RGB,
            img_check_hover_rgb=p_base.IMG_CHECK_HOVER_RGB,
            img_unroll_rgb=p_base.IMG_UNROLL_RGB,
            img_unroll_hover_rgb=p_base.IMG_UNROLL_HOVER_RGB,
            # Images DIM
            img_width=p_base.IMG_WIDTH,
            img_height=p_base.IMG_HEIGHT,
            # Images margin
            img_margin_top=0,
            img_margin_bottom=0,
            img_margin_right=0,
            img_margin_left=(p_base.WG_HEIGHT - (p_base.WG_HEIGHT * P_style().x_ico())) / 2,

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
        # BG
        if not bg_gen is None:
            bg = bg_gen
            bg_hover = bg_gen
            bg_checked = bg_gen
            bg_checked_hover = bg_gen
        # FG
        if not fg_gen is None:
            fg = fg_gen
            fg_hover = fg_gen
            fg_checked = fg_gen
            fg_checked_hover = fg_gen
        # Bordure
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
        # Bordure style
        if not border_gen_style is None:
            border_style = border_gen_style
            border_style_hover = border_gen_style
            border_style_checked = border_gen_style
            border_style_checked_hover = border_gen_style
        # Bordure RGB
        if not border_gen_rgb is None:
            border_rgb = border_gen_rgb
            border_rgb_hover = border_gen_rgb
            border_rgb_checked = border_gen_rgb
            border_rgb_checked_hover = border_gen_rgb
        # Radius
        if not radius_all is None:
            radius_top_right = radius_all
            radius_top_left = radius_all
            radius_bottom_right = radius_all
            radius_bottom_left = radius_all


        self.style = f"""
                /****************
                **  QCheckBox  **
                *****************/
                QCheckBox {{
                background-color: rgba{bg};
                color: rgba{fg};
                spacing: {spacing}px;
                }}
                QCheckBox:hover {{
                background-color: rgba{bg_hover};
                color: rgba{fg_hover};
                }}
                QCheckBox:checked {{
                background-color: rgba{bg_checked};
                color: rgba{fg_checked};
                }}
                QCheckBox:checked:hover {{
                background-color: rgba{bg_checked_hover};
                color: rgba{fg_checked_hover};
                }}

                /* IMG */
                QCheckBox::indicator {{
                margin-top: {img_margin_top}px;
                margin-bottom: {img_margin_bottom}px;
                margin-right: {img_margin_right}px;
                margin-left: {img_margin_left}px;
                width: {img_width}px;
                height: {img_height}px;
                }}
                QCheckBox::indicator:unchecked {{
                image: url({f"{img_uncheck}{img_uncheck_rgb}.svg"});
                }}
                QCheckBox::indicator:hover {{
                image: url({f"{img_uncheck_hover}{img_uncheck_hover_rgb}.svg"});
                }}
                QCheckBox::indicator:checked {{
                image: url({f"{img_check}{img_check_rgb}.svg"});
                }}
                QCheckBox::indicator:checked:hover {{
                image: url({f"{img_check_hover}{img_check_hover_rgb}.svg"});
                }}

                /* BORDURES */
                .QCheckBox {{
                border-top: {border_top}px {border_style} rgba{border_rgb};
                border-bottom: {border_bottom}px {border_style} rgba{border_rgb};
                border-right: {border_right}px {border_style} rgba{border_rgb};
                border-left: {border_left}px {border_style} rgba{border_rgb};
                }}
                .QCheckBox:hover {{
                border-top: {border_top_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-bottom: {border_bottom_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-right: {border_right_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-left: {border_left_hover}px {border_style_hover} rgba{border_rgb_hover};
                }}
                .QCheckBox:checked {{
                border-top: {border_top_checked}px {border_style_checked} rgba{border_rgb_checked};
                border-bottom: {border_bottom_checked}px {border_style_checked} rgba{border_rgb_checked};
                border-right: {border_right_checked}px {border_style_checked} rgba{border_rgb_checked};
                border-left: {border_left_checked}px {border_style_checked} rgba{border_rgb_checked};
                }}
                .QCheckBox:checked:hover {{
                border-top: {border_top_checked_hover}px {border_style_checked_hover} rgba{border_rgb_checked_hover};
                border-bottom: {border_bottom_checked_hover}px {border_style_checked_hover} rgba{border_rgb_checked_hover};
                border-right: {border_right_checked_hover}px {border_style_checked_hover} rgba{border_rgb_checked_hover};
                border-left: {border_left_checked_hover}px {border_style_checked_hover} rgba{border_rgb_checked_hover};
                }}

                /* RAYONS */
                .QCheckBox {{
                border-top-right-radius: {radius_top_right}px;
                border-top-left-radius: {radius_top_left}px;
                border-bottom-right-radius: {radius_bottom_right}px;
                border-bottom-left-radius: {radius_bottom_left}px;
                }}
                /****************
                ** /QCheckBox  **
                *****************/
        
        
        
                /****************
                **  QComboBox  **
                *****************/
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
                image: url({f"{img_unroll}{img_unroll_rgb}.svg"});
                width: {img_width}px;
                height: {img_height}px;
                }}
                QComboBox::down-arrow:hover, QFontComboBox::down-arrow:hover {{
                image: url({f"{img_unroll_hover}{img_unroll_hover_rgb}.svg"});
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
                
                /* RAYONS */
                .QComboBox, .QFontComboBox {{
                border-top-right-radius: {radius_top_right}px;
                border-top-left-radius: {radius_top_left}px;
                border-bottom-right-radius: {radius_bottom_right}px;
                border-bottom-left-radius: {radius_bottom_left}px;
                }}

                /* SCROLL */
                QComboBox QScrollBar, QFontComboBox QScrollBar {{
                background-color: rgba{scroll_bg};
                width: {scroll_width}px;
                height: {scroll_height}px;
                }}
                QComboBox::handle:horizontal, QFontComboBox::handle:horizontal {{
                min-width: {scroll_handle_min_width}px;
                }}
                QComboBox::handle:vertical, QFontComboBox::handle:vertical {{
                min-height: {scroll_handle_min_height}px;
                }}
                QComboBox QScrollBar::handle, QFontComboBox QScrollBar::handle {{
                background-color: rgba{scroll_handle_fg};
                }}
                QComboBox QScrollBar::handle:hover, QFontComboBox QScrollBar::handle:hover {{
                background-color: rgba{scroll_handle_fg_hover};
                }}
                
                QComboBox QScrollBar::add-page, QComboBox QScrollBar::sub-page, QFontComboBox QScrollBar::add-page, QFontComboBox QScrollBar::sub-page {{
                background-color: rgba{scroll_handle_bg};
                border: none;
                }}
                QComboBox QScrollBar::add-page:hover, QComboBox QScrollBar::sub-page:hover, QFontComboBox QScrollBar::add-page:hover, QFontComboBox QScrollBar::sub-page:hover {{
                background-color: rgba{scroll_handle_bg_hover};
                border: none;
                }}
                /****************
                ** /QComboBox  **
                *****************/
"""


    def get(self): return self.style
