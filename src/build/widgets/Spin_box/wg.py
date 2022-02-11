from PySide6 import QtWidgets, QtCore

from ....build import *
from .. import p_base


class wg:
    def __init__(self,
                 *wgs,
                 colors,

                 dim_width=p_base.DIM_WG_WIDTH,
                 dim_height=p_base.DIM_WG_HEIGHT,

                 police=p_base.FONT,
                 police_taille=p_base.FONT_SIZE,

                 tm,

                 bordure_width_top=p_base.BD_WIDTH,
                 bordure_width_bottom=p_base.BD_WIDTH,
                 bordure_width_right=p_base.BD_WIDTH,
                 bordure_width_left=p_base.BD_WIDTH,
                 bordure_style_top=p_base.BD_STYLE,
                 bordure_style_bottom=p_base.BD_STYLE,
                 bordure_style_right=p_base.BD_STYLE,
                 bordure_style_left=p_base.BD_STYLE,
                 bordure_couleur_top=p_base.BD_COULEUR,
                 bordure_couleur_bottom=p_base.BD_COULEUR,
                 bordure_couleur_right=p_base.BD_COULEUR,
                 bordure_couleur_left=p_base.BD_COULEUR,
                 rayon_top_left=p_base.RD_WG,
                 rayon_top_right=p_base.RD_WG,
                 rayon_bottom_right=p_base.RD_WG,
                 rayon_bottom_left=p_base.RD_WG,

                 align=p_base.ALIGN,

                 buttons_type=p_base.SB_BUTTONS_TYPE,
                 pb_side,
                 no_focus,

                 valeur_min=p_base.VAL_MIN,
                 valeur_max=p_base.VAL_MAX,
                 valeur_pas=p_base.VAL_PAS,

                 curseur=p_base.CUR,
                 curseur_le=p_base.CUR_LE
                 ):
        style = f"""
        /* SPIN_BOX */
        QSpinBox, QDoubleSpinBox {{
        background-color: rgb{colors.get("c1")};
        color: rgb{colors.get("c3")};
        selection-background-color: rgba(0, 0, 0, 0);
        selection-color: rgb{colors.get("c3")}
        }}

        /* BORDURES */
        .QSpinBox, .QDoubleSpinBox {{
        border-top: {bordure_width_top}px {bordure_style_top} rgba{bordure_couleur_top};
        border-bottom: {bordure_width_bottom}px {bordure_style_bottom} rgba{bordure_couleur_bottom};
        border-right: {bordure_width_right}px {bordure_style_right} rgba{bordure_couleur_right};
        border-left: {bordure_width_left}px {bordure_style_left} rgba{bordure_couleur_left};
        }}
        
        /* RAYONS */
        .QSpinBox, .QDoubleSpinBox {{
        border-top-left-radius: {rayon_top_left}px;
        border-top-right-radius: {rayon_top_right}px;
        border-bottom-right-radius: {rayon_bottom_right}px;
        border-bottom-left-radius: {rayon_bottom_left}px;
        }}"""

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
                    QSpinBox::up-button, QDoubleSpinBox::up-button  {{
                    subcontrol-position: top right;
                    top: {(dim_h - (dim_h  * P_style().x_ico())) / 4}px;
                    right: {(dim_h - (dim_h  * P_style().x_ico())) / 4}px;
                    image: url({pb_up + tm + ".svg"});
                    height: {dim_h  * P_style().x_ico() / 2}px;
                    width: {dim_h  * P_style().x_ico() / 2}px;
                    }}

                    QSpinBox::down-button, QDoubleSpinBox::down-button  {{
                    subcontrol-position: bottom right;
                    bottom: {(dim_h - (dim_h  * P_style().x_ico())) / 4}px;
                    right: {(dim_h - (dim_h  * P_style().x_ico())) / 4}px;
                    image: url({pb_down + tm + ".svg"});
                    height: {dim_h  * P_style().x_ico() / 2}px;
                    width: {dim_h  * P_style().x_ico() / 2}px;
                    }}
"""