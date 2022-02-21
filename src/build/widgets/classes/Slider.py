from .StyleSheet import StyleSheet
from ....build import *
from ....build.widgets import p_base

class Style:
    def __init__(
            self,
            *wgs,
            width=p_base.WIDTH,
            height=p_base.HEIGHT,
            value_min=p_base.VAL_MIN,
            value_max=p_base.VAL_MAX,
            value_step=p_base.VAL_STEP,
            curseur=p_base.CUR,
            style=StyleSheet()
    ):
        for wg in wgs:
            wg.setStyleSheet(style.get())

            Fct(wg=wg, w=width, h=height).DIM()

            wg.setMinimum(value_min)
            wg.setMaximum(value_max)
            wg.setSingleStep(value_step)

            wg.setCursor(Fct(cur=curseur).CUR())


class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            style=StyleSheet(
            )
        )
class Base_rond(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            width=100,
            height=100,

            style=StyleSheet(
                bg=Rgb().th1(),
                bg_handle=Rgb().tr(),
                bg_handle_hover = Rgb().tr(),
                bg_handle_pressed = Rgb().tr(),

                height_groove=20,
                width_groove=20,
                width_handle_h=14,
                height_handle_h=5,
                width_handle_v=5,
                height_handle_v=14,

                margin_top_handle_h=-5,
                margin_bottom_handle_h=-5,
                margin_right_handle_v=-5,
                margin_left_handle_v=-5,

                border_handle_gen_all=8,
                border_handle_gen_rgb=Rgb().th2(),

                border_radius_groove_h=10,
                border_radius_groove_v=10,
                border_radius_handle_h=15,
                border_radius_handle_v=15,
            )
        )
class rgb(Style):
    def __init__(self,
                 *wgs,
                 gradient_rgb_1=None,
                 gradient_rgb_2=None,
    ):
        super().__init__(
            *wgs,
            width=100,
            height=100,

            style=StyleSheet(
                bg=Rgb().th1(),
                bg_handle=Rgb().tr(),
                bg_handle_hover = Rgb().tr(),
                bg_handle_pressed = Rgb().tr(),

                height_groove=20,
                width_groove=20,
                width_handle_h=14,
                height_handle_h=5,
                width_handle_v=5,
                height_handle_v=14,

                margin_top_handle_h=-5,
                margin_bottom_handle_h=-5,
                margin_right_handle_v=-5,
                margin_left_handle_v=-5,

                border_handle_gen_all=8,
                border_handle_gen_rgb=Rgb().th2(),

                border_radius_groove_h=10,
                border_radius_groove_v=10,
                border_radius_handle_h=15,
                border_radius_handle_v=15,
            )
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