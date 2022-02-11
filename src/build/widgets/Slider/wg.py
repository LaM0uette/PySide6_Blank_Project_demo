from ....build import *
from .. import p_base


class wg:
    def __init__(self,
                 *wgs,
                 colors_type,
                 colors,
                 gradient_colors,
                 dim,
                 bd,
                 rd,
                 val_min,
                 val_max,
                 step,
                 cur
    ):
        style = f"""
                            /* BORDURES */
                            .QSlider#{wg.objectName()} {{
                            border-width: {bd.get("px")}px;
                            border-style: solid;
                            border-color: rgba{bds.get("o1")} rgba{bds.get("o2")} rgba{bds.get("o3")} rgba{bds.get("o4")};
                            }}

                            /* RAYONS */
                            .QSlider#{wg.objectName()} {{
                            border-top-left-radius: {rds.get("r1")}px;
                            border-top-right-radius: {rds.get("r2")}px;
                            border-bottom-right-radius: {rds.get("r4")}px;
                            border-bottom-left-radius: {rds.get("r3")}px;
                            }}
                    """
        for wg in wgs:

            wg.setStyleSheet(style)

            try:
                Fct(wg=wg, w=dim.get("w"), h=dim.get("h")).DIM()

                wg.setMinimum(val_min)
                wg.setMaximum(val_max)
                wg.setSingleStep(step)

                wg.setCursor(Fct(cur=cur).CUR())
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