from PySide6 import QtWidgets

from ....build.widgets.classes import Classe_pb
from ....build import *
from ....build.widgets import p_base

class Style:
    def __init__(self,
                 *wgs,
                 type_bouton=None,
                 couleur_bg=p_base._COLORS_BG,
                 couleur_bg_hover=p_base._COLORS_BG_HOVER,
                 couleur_bg_checked=p_base._COLORS_BG_CHECKED,
                 couleur_bg_checked_hover=p_base._COLORS_BG_CHECKED_HOVER,
                 couleur_bg_pressed=p_base.COLORS_BG_PRESSED,
                 couleur_bg_checked_pressed=p_base.COLORS_BG_CHECKED_PRESSED,
                 couleur_fg=p_base._COLORS_FG,
                 couleur_fg_hover=p_base._COLORS_FG_HOVER,
                 couleur_fg_checked=p_base._COLORS_FG_CHECKED,
                 couleur_fg_checked_hover=p_base._COLORS_FG_CHECKED_HOVER,
                 couleur_fg_pressed=p_base.COLORS_FG_PRESSED,
                 couleur_fg_checked_pressed=p_base.COLORS_FG_CHECKED_PRESSED,
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
                 dim_width=p_base.WG_WIDTH,
                 dim_height=p_base.WG_HEIGHT,
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

            if img_uncheck is not None and type_bouton is not None:
                Fct(wg=wg, img=f"{img_uncheck}{tm_uncheck}", dim=dim_height * x_ico).ICON()

            try:
                if type_bouton is not None and type_bouton is not None:
                    cls = Classe_pb.Classe_pb(wg=wg,
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


class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs)
class Base_tr(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                 couleur_bg=(0, 0, 0, 0),
                 couleur_bg_hover=(0, 0, 0, 0),
                 couleur_bg_checked=(0, 0, 0, 0),
                 couleur_bg_checked_hover=(0, 0, 0, 0),
                 couleur_fg_checked=p_base.COULEURS.get("c3"),
    )

class menu_top:
    def __init__(self, *wgs):
        self.wgs = wgs

    def rtn(self,
            type_bouton="zoom",
            couleur_bg=(0, 0, 0, 0),
            couleur_bg_hover=(0, 0, 0, 0),
            couleur_bg_checked=(0, 0, 0, 0),
            couleur_bg_checked_hover=(0, 0, 0, 0),
            couleur_fg_checked=p_base.COULEURS.get("c3"),
            couleur_bg_pressed=(0, 0, 0, 0),
            img_uncheck=P_img().main(),
            tm_uncheck="th2",
            dim_width=P_dim().h9()*1.2,
            curseur=P_cur().souris_main()
    ):
        Style(*self.wgs,
                 type_bouton=type_bouton,
                 couleur_bg=couleur_bg,
                 couleur_bg_hover=couleur_bg_hover,
                 couleur_bg_checked=couleur_bg_checked,
                 couleur_bg_checked_hover=couleur_bg_checked_hover,
                 couleur_fg_checked=couleur_fg_checked,
                 couleur_bg_pressed=couleur_bg_pressed,
                 img_uncheck=img_uncheck,
                 tm_uncheck=tm_uncheck,
                 dim_width=dim_width,
                 curseur=curseur
                 )

    def option(self):
        self.rtn(
            img_uncheck=P_img().option()
        )
    def reduire(self):
        self.rtn(
            img_uncheck=P_img().reduire(),
            tm_uncheck="bn1"
        )
    def agrandir(self):
        self.rtn(
            img_uncheck=P_img().agrandir(),
            tm_uncheck="th3"
        )
    def quitter(self):
        self.rtn(
            img_uncheck=P_img().quitter(),
            tm_uncheck="bn2"
        )


class txt(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                 couleur_bg=P_rgb().th1() + (255,),
                 couleur_fg=P_rgb().th3(),
                 couleur_bg_hover=P_rgb().th3() + (255,),
                 couleur_fg_hover=P_rgb().th1(),
                 couleur_bg_pressed=P_rgb().th3() + (255,),

                 bordure_width_top=P_style().bd(),
                 bordure_width_bottom=P_style().bd(),
                 bordure_width_right=P_style().bd(),
                 bordure_width_left=P_style().bd(),
                 bordure_couleur_top=P_rgb().th3() + (255,),
                 bordure_couleur_bottom=P_rgb().th3() + (255,),
                 bordure_couleur_right=P_rgb().th3() + (255,),
                 bordure_couleur_left=P_rgb().th3() + (255,),
    )
class txt_inv(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                 couleur_bg=P_rgb().th3()+(255, ),
                 couleur_fg=P_rgb().th1(),
                 couleur_bg_hover=P_rgb().th1()+(255, ),
                 couleur_fg_hover=P_rgb().th3(),
                 couleur_bg_pressed=P_rgb().th1() + (255,),

                 bordure_width_top=P_style().bd(),
                 bordure_width_bottom=P_style().bd(),
                 bordure_width_right=P_style().bd(),
                 bordure_width_left=P_style().bd(),
                 bordure_couleur_top=P_rgb().th3()+(255, ),
                 bordure_couleur_bottom=P_rgb().th3()+(255, ),
                 bordure_couleur_right=P_rgb().th3()+(255, ),
                 bordure_couleur_left=P_rgb().th3()+(255, ),
    )

class Demo_bd(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                 bordure_width_top=P_style().bd(),
                 bordure_width_bottom=P_style().bd(),
                 bordure_width_right=P_style().bd(),
                 bordure_width_left=P_style().bd(),
                 bordure_couleur_top=P_rgb().bn1() + (255,),
                 bordure_couleur_bottom=P_rgb().bn1() + (255,),
                 bordure_couleur_right=P_rgb().bn1() + (255,),
                 bordure_couleur_left=P_rgb().bn1() + (255,),
    )
class Demo_rd(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                 rayon_top_left=10,
                 rayon_top_right=10,
                 rayon_bottom_left=10,
                 rayon_bottom_right=10,
    )

class ck_ico(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                 type_bouton="check",

                 couleur_bg=(0, 0, 0, 0),
                 couleur_bg_hover=(0, 0, 0, 0),
                 couleur_bg_checked=(0, 0, 0, 0),
                 couleur_bg_checked_hover=(0, 0, 0, 0),
                 couleur_fg_checked=p_base.COULEURS.get("c3"),
                 couleur_bg_pressed=(0, 0, 0, 0),
                 couleur_bg_checked_pressed=(0, 0, 0, 0),
    )
class zoom(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                 type_bouton="zoom",

                 couleur_bg=(0, 0, 0, 0),
                 couleur_bg_hover=(0, 0, 0, 0),
                 couleur_bg_checked=(0, 0, 0, 0),
                 couleur_bg_checked_hover=(0, 0, 0, 0),
                 couleur_fg_checked=p_base.COULEURS.get("c3"),
                 couleur_bg_pressed=(0, 0, 0, 0),
                 couleur_bg_checked_pressed=(0, 0, 0, 0),
                 img_uncheck=P_img().calendrier(),
                 tm_uncheck=""
    )

class dlg_ok(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                 couleur_bg=P_rgb().th1() + (255,),
                 couleur_fg=P_rgb().vert(),
                 couleur_bg_hover=P_rgb().vert() + (255,),
                 couleur_fg_hover=P_rgb().th1(),
                 couleur_bg_pressed=P_rgb().vert() + (255,),
                 bordure_width_top=P_style().bd(),
                 bordure_width_bottom=P_style().bd(),
                 bordure_width_right=P_style().bd(),
                 bordure_width_left=P_style().bd(),
                 bordure_couleur_top=P_rgb().vert() + (255,),
                 bordure_couleur_bottom=P_rgb().vert() + (255,),
                 bordure_couleur_right=P_rgb().vert() + (255,),
                 bordure_couleur_left=P_rgb().vert() + (255,),
                 dim_width=P_dim().h6(),
                 dim_height=None
    )
class dlg_ok_inv(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                 couleur_bg=P_rgb().vert() + (255,),
                 couleur_fg=P_rgb().th1(),
                 couleur_bg_hover=P_rgb().th1() + (255,),
                 couleur_fg_hover=P_rgb().vert(),
                 couleur_bg_pressed=P_rgb().th1() + (255,),
                 bordure_width_top=P_style().bd(),
                 bordure_width_bottom=P_style().bd(),
                 bordure_width_right=P_style().bd(),
                 bordure_width_left=P_style().bd(),
                 bordure_couleur_top=P_rgb().vert() + (255,),
                 bordure_couleur_bottom=P_rgb().vert() + (255,),
                 bordure_couleur_right=P_rgb().vert() + (255,),
                 bordure_couleur_left=P_rgb().vert() + (255,),
                 dim_width=P_dim().h6(),
                 dim_height=None
    )
class dlg_nok(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                 couleur_bg=P_rgb().th1() + (255,),
                 couleur_fg=P_rgb().rouge(),
                 couleur_bg_hover=P_rgb().rouge() + (255,),
                 couleur_fg_hover=P_rgb().th1(),
                 couleur_bg_pressed=P_rgb().rouge() + (255,),
                 bordure_width_top=P_style().bd(),
                 bordure_width_bottom=P_style().bd(),
                 bordure_width_right=P_style().bd(),
                 bordure_width_left=P_style().bd(),
                 bordure_couleur_top=P_rgb().rouge() + (255,),
                 bordure_couleur_bottom=P_rgb().rouge() + (255,),
                 bordure_couleur_right=P_rgb().rouge() + (255,),
                 bordure_couleur_left=P_rgb().rouge() + (255,),
                 dim_width=P_dim().h6(),
                 dim_height=None
    )
class dlg_nok_inv(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                 couleur_bg=P_rgb().rouge()+(255, ),
                 couleur_fg=P_rgb().th1(),
                 couleur_bg_hover=P_rgb().th1()+(255, ),
                 couleur_fg_hover=P_rgb().rouge(),
                 couleur_bg_pressed=P_rgb().th1()+(255, ),
                 bordure_width_top=P_style().bd(),
                 bordure_width_bottom=P_style().bd(),
                 bordure_width_right=P_style().bd(),
                 bordure_width_left=P_style().bd(),
                 bordure_couleur_top=P_rgb().rouge()+(255, ),
                 bordure_couleur_bottom=P_rgb().rouge()+(255, ),
                 bordure_couleur_right=P_rgb().rouge()+(255, ),
                 bordure_couleur_left=P_rgb().rouge()+(255, ),
                 dim_width=P_dim().h6(),
                 dim_height=None
    )

class plein:
    def __init__(self, *wgs):
        self.wgs = wgs


    def rtn(self,
            couleur_bg=(0, 0, 0, 0),
            couleur_fg=(0, 0, 0),
            couleur_bg_hover=(0, 0, 0, 0),
            couleur_fg_hover=(0, 0, 0),
            dim_height=P_dim().h5(),

            bordure_width_top=0,
            bordure_width_bottom=0,
            bordure_width_right=0,
            bordure_width_left=0,
            bordure_couleur_top=(0, 0, 0, 0),
            bordure_couleur_bottom=(0, 0, 0, 0),
            bordure_couleur_right=(0, 0, 0, 0),
            bordure_couleur_left=(0, 0, 0, 0),
            curseur=P_cur().main()
            ):
        Style(*self.wgs,
                 couleur_bg=couleur_bg,
                 couleur_fg=couleur_fg,
                 couleur_bg_hover=couleur_bg_hover,
                 couleur_fg_hover=couleur_fg_hover,
                 dim_height=dim_height,

                 bordure_width_top=bordure_width_top,
                 bordure_width_bottom=bordure_width_bottom,
                 bordure_width_right=bordure_width_right,
                 bordure_width_left=bordure_width_left,
                 bordure_couleur_top=bordure_couleur_top,
                 bordure_couleur_bottom=bordure_couleur_bottom,
                 bordure_couleur_right=bordure_couleur_right,
                 bordure_couleur_left=bordure_couleur_left,
                 curseur=curseur
                 )

    def th1(self):
        self.rtn(
            couleur_bg=P_rgb().th1()+(255, ),
            couleur_fg=P_rgb().th3(),
            couleur_bg_hover=P_rgb().th1()+(255, ),
            couleur_fg_hover=P_rgb().th3()+(255, ),

            bordure_width_top=P_style().bd(),
            bordure_width_bottom=P_style().bd(),
            bordure_width_right=P_style().bd(),
            bordure_width_left=P_style().bd(),
            bordure_couleur_top=P_rgb().th2() + (255,),
            bordure_couleur_bottom=P_rgb().th2() + (255,),
            bordure_couleur_right=P_rgb().th2() + (255,),
            bordure_couleur_left=P_rgb().th2() + (255,),
        )
    def th2(self):
        self.rtn(
            couleur_bg=P_rgb().th2()+(255, ),
            couleur_fg=P_rgb().th3(),
            couleur_bg_hover=P_rgb().th2()+(255, ),
            couleur_fg_hover=P_rgb().th3()+(255, ),
        )
    def th3(self):
        self.rtn(
            couleur_bg=P_rgb().th3()+(255, ),
            couleur_fg=P_rgb().th1(),
            couleur_bg_hover=P_rgb().th3()+(255, ),
            couleur_fg_hover=P_rgb().th1()+(255, ),
        )
    def bn1(self):
        self.rtn(
            couleur_bg=P_rgb().bn1()+(255, ),
            couleur_fg=P_rgb().th3(),
            couleur_bg_hover=P_rgb().bn1()+(255, ),
            couleur_fg_hover=P_rgb().th3()+(255, ),
        )
    def bn2(self):
        self.rtn(
            couleur_bg=P_rgb().bn2()+(255, ),
            couleur_fg=P_rgb().th3(),
            couleur_bg_hover=P_rgb().bn2()+(255, ),
            couleur_fg_hover=P_rgb().th3()+(255, ),
        )
