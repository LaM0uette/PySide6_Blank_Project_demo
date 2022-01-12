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
                 pad
    ):
        bds = Attrs(bd=bd).GET_BD()
        rds = Attrs(rd=rd).GET_RD()

        for wg in wgs:
            style_gen = f"""
            /* FOND */
            QProgressBar {{
            color: rgb{colors.get("c3")};
            }}
            
            
                
            /* BORDURES */
            .QProgressBar#{wg.objectName()} {{
            border-width: {bd.get("px")}px;
            border-style: solid;
            border-color: rgba{bds.get("o1")} rgba{bds.get("o2")} rgba{bds.get("o3")} rgba{bds.get("o4")};
            padding: {pad}px;
            }}

            /* RAYONS */
            .QProgressBar#{wg.objectName()} {{
            border-top-left-radius: {rds.get("r1")}px;
            border-top-right-radius: {rds.get("r2")}px;
            border-bottom-right-radius: {rds.get("r4")}px;
            border-bottom-left-radius: {rds.get("r3")}px;
            }}"""
            style_type = {
                "th": f"""
                /* FOND */
                QProgressBar {{
                background-color: rgb{colors.get("c1")};
                }}
                
                /* PROGRESS */
                QProgressBar::chunk {{
                background-color: rgb{colors.get("bn1")};
                }}
                """,

                "tr": f"""
                /* FOND */
                QProgressBar {{
                background-color: rgba(0, 0, 0, 0);
                }}
                
                /* PROGRESS */
                QProgressBar::chunk {{
                background-color: rgb{colors.get("c1")};
                }}
                """
            }
            style = style_gen + style_type.get(colors_type)

            wg.setStyleSheet(style)

            try:
                Fct(wg=wg, w=dim.get("w"), h=dim.get("h")).DIM()
                wg.setFont(Fct(font_size=font).FONT())

                wg.setAlignment(P_align().c().c())
            except: pass
