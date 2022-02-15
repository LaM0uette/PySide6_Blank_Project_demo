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
            border_all=None,
            border_top=p_base.WG_BORDER_WIDTH,
            border_bottom=p_base.WG_BORDER_WIDTH,
            border_right=p_base.WG_BORDER_WIDTH,
            border_left=p_base.WG_BORDER_WIDTH,
            border_style=p_base.WG_BORDER_STYLE,
            border_rgb=p_base.WG_BORDER_RGB,
            # Bordures hover
            border_all_hover=None,
            border_top_hover=p_base.WG_BORDER_WIDTH,
            border_bottom_hover=p_base.WG_BORDER_WIDTH,
            border_right_hover=p_base.WG_BORDER_WIDTH,
            border_left_hover=p_base.WG_BORDER_WIDTH,
            border_style_hover=p_base.WG_BORDER_STYLE,
            border_rgb_hover=p_base.WG_BORDER_RGB,
            # Bordures checked
            border_all_checked=None,
            border_top_checked=p_base.WG_BORDER_WIDTH,
            border_bottom_checked=p_base.WG_BORDER_WIDTH,
            border_right_checked=p_base.WG_BORDER_WIDTH,
            border_left_checked=p_base.WG_BORDER_WIDTH,
            border_style_checked=p_base.WG_BORDER_STYLE,
            border_rgb_checked=p_base.WG_BORDER_RGB,
            # Bordures checked hover
            border_all_checked_hover=None,
            border_top_checked_hover=p_base.WG_BORDER_WIDTH,
            border_bottom_checked_hover=p_base.WG_BORDER_WIDTH,
            border_right_checked_hover=p_base.WG_BORDER_WIDTH,
            border_left_checked_hover=p_base.WG_BORDER_WIDTH,
            border_style_checked_hover=p_base.WG_BORDER_STYLE,
            border_rgb_checked_hover=p_base.WG_BORDER_RGB,

            # Rayons
            radius_all=None,
            radius_top_right=p_base.WG_RADIUS,
            radius_top_left=p_base.WG_RADIUS,
            radius_bottom_right=p_base.WG_RADIUS,
            radius_bottom_left=p_base.WG_RADIUS,

            # Curseur
            curseur=P_cur().souris_main()
    ):
        Act().bd_rd_all(border_all, border_top, border_bottom, border_right, border_left)
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
        if not border_all_checked is None:
            border_top_checked = border_all_checked
            border_bottom_checked = border_all_checked
            border_right_checked = border_all_checked
            border_left_checked = border_all_checked
        if not border_all_checked_hover is None:
            border_top_checked_hover = border_all_checked_hover
            border_bottom_checked_hover = border_all_checked_hover
            border_right_checked_hover = border_all_checked_hover
            border_left_checked_hover = border_all_checked_hover
        if not radius_all is None:
            radius_top_right = radius_all
            radius_top_left = radius_all
            radius_bottom_right = radius_all
            radius_bottom_left = radius_all

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
                    border-top: {border_top}px {border_style} rgba{border_rgb};
                    border-bottom: {border_bottom}px {border_style} rgba{border_rgb};
                    border-right: {border_right}px {border_style} rgba{border_rgb};
                    border-left: {border_left}px {border_style} rgba{border_rgb};
                    }}
                    .QCheckBox:hover {{
                    border-top: {border_top_hover}px {border_style_hover} rgba{border_rgb_hover};
                    border-bottom: {border_bottom_hover}px {border_style_hover} rgba{border_rgb_hover};
                    border-right: {border_right_hover}px {border_style_hover} rgba{border_rgb_hover};
                    border-left: {border_left_hover}px {border_style_hover} rgba{border_rgb_hover};
                    }}
                    .QCheckBox:checked {{
                    border-top: {border_top_checked}px {border_style_checked} rgba{border_rgb_checked};
                    border-bottom: {border_bottom_checked}px {border_style_checked} rgba{border_rgb_checked};
                    border-right: {border_right_checked}px {border_style_checked} rgba{border_rgb_checked};
                    border-left: {border_left_checked}px {border_style_checked} rgba{border_rgb_checked};
                    }}
                    .QCheckBox:checked:hover {{
                    border-top: {border_top_checked_hover}px {border_style_checked_hover} rgba{border_rgb_checked_hover};
                    border-bottom: {border_bottom_checked_hover}px {border_style_checked_hover} rgba{border_rgb_checked_hover};
                    border-right: {border_right_checked_hover}px {border_style_checked_hover} rgba{border_rgb_checked_hover};
                    border-left: {border_left_checked_hover}px {border_style_checked_hover} rgba{border_rgb_checked_hover};
                    }}

                    /* RAYONS */
                    .QCheckBox {{
                    border-top-left-radius: {radius_top_left}px;
                    border-top-right-radius: {radius_top_right}px;
                    border-bottom-right-radius: {radius_bottom_right}px;
                    border-bottom-left-radius: {radius_bottom_left}px;
                    }}"""

        for wg in wgs:
            wg.setStyleSheet(style)

            Fct(wg=wg, w=width, h=height).DIM()
            wg.setFont(Fct(font=font, font_size=font_size).FONT())

            wg.setCursor(Fct(cur=curseur).CUR())


class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                         border_bottom=2,
                         border_rgb=Rgb().bn1(),
                         border_bottom_hover=2,
                         border_rgb_hover=Rgb().bn2(),
                         border_bottom_checked=4,
                         border_rgb_checked=Rgb().th2(),
                         border_bottom_checked_hover=4,
                         border_rgb_checked_hover=Rgb().bn1(),
                         )
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
