from PySide6 import QtCore, QtWidgets

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

            # Couleurs BG
            bg=p_base.BG,
            bg_selection=p_base.BG_SELECTION,
            # Couleurs FG
            fg=p_base.FG,
            fg_selection=p_base.FG_SELECTION,

            # Images
            img_up=p_base.IMG_UP,
            img_down=p_base.IMG_DOWN,
            # Images RGB
            img_up_rgb=p_base.IMG_UP_RGB,
            img_down_rgb=p_base.IMG_DOWN_RGB,
            # Images DIM
            img_up_width=10,
            img_up_height=10,
            img_down_width=10,
            img_down_height=10,
            # Images positions
            img_up_top=2,
            img_up_bottom=0,
            img_up_right=2,
            img_up_left=0,
            img_down_top=0,
            img_down_bottom=2,
            img_down_right=2,
            img_down_left=0,

            # Bordures
            border=p_base.WG_BORDER_WIDTH,
            border_style=p_base.WG_BORDER_STYLE,
            border_rgb=p_base.WG_BORDER_RGB,
            # Bordures hover
            border_hover=p_base.WG_BORDER_WIDTH,
            border_hover_style=p_base.WG_BORDER_STYLE,
            border_hover_rgb=p_base.WG_BORDER_RGB,

            # Rayons
            radius=p_base.WG_RADIUS,
    ):
        style = f"""
                /* SPINBOX */
                QSpinBox, QDoubleSpinBox {{
                background-color: rgba{bg};
                color: rgba{fg};
                selection-background-color: rgba{bg_selection};
                selection-color: rgba{fg_selection}
                }}
        
                QSpinBox::up-button, QDoubleSpinBox::up-button  {{
                subcontrol-position: top right;
                top: {img_up_top}px;
                bottom: {img_up_bottom}px;
                right: {img_up_right}px;
                left: {img_up_left}px;
                image: url({f"{img_up}{img_up_rgb}.svg"});
                width: {img_up_width}px;
                height: {img_up_height}px;
                }}
        
                QSpinBox::down-button, QDoubleSpinBox::down-button  {{
                subcontrol-position: bottom right;
                top: {img_down_top}px;
                bottom: {img_down_bottom}px;
                right: {img_down_right}px;
                left: {img_down_left}px;
                image: url({f"{img_down}{img_down_rgb}.svg"});
                width: {img_down_width}px;
                height: {img_down_height}px;
                }}
        
                /* BORDURES */
                .QSpinBox, .QDoubleSpinBox {{
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}
                .QSpinBox:hover, .QDoubleSpinBox:hover {{
                border-top: {border_hover[0]}px {border_hover_style} rgba{border_hover_rgb};
                border-bottom: {border_hover[1]}px {border_hover_style} rgba{border_hover_rgb};
                border-right: {border_hover[2]}px {border_hover_style} rgba{border_hover_rgb};
                border-left: {border_hover[3]}px {border_hover_style} rgba{border_hover_rgb};
                }}
                
                /* RAYONS */
                .QComboBox, .QFontComboBox {{
                border-top-right-radius: {radius[0]}px;
                border-top-left-radius: {radius[1]}px;
                border-bottom-right-radius: {radius[2]}px;
                border-bottom-left-radius: {radius[3]}px;
                }}"""

        for wg in wgs:
            wg.setStyleSheet(style)

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
                bg_gen=Rgb().tr(),
                fg_gen=Rgb().th3(),
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
                fg_gen=Rgb().th3(),
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
"""