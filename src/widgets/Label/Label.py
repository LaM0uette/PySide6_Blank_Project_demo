from src.build import *
from src.build.widgets import VBase

class Style:
    def __init__(
            self,
            *wgs,
            width=None,
            height=None,
            font=VBase.FONT,
            font_size=VBase.FONT_SIZE,
            align_horizontal=Align().left(),
            align_vertical=Align().v_center(),
            word_wrap=VBase.WORD_WRAP,
            curseur=VBase.CUR,

            # Couleurs BG
            bg=VBase.BG,
            bg_hover=VBase.BG_HOVER,
            # Couleurs FG
            fg=VBase.FG,
            fg_hover=VBase.FG_HOVER,

            # Positions WG
            margin=((0, )*4),
            padding=((0, )*4),

            # Bordures
            border=VBase.WG_BORDER_WIDTH,
            border_style=VBase.WG_BORDER_STYLE,
            border_rgb=VBase.WG_BORDER_RGB,
            # Bordures hover
            border_hover=VBase.WG_BORDER_WIDTH,
            border_hover_style=VBase.WG_BORDER_STYLE,
            border_hover_rgb=VBase.WG_BORDER_RGB,

            # Rayons
            radius=VBase.WG_RADIUS,

    ):
        style = f"""
                /* LABEL */
                .QLabel {{
                background-color: rgba{bg};
                color: rgba{fg};
                margin-top: {margin[0]}px;
                margin-bottom: {margin[1]}px;
                margin-right: {margin[2]}px;
                margin-left: {margin[3]}px;
                padding-top: {padding[0]}px;
                padding-bottom: {padding[1]}px;
                padding-right: {padding[2]}px;
                padding-left: {padding[3]}px;
                }}
                .QLabel:hover {{
                background-color: rgba{bg_hover};
                color: rgba{fg_hover};
                }}
        
                /* BORDURES */
                .QLabel {{
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}
                .QLabel:hover {{
                border-top: {border_hover[0]}px {border_hover_style} rgba{border_hover_rgb};
                border-bottom: {border_hover[1]}px {border_hover_style} rgba{border_hover_rgb};
                border-right: {border_hover[2]}px {border_hover_style} rgba{border_hover_rgb};
                border-left: {border_hover[3]}px {border_hover_style} rgba{border_hover_rgb};
                }}
                
                /* RAYONS */
                .QLabel {{
                border-top-right-radius: {radius[0]}px;
                border-top-left-radius: {radius[1]}px;
                border-bottom-right-radius: {radius[2]}px;
                border-bottom-left-radius: {radius[3]}px;
                }}"""

        for wg in wgs:
            wg.setStyleSheet(style)

            Fct(wg=wg, w=width, h=height).DIM()
            wg.setFont(Fct(font=font, font_size=font_size).FONT())

            wg.setAlignment(align_horizontal | align_vertical)
            wg.setWordWrap(word_wrap)

            wg.setCursor(Fct(cur=curseur).CUR())


##################
##     BASE     ##
##################
class Base_th(Style):
    def __init__(self, *wgs, font_size=VBase.FONT_SIZE):
        super().__init__(
            *wgs,
            font_size=font_size,
    )
class Base_tr(Style):
    def __init__(self, *wgs, font_size=VBase.FONT_SIZE):
        super().__init__(
            *wgs,
            font_size=font_size,
            bg=Rgb().tr(),
            bg_hover=Rgb().tr(),
            fg=Rgb().th3(),
            fg_hover=Rgb().th3(),
    )
class Titre(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            font_size=Font().h1(),
            align_horizontal=Align().h_center(),

            bg=Rgb().tr(),
            bg_hover=Rgb().tr(),
            fg=Rgb().th3(),
            fg_hover=Rgb().th3(),
    )


##################
##     DEMO     ##
##################
class Demo_th(Style):
    def __init__(self, *wgs, font_size=VBase.FONT_SIZE):
        super().__init__(
            *wgs,
            height=Dim().h9(),
            font_size=font_size,
    )
class Demo_tr(Style):
    def __init__(self, *wgs, font_size=VBase.FONT_SIZE):
        super().__init__(
            *wgs,
            height=Dim().h9(),
            font_size=font_size,
            bg=Rgb().tr(),
            bg_hover=Rgb().tr(),
            fg=Rgb().th3(),
            fg_hover=Rgb().th3(),
    )
class DemoCat(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            font_size=Font().h2(),
            align_horizontal=Align().h_center(),

            bg=Rgb().tr(),
            bg_hover=Rgb().tr(),
            fg=Rgb().th3(),
            fg_hover=Rgb().th3(),
            border=(0, StyleBase().bd(), 0, 0),
            border_hover=(0, StyleBase().bd(), 0, 0),
            border_rgb=Rgb().bn1(),
            border_hover_rgb=Rgb().bn1(),
            radius=((0,) * 4)
    )
