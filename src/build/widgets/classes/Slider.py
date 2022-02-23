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

            # Couleurs BG
            bg_gen=None,
            bg=p_base.BG,
            bg_groove=p_base.BG_GROOVE,
            bg_groove_hover=p_base.BG_GROOVE_HOVER,
            bg_groove_pressed=p_base.BG_GROOVE_PRESSED,
            bg_handle=p_base.BG_HANDLE,
            bg_handle_hover=p_base.BG_HANDLE_HOVER,
            bg_handle_pressed=p_base.BG_HANDLE_PRESSED,
            # couleurs autres
            gradient_rgb_1=None,
            gradient_rgb_2=None,

            # Dimensions WG
            width_groove=P_dim().h9(),
            height_groove=P_dim().h9(),
            width_handle_h=P_dim().h9(),
            height_handle_h=P_dim().h9(),
            width_handle_v=P_dim().h9(),
            height_handle_v=P_dim().h9(),

            # Positions WG
            margin_top_handle_h=0,
            margin_bottom_handle_h=0,
            margin_right_handle_h=0,
            margin_left_handle_h=0,
            margin_top_handle_v=0,
            margin_bottom_handle_v=0,
            margin_right_handle_v=0,
            margin_left_handle_v=0,

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
            # Bordures slider
            border_handle_gen_all=None,
            border_handle_gen_style=None,
            border_handle_gen_rgb=None,
            # Bordures slider h
            border_handle_h_all=None,
            border_handle_h_style=p_base.WG_BORDER_STYLE,
            border_handle_h_rgb=p_base.WG_BORDER_RGB,
            border_handle_h_top=p_base.WG_BORDER_WIDTH, border_handle_h_bottom=p_base.WG_BORDER_WIDTH, border_handle_h_right=p_base.WG_BORDER_WIDTH, border_handle_h_left=p_base.WG_BORDER_WIDTH,
            # Bordures slider v
            border_handle_v_all=None,
            border_handle_v_style=p_base.WG_BORDER_STYLE,
            border_handle_v_rgb=p_base.WG_BORDER_RGB,
            border_handle_v_top=p_base.WG_BORDER_WIDTH, border_handle_v_bottom=p_base.WG_BORDER_WIDTH, border_handle_v_right=p_base.WG_BORDER_WIDTH, border_handle_v_left=p_base.WG_BORDER_WIDTH,

            # Rayons slider
            border_radius_groove_h=0,
            border_radius_groove_v=0,
            border_radius_handle_h=0,
            border_radius_handle_v=0,

            # Rayons
            radius_all=None,
            radius_top_right=p_base.WG_RADIUS,
            radius_top_left=p_base.WG_RADIUS,
            radius_bottom_right=p_base.WG_RADIUS,
            radius_bottom_left=p_base.WG_RADIUS,
    ):
        try:
            # BG / FG
            if not bg_gen is None:
                bg = bg_gen
                bg_hover = bg_gen
                bg_pressed = bg_gen

            if gradient_rgb_1 is None or gradient_rgb_2 is None:
                gradient_rgb_1 = bg_groove
                gradient_rgb_2 = bg_groove

            # Bordure GEN
            if not border_gen_all is None:
                border_top = border_gen_all
                border_bottom = border_gen_all
                border_right = border_gen_all
                border_left = border_gen_all
                border_top_hover = border_gen_all
                border_bottom_hover = border_gen_all
                border_right_hover = border_gen_all
                border_left_hover = border_gen_all
            elif border_gen_all is None:
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

                if not border_gen_top is None:
                    border_top = border_gen_top
                    border_top_hover = border_gen_top
                if not border_gen_bottom is None:
                    border_bottom = border_gen_bottom
                    border_bottom_hover = border_gen_bottom
                if not border_gen_right is None:
                    border_right = border_gen_right
                    border_right_hover = border_gen_right
                if not border_gen_left is None:
                    border_left = border_gen_left
                    border_left_hover = border_gen_left
            if not border_gen_style is None:
                border_style = border_gen_style
                border_style_hover = border_gen_style
            if not border_gen_rgb is None:
                border_rgb = border_gen_rgb
                border_rgb_hover = border_gen_rgb


            # Bordure handle
            if not border_handle_gen_all is None:
                border_handle_h_top = border_handle_gen_all
                border_handle_h_bottom = border_handle_gen_all
                border_handle_h_right = border_handle_gen_all
                border_handle_h_left = border_handle_gen_all
                border_handle_v_top = border_handle_gen_all
                border_handle_v_bottom = border_handle_gen_all
                border_handle_v_right = border_handle_gen_all
                border_handle_v_left = border_handle_gen_all
            elif border_handle_gen_all is None:
                if not border_handle_h_all is None:
                    border_handle_h_top = border_handle_h_all
                    border_handle_h_bottom = border_handle_h_all
                    border_handle_h_right = border_handle_h_all
                    border_handle_h_left = border_handle_h_all
                if not border_handle_v_all is None:
                    border_handle_v_top = border_handle_v_all
                    border_handle_v_bottom = border_handle_v_all
                    border_handle_v_right = border_handle_v_all
                    border_handle_v_left = border_handle_v_all
            if not border_handle_gen_style is None:
                border_handle_h_style = border_handle_gen_style
                border_handle_v_style = border_handle_gen_style
            if not border_handle_gen_rgb is None:
                border_handle_h_rgb = border_handle_gen_rgb
                border_handle_v_rgb = border_handle_gen_rgb

            # Radius
            if not radius_all is None:
                radius_top_right = radius_all
                radius_top_left = radius_all
                radius_bottom_right = radius_all
                radius_bottom_left = radius_all
        except: pass

        style = f"""
                /* SLIDER  */
                QSlider {{
                background-color: rgba{bg};
                }}
        
                /* BARRE_H */
                QSlider::groove:horizontal {{
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba{gradient_rgb_1}, stop:1 rgba{gradient_rgb_2});
                height: {height_groove}px;
                border-radius: {border_radius_groove_h}px;
                }}
                QSlider::groove:horizontal:hover {{
                background-color: rgba{bg_groove_hover};
                }}
                QSlider::groove:horizontal:pressed {{
                background-color: rgba{bg_groove_pressed};
                }}

                /* CURSEUR_H */
                QSlider::handle:horizontal {{
                background-color: rgba{bg_handle};
                width: {width_handle_h}px;
                height: {height_handle_h}px;
                border-radius: {border_radius_handle_h}px;
                margin-top: {margin_top_handle_h}px;
                margin-bottom: {margin_bottom_handle_h}px;
                margin-right: {margin_right_handle_h}px;
                margin-left: {margin_left_handle_h}px;
                border-top: {border_handle_h_top}px {border_handle_h_style} rgba{border_handle_h_rgb};
                border-bottom: {border_handle_h_bottom}px {border_handle_h_style} rgba{border_handle_h_rgb};
                border-right: {border_handle_h_right}px {border_handle_h_style} rgba{border_handle_h_rgb};
                border-left: {border_handle_h_left}px {border_handle_h_style} rgba{border_handle_h_rgb};
                }}
                QSlider::handle:horizontal:hover {{
                background-color: rgba{bg_handle_hover};
                }}
                QSlider::handle:horizontal:pressed {{
                background-color: rgba{bg_handle_pressed};
                }}
        
                /* BARRE_V */
                QSlider::groove:vertical {{
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba{gradient_rgb_1}, stop:1 rgba{gradient_rgb_2});
                width: {width_groove}px;
                border-radius: {border_radius_groove_v}px;
                }}
                QSlider::groove:vertical:hover {{
                background-color: rgba{bg_groove_hover};
                }}
                QSlider::groove:vertical:pressed {{
                background-color: rgba{bg_groove_pressed};
                }}
        
                /* CURSEUR_V */
                QSlider::handle:vertical {{
                background-color: rgba{bg_handle};
                width: {width_handle_v}px;
                height: {height_handle_v}px;
                border-radius: {border_radius_handle_v}px;
                margin-top: {margin_top_handle_v}px;
                margin-bottom: {margin_bottom_handle_v}px;
                margin-right: {margin_right_handle_v}px;
                margin-left: {margin_left_handle_v}px;
                border-top: {border_handle_v_top}px {border_handle_v_style} rgba{border_handle_v_rgb};
                border-bottom: {border_handle_v_bottom}px {border_handle_v_style} rgba{border_handle_v_rgb};
                border-right: {border_handle_v_right}px {border_handle_v_style} rgba{border_handle_v_rgb};
                border-left: {border_handle_v_left}px {border_handle_v_style} rgba{border_handle_v_rgb};
                }}
                QSlider::handle:vertical:hover {{
                background-color: rgba{bg_handle_hover};
                }}
                QSlider::handle:vertical:pressed {{
                background-color: rgba{bg_handle_pressed};
                }}
        
                /* BORDURES */
                .QSlider {{
                border-top: {border_top}px {border_style} rgba{border_rgb};
                border-bottom: {border_bottom}px {border_style} rgba{border_rgb};
                border-right: {border_right}px {border_style} rgba{border_rgb};
                border-left: {border_left}px {border_style} rgba{border_rgb};
                }}
                .QSlider:hover {{
                border-top: {border_top_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-bottom: {border_bottom_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-right: {border_right_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-left: {border_left_hover}px {border_style_hover} rgba{border_rgb_hover};
                }}
                
                .QSlider {{
                border-top-right-radius: {radius_top_right}px;
                border-top-left-radius: {radius_top_left}px;
                border-bottom-right-radius: {radius_bottom_right}px;
                border-bottom-left-radius: {radius_bottom_left}px;
                }}"""

        for wg in wgs:
            wg.setStyleSheet(style)

            Fct(wg=wg, w=width, h=height).DIM()

            wg.setMinimum(value_min)
            wg.setMaximum(value_max)
            wg.setSingleStep(value_step)

            wg.setCursor(Fct(cur=curseur).CUR())


class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
        )
class Base_rond(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            width=100,
            height=100,


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


            bg=Rgb().th1(),
            bg_handle=Rgb().tr(),
            bg_handle_hover = Rgb().tr(),
            bg_handle_pressed = Rgb().tr(),
            gradient_rgb_1=gradient_rgb_1,
            gradient_rgb_2=gradient_rgb_2,

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