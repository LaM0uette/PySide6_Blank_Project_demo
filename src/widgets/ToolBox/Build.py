from src.build.mods import Functions
from src.widgets import vb_wg


class Style:
    def __init__(
            self,
            *wgs,

            # Dimensions
            width=vb_wg.WIDTH,
            height=vb_wg.HEIGHT,

            # Police
            font=vb_wg.FONT,
            font_size=vb_wg.FONT_SIZE,

            # Paramètres
            focus_policy=vb_wg.FOCUS_POLICY,
            frame_shape=vb_wg.FRAME_SHAPE,
            frame_shadow=vb_wg.FRAME_SHADOW,
            line_width=0,
            tab_spacing=0,

            # Curseur
            cursor=vb_wg.CUR,

            # Couleurs BG
            bg=vb_wg.BG,
            bg_hover=vb_wg.BG_HOVER,
            bg_checked=vb_wg.BG_CHECKED,
            bg_checked_hover=vb_wg.BG_CHECKED_HOVER,
            # Couleurs FG
            fg=vb_wg.FG,
            fg_hover=vb_wg.FG_HOVER,
            fg_checked=vb_wg.FG_CHECKED,
            fg_checked_hover=vb_wg.FG_CHECKED_HOVER,

            # Bordures
            border=vb_wg.BORDER_WIDTH,
            border_style=vb_wg.BORDER_STYLE,
            border_rgb=vb_wg.BORDER_RGB,
            # Bordures hover
            border_hover=vb_wg.BORDER_WIDTH,
            border_hover_style=vb_wg.BORDER_STYLE,
            border_hover_rgb=vb_wg.BORDER_RGB,
            # Bordures HD
            border_hd=vb_wg.BORDER_WIDTH,
            border_hd_style=vb_wg.BORDER_STYLE,
            border_hd_rgb=vb_wg.BORDER_RGB,
            # Bordures HD hover
            border_hd_hover=vb_wg.BORDER_WIDTH,
            border_hd_hover_style=vb_wg.BORDER_STYLE,
            border_hd_hover_rgb=vb_wg.BORDER_RGB,
            # Bordures HD checked
            border_hd_checked=vb_wg.BORDER_WIDTH,
            border_hd_checked_style=vb_wg.BORDER_STYLE,
            border_hd_checked_rgb=vb_wg.BORDER_RGB,
            # Bordures HD checked hover
            border_hd_checked_hover=vb_wg.BORDER_WIDTH,
            border_hd_checked_hover_style=vb_wg.BORDER_STYLE,
            border_hd_checked_hover_rgb=vb_wg.BORDER_RGB,

            # Rayons
            radius=vb_wg.RADIUS,
            radius_tab=vb_wg.RADIUS,

            # Scroll
            scroll_bg=vb_wg.SCROLL_BG,
            scroll_width=vb_wg.SCROLL_WIDTH,
            scroll_height=vb_wg.SCROLL_HEIGHT,
            scroll_handle_bg=vb_wg.SCROLL_HANDLE_BG,
            scroll_handle_bg_hover=vb_wg.SCROLL_HANDLE_BG_HOVER,
            scroll_handle_fg=vb_wg.SCROLL_HANDLE_FG,
            scroll_handle_fg_hover=vb_wg.SCROLL_HANDLE_FG_HOVER,
            scroll_handle_min_width=vb_wg.SCROLL_HANDLE_MIN_WIDTH,
            scroll_handle_min_height=vb_wg.SCROLL_HANDLE_MIN_HEIGHT,
    ):
        """

        :param wgs:
        :param width:
        :param height:
        :param font:
        :param font_size:
        :param focus_policy:
        :param frame_shape:
        :param frame_shadow:
        :param line_width:
        :param tab_spacing:
        :param cursor:
        :param bg:
        :param bg_hover:
        :param bg_checked:
        :param bg_checked_hover:
        :param fg:
        :param fg_hover:
        :param fg_checked:
        :param fg_checked_hover:
        :param border:
        :param border_style:
        :param border_rgb:
        :param border_hover:
        :param border_hover_style:
        :param border_hover_rgb:
        :param border_hd:
        :param border_hd_style:
        :param border_hd_rgb:
        :param border_hd_hover:
        :param border_hd_hover_style:
        :param border_hd_hover_rgb:
        :param border_hd_checked:
        :param border_hd_checked_style:
        :param border_hd_checked_rgb:
        :param border_hd_checked_hover:
        :param border_hd_checked_hover_style:
        :param border_hd_checked_hover_rgb:
        :param radius:
        :param radius_tab:
        :param scroll_bg:
        :param scroll_width:
        :param scroll_height:
        :param scroll_handle_bg:
        :param scroll_handle_bg_hover:
        :param scroll_handle_fg:
        :param scroll_handle_fg_hover:
        :param scroll_handle_min_width:
        :param scroll_handle_min_height:
        """

        style = f"""
                /* TOOLBOX */
                QToolBox::tab {{
                background-color: rgba{bg};
                color: rgba{fg};
                border-top: {border_hd[0]}px {border_hd_style} rgba{border_hd_rgb};
                border-bottom: {border_hd[1]}px {border_hd_style} rgba{border_hd_rgb};
                border-right: {border_hd[2]}px {border_hd_style} rgba{border_hd_rgb};
                border-left: {border_hd[3]}px {border_hd_style} rgba{border_hd_rgb};
                border-top-right-radius: {radius_tab[0]}px;
                border-top-left-radius: {radius_tab[1]}px;
                border-bottom-right-radius: {radius_tab[2]}px;
                border-bottom-left-radius: {radius_tab[3]}px;
                }}

                QToolBox::tab:hover {{
                background-color: rgba{bg_hover};
                color: rgba{fg_hover};
                border-top: {border_hd_hover[0]}px {border_hd_hover_style} rgba{border_hd_hover_rgb};
                border-bottom: {border_hd_hover[1]}px {border_hd_hover_style} rgba{border_hd_hover_rgb};
                border-right: {border_hd_hover[2]}px {border_hd_hover_style} rgba{border_hd_hover_rgb};
                border-left: {border_hd_hover[3]}px {border_hd_hover_style} rgba{border_hd_hover_rgb};
                }}

                QToolBox::tab:selected {{
                background-color: rgba{bg_checked};
                color: rgba{fg_checked};
                border-top: {border_hd_checked[0]}px {border_hd_checked_style} rgba{border_hd_checked_rgb};
                border-bottom: {border_hd_checked[1]}px {border_hd_checked_style} rgba{border_hd_checked_rgb};
                border-right: {border_hd_checked[2]}px {border_hd_checked_style} rgba{border_hd_checked_rgb};
                border-left: {border_hd_checked[3]}px {border_hd_checked_style} rgba{border_hd_checked_rgb};
                }}

                QToolBox::tab:selected:hover {{
                background-color: rgba{bg_checked_hover};
                color: rgba{fg_checked_hover};
                border-top: {border_hd_checked_hover[0]}px {border_hd_checked_hover_style} rgba{border_hd_checked_hover_rgb};
                border-bottom: {border_hd_checked_hover[1]}px {border_hd_checked_hover_style} rgba{border_hd_checked_hover_rgb};
                border-right: {border_hd_checked_hover[2]}px {border_hd_checked_hover_style} rgba{border_hd_checked_hover_rgb};
                border-left: {border_hd_checked_hover[3]}px {border_hd_checked_hover_style} rgba{border_hd_checked_hover_rgb};
                }}

                /* BORDURES */
                .QToolBox {{
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}
                .QToolBox:hover {{
                border-top: {border_hover[0]}px {border_hover_style} rgba{border_hover_rgb};
                border-bottom: {border_hover[1]}px {border_hover_style} rgba{border_hover_rgb};
                border-right: {border_hover[2]}px {border_hover_style} rgba{border_hover_rgb};
                border-left: {border_hover[3]}px {border_hover_style} rgba{border_hover_rgb};
                }}

                /* RAYONS */
                .QToolBox {{
                border-top-right-radius: {radius[0]}px;
                border-top-left-radius: {radius[1]}px;
                border-bottom-right-radius: {radius[2]}px;
                border-bottom-left-radius: {radius[3]}px;
                }}

                /* SCROLL */
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
                }}"""
        for wg in wgs:
            # Dimensions
            Functions().SET_DIM(wg, width=width, height=height)

            # Police
            Functions().SET_FONT(wg, font=font, font_size=font_size)

            # Paramètres
            wg.setFocusPolicy(focus_policy)
            wg.setFrameShape(frame_shape)
            wg.setFrameShadow(frame_shadow)
            wg.setLineWidth(line_width)
            wg.layout().setSpacing(tab_spacing)

            # Curseur
            wg.setCursor(Functions().SET_CURSOR(cursor))

            # Style
            wg.setStyleSheet(style)
