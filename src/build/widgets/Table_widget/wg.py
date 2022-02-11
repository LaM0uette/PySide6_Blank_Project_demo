from PySide6 import QtWidgets, QtCore

from ..Attrs import Attrs
from ....build import *


class wg:
    def __init__(self,
                 *wgs,

                 couleur_bg=p_base.COULEUR_BG,
                 couleur_bg_checked=p_base.COULEUR_BG_CHECKED,
                 couleur_bg_checked_hover=p_base.COULEUR_BG_CHECKED_HOVER,
                 couleur_bg_item=p_base.COULEUR_BG_ITEM,
                 couleur_bg_item_hover=p_base.COULEUR_BG_ITEM_HOVER,
                 couleur_fg=p_base.COULEUR_FG,
                 couleur_fg_checked=p_base.COULEUR_FG_CHECKED,
                 couleur_fg_checked_hover=p_base.COULEUR_FG_CHECKED_HOVER,
                 couleur_fg_item=p_base.COULEUR_FG_ITEM,
                 couleur_fg_item_hover=p_base.COULEUR_FG_ITEM_HOVER,

                 dim_width=p_base.DIM_WG_WIDTH,
                 dim_height=p_base.DIM_WG_HEIGHT,

                 police=p_base.FONT,
                 police_taille=p_base.FONT_SIZE,
                 police_hd_taille=p_base.HD_FONT_SIZE,

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
                 scroll_bg=p_base.SCROLL_BG,
                 scroll_handle_bg=p_base.SCROLL_HANDLE_BG,
                 scroll_handle_fg=p_base.SCROLL_HANDLE_FG,
                 scroll_width=p_base.SCROLL_WIDTH,
                 scroll_height=p_base.SCROLL_HEIGHT,
                 scroll_handle_min_width=p_base.SCROLL_HANDLE_MIN_WIDTH,
                 scroll_handle_min_height=p_base.SCROLL_HANDLE_MIN_HEIGHT,
                 scroll_h=p_base.SCROLL_H,
                 scroll_v=p_base.SCROLL_V,

                 header_h=p_base.HEADER_H,
                 header_v=p_base.HEADER_V,

                 curseur=p_base.CUR
    ):
        bds = Attrs(bd=bd).GET_BD()
        rds = Attrs(rd=rd).GET_RD()

        for wg in wgs:
            style_gen = f"""
            /* BORDURES */
            .QTableWidget#{wg.objectName()} {{
            border-width: {bd.get("px")}px;
            border-style: solid;
            border-color: rgba{bds.get("o1")} rgba{bds.get("o2")} rgba{bds.get("o3")} rgba{bds.get("o4")};
            }}

            /* RAYONS */
            .QTableWidget#{wg.objectName()} {{
            border-top-left-radius: {rds.get("r1")}px;
            border-top-right-radius: {rds.get("r2")}px;
            border-bottom-right-radius: {rds.get("r4")}px;
            border-bottom-left-radius: {rds.get("r3")}px;
            }}
            
            /* SCROLL */
            QTableWidget QScrollBar {{
            background-color: rgb{colors.get("c1")};
            width: 20px;
            height: 20px;
            }}
            QTableWidget ::handle:vertical {{
            min-height: 100px;
            }}
            QTableWidget ::handle:vertical {{
            min-height: 100px;
            }}
            QTableWidget ::handle:horizontal {{
            min-width: 100px;
            }}
            QTableWidget QScrollBar::handle {{
            background-color: rgb{colors.get("c3")};
            }}
            QTableWidget QScrollBar::add-page, QTableWidget QScrollBar::sub-page {{
            background-color: rgb{colors.get("c1")};
            border: rgb{colors.get("c1")};
            }}
            """
            style_type = {
                "th": f"""
                /* CORNER */
                QTableCornerButton::section {{
                background-color: rgb{colors.get("c1")};
                }}
                
                /* TABLE_WIDGET */
                QTableWidget {{
                background-color: rgb{colors.get("c1")};
                gridline-color: rgb{colors.get("c3")};
                color: rgb{colors.get("c3")};
                }}
                
                /* ITEM */
                QTableWidget::item {{
                background-color: rgb{colors.get("c1")};
                color: rgb{colors.get("c3")};
                }}
                QTableWidget::item:hover {{
                color: rgb{colors.get("bn1")};
                }}
                QTableWidget::item:selected {{
                background-color: rgb{colors.get("c2")};
                color: rgb{colors.get("bn1")};
                }}
                QTableWidget::item:selected:hover {{
                color: rgb{colors.get("bn2")};
                }}
                """,

                "tr": f"""
                /* CORNER */
                QTableCornerButton::section {{
                background-color: rgb{colors.get("c1")};
                }}
                
                /* TABLE_WIDGET */
                QTableWidget {{
                background-color: rgba(0, 0, 0, 0);
                gridline-color: rgb{colors.get("c1")};
                color: rgb{colors.get("c1")};
                }}
                
                /* ITEM */
                QTableWidget::item {{
                background-color: rgba(0, 0, 0, 0);
                color: rgb{colors.get("c1")};
                }}
                QTableWidget::item:hover {{
                color: rgb{colors.get("bn1")};
                }}
                QTableWidget::item:selected {{
                background-color: rgb{colors.get("c3")};
                color: rgb{colors.get("bn1")};
                }}
                QTableWidget::item:selected:hover {{
                color: rgb{colors.get("bn2")};
                }}
                """
            }
            style_type_header = {
                "th": f"""
                QHeaderView::section {{
                background-color: rgb{colors.get("c1")};
                color: rgb{colors.get("c3")};
                border-style: none;
                }}
                QHeaderView::section:checked {{
                background-color: rgb{colors.get("c1")};
                color: rgb{colors.get("c3")};
                }}
                """,

                "tr": f"""
                QHeaderView::section {{
                background-color: rgb{colors.get("c1")};
                color: rgb{colors.get("c3")};
                border-style: none;
                }}
                QHeaderView::section:checked {{
                background-color: rgb{colors.get("c1")};
                color: rgb{colors.get("c3")};
                }}
                """
            }

            style_main = style_gen + style_type.get(colors_type)
            style_header = style_type_header.get(colors_type)

            wg.setStyleSheet(style_main)
            wg.horizontalHeader().setStyleSheet(style_header)
            wg.verticalHeader().setStyleSheet(style_header)

            try:
                Fct(wg=wg, w=dim_width, h=dim_height).DIM()
                wg.setFont(Fct(font=police, font_size=police_taille).FONT())
                wg.horizontalHeader().setFont(Fct(font_size=police_hd_taille).FONT())
                wg.verticalHeader().setFont(Fct(font_size=police_hd_taille).FONT())

                wg.setHorizontalScrollBarPolicy(scroll_h)
                wg.setVerticalScrollBarPolicy(scroll_v)
                wg.horizontalHeader().setVisible(header.get("h"))
                wg.verticalHeader().setVisible(header.get("v"))

                wg.setCursor(Fct(cur=curseur).CUR())
                wg.viewport().setCursor(Fct(cur=curseur).CUR())

                wg.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
                wg.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
                wg.verticalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
                wg.setFrameShape(QtWidgets.QFrame.NoFrame)

                wg.resizeColumnsToContents()
            except: pass
