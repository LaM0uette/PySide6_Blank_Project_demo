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
            bg=p_base.BG,
            bg_groove=p_base.BG_GROOVE,
            bg_groove_2=None,
            bg_groove_hover=p_base.BG_GROOVE_HOVER,
            bg_groove_hover_2=None,
            bg_groove_pressed=p_base.BG_GROOVE_PRESSED,
            bg_groove_pressed_2=None,
            bg_handle=p_base.BG_HANDLE,
            bg_handle_hover=p_base.BG_HANDLE_HOVER,
            bg_handle_pressed=p_base.BG_HANDLE_PRESSED,
            gradient=(0, 0, 0, 0),

            # Dimensions WG
            width_groove=P_dim().h9(),
            height_groove=P_dim().h9(),
            width_handle_h=P_dim().h9(),
            height_handle_h=P_dim().h9(),
            width_handle_v=P_dim().h9(),
            height_handle_v=P_dim().h9(),

            # Positions WG
            margin_handle_h=(0, 0, 0, 0),
            margin_handle_v=(0, 0, 0, 0),

            # Bordures
            border=p_base.WG_BORDER_WIDTH,
            border_style=p_base.WG_BORDER_STYLE,
            border_rgb=p_base.WG_BORDER_RGB,
            # Bordures hover
            border_hover=p_base.WG_BORDER_WIDTH,
            border_style_hover=p_base.WG_BORDER_STYLE,
            border_rgb_hover=p_base.WG_BORDER_RGB,
            # Bordures slider h
            border_handle_h=p_base.WG_BORDER_WIDTH,
            border_handle_h_style=p_base.WG_BORDER_STYLE,
            border_handle_h_rgb=p_base.WG_BORDER_RGB,
            # Bordures slider v
            border_handle_v=p_base.WG_BORDER_WIDTH,
            border_handle_v_style=p_base.WG_BORDER_STYLE,
            border_handle_v_rgb=p_base.WG_BORDER_RGB,

            # Rayons
            radius=(0, 0, 0, 0),
            radius_groove_h=0,
            radius_groove_v=0,
            radius_handle_h=0,
            radius_handle_v=0,
    ):
        style = f"""
                /* SLIDER  */
                QSlider {{
                background-color: rgba{bg};
                }}
        
                /* BARRE_H */
                QSlider::groove:horizontal {{
                background-color: qlineargradient(spread:pad, x1:{gradient[0]}, y1:{gradient[1]}, x2:{gradient[2]}, y2:{gradient[3]}, stop:0 rgba{bg_groove}, stop:1 rgba{bg_groove_2});
                height: {height_groove}px;
                border-radius: {radius_groove_h}px;
                }}
                QSlider::groove:horizontal:hover {{
                background-color: qlineargradient(spread:pad, x1:{gradient[0]}, y1:{gradient[1]}, x2:{gradient[2]}, y2:{gradient[3]}, stop:0 rgba{bg_groove_hover}, stop:1 rgba{bg_groove_hover_2});
                }}
                QSlider::groove:horizontal:pressed {{
                background-color: qlineargradient(spread:pad, x1:{gradient[0]}, y1:{gradient[1]}, x2:{gradient[2]}, y2:{gradient[3]}, stop:0 rgba{bg_groove_pressed}, stop:1 rgba{bg_groove_pressed_2});
                }}

                /* CURSEUR_H */
                QSlider::handle:horizontal {{
                background-color: rgba{bg_handle};
                width: {width_handle_h}px;
                height: {height_handle_h}px;
                border-radius: {radius_handle_h}px;
                margin-top: {margin_handle_h[0]}px;
                margin-bottom: {margin_handle_h[1]}px;
                margin-right: {margin_handle_h[2]}px;
                margin-left: {margin_handle_h[3]}px;
                border-top: {border_handle_h[0]}px {border_handle_h_style} rgba{border_handle_h_rgb};
                border-bottom: {border_handle_h[1]}px {border_handle_h_style} rgba{border_handle_h_rgb};
                border-right: {border_handle_h[2]}px {border_handle_h_style} rgba{border_handle_h_rgb};
                border-left: {border_handle_h[3]}px {border_handle_h_style} rgba{border_handle_h_rgb};
                }}
                QSlider::handle:horizontal:hover {{
                background-color: rgba{bg_handle_hover};
                }}
                QSlider::handle:horizontal:pressed {{
                background-color: rgba{bg_handle_pressed};
                }}
        
                /* BARRE_V */
                QSlider::groove:vertical {{
                background-color: qlineargradient(spread:pad, x1:{gradient[0]}, y1:{gradient[1]}, x2:{gradient[2]}, y2:{gradient[3]}, stop:0 rgba{bg_groove}, stop:1 rgba{bg_groove_2});
                width: {width_groove}px;
                border-radius: {radius_groove_v}px;
                }}
                QSlider::groove:vertical:hover {{
                background-color: qlineargradient(spread:pad, x1:{gradient[0]}, y1:{gradient[1]}, x2:{gradient[2]}, y2:{gradient[3]}, stop:0 rgba{bg_groove_hover}, stop:1 rgba{bg_groove_hover_2});
                }}
                QSlider::groove:vertical:pressed {{
                background-color: qlineargradient(spread:pad, x1:{gradient[0]}, y1:{gradient[1]}, x2:{gradient[2]}, y2:{gradient[3]}, stop:0 rgba{bg_groove_pressed}, stop:1 rgba{bg_groove_pressed_2});
                }}
        
                /* CURSEUR_V */
                QSlider::handle:vertical {{
                background-color: rgba{bg_handle};
                width: {width_handle_v}px;
                height: {height_handle_v}px;
                border-radius: {radius_handle_v}px;
                margin-top: {margin_handle_v[0]}px;
                margin-bottom: {margin_handle_v[1]}px;
                margin-right: {margin_handle_v[2]}px;
                margin-left: {margin_handle_v[3]}px;
                border-top: {border_handle_v[0]}px {border_handle_v_style} rgba{border_handle_v_rgb};
                border-bottom: {border_handle_v[1]}px {border_handle_v_style} rgba{border_handle_v_rgb};
                border-right: {border_handle_v[2]}px {border_handle_v_style} rgba{border_handle_v_rgb};
                border-left: {border_handle_v[3]}px {border_handle_v_style} rgba{border_handle_v_rgb};
                }}
                QSlider::handle:vertical:hover {{
                background-color: rgba{bg_handle_hover};
                }}
                QSlider::handle:vertical:pressed {{
                background-color: rgba{bg_handle_pressed};
                }}
        
                /* BORDURES */
                .QSlider {{
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}
                .QSlider:hover {{
                border-top: {border_hover[0]}px {border_style_hover} rgba{border_rgb_hover};
                border-bottom: {border_hover[1]}px {border_style_hover} rgba{border_rgb_hover};
                border-right: {border_hover[2]}px {border_style_hover} rgba{border_rgb_hover};
                border-left: {border_hover[3]}px {border_style_hover} rgba{border_rgb_hover};
                }}
                
                .QSlider {{
                border-top-right-radius: {radius[0]}px;
                border-top-left-radius: {radius[1]}px;
                border-bottom-right-radius: {radius[2]}px;
                border-bottom-left-radius: {radius[3]}px;
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
            width=200,
            height=200,

            bg=Rgb().th1(),
            bg_handle=Rgb().th3(),
            bg_handle_hover = Rgb().th3(),
            bg_handle_pressed = Rgb().th3(),

            height_groove=12,
            width_groove=12,
            width_handle_h=6,
            height_handle_h=6,
            width_handle_v=6,
            height_handle_v=6,

            margin_handle_h=(-4, -4, 0, 0),
            margin_handle_v=(0, 0, -4, -4),

            border_handle_h=(4, 4, 4, 4),
            border_handle_h_rgb=Rgb().th2(),
            border_handle_v=(4, 4, 4, 4),
            border_handle_v_rgb=Rgb().th2(),

            radius_groove_h=3,
            radius_groove_v=3,
            radius_handle_h=4,
            radius_handle_v=4,
        )
class rgb(Style):
    def __init__(self,
                 *wgs,
                 rgb_1=None,
                 rgb_2=None,
                 ):
        super().__init__(
            *wgs,
            height=P_dim().h8(),
            value_max=255,

            bg=Rgb().th1(),
            bg_handle=Rgb().tr(),
            bg_handle_hover = Rgb().tr(),
            bg_handle_pressed = Rgb().tr(),

            bg_groove=rgb_1,
            bg_groove_2=rgb_2,
            bg_groove_hover=rgb_1,
            bg_groove_hover_2=rgb_2,
            bg_groove_pressed=rgb_1,
            bg_groove_pressed_2=rgb_2,
            gradient=(0, 0, 1, 0),

            height_groove=20,
            width_groove=20,
            width_handle_h=14,
            height_handle_h=5,
            width_handle_v=5,
            height_handle_v=14,

            margin_handle_h=(-5, -5, 0, 0),
            margin_handle_v=(0, 0, -5, -5),
            border_handle_h=(8, 8, 8, 8),
            border_handle_h_rgb=Rgb().th2(),
            border_handle_v=(8, 8, 8, 8),
            border_handle_v_rgb=Rgb().th2(),

            radius_groove_h=10,
            radius_groove_v=10,
            radius_handle_h=15,
            radius_handle_v=15,
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