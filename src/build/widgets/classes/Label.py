from ....build import *
from ....build.widgets import p_base

class Style:
    def __init__(
            self,

            # Widgets
            *wgs,

            # Couleurs BG
            bg_gen=None,
            bg=p_base.BG,
            bg_hover=p_base.BG_HOVER,

            # Couleurs FG
            fg_gen=None,
            fg=p_base.FG,
            fg_hover=p_base.FG_HOVER,

            # Dimensions WG
            width=None,
            height=None,

            # Police
            font=p_base.FONT,
            font_size=p_base.FONT_SIZE,

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

            # Rayons
            radius_all=None,
            radius_top_right=p_base.WG_RADIUS,
            radius_top_left=p_base.WG_RADIUS,
            radius_bottom_right=p_base.WG_RADIUS,
            radius_bottom_left=p_base.WG_RADIUS,

            # Paramètres
            align_horizontal=Align().h_center(),
            align_vertical=Align().v_center(),
            word_wrap=p_base.WORD_WRAP,

            # Curseur
            curseur=p_base.CUR
    ):
        # BG
        if not bg_gen is None:
            bg = bg_gen
            bg_hover = bg_gen
        # FG
        if not fg_gen is None:
            fg = fg_gen
            fg_hover = fg_gen
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

            if not border_gen_top is None:
                border_top = border_gen_top
                border_top_hover = border_gen_top
            if not border_gen_bottom is None:
                border_bottom = border_gen_bottom
                border_bottom_hover = border_gen_bottom
            if not border_gen_right is None:
                border_right = border_gen_right
                border_right_hover = border_gen_right
            if not border_gen_left is None:
                border_left = border_gen_left
                border_left_hover = border_gen_left
        # Bordure style
        if not border_gen_style is None:
            border_style = border_gen_style
            border_style_hover = border_gen_style
        # Bordure RGB
        if not border_gen_rgb is None:
            border_rgb = border_gen_rgb
            border_rgb_hover = border_gen_rgb
        # Radius
        if not radius_all is None:
            radius_top_right = radius_all
            radius_top_left = radius_all
            radius_bottom_right = radius_all
            radius_bottom_left = radius_all


        style = f"""
        /* LABEL */
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
        
        /* RAYONS */
        .QLabel {{
        border-top-right-radius: {radius_top_right}px;
        border-top-left-radius: {radius_top_left}px;
        border-bottom-right-radius: {radius_bottom_right}px;
        border-bottom-left-radius: {radius_bottom_left}px;
        }}"""

        for wg in wgs:
            wg.setStyleSheet(style)

            Fct(wg=wg, w=width, h=height).DIM()
            wg.setFont(Fct(font=font, font_size=font_size).FONT())

            wg.setAlignment(align_horizontal | align_vertical)
            wg.setWordWrap(word_wrap)

            wg.setCursor(Fct(cur=curseur).CUR())


class Base_th(Style):
    def __init__(self, *wgs, font_size=p_base.FONT_SIZE):
        super().__init__(
            *wgs,
            font_size=font_size,
    )
class Base_tr(Style):
    def __init__(self, *wgs, font_size=p_base.FONT_SIZE):
        super().__init__(
            *wgs,
            bg_gen=Rgb().tr(),
            fg_gen=Rgb().th3(),
            font_size=font_size,
    )


class DemoCat(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            bg_gen=Rgb().tr(),
            fg_gen=Rgb().th3(),
            font_size=P_font().h2(),
            border_gen_bottom=P_style().bd(),
            border_gen_rgb=Rgb().bn1(),
            align_horizontal=Align().h_center(),
            align_vertical=Align().v_center(),
    )
