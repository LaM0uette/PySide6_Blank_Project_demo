from ....build import *
from ....build.widgets import p_base

class Style:
    def __init__(self,
                 *wgs,
                 couleur_bg=p_base._COLORS_BG,
                 couleur_bg_barre=p_base.COLORS_BG_BARRE,
                 couleur_fg=p_base._COLORS_FG,
                 dim_width=p_base.WG_WIDTH,
                 dim_height=p_base.WG_HEIGHT,
                 police=p_base.FONT,
                 police_taille=p_base.FONT_SIZE,
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
                 padding_top=0,
                 padding_bottom=0,
                 padding_right=0,
                 padding_left=0,
                 text_visible=p_base.TEXT_VISIBLE
                 ):
        style = f"""
        /* FOND */
        QProgressBar {{
        background-color: rgba{couleur_bg};
        color: rgb{couleur_fg};
        }}

        /* PROGRESS */
        QProgressBar::chunk {{
        background-color: rgba{couleur_bg_barre};
        }}

        /* BORDURES */
        .QProgressBar {{
        border-top: {bordure_width_top}px {bordure_style_top} rgba{bordure_couleur_top};
        border-bottom: {bordure_width_bottom}px {bordure_style_bottom} rgba{bordure_couleur_bottom};
        border-right: {bordure_width_right}px {bordure_style_right} rgba{bordure_couleur_right};
        border-left: {bordure_width_left}px {bordure_style_left} rgba{bordure_couleur_left};
        padding-top={padding_top}px;
        padding-bottom={padding_bottom}px;
        padding-right={padding_right}px;
        padding-left={padding_left}px;
        }}

        /* RAYONS */
        .QProgressBar {{
        border-top-left-radius: {rayon_top_left}px;
        border-top-right-radius: {rayon_top_right}px;
        border-bottom-right-radius: {rayon_bottom_right}px;
        border-bottom-left-radius: {rayon_bottom_left}px;
        }}"""

        for wg in wgs:
            wg.setStyleSheet(style)

            try:
                Fct(wg=wg, w=dim_width, h=dim_height).DIM()
                wg.setFont(Fct(font=police, font_size=police_taille).FONT())

                wg.setAlignment(P_align().c().c())
                wg.setTextVisible(text_visible)
            except: pass


class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs)
class Base_tr(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              couleur_bg=(0, 0, 0, 0),
              text_visible=False
    )
