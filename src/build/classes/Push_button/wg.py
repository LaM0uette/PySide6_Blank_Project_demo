from ..Attrs import Attrs
from .. import Classe_wg
from ....build import *


class wg:
    def __init__(self,
                 *wgs,
                 pb_type,
                 colors_type,
                 colors,
                 x_ico,
                 X_ICO,
                 dim,
                 img,
                 img_check,
                 tm,
                 tm_hover,
                 tm_check,
                 font,
                 bd,
                 rd,
                 cur
    ):  # sourcery no-metrics
        bds = Attrs(bd=bd).GET_BD()
        rds = Attrs(rd=rd).GET_RD()

        for wg in wgs:
            style_gen = f"""
            /* BORDURES */
            QPushButton {{
            border-width: {bd.get("px")}px;
            border-style: solid;
            border-color: rgba{bds.get("o1")} rgba{bds.get("o2")} rgba{bds.get("o3")} rgba{bds.get("o4")};
            }}

            /* RAYONS */
            QPushButton {{
            border-top-left-radius: {rds.get("r1")}px;
            border-top-right-radius: {rds.get("r2")}px;
            border-bottom-right-radius: {rds.get("r4")}px;
            border-bottom-left-radius: {rds.get("r3")}px;
            }}
            """
            style_type = {
                "txt": f"""
                QPushButton {{
                background-color: rgba{colors.get("c3")};
                color: rgb{colors.get("c1")};
                border: {P_style().bd()}px solid rgb{colors.get("c1")};
                }}
                
                QPushButton:hover {{
                background-color: rgb{colors.get("c1")};
                color: rgb{colors.get("c3")};
                border: {P_style().bd()}px solid rgb{colors.get("c1")};
                }}

                QPushButton:pressed {{
                color: rgb{colors.get("bn1")};
                }}""",

                "txt_inv": f"""
                QPushButton {{
                background-color: rgb{colors.get("c1")};
                color: rgb{colors.get("c3")};
                border: {P_style().bd()}px solid rgb{colors.get("c1")};
                }}
                
                QPushButton:hover {{
                background-color: rgba{colors.get("c3")};
                color: rgb{colors.get("c1")};
                border: {P_style().bd()}px solid rgb{colors.get("c1")};
                }}

                QPushButton:pressed {{
                color: rgb{colors.get("bn1")};
                }}""",

                "th": f"""
                QPushButton {{
                background-color: rgb{colors.get("c1")};
                color: rgb{colors.get("c3")};
                }}
                
                QPushButton:hover {{
                background-color: rgb{colors.get("c1")};
                color: rgb{colors.get("bn1")};
                }}
                
                QPushButton:checked {{
                background-color: rgb{colors.get("c3")};
                color: rgb{colors.get("c1")};
                }}
                
                QPushButton:checked:hover {{
                background-color: rgb{colors.get("c3")};
                color: rgb{colors.get("bn1")};
                }}

                QPushButton:pressed {{
                color: rgb{colors.get("bn2")};
                }}
                
                QPushButton:checked:pressed {{
                color: rgb{colors.get("bn2")};
                }}
                
                QPushButton:flat {{
                border: none;
                }}""",

                "tr": f"""
                QPushButton {{
                color: rgb{colors.get("c3")};
                }}
                
                QPushButton:hover {{
                color: rgb{colors.get("bn1")};
                }}
                
                QPushButton:checked:hover {{
                color: rgb{colors.get("bn1")};
                }}

                QPushButton:pressed {{
                color: rgb{colors.get("bn2")};
                }}
                
                QPushButton:checked:pressed {{
                color: rgb{colors.get("bn2")};
                }}
                
                QPushButton:flat {{
                border: none;
                }}""",

                "zoom": f"""
                QPushButton {{
                background-color: rgb{colors.get("c1")};
                color: rgb{colors.get("c3")};
                }}
                
                QPushButton:checked {{
                background-color: rgb{colors.get("c3")};
                }}

                QPushButton:pressed {{
                color: rgb{colors.get("bn1")};
                }}
                
                QPushButton:checked:pressed {{
                color: rgb{colors.get("bn1")};
                }}
                
                QPushButton:flat {{
                border: none;
                }}""",

                "uni": f"""
                QPushButton {{
                background-color: rgb{colors.get("c1")};
                color: rgb{colors.get("c1")};
                }}

                QPushButton:pressed {{
                color: rgb{colors.get("bn1")};
                }}
                
                QPushButton:flat {{
                border: none;
                }}"""
            }
            style = style_gen + style_type.get(colors_type)

            wg.setStyleSheet(style)

            try:
                Fct(wg=wg, w=dim.get("w"), h=dim.get("h")).DIM()
                wg.setFont(Fct(font_size=font).FONT())

                if img is not None:
                    Fct(wg=wg, img=f"{img}{tm}", dim=dim.get("h") * x_ico).ICON()

                wg.setFlat(True)

                wg.setCursor(Fct(cur=cur).CUR())
            except: pass

            try:
                if pb_type is not None:
                    cls = Classe_wg.Classe_wg(wg=wg,
                                                dim_ico=dim.get("h") * x_ico,
                                                DIM_ICO=dim.get("h") * X_ICO,
                                                img=img,
                                                img_check=img_check,
                                                tm=tm,
                                                tm_hover=tm_hover,
                                                tm_check=tm_check)

                    if pb_type == "check":
                        wg.mousePressEvent = cls.MP_CHECK
                    elif pb_type == "ico":
                        wg.enterEvent = cls.ENT_ICO
                        wg.leaveEvent = cls.LVE_ICO
                        wg.mousePressEvent = cls.MP_ICO
                    elif pb_type == "zoom":
                        wg.enterEvent = cls.ENT_ZOOM
                        wg.leaveEvent = cls.LVE_ZOOM
            except: pass
