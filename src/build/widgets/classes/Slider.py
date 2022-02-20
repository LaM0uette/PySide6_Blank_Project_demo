from .StyleSheet import StyleSheet
from ....build import *
from ....build.widgets import p_base

class Style:
    def __init__(self,
                 *wgs,
                 couleur_bg=(0, 0, 0, 0),
                 couleur_bg_barre=p_base.COLORS_BG_BARRE,
                 couleur_bg_barre_hover=p_base.COLORS_BG_BARRE_HOVER,
                 couleur_bg_barre_pressed=p_base.COLORS_BG_BARRE_PRESSED,
                 couleur_bg_cur=p_base.COLORS_BG_CUR,
                 couleur_bg_cur_hover=p_base.COLORS_BG_CUR_HOVER,
                 couleur_bg_cur_pressed=p_base.COLORS_BG_CUR_PRESSED,
                 couleur_degrade_1=p_base._COLORS_BG,
                 couleur_degrade_2=p_base._COLORS_BG,
                 dim_width=p_base.WIDTH,
                 dim_height=p_base.HEIGHT,
                 hauteur_barre_h=10,
                 hauteur_main_h=20,
                 largeur_main_h=20,
                 largeur_barre_v=10,
                 hauteur_main_v=20,
                 largeur_main_v=20,
                 margin_top=-10,
                 margin_bottom=-10,
                 margin_right=-10,
                 margin_left=-10,
                 valeur_min=p_base.VAL_MIN,
                 valeur_max=p_base.VAL_MAX,
                 valeur_pas=p_base.VAL_PAS,
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
                 curseur=p_base.CUR
    ):
        for wg in wgs:
            wg.setStyleSheet(style)

            try:
                Fct(wg=wg, w=dim_width, h=dim_height).DIM()

                wg.setMinimum(valeur_min)
                wg.setMaximum(valeur_max)
                wg.setSingleStep(valeur_pas)

                wg.setCursor(Fct(cur=curseur).CUR())
            except: pass


class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs)
class Base_rond(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs)
class rgb(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              valeur_max=255
    )

"""
"rgb": 
/* SLIDER  */
QSlider {{
background-color: rgba(0, 0, 0, 0);
margin: 0px
}}

/* BARRE_H */
QSlider::groove:horizontal {{
border-radius: 10px;
height: 20px;
margin: 0px;
background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba{gradient_colors.get("c1")}, stop:1 rgba{gradient_colors.get("c2")});
}}

/* CURSEUR_H */
QSlider::handle:horizontal {{
border: none;
height: 5px;
width: 14px;
margin: -5px 0px;
border-radius: 15px;
border: 8px solid rgb{colors.get("c1")};
}}

/* BARRE_V */
QSlider::groove:vertical {{
border-radius: 10px;
width: 20px;
margin: 0px;
background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba{gradient_colors.get("c1")}, stop:1 rgba{gradient_colors.get("c2")});
}}

QSlider::groove:vertical:hover {{
background-color: rgb{colors.get("c3")};
}}

/* CURSEUR_V */
QSlider::handle:vertical {{
border: none;
height: 14px;
width: 5px;
margin: 0px -5px;
border-radius: 15px;
border: 8px solid rgb{colors.get("c1")};
}}
"""