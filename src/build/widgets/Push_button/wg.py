from PySide6 import QtWidgets

from . import Classe_wg
from ....build import *
from .. import p_base


class wg:
    def __init__(self,
                 *wgs,
                 type_bouton=None,

                 couleur_bg=p_base.COULEUR_BG,
                 couleur_bg_hover=p_base.COULEUR_BG_HOVER,
                 couleur_bg_checked=p_base.COULEUR_BG_CHECKED,
                 couleur_bg_checked_hover=p_base.COULEUR_BG_CHECKED_HOVER,
                 couleur_bg_pressed=p_base.COULEUR_BG_PRESSED,
                 couleur_bg_checked_pressed=p_base.COULEUR_BG_CHECKED_PRESSED,
                 couleur_fg=p_base.COULEUR_FG,
                 couleur_fg_hover=p_base.COULEUR_FG_HOVER,
                 couleur_fg_checked=p_base.COULEUR_FG_CHECKED,
                 couleur_fg_checked_hover=p_base.COULEUR_FG_CHECKED_HOVER,
                 couleur_fg_pressed=p_base.COULEUR_FG_PRESSED,
                 couleur_fg_checked_pressed=p_base.COULEUR_FG_CHECKED_PRESSED,

                 img_uncheck=p_base.IMG_UNCHECK,
                 tm_uncheck=p_base.TM_UNCHECK,
                 img_hover=p_base.IMG_HOVER,
                 tm_hover=p_base.TM_HOVER,
                 img_check=p_base.IMG_CHECK,
                 tm_check=p_base.TM_CHECK,
                 img_check_hover=p_base.IMG_CHECK_HOVER,
                 tm_check_hover=p_base.TM_CHECK_HOVER,
                 img_width=p_base.IMG_WIDTH,
                 img_height=p_base.IMG_HEIGHT,
                 img_margin_top=0,
                 img_margin_bottom=0,
                 img_margin_right=0,
                 img_margin_left=0,

                 dim_width=p_base.DIM_WG_WIDTH,
                 dim_height=p_base.DIM_WG_HEIGHT,
                 x_ico=p_base.P_style().x_ico(),
                 X_ICO=p_base.P_style().X_ICO(),

                 police=p_base.FONT,
                 police_taille=p_base.FONT_SIZE,
                 bordure_width_top=p_base.BD_WIDTH,
                 bordure_width_bottom=p_base.BD_WIDTH,
                 bordure_width_right=p_base.BD_WIDTH,
                 bordure_width_left=p_base.BD_WIDTH,
                 bordure_style_top=p_base.BD_STYLE,
                 bordure_style_bottom=p_base.BD_STYLE,
                 bordure_style_right=p_base.BD_STYLE,
                 bordure_style_left=p_base.BD_STYLE,
                 bordure_couleur_top=p_base.BD_COULEUR,
                 bordure_couleur_bottom=p_base.BD_COULEUR,
                 bordure_couleur_right=p_base.BD_COULEUR,
                 bordure_couleur_left=p_base.BD_COULEUR,
                 rayon_top_left=p_base.RD_WG,
                 rayon_top_right=p_base.RD_WG,
                 rayon_bottom_right=p_base.RD_WG,
                 rayon_bottom_left=p_base.RD_WG,

                 curseur=p_base.CUR
                 ):
        style = f"""
        QPushButton {{
        background-color: rgba{couleur_bg};
        color: rgb{couleur_fg};
        }}

        QPushButton:hover {{
        background-color: rgba{couleur_bg_hover};
        color: rgb{couleur_fg_hover};
        }}
        
        QPushButton:checked {{
        background-color: rgb{couleur_bg_checked};
        color: rgb{couleur_fg_checked};
        }}

        QPushButton:checked:hover {{
        background-color: rgb{couleur_bg_checked_hover};
        color: rgb{couleur_fg_checked_hover};
        }}

        QPushButton:pressed {{
        background-color: rgba{couleur_bg_pressed};
        color: rgb{couleur_fg_pressed};
        }}
        
        QPushButton:checked:pressed {{
        background-color: rgba{couleur_bg_checked_pressed};
        color: rgb{couleur_fg_checked_pressed};
        }}
                        
        /* BORDURES */
        .QPushButton {{
        border-top: {bordure_width_top}px {bordure_style_top} rgba{bordure_couleur_top};
        border-bottom: {bordure_width_bottom}px {bordure_style_bottom} rgba{bordure_couleur_bottom};
        border-right: {bordure_width_right}px {bordure_style_right} rgba{bordure_couleur_right};
        border-left: {bordure_width_left}px {bordure_style_left} rgba{bordure_couleur_left};
        }}
        
        /* RAYONS */
        .QPushButton {{
        border-top-left-radius: {rayon_top_left}px;
        border-top-right-radius: {rayon_top_right}px;
        border-bottom-right-radius: {rayon_bottom_right}px;
        border-bottom-left-radius: {rayon_bottom_left}px;
        }}"""

        for wg in wgs:
            wg.setStyleSheet(style)

            try:
                Fct(wg=wg, w=dim_width, h=dim_height).DIM()
                wg.setFont(Fct(font=police, font_size=police_taille).FONT())

                wg.setFlat(True)
                wg.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

                wg.setCursor(Fct(cur=curseur).CUR())
            except: pass

            if img_uncheck is not None:
                Fct(wg=wg, img=f"{img_uncheck}{tm_uncheck}", dim=dim_height * x_ico).ICON()

            try:
                if type_bouton is not None:
                    cls = Classe_wg.Classe_wg(wg=wg,
                                              dim_ico=dim_height * x_ico,
                                              DIM_ICO=dim_height * X_ICO,
                                              img=img_uncheck,
                                              img_check=img_check,
                                              tm=tm_uncheck,
                                              tm_hover=tm_hover,
                                              tm_check=tm_check)

                    if type_bouton == "check":
                        wg.mousePressEvent = cls.MP_CHECK
                    elif type_bouton == "ico":
                        wg.enterEvent = cls.ENT_ICO
                        wg.leaveEvent = cls.LVE_ICO
                        wg.mousePressEvent = cls.MP_ICO
                    elif type_bouton == "zoom":
                        wg.enterEvent = cls.ENT_ZOOM
                        wg.leaveEvent = cls.LVE_ZOOM
            except: pass
