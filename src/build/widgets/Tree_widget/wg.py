from PySide6 import QtWidgets

from ....build import *
from .. import p_base


class wg:
    def __init__(self,
                 *wgs,
                 colors_type,
                 colors,
                 dim,
                 font,
                 bd,
                 rd,
                 scroll,
                 cur
    ):
        style = f"""
        QHeaderView::section {{
        background-color: rgb{colors.get("c1")};
        color: rgb{colors.get("c3")};
        border: none;
        }}

        QTreeWidget {{
        background-color: rgb{colors.get("c1")};
        }}

        QTreeWidget::item {{
        background-color: rgb{colors.get("c1")};
        color: rgb{colors.get("c3")};
        }}

        QTreeWidget::item:hover {{
        color: rgb{colors.get("bn1")};
        }}

        QTreeWidget::item:selected {{
        background-color: rgb{colors.get("c3")};
        color: rgb{colors.get("bn1")};
        }}

        QTreeWidget::item:selected:hover {{
        color: rgb{colors.get("bn2")};
        }}

        /* BORDURES */
        .QTreeWidget#{wg.objectName()} {{
        border-width: {bd.get("px")}px;
        border-style: solid;
        border-color: rgba{bds.get("o1")} rgba{bds.get("o2")} rgba{bds.get("o3")} rgba{bds.get("o4")};
        }}

        /* RAYONS */
        .QTreeWidget#{wg.objectName()} {{
        border-top-left-radius: {rds.get("r1")}px;
        border-top-right-radius: {rds.get("r2")}px;
        border-bottom-right-radius: {rds.get("r4")}px;
        border-bottom-left-radius: {rds.get("r3")}px;
        }}

        /* SCROLL */
        QTreeWidget QScrollBar {{
        background-color: rgb{colors.get("c1")};
        width: 20px;
        height: 20px;
        }}
        QTreeWidget ::handle:vertical {{
        min-height: 100px;
        }}
        QTreeWidget ::handle:vertical {{
        min-height: 100px;
        }}
        QTreeWidget ::handle:horizontal {{
        min-width: 100px;
        }}
        QTreeWidget QScrollBar::handle {{
        background-color: rgb{colors.get("c3")};
        }}
        QTreeWidget QScrollBar::add-page, QTreeWidget QScrollBar::sub-page {{
        background-color: rgb{colors.get("c1")};
        border: rgb{colors.get("c1")};
        }}"""

        for wg in wgs:
            wg.setStyleSheet(style)

            try:
                Fct(wg=wg, w=dim.get("w"), h=dim.get("h")).DIM()
                wg.setFont(Fct(font_size=font).FONT())

                wg.setHorizontalScrollBarPolicy(scroll.get("h"))
                wg.setVerticalScrollBarPolicy(scroll.get("v"))

                wg.setFrameShape(QtWidgets.QFrame.NoFrame)

                wg.setCursor(Fct(cur=cur).CUR())
            except: pass
