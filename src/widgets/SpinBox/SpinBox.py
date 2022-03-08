from PySide6 import QtCore, QtWidgets

from src.build import *
from src.build.widgets import VBase




##################
##     BASE     ##
##################
class Plus_moins_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
        )
class Plus_moins_tr(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            no_focus=True,

            bg=Rgb().tr(),
            fg=Rgb().th3(),
    )
class Up_down_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            img_up=Img().fleche_top(),
            img_down=Img().fleche_bottom(),

    )
class Up_down_tr(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            no_focus=True,

            bg=Rgb().tr(),
            fg=Rgb().th3(),
            img_up=Img().fleche_top(),
            img_down=Img().fleche_bottom(),
    )

class rgb_bd_th3(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            value_max=255,

            border=((StyleBase().bd(),) * 4),
            border_hover=((StyleBase().bd(),) * 4),
            border_rgb=Rgb().th3(),
            border_hover_rgb=Rgb().th3(),
        )
class Plus_moins_bd_th3(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,

            border=((StyleBase().bd(),) * 4),
            border_hover=((StyleBase().bd(),) * 4),
            border_rgb=Rgb().th3(),
            border_hover_rgb=Rgb().th3(),
    )
class Plus_moins_inf_bd_th3(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            value_max=999999,

            border=((StyleBase().bd(),) * 4),
            border_hover=((StyleBase().bd(),) * 4),
            border_rgb=Rgb().th3(),
            border_hover_rgb=Rgb().th3(),
        )

"""
"lr":
QSpinBox::up-button, QDoubleSpinBox::up-button  {{
subcontrol-origin: margin;
subcontrol-position: center right;
right: {(dim_h - (dim_h  * P_style().x_ico())) / 2}px;
image: url({pb_up + tm + ".svg"});
height: {dim_h * P_style().x_ico() / 1.6}px;
width: {dim_h * P_style().x_ico() / 1.6}px;
}}

QSpinBox::down-button, QDoubleSpinBox::down-button  {{
subcontrol-origin: margin;
subcontrol-position: center left;
left: {(dim_h - (dim_h  * P_style().x_ico())) / 2}px;
image: url({pb_down + tm + ".svg"});
height: {dim_h * P_style().x_ico() / 1.6}px;
width: {dim_h * P_style().x_ico() / 1.6}px;
}}
"""
