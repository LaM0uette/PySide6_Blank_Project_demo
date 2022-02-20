from PySide6 import QtCore, QtWidgets

from .StyleSheet import StyleSheet
from ....build import *
from ....build.widgets import p_base

class Style:
    def __init__(
            self,
            *wgs,
            wg_type=p_base.SB_BUTTONS_TYPE,
            width=p_base.WG_WIDTH,
            height=p_base.WG_HEIGHT,
            font=p_base.FONT,
            font_size=p_base.FONT_SIZE,
            no_focus=p_base.NO_FOCUS,
            value_min=p_base.VAL_MIN,
            value_max=p_base.VAL_MAX,
            value_step=p_base.VAL_STEP,
            align_horizontal=Align().h_center(),
            align_vertical=Align().v_center(),
            curseur=p_base.CUR,
            curseur_le=p_base.CUR_LE,
            style=StyleSheet()
    ):
        for wg in wgs:
            wg.setStyleSheet(style.get())

            try: Fct(wg=wg, w=width, h=height).DIM()
            except: pass

            wg.setFont(Fct(font=font, font_size=font_size).FONT())

            wg.setAlignment(align_horizontal | align_vertical)

            wg.setMinimum(value_min)
            wg.setMaximum(value_max)
            wg.setSingleStep(value_step)

            wg.setFrame(QtWidgets.QFrame.NoFrame)
            wg.setButtonSymbols(wg_type)
            if no_focus: wg.setFocusPolicy(QtCore.Qt.NoFocus)

            wg.setCursor(Fct(cur=curseur).CUR())
            wg.lineEdit().setCursor(Fct(cur=curseur_le).CUR())


class Plus_moins_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            style=StyleSheet(
            )
        )
class Plus_moins_tr(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            no_focus=True,

            style=StyleSheet(
                bg_gen=Rgb().tr()
            )
    )

class Up_down_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            style=StyleSheet(
                img_up=P_img().fleche_top(),
                img_down=P_img().fleche_bottom(),
            )

    )
class Up_down_tr(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            no_focus=True,

            style=StyleSheet(
                bg_gen=Rgb().tr(),
                img_up=P_img().fleche_top(),
                img_down=P_img().fleche_bottom(),
            )
    )


class rgb_bd_th3(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            value_max=255,

            style=StyleSheet(
                border_gen_all=P_style().bd(),
                border_gen_rgb=P_rgb().th3(),
            )
        )
class Plus_moins_bd_th3(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            style=StyleSheet(
                border_gen_all=P_style().bd(),
                border_gen_rgb=P_rgb().th3(),
            )
    )
class Plus_moins_inf_bd_th3(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            value_max=999999,

            style=StyleSheet(
                border_gen_all=P_style().bd(),
                border_gen_rgb=P_rgb().th3(),
            )
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

                "tb": 

"""