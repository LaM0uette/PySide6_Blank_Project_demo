from ..Attrs import Attrs
from ....build import *
from ....config import *
from .. import p_base


class wg:
    def __init__(
            self,
            *wgs,
            couleur_bg=p_base.COLORS.get("c1"),
            couleur_fg=p_base.COLORS.get("c3"),
            couleur_bg_hover=p_base.COLORS.get("c1"),
            couleur_fg_hover=p_base.COLORS.get("bn1"),
            couleur_bg_checked=p_base.COLORS.get("c3"),
            couleur_fg_checked=p_base.COLORS.get("c1"),
            couleur_bg_checked_hover=p_base.COLORS.get("c3"),
            couleur_fg_checked_hover=p_base.COLORS.get("bn1"),
            wg_dim_width=None,
            wg_dim_height=None,
            img_uncheck=P_img().check(),
            tm_uncheck=p_base.TM_UNCHECK,
            img_disable=P_img().check(),
            tm_disable=p_base.TM_DISABLE,
            img_check=P_img().valider(),
            tm_check=p_base.TM_CHECK,
            img_margin_top=0,
            img_margin_bottom=0,
            img_margin_right=0,
            img_margin_left=0,
            img_width=0,
            img_height=0,
            bordure_width=P_style().bd(),
            bordure_style="solid",
            police=config.font,
            taille_police=p_base.FONT,
            curseur=p_base.CUR
    ):
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
                    margin-top: {img_margin_top}px;
                    margin-bottom: {img_margin_bottom}px;
                    margin-right: {img_margin_right}px;
                    margin-left: {img_margin_left}px;
                    width: {img_width}px;
                    height: {img_height}px
                    }}
                    QCheckBox::indicator:unchecked {{
                    image: url({f"{img_uncheck}{tm_uncheck}.svg"});
                    }}
                    QCheckBox::indicator:disabled {{
                    image: url({f"{img_disable}{tm_disable}.svg"});
                    }}
                    QCheckBox::indicator:checked {{
                    image: url({f"{img_check}{tm_check}.svg"});
                    }}"""

        for wg in wgs:
            wg.setStyleSheet(style)

            try:
                Fct(wg=wg, w=wg_dim_width, h=wg_dim_height).DIM()
                wg.setFont(Fct(font=police, font_size=taille_police).FONT())

                wg.setCursor(Fct(cur=curseur).CUR())
            except: pass


"""
        # bds = Attrs(bd=bd).GET_BD()
        # rds = Attrs(rd=rd).GET_RD()
        
/* BORDURES */
.QCheckBox {{
border-width: {bordure_width}px;
border-style: {bordure_style};
border-color: rgba{bds.get("o1")} rgba{bds.get("o2")} rgba{bds.get("o3")} rgba{bds.get("o4")};
padding: {P_style().bd()}px;
}}

/* RAYONS */
.QCheckBox {{
border-top-left-radius: {rds.get("r1")}px;
border-top-right-radius: {rds.get("r2")}px;
border-bottom-right-radius: {rds.get("r4")}px;
border-bottom-left-radius: {rds.get("r3")}px;
"""