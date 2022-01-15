from ..Attrs import Attrs
from ....build import *


class wg:
    def __init__(self,
                 *wgs,
                 colors_type,
                 colors,
                 dim,
                 img,
                 img_check,
                 tm,
                 tm_check,
                 font,
                 bd,
                 rd,
                 cur
    ):
        bds = Attrs(bd=bd).GET_BD()
        rds = Attrs(rd=rd).GET_RD()

        for wg in wgs:
            style_gen = f"""
            QRadioButton:hover {{
            color: rgb{colors.get("bn1")};
            }}

            QRadioButton:checked:hover {{
            color: rgb{colors.get("bn1")};
            }}

            QRadioButton:flat {{
            border: none;
            }}
            
            QRadioButton::indicator {{
            margin-left: {(dim.get('h') - (dim.get('h') * P_style().x_ico())) / 2}px;
            width: {dim.get('h') * P_style().x_ico()}px;
            height: {dim.get('h') * P_style().x_ico()}px
            }}
            
            QRadioButton::indicator:unchecked {{
            image: url({img + tm + '.svg'});
            }}
            
            QRadioButton::indicator:disabled {{
            image: url({img + tm + '.svg'});
            }}
            
            QRadioButton::indicator:checked {{
            image: url({img_check + tm_check + '.svg'});
            }}
            


            /* BORDURES */
            .QRadioButton#{wg.objectName()} {{
            border-width: {bd.get("px")}px;
            border-style: solid;
            border-color: rgba{bds.get("o1")} rgba{bds.get("o2")} rgba{bds.get("o3")} rgba{bds.get("o4")};
            padding: {P_style().bd()}px;
            }}

            /* RAYONS */
            .QRadioButton#{wg.objectName()} {{
            border-top-left-radius: {rds.get("r1")}px;
            border-top-right-radius: {rds.get("r2")}px;
            border-bottom-right-radius: {rds.get("r4")}px;
            border-bottom-left-radius: {rds.get("r3")}px;
            }}
            """
            style_type = {
                "th": f"""
                QRadioButton {{
                background-color: rgb{colors.get("c1")};
                color: rgb{colors.get("c3")};
                }}
                
                QRadioButton:checked {{
                background-color: rgb{colors.get("c3")};
                color: rgb{colors.get("c1")};
                }}
                
                QRadioButton:checked:hover {{
                background-color: rgb{colors.get("c3")};
                }}
                """,

                "tr": f"""
                QRadioButton {{
                color: rgb{colors.get("c3")};
                spacing: 10px;
                }}
                """
            }
            style = style_gen + style_type.get(colors_type)

            wg.setStyleSheet(style)

            try:
                Fct(wg=wg, w=dim.get("w"), h=dim.get("h")).DIM()
                wg.setFont(Fct(font_size=font).FONT())

                wg.setCursor(Fct(cur=cur).CUR())
            except: pass
