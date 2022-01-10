from PySide6 import QtWidgets

from ..Attrs import Attrs
from ....build import *


class wg:
    def __init__(self,
                 *wgs,
                 colors_type,
                 colors,
                 dim,
                 bd,
                 rd,
    ):
        bds = Attrs(bd=bd).GET_BD()
        rds = Attrs(rd=rd).GET_RD()

        for wg in wgs:
            style_gen = f"""
                    /* BORDURES */
                    .QFrame#{wg.objectName()} {{
                    border-width: {P_style().bd()}px;
                    border-style: solid;
                    border-color: rgba{bds.get("o1")} rgba{bds.get("o2")} rgba{bds.get("o3")} rgba{bds.get("o4")};
                    padding: {P_style().bd()}px;
                    }}

                    /* RAYONS */
                    .QFrame#{wg.objectName()} {{
                    border-top-left-radius: {rds.get("r1")}px;
                    border-top-right-radius: {rds.get("r2")}px;
                    border-bottom-right-radius: {rds.get("r4")}px;
                    border-bottom-left-radius: {rds.get("r3")}px;
                    }}
            """
            style_type = {
                "th": f"""
                        /* FRAME */
                        .QFrame#{wg.objectName()} {{
                        background-color: rgb{colors.get("c1")};
                        }}""",
                "tr": f"""
                        /* FRAME */
                        .QFrame#{wg.objectName()} {{
                        background-color: rgba(0, 0, 0, 0);
                        }}"""
            }
            style = style_gen + style_type.get(colors_type)

            wg.setStyleSheet(style)

            try:
                Fct(wg=wg, w=dim.get("w"), h=dim.get("h")).DIM()

                wg.setFrameShape(QtWidgets.QFrame.NoFrame)
            except: pass
