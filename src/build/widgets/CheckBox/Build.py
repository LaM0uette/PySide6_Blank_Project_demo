from src import *


class Style:
    def __init__(
            self,
            *wgs,

            # Dimensions
            width=vbase.WG_WIDTH,
            height=vbase.WG_HEIGHT,

            # Police
            font=vbase.FONT,
            font_size=vbase.FONT_SIZE,

            # Curseur
            curseur=Cur().souris_main(),


            # Couleurs BG
            bg=vbase.BG,
            bg_hover=vbase.BG_HOVER,
            bg_checked=vbase.BG_CHECKED,
            bg_checked_hover=vbase.BG_CHECKED_HOVER,
            # Couleurs FG
            fg=vbase.FG,
            fg_hover=vbase.FG_HOVER,
            fg_checked=vbase.FG_CHECKED,
            fg_checked_hover=vbase.FG_CHECKED_HOVER,

            # Positions WG
            spacing=10,

            # Images
            img_uncheck=vbase.IMG_UNCHECK,
            img_uncheck_hover=vbase.IMG_UNCHECK_HOVER,
            img_check=vbase.IMG_CHECK,
            img_check_hover=vbase.IMG_CHECK_HOVER,
            # Images RGB
            img_uncheck_rgb=vbase.IMG_UNCHECK_RGB,
            img_uncheck_hover_rgb=vbase.IMG_UNCHECK_HOVER_RGB,
            img_check_rgb=vbase.IMG_CHECK_RGB,
            img_check_hover_rgb=vbase.IMG_CHECK_HOVER_RGB,
            # Images DIM
            img_width=vbase.img_width,
            img_height=vbase.img_height,
            # Images positions
            img_margin=((0,) * 4),

            # Bordures
            border=vbase.WG_BORDER_WIDTH,
            border_style=vbase.WG_BORDER_STYLE,
            border_rgb=vbase.WG_BORDER_RGB,
            # Bordures hover
            border_hover=vbase.WG_BORDER_WIDTH,
            border_hover_style=vbase.WG_BORDER_STYLE,
            border_hover_rgb=vbase.WG_BORDER_RGB,
            # Bordures checked
            border_checked=vbase.WG_BORDER_WIDTH,
            border_checked_style=vbase.WG_BORDER_STYLE,
            border_checked_rgb=vbase.WG_BORDER_RGB,
            # Bordures checked hover
            border_checked_hover=vbase.WG_BORDER_WIDTH,
            border_checked_hover_style=vbase.WG_BORDER_STYLE,
            border_checked_hover_rgb=vbase.WG_BORDER_RGB,

            # Rayons
            radius=vbase.WG_RADIUS
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
            # Style
            wg.setStyleSheet(style)

            # Dimensions
            Functions().SET_DIM(wg, width=width, height=height)

            # Police
            Functions().SET_FONT(wg, font=font, font_size=font_size)

            # Curseur
            wg.setCursor(curseur)
