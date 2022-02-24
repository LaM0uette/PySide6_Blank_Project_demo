from ....build import *
from ....build.widgets import p_base

class Style:
    def __init__(
            self,
            *wgs,
            width=None,
            height=None,
            font=p_base.FONT,
            font_size=p_base.FONT_SIZE,
            align_horizontal=Align().left(),
            align_vertical=Align().v_center(),
            word_wrap=p_base.WORD_WRAP,
            curseur=p_base.CUR,

            # Couleurs BG
            bg=p_base.BG,
            bg_hover=p_base.BG_HOVER,
            # Couleurs FG
            fg=p_base.FG,
            fg_hover=p_base.FG_HOVER,

            # Bordures
            border=p_base.WG_BORDER_WIDTH,
            border_style=p_base.WG_BORDER_STYLE,
            border_rgb=p_base.WG_BORDER_RGB,
            # Bordures hover
            border_hover=p_base.WG_BORDER_WIDTH,
            border_style_hover=p_base.WG_BORDER_STYLE,
            border_rgb_hover=p_base.WG_BORDER_RGB,

            # Rayons
            radius=p_base.WG_RADIUS,

    ):
        style = f"""
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
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}
                .QLabel:hover {{
                border-top: {border_hover[0]}px {border_style_hover} rgba{border_rgb_hover};
                border-bottom: {border_hover[1]}px {border_style_hover} rgba{border_rgb_hover};
                border-right: {border_hover[2]}px {border_style_hover} rgba{border_rgb_hover};
                border-left: {border_hover[3]}px {border_style_hover} rgba{border_rgb_hover};
                }}
                
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
    def __init__(self, *wgs, font_size=p_base.FONT_SIZE):
        super().__init__(
            *wgs,
            font_size=font_size,
            style=StyleSheet(
            )
    )
class Base_tr(Style):
    def __init__(self, *wgs, font_size=p_base.FONT_SIZE):
        super().__init__(
            *wgs,
            font_size=font_size,
            style=StyleSheet(
                bg_gen=Rgb().tr(),
                fg_gen=Rgb().th3(),
            )
    )
class Titre(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            font_size=P_font().h1(),
            align_horizontal=Align().h_center(),
            style=StyleSheet(
                bg_gen=Rgb().tr(),
                fg_gen=Rgb().th3(),
            )
    )


##################
##     DEMO     ##
##################
class DemoCat(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            font_size=P_font().h2(),
            align_horizontal=Align().h_center(),
            style=StyleSheet(
                bg_gen=Rgb().tr(),
                fg_gen=Rgb().th3(),
                border_gen_bottom=P_style().bd(),
                border_gen_rgb=Rgb().bn1(),
            )
    )
