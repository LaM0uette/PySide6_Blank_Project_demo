from PySide6 import QtCore

from ....build import *
from ....build.widgets import p_base
from ....config import vrb

class Style:
    def __init__(
            self,

            # Widgets
            *wgs,

            # Couleurs BG
            bg_gen=None,
            bg=p_base.BG,
            bg_hover=p_base.BG_HOVER,
            bg_selection=p_base.BG_SELECTION,
            bg_item=p_base.BG_ITEM,
            bg_item_hover=p_base.BG_ITEM_HOVER,
            bg_header=Rgb().th2(),
            bg_header_hover=Rgb().th2(),
            bg_mois=Rgb().th2(),

            # Couleurs FG
            fg_gen=None,
            fg=p_base.FG,
            fg_hover=p_base.FG_HOVER,
            fg_selection=p_base.FG_SELECTION,
            fg_item=p_base.FG_ITEM,
            fg_item_hover=p_base.FG_ITEM_HOVER,
            fg_header=Rgb().th1(),
            fg_header_hover=Rgb().bn1(),
            fg_mois=Rgb().th1(),

            # Dimensions WG
            width=p_base.WG_WIDTH,
            height=p_base.WG_HEIGHT,

            # Police
            font=p_base.FONT,
            font_size=p_base.FONT_SIZE,

            # Images
            img=P_img().calendrier(),
            img_hover=P_img().calendrier(),
            img_right=p_base.IMG_RIGHT,
            img_left=p_base.IMG_LEFT,
            # Images RGB
            img_rgb="",
            img_hover_rgb="",
            img_right_rgb=p_base.IMG_RIGHT_RGB,
            img_left_rgb=p_base.IMG_LEFT_RGB,
            # Images DIM
            img_width=p_base.IMG_WIDTH,
            img_height=p_base.IMG_HEIGHT,
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
            curseur=p_base.CUR
    ):
        # BG
        if not bg_gen is None:
            bg = bg_gen
            bg_hover = bg_gen
        # FG
        if not fg_gen is None:
            fg = fg_gen
            fg_hover = fg_gen
        # Bordure
        if not border_gen_all is None:
            border_top = border_gen_all
            border_bottom = border_gen_all
            border_right = border_gen_all
            border_left = border_gen_all
            border_top_hover = border_gen_all
            border_bottom_hover = border_gen_all
            border_right_hover = border_gen_all
            border_left_hover = border_gen_all
        elif border_gen_all is None:
            if not border_all is None:
                border_top = border_all
                border_bottom = border_all
                border_right = border_all
                border_left = border_all
            if not border_all_hover is None:
                border_top_hover = border_all_hover
                border_bottom_hover = border_all_hover
                border_right_hover = border_all_hover
                border_left_hover = border_all_hover

            if not border_gen_top is None:
                border_top = border_gen_top
                border_top_hover = border_gen_top
            if not border_gen_bottom is None:
                border_bottom = border_gen_bottom
                border_bottom_hover = border_gen_bottom
            if not border_gen_right is None:
                border_right = border_gen_right
                border_right_hover = border_gen_right
            if not border_gen_left is None:
                border_left = border_gen_left
                border_left_hover = border_gen_left
        # Bordure style
        if not border_gen_style is None:
            border_style = border_gen_style
            border_style_hover = border_gen_style
        # Bordure RGB
        if not border_gen_rgb is None:
            border_rgb = border_gen_rgb
            border_rgb_hover = border_gen_rgb
        # Radius
        if not radius_all is None:
            radius_top_right = radius_all
            radius_top_left = radius_all
            radius_bottom_right = radius_all
            radius_bottom_left = radius_all


        style = f"""
                """

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
