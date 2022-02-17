from .StyleSheet import StyleSheet
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
            # Bordures checked
            border_all_checked=None,
            border_style_checked=p_base.WG_BORDER_STYLE,
            border_rgb_checked=p_base.WG_BORDER_RGB,
            border_top_checked=p_base.WG_BORDER_WIDTH, border_bottom_checked=p_base.WG_BORDER_WIDTH, border_right_checked=p_base.WG_BORDER_WIDTH, border_left_checked=p_base.WG_BORDER_WIDTH,
            # Bordures checked hover
            border_all_checked_hover=None,
            border_style_checked_hover=p_base.WG_BORDER_STYLE,
            border_rgb_checked_hover=p_base.WG_BORDER_RGB,
            border_top_checked_hover=p_base.WG_BORDER_WIDTH, border_bottom_checked_hover=p_base.WG_BORDER_WIDTH, border_right_checked_hover=p_base.WG_BORDER_WIDTH, border_left_checked_hover=p_base.WG_BORDER_WIDTH,

            # Rayons
            radius_all=None,
            radius_top_right=p_base.WG_RADIUS,
            radius_top_left=p_base.WG_RADIUS,
            radius_bottom_right=p_base.WG_RADIUS,
            radius_bottom_left=p_base.WG_RADIUS,

            # Curseur
            curseur=P_cur().souris_main()
    ):
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
        super().__init__(
            *wgs,
            bg_gen=Rgb().tr(),
            fg=Rgb().th3(),
            fg_checked=Rgb().th3(),
        )
