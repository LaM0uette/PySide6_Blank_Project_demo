from PySide6 import QtWidgets, QtCore

from ..Attrs import Attrs
from ....build import *


class wg:
    def __init__(self,
                 *wgs,
                 colors_type,
                 colors,
                 dim,
                 tm,
                 font,
                 bd,
                 rd,
                 align,
                 pb_sb,
                 pb_side,
                 no_focus,
                 val_min,
                 val_max,
                 step,
                 cur
    ):
        bds = Attrs(bd=bd).GET_BD()
        rds = Attrs(rd=rd).GET_RD()

        dim_h = 0 if dim["h"] is None else dim["h"]

        if no_focus and colors_type != "tr":
            select_bg = f"""
            selection-background-color: rgba(0, 0, 0, 0);
            selection-color: rgb{colors.get("c3")};"""
        elif no_focus:
            select_bg = f"""
            selection-background-color: rgba(0, 0, 0, 0);
            selection-color: rgb{colors.get("c1")};"""
        else:
            select_bg = f"""
            selection-background-color: rgb{colors.get("c3")};
            selection-color: rgb{colors.get("c1")};"""

        if pb_sb == QtWidgets.QAbstractSpinBox.ButtonSymbols.PlusMinus:
            pb_up = P_img().plus()
            pb_down = P_img().moins()
        elif pb_sb == QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows:
            pb_up = P_img().fleche_top()
            pb_down = P_img().fleche_bottom()
        else:
            pb_up = ""
            pb_down = ""

        for wg in wgs:
            style_gen = f"""
            /* BORDURES */
            .QSpinBox#{wg.objectName()}, .QDoubleSpinBox#{wg.objectName()} {{
            border-width: {bd.get("px")}px;
            border-style: solid;
            border-color: rgba{bds.get("o1")} rgba{bds.get("o2")} rgba{bds.get("o3")} rgba{bds.get("o4")};
            }}

            /* RAYONS */
            .QSpinBox#{wg.objectName()}, .QDoubleSpinBox#{wg.objectName()} {{
            border-top-left-radius: {rds.get("r1")}px;
            border-top-right-radius: {rds.get("r2")}px;
            border-bottom-right-radius: {rds.get("r4")}px;
            border-bottom-left-radius: {rds.get("r3")}px;
            }}
            """
            style_type = {
                "th": f"""
                /* SPIN_BOX */
                QSpinBox, QDoubleSpinBox {{
                background-color: rgb{colors.get("c1")};
                color: rgb{colors.get("c3")};
                {select_bg}
                }}""",

                "tr": f"""
                /* SPIN_BOX */
                QSpinBox, QDoubleSpinBox {{
                background-color: rgba(0, 0, 0, 0);
                color: rgb{colors.get("c1")};
                {select_bg}
                }}
                """
            }
            style_pb = {
                "lr": f"""
                    QSpinBox::up-button, QDoubleSpinBox::up-button  {{
                    subcontrol-origin: margin;
                    subcontrol-position: center right;
                    right: {(dim_h - (dim_h  * P_style().x_ico())) / 2}px;
                    image: url({pb_up + tm + ".svg"});
                    height: {dim_h * P_style().x_ico() / 1.6}px;
                    width: {dim_h * P_style().x_ico() / 1.6}px;
                    }}

                    QSpinBox::down-button, QDoubleSpinBox::down-button  {{
                    subcontrol-origin: margin;
                    subcontrol-position: center left;
                    left: {(dim_h - (dim_h  * P_style().x_ico())) / 2}px;
                    image: url({pb_down + tm + ".svg"});
                    height: {dim_h * P_style().x_ico() / 1.6}px;
                    width: {dim_h * P_style().x_ico() / 1.6}px;
                    }}""",

                "tb": f"""
                    QSpinBox::up-button, QDoubleSpinBox::up-button  {{
                    subcontrol-position: top right;
                    top: {(dim_h - (dim_h  * P_style().x_ico())) / 4}px;
                    right: {(dim_h - (dim_h  * P_style().x_ico())) / 4}px;
                    image: url({pb_up + tm + ".svg"});
                    height: {dim_h  * P_style().x_ico() / 2}px;
                    width: {dim_h  * P_style().x_ico() / 2}px;
                    }}

                    QSpinBox::down-button, QDoubleSpinBox::down-button  {{
                    subcontrol-position: bottom right;
                    bottom: {(dim_h - (dim_h  * P_style().x_ico())) / 4}px;
                    right: {(dim_h - (dim_h  * P_style().x_ico())) / 4}px;
                    image: url({pb_down + tm + ".svg"});
                    height: {dim_h  * P_style().x_ico() / 2}px;
                    width: {dim_h  * P_style().x_ico() / 2}px;
                    }}"""
            }
            style = style_gen + style_type.get(colors_type) + style_pb.get(pb_side)

            wg.setStyleSheet(style)

            try: Fct(wg=wg, w=dim.get("w"), h=dim.get("h")).DIM()
            except: pass

            try:
                wg.setFont(Fct(font_size=font).FONT())

                wg.setAlignment(align)
                wg.setButtonSymbols(pb_sb)

                wg.setMinimum(val_min)
                wg.setMaximum(val_max)
                wg.setSingleStep(step)

                wg.setFrame(QtWidgets.QFrame.NoFrame)
                wg.setButtonSymbols(pb_sb)
                if no_focus: wg.setFocusPolicy(QtCore.Qt.NoFocus)

                wg.setCursor(Fct(cur=cur).CUR())
                if colors_type != "tr":
                    wg.lineEdit().setCursor(Fct(cur=P_cur().IBeam()).CUR())
                else:
                    wg.lineEdit().setCursor(Fct(cur=P_cur().souris_main()).CUR())
            except: pass
