from ....build import *
from ....build.widgets import p_base

class Style:
    def __init__(
            self,
            *wgs,
            width=p_base.WG_WIDTH,
            height=p_base.WG_HEIGHT,
            font=p_base.FONT,
            font_size=p_base.FONT_SIZE,
            curseur=P_cur().souris_main(),


    ):
        style = f"""
                QCheckBox, QRadioButton {{
                background-color: rgba{bg};
                color: rgba{fg};
                spacing: {spacing}px;
                }}
                QCheckBox:hover, QRadioButton:hover {{
                background-color: rgba{bg_hover};
                color: rgba{fg_hover};
                }}
                QCheckBox:checked, QRadioButton:checked {{
                background-color: rgba{bg_checked};
                color: rgba{fg_checked};
                }}
                QCheckBox:checked:hover, QRadioButton:checked:hover {{
                background-color: rgba{bg_checked_hover};
                color: rgba{fg_checked_hover};
                }}

                /* IMG */
                QCheckBox::indicator, QRadioButton::indicator {{
                margin-top: {img_margin_top}px;
                margin-bottom: {img_margin_bottom}px;
                margin-right: {img_margin_right}px;
                margin-left: {img_margin_left}px;
                width: {img_width}px;
                height: {img_height}px;
                }}
                QCheckBox::indicator:unchecked, QRadioButton::indicator:unchecked {{
                image: url({f"{img_uncheck}{img_uncheck_rgb}.svg"});
                }}
                QCheckBox::indicator:hover, QRadioButton::indicator:hover {{
                image: url({f"{img_uncheck_hover}{img_uncheck_hover_rgb}.svg"});
                }}
                QCheckBox::indicator:checked, QRadioButton::indicator:checked {{
                image: url({f"{img_check}{img_check_rgb}.svg"});
                }}
                QCheckBox::indicator:checked:hover, QRadioButton::indicator:checked:hover {{
                image: url({f"{img_check_hover}{img_check_hover_rgb}.svg"});
                }}

                /* BORDURES */
                .QCheckBox, .QRadioButton {{
                border-top: {border_top}px {border_style} rgba{border_rgb};
                border-bottom: {border_bottom}px {border_style} rgba{border_rgb};
                border-right: {border_right}px {border_style} rgba{border_rgb};
                border-left: {border_left}px {border_style} rgba{border_rgb};
                }}
                .QCheckBox:hover, QRadioButton:hover {{
                border-top: {border_top_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-bottom: {border_bottom_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-right: {border_right_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-left: {border_left_hover}px {border_style_hover} rgba{border_rgb_hover};
                }}
                .QCheckBox:checked, .QRadioButton:checked {{
                border-top: {border_top_checked}px {border_style_checked} rgba{border_rgb_checked};
                border-bottom: {border_bottom_checked}px {border_style_checked} rgba{border_rgb_checked};
                border-right: {border_right_checked}px {border_style_checked} rgba{border_rgb_checked};
                border-left: {border_left_checked}px {border_style_checked} rgba{border_rgb_checked};
                }}
                .QCheckBox:checked:hover, .QRadioButton:checked:hover {{
                border-top: {border_top_checked_hover}px {border_style_checked_hover} rgba{border_rgb_checked_hover};
                border-bottom: {border_bottom_checked_hover}px {border_style_checked_hover} rgba{border_rgb_checked_hover};
                border-right: {border_right_checked_hover}px {border_style_checked_hover} rgba{border_rgb_checked_hover};
                border-left: {border_left_checked_hover}px {border_style_checked_hover} rgba{border_rgb_checked_hover};
                }}
        """

        for wg in wgs:
            wg.setStyleSheet(style)

            Fct(wg=wg, w=width, h=height).DIM()
            wg.setFont(Fct(font=font, font_size=font_size).FONT())

            wg.setCursor(Fct(cur=curseur).CUR())


class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            style=StyleSheet(
                img_margin_left=(p_base.WG_HEIGHT - (p_base.WG_HEIGHT * P_style().x_ico())) / 2,
            )
        )
class Base_tr(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            style=StyleSheet(
                bg_gen=Rgb().tr(),
                fg=Rgb().th3(),
                fg_checked=Rgb().th3(),
                img_margin_left=(p_base.WG_HEIGHT - (p_base.WG_HEIGHT * P_style().x_ico())) / 2
            )
        )
