from ....build import *
from ....build.widgets import p_base

class Style:
    def __init__(
            self,
            *wgs,
            colors_bg=p_base.COLORS_BG,
            colors_bg_hover=p_base.COLORS_BG_HOVER,
            colors_bg_checked=p_base.COLORS_BG_CHECKED,
            colors_bg_checked_hover=p_base.COLORS_BG_CHECKED_HOVER,
            colors_fg=p_base.COLORS_FG,
            colors_fg_hover=p_base.COLORS_FG_HOVER,
            colors_fg_checked=p_base.COLORS_FG_CHECKED,
            colors_fg_checked_hover=p_base.COLORS_FG_CHECKED_HOVER,
            dim_width=p_base.DIM_WG_WIDTH,
            dim_height=p_base.DIM_WG_HEIGHT,
            spacing=p_base.SPACING,
            police=p_base.FONT,
            police_taille=p_base.FONT_SIZE,
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
            bordure_width_top=p_base.BD_WIDTH,
            bordure_width_bottom=p_base.BD_WIDTH,
            bordure_width_right=p_base.BD_WIDTH,
            bordure_width_left=p_base.BD_WIDTH,
            bordure_style_top=p_base.BD_STYLE,
            bordure_style_bottom=p_base.BD_STYLE,
            bordure_style_right=p_base.BD_STYLE,
            bordure_style_left=p_base.BD_STYLE,
            bordure_colors_top=p_base.BD_COULEUR,
            bordure_colors_bottom=p_base.BD_COULEUR,
            bordure_colors_right=p_base.BD_COULEUR,
            bordure_colors_left=p_base.BD_COULEUR,
            rayon_top_left=p_base.RD_WG,
            rayon_top_right=p_base.RD_WG,
            rayon_bottom_right=p_base.RD_WG,
            rayon_bottom_left=p_base.RD_WG,
            curseur=p_base.CUR
    ):
        style = f"""
                    /* CHECKBOX */
                    QCheckBox {{
                    background-color: rgba{colors_bg};
                    color: rgba{colors_fg};
                    spacing: {spacing}px;
                    }}
                    QCheckBox:hover {{
                    background-color: rgba{colors_bg_hover};
                    color: rgba{colors_fg_hover};
                    }}
                    QCheckBox:checked {{
                    background-color: rgba{colors_bg_checked};
                    color: rgba{colors_fg_checked};
                    }}
                    QCheckBox:checked:hover {{
                    background-color: rgba{colors_bg_checked_hover};
                    color: rgba{colors_fg_checked_hover};
                    }}

                    /* IMG */
                    QCheckBox::indicator {{
                    margin-top: {img_margin_top}px;
                    margin-bottom: {img_margin_bottom}px;
                    margin-right: {img_margin_right}px;
                    margin-left: {img_margin_left}px;
                    width: {img_width}px;
                    height: {img_height}px;
                    }}
                    QCheckBox::indicator:unchecked {{
                    image: url({f"{img_uncheck}{tm_uncheck}.svg"});
                    }}
                    QCheckBox::indicator:hover {{
                    image: url({f"{img_hover}{tm_hover}.svg"});
                    }}
                    QCheckBox::indicator:checked {{
                    image: url({f"{img_check}{tm_check}.svg"});
                    }}
                    QCheckBox::indicator:checked:hover {{
                    image: url({f"{img_check_hover}{tm_check_hover}.svg"});
                    }}

                    /* BORDURES */
                    .QCheckBox {{
                    border-top: {bordure_width_top}px {bordure_style_top} rgba{bordure_colors_top};
                    border-bottom: {bordure_width_bottom}px {bordure_style_bottom} rgba{bordure_colors_bottom};
                    border-right: {bordure_width_right}px {bordure_style_right} rgba{bordure_colors_right};
                    border-left: {bordure_width_left}px {bordure_style_left} rgba{bordure_colors_left};
                    }}

                    /* RAYONS */
                    .QCheckBox {{
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


class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs)
class Base_tr(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              colors_bg=(0, 0, 0, 0),
              colors_bg_hover=(0, 0, 0, 0),
              colors_bg_checked=(0, 0, 0, 0),
              colors_bg_checked_hover=(0, 0, 0, 0),
              colors_fg=Rgb().th3(),
              colors_fg_checked=Rgb().th3(),
        )
