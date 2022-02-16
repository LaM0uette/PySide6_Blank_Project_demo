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

            bordure_width_top=p_base.WG_BORDER_WIDTH,
            bordure_width_bottom=p_base.WG_BORDER_WIDTH,
            bordure_width_right=p_base.WG_BORDER_WIDTH,
            bordure_width_left=p_base.WG_BORDER_WIDTH,
            bordure_style_top=p_base.WG_BORDER_STYLE,
            bordure_style_bottom=p_base.WG_BORDER_STYLE,
            bordure_style_right=p_base.WG_BORDER_STYLE,
            bordure_style_left=p_base.WG_BORDER_STYLE,
            bordure_couleur_top=p_base.WG_BORDER_RGB,
            bordure_couleur_bottom=p_base.WG_BORDER_RGB,
            bordure_couleur_right=p_base.WG_BORDER_RGB,
            bordure_couleur_left=p_base.WG_BORDER_RGB,
            rayon_top_left=p_base.WG_RADIUS,
            rayon_top_right=p_base.WG_RADIUS,
            rayon_bottom_right=p_base.WG_RADIUS,
            rayon_bottom_left=p_base.WG_RADIUS,

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
        border-top: {bordure_width_top}px {bordure_style_top} rgba{bordure_couleur_top};
        border-bottom: {bordure_width_bottom}px {bordure_style_bottom} rgba{bordure_couleur_bottom};
        border-right: {bordure_width_right}px {bordure_style_right} rgba{bordure_couleur_right};
        border-left: {bordure_width_left}px {bordure_style_left} rgba{bordure_couleur_left};
        }}

        /* RAYONS */
        .QLabel {{
        border-top-left-radius: {rayon_top_left}px;
        border-top-right-radius: {rayon_top_right}px;
        border-bottom-right-radius: {rayon_bottom_right}px;
        border-bottom-left-radius: {rayon_bottom_left}px;
        }}"""

        for wg in wgs:
            wg.setStyleSheet(style)

            Fct(wg=wg, w=width, h=height).DIM()
            wg.setFont(Fct(font=font, font_size=font_size).FONT())

            wg.setAlignment(align_horizontal | align_vertical)
            wg.setWordWrap(word_wrap)

            wg.setCursor(Fct(cur=curseur).CUR())


class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs)
class Base_tr(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            bg_gen=Rgb().tr(),
            fg_gen=Rgb().th3(),
    )

class H1(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              bg=Rgb().tr(),
              font_size=P_font().h1()
    )
class H2(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              bg=Rgb().tr(),
              font_size=P_font().h2()
    )
class H3(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              bg=Rgb().tr(),
              font_size=P_font().h3()
    )
class H4(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              bg=Rgb().tr(),
              font_size=P_font().h4()
    )
class H5(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              bg=Rgb().tr(),
              font_size=P_font().h5()
    )


class DemoCat(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            bg_gen=Rgb().tr(),
            fg_gen=Rgb().th3(),
            font_size=P_font().h2(),
            bordure_width_bottom=P_style().bd(),
            bordure_couleur_bottom=P_rgb().bn1()+(255, ),
    )
