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
                    /* CHECKBOX */
                    QCheckBox {{
                    color: rgb{colors.get("c3")};
                    }}
                    QCheckBox:hover {{
                    color: rgb{colors.get("bn1")};
                    }}
                    QCheckBox:checked:hover {{
                    color: rgb{colors.get("bn1")};
                    }}
                    QCheckBox:flat {{
                    border: none;
                    }}

                    /* IMG */
                    QCheckBox::indicator {{
                    margin-left: {(dim.get('h') - (dim.get('h') * P_style().x_ico())) / 2}px;
                    width: {dim.get('h') * P_style().x_ico()}px;
                    height: {dim.get('h') * P_style().x_ico()}px
                    }}
                    QCheckBox::indicator:unchecked {{
                    image: url({img + tm + '.svg'});
                    }}
                    QCheckBox::indicator:disabled {{
                    image: url({img + tm + '.svg'});
                    }}
                    QCheckBox::indicator:checked {{
                    image: url({img_check + tm_check + '.svg'});
                    }}


                    /* BORDURES */
                    QCheckBox {{
                    border-width: {bd.get("px")}px;
                    border-style: solid;
                    border-color: rgba{bds.get("o1")} rgba{bds.get("o2")} rgba{bds.get("o3")} rgba{bds.get("o4")};
                    padding: {P_style().bd()}px;
                    }}

                    /* RAYONS */
                    QCheckBox {{
                    border-top-left-radius: {rds.get("r1")}px;
                    border-top-right-radius: {rds.get("r2")}px;
                    border-bottom-right-radius: {rds.get("r4")}px;
                    border-bottom-left-radius: {rds.get("r3")}px;
                    }}
            """
            style_type = {
                "th": f"""
                        QCheckBox {{
                        background-color: rgb{colors.get("c1")};
                        spacing: 10px;
                        }}
                        QCheckBox:hover {{
                        background-color: rgb{colors.get("c1")};
                        }}
                        QCheckBox:checked {{
                        background-color: rgb{colors.get("c3")};
                        color: rgb{colors.get("c1")};
                        }}
                        QCheckBox:checked:hover {{
                        background-color: rgb{colors.get("c3")};
                        }}""",
                "tr": f"""
                        QCheckBox {{
                        background-color: rgba(0, 0, 0, 0);
                        spacing: 10px;
                        }}
                        QCheckBox:hover {{
                        background-color: rgba(0, 0, 0, 0);
                        }}
                        QCheckBox:checked {{
                        background-color: rgba(0, 0, 0, 0);
                        color: rgb{colors.get("c3")};
                        }}
                        QCheckBox:checked:hover {{
                        background-color: rgba(0, 0, 0, 0);
                        }}"""
            }
            style = style_gen + style_type.get(colors_type)

            wg.setStyleSheet(style)

            try:
                Fct(wg=wg, w=dim.get("w"), h=dim.get("h")).DIM()
                wg.setFont(Fct(font_size=font).FONT())

                wg.setCursor(Fct(cur=cur).CUR())
            except: pass
