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
                 edit,
                 cur
    ):
        bds = Attrs(bd=bd).GET_BD()
        rds = Attrs(rd=rd).GET_RD()


        style_gen = f"""
        /* COMBOBOX */
        QComboBox {{
        color: rgb{colors.get("c3")};
        selection-background-color: rgb{colors.get("c3")};
        selection-color: rgb{colors.get("c1")};
        padding: 1px 0px 1px 3px;
        }}
        
        /* BOUTON DE DEROULEMENT */
        QComboBox::drop-down {{
        width: {dim.get("h")}px;
        border: none;
        }}

        /* IMAGE DU BOUTON DE DEROULEMENT */
        QComboBox::down-arrow {{
        image: url({P_img().fleche_bottom() + "bn1" + ".svg"});
        width: {dim.get("h") * P_style().x_ico()}px;
        height: {dim.get("h") * P_style().x_ico()}px;
        }}
        QComboBox::down-arrow:hover {{
        image: url({P_img().fleche_bottom() + "bn2" + ".svg"});
        width: {dim.get("h") * P_style().x_ico()}px;
        height: {dim.get("h") * P_style().x_ico()}px;
        }}

        /* ELEMENTS DEROULEMENT */
        QComboBox QAbstractItemView::item {{
        background-color: rgb{colors.get("c1")};
        color: rgb{colors.get("c3")};
        border: none;
        }}
        QComboBox QAbstractItemView::item:hover {{
        background-color: rgb{colors.get("c3")};
        color: rgb{colors.get("c1")};
        border: none;
        }}
        

        /* BORDURES */
        QComboBox {{
        border-width: {P_style().bd()}px;
        border-style: solid;
        border-color: rgba{bds.get("o1")} rgba{bds.get("o2")} rgba{bds.get("o3")} rgba{bds.get("o4")};
        padding: {P_style().bd()}px;
        }}
        
        /* RAYONS */
        QComboBox {{
        border-top-left-radius: {rds.get("r1")}px;
        border-top-right-radius: {rds.get("r2")}px;
        border-bottom-right-radius: {rds.get("r4")}px;
        border-bottom-left-radius: {rds.get("r3")}px;
        }}
        
        /* SCROLL */
        QComboBox QScrollBar {{
        background-color: rgb{colors.get("c1")};
        width: 20px;
        height: 20px;
        }}
        QComboBox ::handle:vertical {{
        min-height: 100px;
        }}
        QComboBox ::handle:vertical {{
        min-height: 100px;
        }}
        QComboBox ::handle:horizontal {{
        min-width: 100px;
        }}
        QComboBox QScrollBar::handle {{
        background-color: rgb{colors.get("c3")};
        }}
        QComboBox QScrollBar::add-page, QComboBox QScrollBar::sub-page {{
        background-color: rgb{colors.get("c1")};
        border: rgb{colors.get("c1")};
        }}
"""
        style_type = {
            "th": f"""
            /* COMBOBOX */
            QComboBox {{
            background-color: rgb{colors.get("c1")};
            }}""",

            "tr": """
            /* COMBOBOX */
            QComboBox {
            background-color: rgba(0, 0, 0, 0);
            }"""
        }


        style = style_gen + style_type.get(colors_type)
        for wg in wgs:
            wg.setStyleSheet(style)

            try:
                Fct(wg=wg, w=dim.get("w"), h=dim.get("h")).DIM()
                wg.setFont(Fct(font_size=font).FONT())

                wg.setEditable(edit)

                wg.setCursor(Fct(cur=cur).CUR())
                wg.view().setCursor(Fct(cur=P_cur().souris_main()).CUR())
                if edit:
                    wg.lineEdit().setFont(Fct(font_size=font).FONT())
                    wg.lineEdit().setCursor(Fct(cur=P_cur().IBeam()).CUR())
            except: pass
