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
            style=StyleSheet(
                height_groove=20,
                width_groove=20,
                width_handle_h=5,
                height_handle_h=14,
                width_handle_v=14,
                height_handle_v=5,
                border_radius_groove_h=15,
                border_radius_groove_v=15,
                border_radius_handle_h=15,
                border_radius_handle_v=15,
            )
        )
class rgb(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            value_max=255,

            style=StyleSheet(
            )
        )
