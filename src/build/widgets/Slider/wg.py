from ....build import *
from .. import p_base


class wg:
    def __init__(self,
                 *wgs,
                 colors_type,
                 colors,
                 gradient_colors,

                 dim_width=p_base.DIM_WG_WIDTH,
                 dim_height=p_base.DIM_WG_HEIGHT,

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

                 val_min,
                 val_max,
                 step,

                 curseur=p_base.CUR
    ):
        style = f"""
         /* BORDURES */
         .QSlider {{
         border-top: {bordure_width_top}px {bordure_style_top} rgba{bordure_couleur_top};
         border-bottom: {bordure_width_bottom}px {bordure_style_bottom} rgba{bordure_couleur_bottom};
         border-right: {bordure_width_right}px {bordure_style_right} rgba{bordure_couleur_right};
         border-left: {bordure_width_left}px {bordure_style_left} rgba{bordure_couleur_left};
         }}
         
         /* RAYONS */
         .QSlider {{
         border-top-left-radius: {rayon_top_left}px;
         border-top-right-radius: {rayon_top_right}px;
         border-bottom-right-radius: {rayon_bottom_right}px;
         border-bottom-left-radius: {rayon_bottom_left}px;
         }}"""
        for wg in wgs:

            wg.setStyleSheet(style)

            try:
                Fct(wg=wg, w=dim_width, h=dim_height).DIM()

                wg.setMinimum(val_min)
                wg.setMaximum(val_max)
                wg.setSingleStep(step)

                wg.setCursor(Fct(cur=curseur).CUR())
            except: pass


"""
"th":
                /* SLIDER  */
                QSlider {{
                background-color: rgba(0, 0, 0, 0);
                margin: 0px
                }}
                
                /* BARRE_H */
                QSlider::groove:horizontal {{
                border-radius: 5px;
                height: 20px;
                margin: 0px;
                background-color: rgb{colors.get("c3")};
                }}
                QSlider::groove:horizontal:hover {{
                background-color: rgb{colors.get("c3")};
                }}
                
                /* CURSEUR_H */
                QSlider::handle:horizontal {{
                border: none;
                height: 20px;
                width: 20px;
                margin: -10px 0px;
                border-radius: 5px;
                background-color: rgb{colors.get("c1")};
                }}
                QSlider::handle:horizontal:hover {{
                background-color: rgb{colors.get("bn1")};
                }}
                QSlider::handle:horizontal:pressed {{
                background-color: rgb{colors.get("bn2")};
                }}
                
                /* BARRE_V */
                QSlider::groove:vertical {{
                border-radius: 5px;
                width: 20px;
                margin: 0px;
                background-color: rgb{colors.get("c3")};
                }}
                QSlider::groove:vertical:hover {{
                background-color: rgb{colors.get("c3")};
                }}
                
                /* CURSEUR_V */
                QSlider::handle:vertical {{
                border: none;
                height: 20px;
                width: 20px;
                margin: 0px -10px;
                border-radius: 5px;
                background-color: rgb{colors.get("c1")};
                }}
                QSlider::handle:vertical:hover {{
                background-color: rgb{colors.get("bn1")};
                }}
                QSlider::handle:vertical:pressed {{
                background-color: rgb{colors.get("bn2")};
                }}
                
"rond": 
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
                background-color: rgb{colors.get("c3")};
                }}
                QSlider::groove:horizontal:hover {{
                background-color: rgb{colors.get("c3")};
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
                QSlider::handle:horizontal:hover {{
                border: 8px solid rgb{colors.get("bn1")};
                }}
                QSlider::handle:horizontal:pressed {{
                border: 8px solid rgb{colors.get("bn2")};
                }}
                
                /* BARRE_V */
                QSlider::groove:vertical {{
                border-radius: 10px;
                width: 20px;
                margin: 0px;
                background-color: rgb{colors.get("c3")};
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
                QSlider::handle:vertical:hover {{
                border: 8px solid rgb{colors.get("bn1")};
                }}
                QSlider::handle:vertical:pressed {{
                border: 8px solid rgb{colors.get("bn2")};
                }}

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