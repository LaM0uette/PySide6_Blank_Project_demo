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

            # Paramètres
            auto_exclusive=False,
            focus_policy=vb_wg.FOCUS_POLICY,
            triple_state=False,

            # Curseur
            cursor=vb_wg.CUR_MAIN,

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
            img_margin=(0,) * 4,

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
        *Border_Style: str() : dashed | dot-dash | dot-dot-dash | dotted | double | groove | inset | outset | ridge | solid | none \n
        *Cur: list() : Cur().%nomCurseur() \n
        *Dim: int() : Dim().%nomDim() \n
        *FocusPolicy: QtCore.Qt : FocusPolicy().%nomFocus \n
        *Font: int() : Font().%nomFont() \n
        *Img: str() : Img().%nomImage() \n
        *Img_rgb: str() : th1 | th2 | th3 | bn1 | bn2 \n
        *RgbBox: tuple() : RgbBox().%nomCouleur() \n
        *Tuple: tuple() : (int(), int(), int(), int()) == (Top, Bottom, Right, Left) | (TopRight, TopLeft, BottomRight, BottomLeft) \n

        :param wgs: Widgets séparés par ","
        :param width: *Dim
        :param height: *Dim
        :param font: str()
        :param font_size: *Font
        :param auto_exclusive: bool()
        :param focus_policy: *FocusPolicy
        :param triple_state: bool()
        :param cursor: *Cur
        :param bg: *RgbBox
        :param bg_hover: *RgbBox
        :param bg_checked: *RgbBox
        :param bg_checked_hover: *RgbBox
        :param bg_indeterminate: *RgbBox
        :param bg_indeterminate_hover: *RgbBox
        :param fg: *RgbBox
        :param fg_hover: *RgbBox
        :param fg_checked: *RgbBox
        :param fg_checked_hover: *RgbBox
        :param fg_indeterminate: *RgbBox
        :param fg_indeterminate_hover: *RgbBox
        :param spacing: int()
        :param img_uncheck: *Img
        :param img_uncheck_hover: *Img
        :param img_check: *Img
        :param img_check_hover: *Img
        :param img_indeterminate: *Img
        :param img_indeterminate_hover: *Img
        :param img_uncheck_rgb: *Img_rgb
        :param img_uncheck_hover_rgb: *Img_rgb
        :param img_check_rgb: *Img_rgb
        :param img_check_hover_rgb: *Img_rgb
        :param img_indeterminate_rgb: *Img_rgb
        :param img_indeterminate_hover_rgb: *Img_rgb
        :param img_width: *Dim
        :param img_height: *Dim
        :param img_margin: *Tuple
        :param border: *Tuple
        :param border_style: *Border_Style
        :param border_rgb: *RgbBox
        :param border_hover: *Tuple
        :param border_hover_style: *Border_Style
        :param border_hover_rgb: *RgbBox
        :param border_checked: *Tuple
        :param border_checked_style: *Border_Style
        :param border_checked_rgb: *RgbBox
        :param border_checked_hover: *Tuple
        :param border_checked_hover_style: *Border_Style
        :param border_checked_hover_rgb: *RgbBox
        :param border_indeterminate: *Tuple
        :param border_indeterminate_style: *Border_Style
        :param border_indeterminate_rgb: *RgbBox
        :param border_indeterminate_hover: *Tuple
        :param border_indeterminate_hover_style: *Border_Style
        :param border_indeterminate_hover_rgb: *RgbBox
        :param radius: *Tuple
        """

        self.wgs = *wgs,
        self.width = width
        self.height = height
        self.font = font
        self.font_size = font_size
        self.auto_exclusive = auto_exclusive
        self.focus_policy = focus_policy
        self.triple_state = triple_state
        self.cursor = cursor
        self.bg = bg
        self.bg_hover = bg_hover
        self.bg_checked = bg_checked
        self.bg_checked_hover = bg_checked_hover
        self.bg_indeterminate = bg_indeterminate
        self.bg_indeterminate_hover = bg_indeterminate_hover
        self.fg = fg
        self.fg_hover = fg_hover
        self.fg_checked = fg_checked
        self.fg_checked_hover = fg_checked_hover
        self.fg_indeterminate = fg_indeterminate
        self.fg_indeterminate_hover = fg_indeterminate_hover
        self.spacing = spacing
        self.img_uncheck = img_uncheck
        self.img_uncheck_hover = img_uncheck_hover
        self.img_check = img_check
        self.img_check_hover = img_check_hover
        self.img_indeterminate = img_indeterminate
        self.img_indeterminate_hover = img_indeterminate_hover
        self.img_uncheck_rgb = img_uncheck_rgb
        self.img_uncheck_hover_rgb = img_uncheck_hover_rgb
        self.img_check_rgb = img_check_rgb
        self.img_check_hover_rgb = img_check_hover_rgb
        self.img_indeterminate_rgb = img_indeterminate_rgb
        self.img_indeterminate_hover_rgb = img_indeterminate_hover_rgb
        self.img_width = img_width
        self.img_height = img_height
        self.img_margin = img_margin
        self.border = border
        self.border_style = border_style
        self.border_rgb = border_rgb
        self.border_hover = border_hover
        self.border_hover_style = border_hover_style
        self.border_hover_rgb = border_hover_rgb
        self.border_checked = border_checked
        self.border_checked_style = border_checked_style
        self.border_checked_rgb = border_checked_rgb
        self.border_checked_hover = border_checked_hover
        self.border_checked_hover_style = border_checked_hover_style
        self.border_checked_hover_rgb = border_checked_hover_rgb
        self.border_indeterminate = border_indeterminate
        self.border_indeterminate_style = border_indeterminate_style
        self.border_indeterminate_rgb = border_indeterminate_rgb
        self.border_indeterminate_hover = border_indeterminate_hover
        self.border_indeterminate_hover_style = border_indeterminate_hover_style
        self.border_indeterminate_hover_rgb = border_indeterminate_hover_rgb
        self.radius = radius

        self.style = f"""
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

            # Paramètres
            wg.setAutoExclusive(auto_exclusive)
            wg.setFocusPolicy(focus_policy)
            wg.setTristate(triple_state)

            # Curseur
            wg.setCursor(Functions().SET_CURSOR(cursor))

            # Style
            wg.setStyleSheet(self.style)

    def test(self):
        style = f"""
                        /* CHECKBOX */
                        QCheckBox {{
                        background-color: rgba{self.bg};
                        color: rgba{self.fg};
                        spacing: {self.spacing}px;
                        }}
                        QCheckBox:hover {{
                        background-color: rgba{self.bg_hover};
                        color: rgba{self.fg_hover};
                        }}
                        QCheckBox:checked {{
                        background-color: rgba{self.bg_checked};
                        color: rgba{self.fg_checked};
                        }}
                        QCheckBox:checked:hover {{
                        background-color: rgba{self.bg_checked_hover};
                        color: rgba{self.fg_checked_hover};
                        }}
                        QCheckBox:indeterminate {{
                        background-color: rgba{self.bg_indeterminate};
                        color: rgba{self.fg_indeterminate};
                        }}
                        QCheckBox:indeterminate:hover {{
                        background-color: rgba{self.bg_indeterminate_hover};
                        color: rgba{self.fg_indeterminate_hover};
                        }}

                        /* IMG */
                        QCheckBox::indicator {{
                        margin-top: {self.img_margin[0]}px;
                        margin-bottom: {self.img_margin[1]}px;
                        margin-right: {self.img_margin[2]}px;
                        margin-left: {self.img_margin[3]}px;
                        width: {self.img_width}px;
                        height: {self.img_height}px;
                        }}
                        QCheckBox::indicator:unchecked {{
                        image: url({f"{self.img_uncheck}{self.img_uncheck_rgb}.svg"});
                        }}
                        QCheckBox::indicator:hover {{
                        image: url({f"{self.img_uncheck_hover}{self.img_uncheck_hover_rgb}.svg"});
                        }}
                        QCheckBox::indicator:checked {{
                        image: url({f"{self.img_check}{self.img_check_rgb}.svg"});
                        }}
                        QCheckBox::indicator:checked:hover {{
                        image: url({f"{self.img_check_hover}{self.img_check_hover_rgb}.svg"});
                        }}
                        QCheckBox::indicator::indeterminate {{
                        image: url({f"{self.img_indeterminate}{self.img_indeterminate_rgb}.svg"});
                        }}
                        QCheckBox::indicator::indeterminate:hover {{
                        image: url({f"{self.img_indeterminate_hover}{self.img_indeterminate_hover_rgb}.svg"});
                        }}

                        /* BORDURES */
                        .QCheckBox {{
                        border-top: {self.border[0]}px {self.border_style} rgba{self.border_rgb};
                        border-bottom: {self.border[1]}px {self.border_style} rgba{self.border_rgb};
                        border-right: {self.border[2]}px {self.border_style} rgba{self.border_rgb};
                        border-left: {self.border[3]}px {self.border_style} rgba{self.border_rgb};
                        }}
                        .QCheckBox:hover {{
                        border-top: {self.border_hover[0]}px {self.border_hover_style} rgba{self.border_hover_rgb};
                        border-bottom: {self.border_hover[1]}px {self.border_hover_style} rgba{self.border_hover_rgb};
                        border-right: {self.border_hover[2]}px {self.border_hover_style} rgba{self.border_hover_rgb};
                        border-left: {self.border_hover[3]}px {self.border_hover_style} rgba{self.border_hover_rgb};
                        }}
                        .QCheckBox:checked {{
                        border-top: {self.border_checked[0]}px {self.border_checked_style} rgba{self.border_checked_rgb};
                        border-bottom: {self.border_checked[1]}px {self.border_checked_style} rgba{self.border_checked_rgb};
                        border-right: {self.border_checked[2]}px {self.border_checked_style} rgba{self.border_checked_rgb};
                        border-left: {self.border_checked[3]}px {self.border_checked_style} rgba{self.border_checked_rgb};
                        }}
                        .QCheckBox:checked:hover {{
                        border-top: {self.border_checked_hover[0]}px {self.border_checked_hover_style} rgba{self.border_checked_hover_rgb};
                        border-bottom: {self.border_checked_hover[1]}px {self.border_checked_hover_style} rgba{self.border_checked_hover_rgb};
                        border-right: {self.border_checked_hover[2]}px {self.border_checked_hover_style} rgba{self.border_checked_hover_rgb};
                        border-left: {self.border_checked_hover[3]}px {self.border_checked_hover_style} rgba{self.border_checked_hover_rgb};
                        }}
                        .QCheckBox:indeterminate {{
                        border-top: {self.border_indeterminate[0]}px {self.border_indeterminate_style} rgba{self.border_indeterminate_rgb};
                        border-bottom: {self.border_indeterminate[1]}px {self.border_indeterminate_style} rgba{self.border_indeterminate_rgb};
                        border-right: {self.border_indeterminate[2]}px {self.border_indeterminate_style} rgba{self.border_indeterminate_rgb};
                        border-left: {self.border_indeterminate[3]}px {self.border_indeterminate_style} rgba{self.border_indeterminate_rgb};
                        }}
                        .QCheckBox:indeterminate:hover {{
                        border-top: {self.border_indeterminate_hover[0]}px {self.border_indeterminate_hover_style} rgba{self.border_indeterminate_hover_rgb};
                        border-bottom: {self.border_indeterminate_hover[1]}px {self.border_indeterminate_hover_style} rgba{self.border_indeterminate_hover_rgb};
                        border-right: {self.border_indeterminate_hover[2]}px {self.border_indeterminate_hover_style} rgba{self.border_indeterminate_hover_rgb};
                        border-left: {self.border_indeterminate_hover[3]}px {self.border_indeterminate_hover_style} rgba{self.border_indeterminate_hover_rgb};
                        }}

                        /* RAYONS */
                        .QCheckBox {{
                        border-top-right-radius: {self.radius[0]}px;
                        border-top-left-radius: {self.radius[1]}px;
                        border-bottom-right-radius: {self.radius[2]}px;
                        border-bottom-left-radius: {self.radius[3]}px;
                        }}"""


        for wg in self.wgs:
            # Dimensions
            Functions().SET_DIM(wg, width=self.width, height=self.height)

            # Police
            Functions().SET_FONT(wg, font=self.font, font_size=self.font_size)

            # Paramètres
            wg.setAutoExclusive(self.auto_exclusive)
            wg.setFocusPolicy(self.focus_policy)
            wg.setTristate(self.triple_state)

            # Curseur
            wg.setCursor(Functions().SET_CURSOR(self.cursor))

            # Style
            wg.setStyleSheet(style)
