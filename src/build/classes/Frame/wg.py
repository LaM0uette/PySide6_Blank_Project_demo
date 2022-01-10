from PySide6 import QtWidgets

from ..Attrs import Attrs
from ....build import *


class wg:
    def __init__(self,
                 *wgs,
                 colors,
                 dim,
                 bd,
                 rd,
    ):
        bds = Attrs(bd=bd).GET_BD()
        rds = Attrs(rd=rd).GET_RD()


        style = f"""
        /* FRAME */
        QFrame {{
        background-color: rgb{colors.get("c1")};
        }}
        
        
        /* BORDURES */
        QCheckBox {{
        border-width: {P_style().bd()}px;
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


        for wg in wgs:
            wg.setStyleSheet(style)

            try:
                Fct(wg=wg, w=dim.get("w"), h=dim.get("h")).DIM()

                wg.setFrameShape(QtWidgets.QFrame.NoFrame)
            except: pass
