from PySide6 import QtWidgets

from ....build import *
from .. import p_base


class wg:
    def __init__(self,
                 *wgs,
                 couleur_bg=p_base.COULEUR_BG,
                 wg_dim_width=p_base.DIM_WIDTH,
                 wg_dim_height=p_base.DIM_HEIGHT,
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
    ):


        for wg in wgs:
            style = f"""
                    /* FRAME */
                    .QFrame#{wg.objectName()} {{
                    background-color: rgba{couleur_bg};
                    }}

                    /* BORDURES */
                    .QFrame#{wg.objectName()} {{
                    border-top: {bordure_width_top}px {bordure_style_top} rgba{bordure_couleur_top};
                    border-bottom: {bordure_width_bottom}px {bordure_style_bottom} rgba{bordure_couleur_bottom};
                    border-right: {bordure_width_right}px {bordure_style_right} rgba{bordure_couleur_right};
                    border-left: {bordure_width_left}px {bordure_style_left} rgba{bordure_couleur_left};
                    }}

                    /* RAYONS */
                    .QFrame#{wg.objectName()} {{
                    border-top-left-radius: {rayon_top_left}px;
                    border-top-right-radius: {rayon_top_right}px;
                    border-bottom-right-radius: {rayon_bottom_right}px;
                    border-bottom-left-radius: {rayon_bottom_left}px;
                    }}"""

            wg.setStyleSheet(style)

            try:
                Fct(wg=wg, w=wg_dim_width, h=wg_dim_height).DIM()

                wg.setFrameShape(QtWidgets.QFrame.NoFrame)
            except: pass
