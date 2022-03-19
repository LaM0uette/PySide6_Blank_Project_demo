from src.lib.palettes import *
from src.widgets import vb_wg
from src.widgets.SpinBox.Build import Build


##################
##     BASE     ##
##################
class PlusMinus:
    def __init__(self, *wgs):
        self.wgs = wgs

    def th(self):
        Build(
            *self.wgs,
        )
    def tr(self):
        Build(
            *self.wgs,

            focus_policy=FocusPolicy.NO,

            bg=Rgb().tr(),
            fg=Rgb.TH3,
        )
class UpDown:
    def __init__(self, *wgs):
        self.wgs = wgs
    def th(self):
        Build(
            *self.wgs,

            img_up=Img.FLECHE_TOP,
            img_down=Img.FLECHE_BOTTOM,
            img_up_hover=Img.FLECHE_TOP,
            img_down_hover=Img.FLECHE_BOTTOM,
        )
    def tr(self):
        Build(
            *self.wgs,
            focus_policy=FocusPolicy.NO,
            bg=Rgb().tr(),
            fg=Rgb.TH3,

            img_up=Img.FLECHE_TOP,
            img_down=Img.FLECHE_BOTTOM,
            img_up_hover=Img.FLECHE_TOP,
            img_down_hover=Img.FLECHE_BOTTOM,
        )


####################
##     CADRES     ##
####################
class Dlg:
    def __init__(self, *wgs):
        self.wgs = wgs

    def rtn(self, value_max):
        Build(
            *self.wgs,

            width=Dim.H7,

            value_max=value_max,
        )

    def th(self): self.rtn(value_max=100)
    def rgb(self): self.rtn(value_max=255)
    def inf(self): self.rtn(value_max=99999999)


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
