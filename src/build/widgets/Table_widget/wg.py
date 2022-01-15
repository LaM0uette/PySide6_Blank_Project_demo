from PySide6 import QtWidgets, QtCore

from ..Attrs import Attrs
from ....build import *


class wg:
    def __init__(self,
                 *wgs,
                 colors_type,
                 colors,
                 dim,
                 font,
                 hd_font,
                 bd,
                 rd,
                 scroll,
                 header,
                 cur
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
                Fct(wg=wg, w=dim.get("w"), h=dim.get("h")).DIM()
                wg.setFont(Fct(font_size=font).FONT())
                wg.horizontalHeader().setFont(Fct(font_size=hd_font).FONT())
                wg.verticalHeader().setFont(Fct(font_size=hd_font).FONT())

                wg.setHorizontalScrollBarPolicy(scroll.get("h"))
                wg.setVerticalScrollBarPolicy(scroll.get("v"))
                wg.horizontalHeader().setVisible(header.get("h"))
                wg.verticalHeader().setVisible(header.get("v"))

                wg.setCursor(Fct(cur=cur).CUR())
                wg.viewport().setCursor(Fct(cur=cur).CUR())

                wg.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
                wg.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
                wg.verticalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
                wg.setFrameShape(QtWidgets.QFrame.NoFrame)

                wg.resizeColumnsToContents()
            except: pass
