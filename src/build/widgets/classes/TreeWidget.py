from PySide6 import QtCore, QtWidgets

from ....build import *
from ....build.widgets import p_base

class Style:
    def __init__(self,
                 *wgs,
                 dim_width=p_base.WIDTH,
                 dim_height=p_base.HEIGHT,
                 police=p_base.FONT,
                 police_taille=p_base.FONT_SIZE,
                 scroll_h=p_base.SCROLL_H,
                 scroll_v=p_base.SCROLL_V,
                 curseur=p_base.CUR,
    ):
        for wg in wgs:
            wg.setStyleSheet(style)

            Fct(wg=wg, w=dim_width, h=dim_height).DIM()
            wg.setFont(Fct(font=police, font_size=police_taille).FONT())

            wg.setHorizontalScrollBarPolicy(scroll_h)
            wg.setVerticalScrollBarPolicy(scroll_v)

            wg.setFrameShape(QtWidgets.QFrame.NoFrame)

            wg.setCursor(Fct(cur=curseur).CUR())


class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs)
class Base_tr(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              couleur_bg=(0, 0, 0, 0),
              couleur_bg_item=(0, 0, 0, 0),
              couleur_bg_item_hover=(0, 0, 0, 0),
              couleur_bg_item_checked=(0, 0, 0, 0),
              couleur_bg_item_checked_hover=(0, 0, 0, 0),
              couleur_fg_item_checked=P_rgb().bn1(),
              couleur_fg_item_checked_hover=P_rgb().bn2(),
    )

class option(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
              couleur_bg=(0, 0, 0, 0),
              couleur_bg_item=(0, 0, 0, 0),
              couleur_bg_item_hover=(0, 0, 0, 0),
              couleur_bg_item_checked=(0, 0, 0, 0),
              couleur_bg_item_checked_hover=(0, 0, 0, 0),
              couleur_fg_item_checked=P_rgb().bn1(),
              couleur_fg_item_checked_hover=P_rgb().bn2(),
              dim_width=P_dim().h5(),
              bordure_width_right=P_style().bd(),
              bordure_couleur_right=P_rgb().th3(),
              scroll_h=QtCore.Qt.ScrollBarAlwaysOff,
              scroll_v=QtCore.Qt.ScrollBarAlwaysOff,
    )
