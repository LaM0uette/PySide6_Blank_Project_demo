from .StyleSheet import StyleSheet
from PySide6 import QtCore

from ....build import *
from ....build.widgets import p_base
from ....config import vrb

class Style:
    def __init__(
            self,
            *wgs,
            width=p_base.WG_WIDTH,
            height=p_base.WG_HEIGHT,

            # Police
            font=p_base.FONT,
            font_size=p_base.FONT_SIZE,

            # Images margin
            img_margin_top=(p_base.WG_HEIGHT - p_base.IMG_HEIGHT)/2,
            img_margin_bottom=0,
            img_margin_right=(p_base.WG_HEIGHT - p_base.IMG_HEIGHT)/2,
            img_margin_left=0,

            # Bordures GEN
            border_gen_all=None,
            border_gen_style=None,
            border_gen_rgb=None,
            border_gen_top=None, border_gen_bottom=None, border_gen_right=None, border_gen_left=None,
            # Bordures
            border_all=None,
            border_style=p_base.WG_BORDER_STYLE,
            border_rgb=p_base.WG_BORDER_RGB,
            border_top=p_base.WG_BORDER_WIDTH, border_bottom=p_base.WG_BORDER_WIDTH, border_right=p_base.WG_BORDER_WIDTH, border_left=p_base.WG_BORDER_WIDTH,
            # Bordures hover
            border_all_hover=None,
            border_style_hover=p_base.WG_BORDER_STYLE,
            border_rgb_hover=p_base.WG_BORDER_RGB,
            border_top_hover=p_base.WG_BORDER_WIDTH, border_bottom_hover=p_base.WG_BORDER_WIDTH, border_right_hover=p_base.WG_BORDER_WIDTH, border_left_hover=p_base.WG_BORDER_WIDTH,
            # Bordures jours
            border_day_size=P_style().bd(),
            border_day_style=p_base.WG_BORDER_STYLE,
            border_day_rgb=p_base.FG_ITEM_HOVER,

            # Rayons
            radius_all=None,
            radius_top_right=p_base.WG_RADIUS,
            radius_top_left=p_base.WG_RADIUS,
            radius_bottom_right=p_base.WG_RADIUS,
            radius_bottom_left=p_base.WG_RADIUS,

            # Paramètres
            align_horizontal=Align().h_center(),
            align_vertical=Align().v_center(),

            # Curseur
            curseur=p_base.CUR,
            style=StyleSheet().get()
    ):
        for wg in wgs:
            wg.setStyleSheet(style)

            wg.setCalendarPopup(True)
            dateDuJour = vrb.DATE_NOW_FORMAT.split("_")
            QdateDuJour = QtCore.QDate(int(dateDuJour[2]), int(dateDuJour[1]), int(dateDuJour[0]))
            wg.setDateTime(QtCore.QDateTime(QdateDuJour, QtCore.QTime(0, 0, 0)))
            wg.setDate(QdateDuJour)
            wg.setFocusPolicy(QtCore.Qt.NoFocus)

            Fct(wg=wg, w=width, h=height).DIM()
            wg.setFont(Fct(font=font, font_size=font_size).FONT())

            wg.setAlignment(align_horizontal | align_vertical)

            wg.setCursor(Fct(cur=curseur).CUR())
            wg.lineEdit().setCursor(Fct(cur=P_cur().IBeam()).CUR())
            wg.calendarWidget().setCursor(Fct(cur=P_cur().souris_main()).CUR())


class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs)
class Base_tr(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            bg_gen=Rgb().tr(),
            fg=Rgb().th3(),
            bg_selection=Rgb().th3(),
            fg_selection=Rgb().th1(),
    )
