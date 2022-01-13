from PySide6 import QtGui

from ..Attrs import Attrs
from ....build import *


class wg:
    def __init__(self,
                 *wgs,
                 colors_type,
                 colors,
                 dim,
                 font,
                 align,
                 bd,
                 rd,
    ):
        bds = Attrs(bd=bd).GET_BD()
        rds = Attrs(rd=rd).GET_RD()

        for wg in wgs:
            style_gen = f"""
            QLineEdit, QPlainTextEdit, QTextEdit {{
            selection-background-color: rgb{colors.get("c3")};
            selection-color: rgb{colors.get("c1")};
            }}
            
            /* BORDURES */
            .QLineEdit#{wg.objectName()}, .QPlainTextEdit#{wg.objectName()}, .QTextEdit#{wg.objectName()} {{
            border-width: {bd.get("px")}px;
            border-style: solid;
            border-color: rgba{bds.get("o1")} rgba{bds.get("o2")} rgba{bds.get("o3")} rgba{bds.get("o4")};
            }}

            /* RAYONS */
            .QLineEdit#{wg.objectName()}, .QPlainTextEdit#{wg.objectName()}, .QTextEdit#{wg.objectName()} {{
            border-top-left-radius: {rds.get("r1")}px;
            border-top-right-radius: {rds.get("r2")}px;
            border-bottom-right-radius: {rds.get("r4")}px;
            border-bottom-left-radius: {rds.get("r3")}px;
            }}

            /* SCROLL */
            QPlainTextEdit QScrollBar, QTextEdit QScrollBar {{
            background-color: rgb{colors.get("c1")};
            width: 20px;
            height: 20px;
            }}
            QPlainTextEdit::handle:vertical, QTextEdit::handle:vertical {{
            min-height: 100px;
            }}
            QPlainTextEdit::handle:vertical, QTextEdit::handle:vertical {{
            min-height: 100px;
            }}
            QPlainTextEdit::handle:horizontal, QTextEdit::handle:horizontal {{
            min-width: 100px;
            }}
            QPlainTextEdit QScrollBar::handle, QTextEdit QScrollBar::handle {{
            background-color: rgb{colors.get("c3")};
            }}
            QPlainTextEdit QScrollBar::add-page, QPlainTextEdit QScrollBar::sub-page, QTextEdit QScrollBar::add-page, QTextEdit QScrollBar::sub-page {{
            background-color: rgb{colors.get("c1")};
            border: rgb{colors.get("c1")};
            }}
            """
            style_type = {
                "th": f"""
                QLineEdit, QPlainTextEdit, QTextEdit {{
                background-color: rgb{colors.get("c1")};
                color: rgb{colors.get("bn1")};
                }}
                
                QLineEdit[text=''], QPlainTextEdit[plainText=''], QTextEdit[plainText=''] {{
                color: rgb{colors.get("c3")};
                }}
                """,

                "tr": f"""
                QLineEdit, QPlainTextEdit, QTextEdit {{
                background-color: rgba(0, 0, 0, 0);
                color: rgb{colors.get("bn1")};
                }}
                
                QLineEdit[text=''], QPlainTextEdit[plainText=''], QTextEdit[plainText=''] {{
                color: rgb{colors.get("c3")};
                }}
                """
            }
            style = style_gen + style_type.get(colors_type)

            wg.setStyleSheet(style)

            try:
                Fct(wg=wg, w=dim.get("w"), h=dim.get("h")).DIM()
                wg.setFont(Fct(font_size=font).FONT())

                wg.setAlignment(align)

                wg.setCursor(Fct(cur=P_cur().IBeam()).CUR())
            except: pass

            try:wg.viewport().setCursor(Fct(cur=P_cur().IBeam()).CUR())
            except: pass

            try: wg.textChanged.connect(lambda: wg.setStyleSheet(style))
            except: pass
