from PySide6 import QtCore, QtWidgets

from ....build import *
from ....build.widgets import p_base

class Style:
    def __init__(self,
                 *wgs,
                 couleur_bg=p_base._COLORS_BG,
                 couleur_bg_hover=p_base._COLORS_BG_HOVER,
                 couleur_bg_selection=p_base.COLORS_BG_SELECTION,
                 couleur_fg=p_base._COLORS_FG,
                 couleur_fg_hover=p_base._COLORS_FG_HOVER,
                 couleur_fg_selection=p_base.COLORS_FG_SELECTION,
                 dim_width=p_base.WG_WIDTH,
                 dim_height=p_base.WG_HEIGHT,
                 police=p_base.FONT,
                 police_taille=p_base.FONT_SIZE,
                 img_up=p_base.IMG_UP,
                 tm_up=p_base.TM_UP,
                 img_down=p_base.IMG_DOWN,
                 tm_down=p_base.TM_DOWN,
                 img_up_width=p_base.IMG_WIDTH,
                 img_up_height=p_base.IMG_HEIGHT,
                 img_down_width=p_base.IMG_WIDTH,
                 img_down_height=p_base.IMG_HEIGHT,
                 img_up_top=0,
                 img_up_bottom=0,
                 img_up_right=0,
                 img_up_left=0,
                 img_down_top=0,
                 img_down_bottom=0,
                 img_down_right=0,
                 img_down_left=0,
                 bordure_width_top=p_base.WG_BORDER_WIDTH,
                 bordure_width_bottom=p_base.WG_BORDER_WIDTH,
                 bordure_width_right=p_base.WG_BORDER_WIDTH,
                 bordure_width_left=p_base.WG_BORDER_WIDTH,
                 bordure_style_top=p_base.WG_BORDER_STYLE,
                 bordure_style_bottom=p_base.WG_BORDER_STYLE,
                 bordure_style_right=p_base.WG_BORDER_STYLE,
                 bordure_style_left=p_base.WG_BORDER_STYLE,
                 bordure_couleur_top=p_base.WG_BORDER_RGB,
                 bordure_couleur_bottom=p_base.WG_BORDER_RGB,
                 bordure_couleur_right=p_base.WG_BORDER_RGB,
                 bordure_couleur_left=p_base.WG_BORDER_RGB,
                 rayon_top_left=p_base.WG_RADIUS,
                 rayon_top_right=p_base.WG_RADIUS,
                 rayon_bottom_right=p_base.WG_RADIUS,
                 rayon_bottom_left=p_base.WG_RADIUS,
                 align=P_align().c().c(),
                 buttons_type=p_base.SB_BUTTONS_TYPE,
                 no_focus=p_base.NO_FOCUS,
                 valeur_min=p_base.VAL_MIN,
                 valeur_max=p_base.VAL_MAX,
                 valeur_pas=p_base.VAL_PAS,
                 curseur=p_base.CUR,
                 curseur_le=p_base.CUR_LE
    ):
        for wg in wgs:
            wg.setStyleSheet(style)

            try: Fct(wg=wg, w=dim_width, h=dim_height).DIM()
            except: pass

            try:
                wg.setFont(Fct(font=police, font_size=police_taille).FONT())

                wg.setAlignment(align)

                wg.setMinimum(valeur_min)
                wg.setMaximum(valeur_max)
                wg.setSingleStep(valeur_pas)

                wg.setFrame(QtWidgets.QFrame.NoFrame)
                wg.setButtonSymbols(buttons_type)
                if no_focus: wg.setFocusPolicy(QtCore.Qt.NoFocus)

                wg.setCursor(Fct(cur=curseur).CUR())
                wg.lineEdit().setCursor(Fct(cur=curseur_le).CUR())
            except: pass


class Plus_moins_th(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs)
class Plus_moins_tr(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              couleur_bg=(0, 0, 0, 0),
              couleur_bg_hover=(0, 0, 0, 0),
              no_focus=True
    )

class Up_down_th(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              img_up=P_img().fleche_top(),
              img_down=P_img().fleche_bottom(),
    )
class Up_down_tr(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              couleur_bg=(0, 0, 0, 0),
              couleur_bg_hover=(0, 0, 0, 0),
              img_up=P_img().fleche_top(),
              img_down=P_img().fleche_bottom(),
              no_focus=True
    )


class rgb_bd_th3(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              bordure_width_top=P_style().bd(),
              bordure_width_bottom=P_style().bd(),
              bordure_width_right=P_style().bd(),
              bordure_width_left=P_style().bd(),
              bordure_couleur_top=P_rgb().th3(),
              bordure_couleur_bottom=P_rgb().th3(),
              bordure_couleur_right=P_rgb().th3(),
              bordure_couleur_left=P_rgb().th3(),
              valeur_max=255
    )
class Plus_moins_bd_th3(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              bordure_width_top=P_style().bd(),
              bordure_width_bottom=P_style().bd(),
              bordure_width_right=P_style().bd(),
              bordure_width_left=P_style().bd(),
              bordure_couleur_top=P_rgb().th3(),
              bordure_couleur_bottom=P_rgb().th3(),
              bordure_couleur_right=P_rgb().th3(),
              bordure_couleur_left=P_rgb().th3(),
    )
class Plus_moins_inf_bd_th3(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              bordure_width_top=P_style().bd(),
              bordure_width_bottom=P_style().bd(),
              bordure_width_right=P_style().bd(),
              bordure_width_left=P_style().bd(),
              bordure_couleur_top=P_rgb().th3(),
              bordure_couleur_bottom=P_rgb().th3(),
              bordure_couleur_right=P_rgb().th3(),
              bordure_couleur_left=P_rgb().th3(),
              valeur_max=999999
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