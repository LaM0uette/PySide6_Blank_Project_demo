from src.lib.palettes import *
from src.widgets import vb_wg
from src.widgets.Slider.Build import Build


##################
##     BASE     ##
##################
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
            width_handle_h=10,
            height_handle_h=4,
            width_handle_v=4,
            height_handle_v=10,

            margin_handle_h=(-3, -3, 0, 0),
            margin_handle_v=(0, 0, -3, -3),

            border_handle_h=((3, )*4),
            border_handle_h_rgb=Rgb().th2(),
            border_handle_v=((3, )*4),
            border_handle_v_rgb=Rgb().th2(),

            radius_groove_h=((3, )*4),
            radius_groove_v=((3, )*4),
            radius_handle_h=((6, )*4),
            radius_handle_v=((6, )*4),
        )
class rgb(Style):
    def __init__(self,
                 *wgs,
                 rgb=None,
                 rgb_1=None,
                 rgb_2=None,
                 ):
        super().__init__(
            *wgs,
            height=Dim().h8(),
            value_max=255,

            bg=Rgb().th1(),
            bg_handle=rgb,
            bg_handle_hover=rgb,
            bg_handle_pressed=rgb,

            bg_groove=rgb_1,
            bg_groove_2=rgb_2,
            bg_groove_hover=rgb_1,
            bg_groove_hover_2=rgb_2,
            bg_groove_pressed=rgb_1,
            bg_groove_pressed_2=rgb_2,
            gradient=(0, 0, 1, 0),

            height_groove=12,
            width_groove=12,
            width_handle_h=12,
            height_handle_h=4,
            width_handle_v=4,
            height_handle_v=12,

            margin_handle_h=(-5, -5, 0, 0),
            margin_handle_v=(0, 0, -5, -5),

            border_handle_h=((3, )*4),
            border_handle_h_rgb=rgb,
            border_handle_v=((3, )*4),
            border_handle_v_rgb=rgb,

            radius_groove_h=((3, )*4),
            radius_groove_v=((3, )*4),
            radius_handle_h=((4, )*4),
            radius_handle_v=((4, )*4),
        )
