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
            bg_indeterminate=vb_wg.BG_INDETERMINATE,
            bg_indeterminate_hover=vb_wg.BG_INDETERMINATE_HOVER,
            # Couleurs FG
            fg=vb_wg.FG,
            fg_hover=vb_wg.FG_HOVER,
            fg_checked=vb_wg.FG_CHECKED,
            fg_checked_hover=vb_wg.FG_CHECKED_HOVER,
            fg_indeterminate=vb_wg.FG_INDETERMINATE,
            fg_indeterminate_hover=vb_wg.FG_INDETERMINATE_HOVER,

            # Positions WG
            spacing=10,

            # Images
            img_uncheck=vb_wg.IMG_UNCHECK,
            img_uncheck_hover=vb_wg.IMG_UNCHECK_HOVER,
            img_check=vb_wg.IMG_CHECK,
            img_check_hover=vb_wg.IMG_CHECK_HOVER,
            img_indeterminate=vb_wg.IMG_INDETERMINATE,
            img_indeterminate_hover=vb_wg.IMG_INDETERMINATE_HOVER,
            # Images RGB
            img_uncheck_rgb=vb_wg.IMG_UNCHECK_RGB,
            img_uncheck_hover_rgb=vb_wg.IMG_UNCHECK_HOVER_RGB,
            img_check_rgb=vb_wg.IMG_CHECK_RGB,
            img_check_hover_rgb=vb_wg.IMG_CHECK_HOVER_RGB,
            img_indeterminate_rgb=vb_wg.IMG_INDETERMINATE_RGB,
            img_indeterminate_hover_rgb=vb_wg.IMG_INDETERMINATE_HOVER_RGB,
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
            # Bordures indeterminate
            border_indeterminate=vb_wg.BORDER_WIDTH,
            border_indeterminate_style=vb_wg.BORDER_STYLE,
            border_indeterminate_rgb=vb_wg.BORDER_RGB,
            # Bordures indeterminate hover
            border_indeterminate_hover=vb_wg.BORDER_WIDTH,
            border_indeterminate_hover_style=vb_wg.BORDER_STYLE,
            border_indeterminate_hover_rgb=vb_wg.BORDER_RGB,

            # Rayons
            radius=vb_wg.RADIUS
    ):
        """
        :param wgs: Widgets séparés par "," .
        :param width: int()
        :param height: int()
        :param font: str()  #nom de la police
        :param font_size: int()
        :param auto_exclusive: bool()
        :param triple_state: bool()
        :param curseur: Cur().%nomCurseur()
        :param bg: Rgb().%nomCouleur()
        :param bg_hover: Rgb().%nomCouleur()
        :param bg_checked: Rgb().%nomCouleur()
        :param bg_checked_hover: Rgb().%nomCouleur()
        :param bg_indeterminate: Rgb().%nomCouleur()
        :param bg_indeterminate_hover: Rgb().%nomCouleur()
        :param fg: Rgb().%nomCouleur()
        :param fg_hover: Rgb().%nomCouleur()
        :param fg_checked: Rgb().%nomCouleur()
        :param fg_checked_hover: Rgb().%nomCouleur()
        :param fg_indeterminate: Rgb().%nomCouleur()
        :param fg_indeterminate_hover: Rgb().%nomCouleur()
        :param spacing: int()
        :param img_uncheck: Img().%nomImage()
        :param img_uncheck_hover: Img().%nomImage()
        :param img_check: Img().%nomImage()
        :param img_check_hover: Img().%nomImage()
        :param img_indeterminate: Img().%nomImage()
        :param img_indeterminate_hover: Img().%nomImage()
        :param img_uncheck_rgb:  Rgb().%nomCouleur()
        :param img_uncheck_hover_rgb:  Rgb().%nomCouleur()
        :param img_check_rgb:  Rgb().%nomCouleur()
        :param img_check_hover_rgb:  Rgb().%nomCouleur()
        :param img_indeterminate_rgb:  Rgb().%nomCouleur()
        :param img_indeterminate_hover_rgb:  Rgb().%nomCouleur()
        :param img_width: int()
        :param img_height: int()
        :param img_margin: tuple(int(), int(), int(), int())
        :param border: tuple(int(), int(), int(), int())
        :param border_style: str()  # dashed | dot-dash | dot-dot-dash | dotted | double | groove | inset | outset | ridge | solid | none
        :param border_rgb:  Rgb().%nomCouleur()
        :param border_hover: tuple(int(), int(), int(), int())
        :param border_hover_style: str()  # dashed | dot-dash | dot-dot-dash | dotted | double | groove | inset | outset | ridge | solid | none
        :param border_hover_rgb:  Rgb().%nomCouleur()
        :param border_checked: tuple(int(), int(), int(), int())
        :param border_checked_style: str()  # dashed | dot-dash | dot-dot-dash | dotted | double | groove | inset | outset | ridge | solid | none
        :param border_checked_rgb:  Rgb().%nomCouleur()
        :param border_checked_hover: tuple(int(), int(), int(), int())
        :param border_checked_hover_style: str()  # dashed | dot-dash | dot-dot-dash | dotted | double | groove | inset | outset | ridge | solid | none
        :param border_checked_hover_rgb:  Rgb().%nomCouleur()
        :param border_indeterminate: tuple(int(), int(), int(), int())
        :param border_indeterminate_style: str()  # dashed | dot-dash | dot-dot-dash | dotted | double | groove | inset | outset | ridge | solid | none
        :param border_indeterminate_rgb:  Rgb().%nomCouleur()
        :param border_indeterminate_hover: tuple(int(), int(), int(), int())
        :param border_indeterminate_hover_style: str()  # dashed | dot-dash | dot-dot-dash | dotted | double | groove | inset | outset | ridge | solid | none
        :param border_indeterminate_hover_rgb:  Rgb().%nomCouleur()
        :param radius: tuple(int(), int(), int(), int())
        """

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
                QCheckBox:indeterminate {{
                background-color: rgba{bg_indeterminate};
                color: rgba{fg_indeterminate};
                }}
                QCheckBox:indeterminate:hover {{
                background-color: rgba{bg_indeterminate_hover};
                color: rgba{fg_indeterminate_hover};
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
                QCheckBox::indicator::indeterminate {{
                image: url({f"{img_indeterminate}{img_indeterminate_rgb}.svg"});
                }}
                QCheckBox::indicator::indeterminate:hover {{
                image: url({f"{img_indeterminate_hover}{img_indeterminate_hover_rgb}.svg"});
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
                .QCheckBox:indeterminate {{
                border-top: {border_indeterminate[0]}px {border_indeterminate_style} rgba{border_indeterminate_rgb};
                border-bottom: {border_indeterminate[1]}px {border_indeterminate_style} rgba{border_indeterminate_rgb};
                border-right: {border_indeterminate[2]}px {border_indeterminate_style} rgba{border_indeterminate_rgb};
                border-left: {border_indeterminate[3]}px {border_indeterminate_style} rgba{border_indeterminate_rgb};
                }}
                .QCheckBox:indeterminate:hover {{
                border-top: {border_indeterminate_hover[0]}px {border_indeterminate_hover_style} rgba{border_indeterminate_hover_rgb};
                border-bottom: {border_indeterminate_hover[1]}px {border_indeterminate_hover_style} rgba{border_indeterminate_hover_rgb};
                border-right: {border_indeterminate_hover[2]}px {border_indeterminate_hover_style} rgba{border_indeterminate_hover_rgb};
                border-left: {border_indeterminate_hover[3]}px {border_indeterminate_hover_style} rgba{border_indeterminate_hover_rgb};
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
