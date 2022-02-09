from ....build import *
from .. import p_base


class wg:
    def __init__(self,
                 *wgs,
                 couleur_bg=p_base.COULEUR_BG,
                 couleur_bg_hover=p_base.COULEUR_BG_HOVER,
                 couleur_bg_checked=p_base.COULEUR_BG_CHECKED,
                 couleur_bg_checked_hover=p_base.COULEUR_BG_CHECKED_HOVER,
                 couleur_fg=p_base.COULEUR_FG,
                 couleur_fg_hover=p_base.COULEUR_FG_HOVER,
                 couleur_fg_checked=p_base.COULEUR_FG_CHECKED,
                 couleur_fg_checked_hover=p_base.COULEUR_FG_CHECKED_HOVER,

                 img_uncheck=p_base.IMG_UNCHECK,
                 tm_uncheck=p_base.TM_UNCHECK,
                 img_hover=p_base.IMG_HOVER,
                 tm_hover=p_base.TM_HOVER,
                 img_check=p_base.IMG_CHECK,
                 tm_check=p_base.TM_CHECK,
                 img_check_hover=p_base.IMG_CHECK_HOVER,
                 tm_check_hover=p_base.TM_CHECK_HOVER,
                 img_width=p_base.IMG_WIDTH,
                 img_height=p_base.IMG_HEIGHT,
                 img_margin_top=0,
                 img_margin_bottom=0,
                 img_margin_right=0,
                 img_margin_left=(P_dim().h9() - (P_dim().h9() * P_style().x_ico())) / 2,

                 dim_width=p_base.DIM_WG_WIDTH,
                 dim_height=p_base.DIM_WG_HEIGHT,
                 spacing=p_base.SPACING,

                 police=p_base.FONT,
                 police_taille=p_base.FONT_SIZE,

                 bordure_width_top=p_base.BD_WIDTH,
                 bordure_width_bottom=p_base.BD_WIDTH,
                 bordure_width_right=p_base.BD_WIDTH,
                 bordure_width_left=p_base.BD_WIDTH,
                 bordure_style_top=p_base.BD_STYLE,
                 bordure_style_bottom=p_base.BD_STYLE,
                 bordure_style_right=p_base.BD_STYLE,
                 bordure_style_left=p_base.BD_STYLE,
                 bordure_couleur_top=p_base.BD_COULEUR,
                 bordure_couleur_bottom=p_base.BD_COULEUR,
                 bordure_couleur_right=p_base.BD_COULEUR,
                 bordure_couleur_left=p_base.BD_COULEUR,
                 rayon_top_left=p_base.RD_WG,
                 rayon_top_right=p_base.RD_WG,
                 rayon_bottom_right=p_base.RD_WG,
                 rayon_bottom_left=p_base.RD_WG,

                 curseur=p_base.CUR
    ):
        style = f"""
        /* RADIOBUTTON */
        QRadioButton {{
        background-color: rgba{couleur_bg};
        color: rgb{couleur_fg};
        spacing: {spacing}px;
        }}   
        QRadioButton:hover {{
        background-color: rgba{couleur_bg_hover};
        color: rgb{couleur_fg_hover};
        }}
        QRadioButton:checked {{
        background-color: rgba{couleur_bg_checked};
        color: rgb{couleur_fg_checked};
        }}
        QRadioButton:checked:hover {{
        background-color: rgba{couleur_bg_checked_hover};
        color: rgb{couleur_fg_checked_hover};
        }}

        /* IMG */
        QRadioButton::indicator {{
        margin-top: {img_margin_top}px;
        margin-bottom: {img_margin_bottom}px;
        margin-right: {img_margin_right}px;
        margin-left: {img_margin_left}px;
        width: {img_width}px;
        height: {img_height}px;
        }}
        QRadioButton::indicator:unchecked {{
        image: url({f"{img_uncheck}{tm_uncheck}.svg"});
        }}
        QRadioButton::indicator:hover {{
        image: url({f"{img_hover}{tm_hover}.svg"});
        }}
        QRadioButton::indicator:checked {{
        image: url({f"{img_check}{tm_check}.svg"});
        }}
        QRadioButton::indicator:checked:hover {{
        image: url({f"{img_check_hover}{tm_check_hover}.svg"});
        }}

        /* BORDURES */
        .QRadioButton {{
        border-top: {bordure_width_top}px {bordure_style_top} rgba{bordure_couleur_top};
        border-bottom: {bordure_width_bottom}px {bordure_style_bottom} rgba{bordure_couleur_bottom};
        border-right: {bordure_width_right}px {bordure_style_right} rgba{bordure_couleur_right};
        border-left: {bordure_width_left}px {bordure_style_left} rgba{bordure_couleur_left};
        }}
        
        /* RAYONS */
        .QRadioButton {{
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

                wg.setCursor(Fct(cur=curseur).CUR())
            except: pass
