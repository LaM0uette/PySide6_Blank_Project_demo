from ....build import *
from ....build.widgets import p_base

class Style:
    def __init__(
            self,

            # Widgets
            *wgs,

            # Couleurs BG
            bg=p_base.BG,
            bg_hover=p_base.BG_HOVER,
            bg_checked=p_base.BG_CHECKED,
            bg_checked_hover=p_base.BG_CHECKED_HOVER,

            # Couleurs FG
            fg=p_base.FG,
            fg_hover=p_base.FG_HOVER,
            fg_checked=p_base.FG_CHECKED,
            fg_checked_hover=p_base.FG_CHECKED_HOVER,

            # Dimensions WG
            width=p_base.WG_WIDTH,
            height=p_base.WG_HEIGHT,

            spacing=10,
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
            curseur=P_cur().souris_main()
    ):
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
                Fct(wg=wg, w=width, h=height).DIM()
                wg.setFont(Fct(font=police, font_size=police_taille).FONT())

                wg.setCursor(Fct(cur=curseur).CUR())
            except: pass


class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs)
class Base_tr(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                         bg=(0, 0, 0, 0),
                         bg_hover=(0, 0, 0, 0),
                         bg_checked=(0, 0, 0, 0),
                         bg_checked_hover=(0, 0, 0, 0),
                         fg=Rgb().th3(),
                         fg_checked=Rgb().th3(),
                         )
