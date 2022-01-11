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
                 word_wrap,
                 bd,
                 rd,
    ):
        bds = Attrs(bd=bd).GET_BD()
        rds = Attrs(rd=rd).GET_RD()

        for wg in wgs:
            style_gen = f"""
                    /* BORDURES */
                    .QLabel#{wg.objectName()} {{
                    border-width: {bd.get("px")}px;
                    border-style: solid;
                    border-color: rgba{bds.get("o1")} rgba{bds.get("o2")} rgba{bds.get("o3")} rgba{bds.get("o4")};
                    }}

                    /* RAYONS */
                    .QLabel#{wg.objectName()} {{
                    border-top-left-radius: {rds.get("r1")}px;
                    border-top-right-radius: {rds.get("r2")}px;
                    border-bottom-right-radius: {rds.get("r4")}px;
                    border-bottom-left-radius: {rds.get("r3")}px;
                    }}
            """
            style_type = {
                "th": f"""
                /* LABEL */
                QLabel {{
                background-color: rgb{colors.get("c1")};
                color: rgb{colors.get("c3")};
                }}""",

                "tr": f"""
                /* LABEL */
                QLabel {{
                background-color: rgba(0, 0, 0, 0);
                color: rgb{colors.get("c1")};
                }}"""
            }
            style = style_gen + style_type.get(colors_type)

            wg.setStyleSheet(style)

            try:
                Fct(wg=wg, w=dim.get("w"), h=dim.get("h")).DIM()
                wg.setFont(Fct(font_size=font).FONT())

                wg.setAlignment(align)
                wg.setWordWrap(word_wrap)
            except: pass
