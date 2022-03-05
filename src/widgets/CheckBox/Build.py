from src.build.mods import Functions
from src.widgets import vb_wg


class Build:
    def __init__(
            self,
            *wgs,

            # Dimensions
            width = vb_wg.WIDTH,
            height = vb_wg.HEIGHT,

            # Police
            font = vb_wg.FONT,
            font_size = vb_wg.FONT_SIZE,

            # Arguments
            auto_exclusive=False,
            triple_state=False,

            # Curseur
            curseur=vb_wg.CUR,


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

            # Positions WG
            spacing=10,

            # Images
            img_uncheck=vb_wg.IMG_UNCHECK,
            img_uncheck_hover=vb_wg.IMG_UNCHECK_HOVER,
            img_check=vb_wg.IMG_CHECK,
            img_check_hover=vb_wg.IMG_CHECK_HOVER,
            # Images RGB
            img_uncheck_rgb=vb_wg.IMG_UNCHECK_RGB,
            img_uncheck_hover_rgb=vb_wg.IMG_UNCHECK_HOVER_RGB,
            img_check_rgb=vb_wg.IMG_CHECK_RGB,
            img_check_hover_rgb=vb_wg.IMG_CHECK_HOVER_RGB,
            # Images DIM
            img_width=vb_wg.img_width,
            img_height=vb_wg.img_height,
            # Images positions
            img_margin=((0,) * 4),

            # Bordures
            border=vb_wg.BORDER_WIDTH,
            border_style=vb_wg.BORDER_STYLE,
            border_rgb=vb_wg.BORDER_RGB,
            # Bordures hover
            border_hover=vb_wg.BORDER_WIDTH,
            border_hover_style=vb_wg.BORDER_STYLE,
            border_hover_rgb=vb_wg.BORDER_RGB,
            # Bordures checked
            border_checked=vb_wg.BORDER_WIDTH,
            border_checked_style=vb_wg.BORDER_STYLE,
            border_checked_rgb=vb_wg.BORDER_RGB,
            # Bordures checked hover
            border_checked_hover=vb_wg.BORDER_WIDTH,
            border_checked_hover_style=vb_wg.BORDER_STYLE,
            border_checked_hover_rgb=vb_wg.BORDER_RGB,

            # Rayons
            radius=vb_wg.RADIUS
    ):
        style = f"""
                /* CHECKBOX */
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
                margin-top: {img_margin[0]}px;
                margin-bottom: {img_margin[1]}px;
                margin-right: {img_margin[2]}px;
                margin-left: {img_margin[3]}px;
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
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}
                .QCheckBox:hover {{
                border-top: {border_hover[0]}px {border_hover_style} rgba{border_hover_rgb};
                border-bottom: {border_hover[1]}px {border_hover_style} rgba{border_hover_rgb};
                border-right: {border_hover[2]}px {border_hover_style} rgba{border_hover_rgb};
                border-left: {border_hover[3]}px {border_hover_style} rgba{border_hover_rgb};
                }}
                .QCheckBox:checked {{
                border-top: {border_checked[0]}px {border_checked_style} rgba{border_checked_rgb};
                border-bottom: {border_checked[1]}px {border_checked_style} rgba{border_checked_rgb};
                border-right: {border_checked[2]}px {border_checked_style} rgba{border_checked_rgb};
                border-left: {border_checked[3]}px {border_checked_style} rgba{border_checked_rgb};
                }}
                .QCheckBox:checked:hover {{
                border-top: {border_checked_hover[0]}px {border_checked_hover_style} rgba{border_checked_hover_rgb};
                border-bottom: {border_checked_hover[1]}px {border_checked_hover_style} rgba{border_checked_hover_rgb};
                border-right: {border_checked_hover[2]}px {border_checked_hover_style} rgba{border_checked_hover_rgb};
                border-left: {border_checked_hover[3]}px {border_checked_hover_style} rgba{border_checked_hover_rgb};
                }}

                /* RAYONS */
                .QCheckBox {{
                border-top-right-radius: {radius[0]}px;
                border-top-left-radius: {radius[1]}px;
                border-bottom-right-radius: {radius[2]}px;
                border-bottom-left-radius: {radius[3]}px;
                }}"""

        for wg in wgs:
            # Dimensions
            Functions().SET_DIM(wg, width=width, height=height)

            # Police
            Functions().SET_FONT(wg, font=font, font_size=font_size)

            wg.setAutoExclusive(auto_exclusive)
            wg.setTristate(triple_state)

            # Curseur
            wg.setCursor(Functions().SET_CURSOR(curseur))

            # Style
            wg.setStyleSheet(style)
