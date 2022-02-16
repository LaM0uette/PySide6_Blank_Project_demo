from ....build import *
from ....build.widgets import p_base

class Style:
    def __init__(self,

                 # Widgets
                 *wgs,

                 # Couleurs BG
                 bg_gen=None,
                 bg=p_base.BG,
                 bg_hover=p_base.BG_HOVER,
                 bg_checked=p_base.BG_CHECKED,
                 bg_checked_hover=p_base.BG_CHECKED_HOVER,
                 # Couleurs FG
                 fg_gen=None,
                 fg=p_base.FG,
                 fg_hover=p_base.FG_HOVER,
                 fg_checked=p_base.FG_CHECKED,
                 fg_checked_hover=p_base.FG_CHECKED_HOVER,

                 # Dimensions WG
                 width=p_base.WG_WIDTH,
                 height=p_base.WG_HEIGHT,
                 spacing=10,
                 # Police
                 font=p_base.FONT,
                 font_size=p_base.FONT_SIZE,
                 # Images
                 img_uncheck=p_base.IMG_UNCHECK,
                 img_uncheck_hover=p_base.IMG_UNCHECK_HOVER,
                 img_check=p_base.IMG_CHECK,
                 img_check_hover=p_base.IMG_CHECK_HOVER,
                 # Images RGB
                 img_uncheck_rgb=p_base.IMG_UNCHECK_RGB,
                 img_uncheck_hover_rgb=p_base.IMG_UNCHECK_HOVER_RGB,
                 img_check_rgb=p_base.IMG_CHECK_RGB,
                 img_check_hover_rgb=p_base.IMG_CHECK_HOVER_RGB,
                 # Images DIM
                 img_width=p_base.IMG_WIDTH,
                 img_height=p_base.IMG_HEIGHT,
                 # Images margin
                 img_margin_top=0,
                 img_margin_bottom=0,
                 img_margin_right=0,
                 img_margin_left=(p_base.WG_HEIGHT - (p_base.WG_HEIGHT * P_style().x_ico())) / 2,

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
        style = f"""
        /* RADIOBUTTON */
        QRadioButton {{
        background-color: rgba{bg};
        color: rgb{fg};
        spacing: {spacing}px;
        }}   
        QRadioButton:hover {{
        background-color: rgba{bg_hover};
        color: rgb{fg_hover};
        }}
        QRadioButton:checked {{
        background-color: rgba{bg_checked};
        color: rgb{fg_checked};
        }}
        QRadioButton:checked:hover {{
        background-color: rgba{bg_checked_hover};
        color: rgb{fg_checked_hover};
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
        image: url({f"{img_uncheck}{img_uncheck_rgb}.svg"});
        }}
        QRadioButton::indicator:hover {{
        image: url({f"{img_uncheck_hover}{img_uncheck_hover_rgb}.svg"});
        }}
        QRadioButton::indicator:checked {{
        image: url({f"{img_check}{img_check_rgb}.svg"});
        }}
        QRadioButton::indicator:checked:hover {{
        image: url({f"{img_check_hover}{img_check_hover_rgb}.svg"});
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
                Fct(wg=wg, w=width, h=height).DIM()
                wg.setFont(Fct(font=font, font_size=font_size).FONT())

                wg.setCursor(Fct(cur=curseur).CUR())
            except: pass


class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs)
class Base_tr(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                         bg_gen=Rgb().tr(),
                         fg=Rgb().th3(),
                         fg_checked=Rgb().th3(),
        )
