from ..Attrs import Attrs
from ....build import *
from .. import p_base


class wg:
    def __init__(
            self,
            *wgs,
            arguments=None,
            couleur_bg=p_base.COLORS.get("c1"),
            couleur_fg=p_base.COLORS.get("c3"),
            couleur_bg_hover=p_base.COLORS.get("c3"),
            couleur_fg_hover=p_base.COLORS.get("c1"),
            couleur_bg_checked=p_base.COLORS.get("c3"),
            couleur_fg_checked=p_base.COLORS.get("c1"),
            couleur_bg_checked_hover=p_base.COLORS.get("c3"),
            couleur_fg_checked_hover=p_base.COLORS.get("bn1"),
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
            style = f"""
            /* CHECKBOX */
            QCheckBox {{
            background-color: rgb{couleur_bg};
            color: rgb{couleur_fg};
            spacing: 10px;
            }}
            QCheckBox:hover {{
            background-color: rgb{couleur_bg_hover};
            color: rgb{couleur_fg_hover};
            }}
            QCheckBox:checked {{
            background-color: rgb{couleur_bg_checked};
            color: rgb{couleur_fg_checked};
            }}
            QCheckBox:checked:hover {{
            background-color: rgb{couleur_bg_checked_hover};
            color: rgb{couleur_fg_checked_hover};
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
            .QCheckBox#{wg.objectName()} {{
            border-width: {bd.get("px")}px;
            border-style: solid;
            border-color: rgba{bds.get("o1")} rgba{bds.get("o2")} rgba{bds.get("o3")} rgba{bds.get("o4")};
            padding: {P_style().bd()}px;
            }}

            /* RAYONS */
            .QCheckBox#{wg.objectName()} {{
            border-top-left-radius: {rds.get("r1")}px;
            border-top-right-radius: {rds.get("r2")}px;
            border-bottom-right-radius: {rds.get("r4")}px;
            border-bottom-left-radius: {rds.get("r3")}px;
            }} """

            wg.setStyleSheet(style)

            try:
                Fct(wg=wg, w=dim.get("w"), h=dim.get("h")).DIM()
                wg.setFont(Fct(font_size=font).FONT())

                wg.setCursor(Fct(cur=cur).CUR())
            except: pass
