from ..Attrs import Attrs
from ....build import *


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
        bds = Attrs(bd=bd).GET_BD()
        rds = Attrs(rd=rd).GET_RD()

        for wg in wgs:
            style_gen = f"""
            /* LIST_WIDGET */
            QListWidget {{
            color: rgb{colors.get("c3")};
            border: {bd.get("px")}px solid rgb{colors.get("c3")};
            }}
            
            /* ITEM */
            QListWidget::item {{
            color: rgb{colors.get("c3")};
            }}
            QListWidget::item:selected {{
            color: rgb{colors.get("bn1")};
            }}
            QListWidget::item:hover {{
            color: rgb{colors.get("bn1")};
            }}
            QListWidget::item:selected:hover {{
            color: rgb{colors.get("bn2")};
            }}



            /* BORDURES */
            QListWidget {{
            border-width: {bd.get("px")}px;
            border-style: solid;
            border-color: rgba{bds.get("o1")} rgba{bds.get("o2")} rgba{bds.get("o3")} rgba{bds.get("o4")};
            }}

            /* RAYONS */
            QListWidget {{
            border-top-left-radius: {rds.get("r1")}px;
            border-top-right-radius: {rds.get("r2")}px;
            border-bottom-right-radius: {rds.get("r4")}px;
            border-bottom-left-radius: {rds.get("r3")}px;
            }}
            
            /* SCROLL */
            QListWidget QScrollBar {{
            background-color: rgb{colors.get("c1")};
            width: 20px;
            height: 20px;
            }}
            QListWidget ::handle:vertical {{
            min-height: 100px;
            }}
            QListWidget ::handle:vertical {{
            min-height: 100px;
            }}
            QListWidget ::handle:horizontal {{
            min-width: 100px;
            }}
            QListWidget QScrollBar::handle {{
            background-color: rgb{colors.get("c3")};
            }}
            QListWidget QScrollBar::add-page, QListWidget QScrollBar::sub-page {{
            background-color: rgb{colors.get("c1")};
            border: rgb{colors.get("c1")};
            }}
            """
            style_type = {
                "th": f"""
                /* LIST_WIDGET */
                QListWidget {{
                background-color: rgb{colors.get("c1")};
                }}
                
                /* ITEM */
                QListWidget::item {{
                background-color: rgb{colors.get("c1")};
                }}
                QListWidget::item:selected {{
                background-color: rgb{colors.get("c2")};
                }}""",

                "tr": """
                /* LIST_WIDGET */
                QListWidget {
                background-color: rgba(0, 0, 0, 0);
                }
                
                /* ITEM */
                QListWidget::item {
                background-color: rgba(0, 0, 0, 0);
                }
                QListWidget::item:selected {
                background-color: rgba(0, 0, 0, 0);
                }"""
            }
            style = style_gen + style_type.get(colors_type)

            wg.setStyleSheet(style)

            try:
                Fct(wg=wg, w=dim.get("w"), h=dim.get("h")).DIM()
                wg.setFont(Fct(font_size=font).FONT())

                wg.setHorizontalScrollBarPolicy(scroll.get("h"))
                wg.setVerticalScrollBarPolicy(scroll.get("v"))

                wg.setCursor(Fct(cur=cur).CUR())
                wg.view().setCursor(Fct(cur=P_cur().souris_main()).CUR())
            except: pass
