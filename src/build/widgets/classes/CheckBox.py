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
            img_margin_left=(P_dim().h9() - (P_dim().h9() * P_style().x_ico())) / 2,

            # Bordures
            border_width_all=None,
            border_width_top=p_base.WG_BORDER_WIDTH,
            border_width_bottom=p_base.WG_BORDER_WIDTH,
            border_width_right=p_base.WG_BORDER_WIDTH,
            border_width_left=p_base.WG_BORDER_WIDTH,
            border_style=p_base.WG_BORDER_STYLE,
            border_rgb=p_base.WG_BORDER_RGB,

            # Rayons
            rayon_top_right=p_base.WG_RADIUS,
            rayon_top_left=p_base.WG_RADIUS,
            rayon_bottom_right=p_base.WG_RADIUS,
            rayon_bottom_left=p_base.WG_RADIUS,

            # Curseur
            curseur=P_cur().souris_main()
    ):
        if not border_width_all is None:
            border_width_top = border_width_all
            border_width_bottom = border_width_all
            border_width_right = border_width_all
            border_width_left = border_width_all

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
                    image: url({f"{img_uncheck}{img_uncheck_rgb}.svg"});
                    }}
                    QCheckBox::indicator:hover {{
                    image: url({f"{img_uncheck_hover}{img_uncheck_hover_rgb}.svg"});
                    }}
                    QCheckBox::indicator:checked {{
                    image: url({f"{img_check}{img_check_rgb}.svg"});
                    }}
                    QCheckBox::indicator:checked:hover {{
                    image: url({f"{img_check_hover}{img_check_hover_rgb}.svg"});
                    }}

                    /* BORDURES */
                    .QCheckBox {{
                    border-top: {border_width_top}px {border_style} rgba{border_rgb};
                    border-bottom: {border_width_bottom}px {border_style} rgba{border_rgb};
                    border-right: {border_width_right}px {border_style} rgba{border_rgb};
                    border-left: {border_width_left}px {border_style} rgba{border_rgb};
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

            Fct(wg=wg, w=width, h=height).DIM()
            wg.setFont(Fct(font=font, font_size=font_size).FONT())

            wg.setCursor(Fct(cur=curseur).CUR())


class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs)
class Base_tr(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                         bg=Rgb().tr(),
                         bg_hover=Rgb().tr(),
                         bg_checked=Rgb().tr(),
                         bg_checked_hover=Rgb().tr(),
                         fg=Rgb().th3(),
                         fg_checked=Rgb().th3(),
        )
