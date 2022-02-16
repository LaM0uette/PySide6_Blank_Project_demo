from PySide6 import QtCore

from ....build import *
from ....build.widgets import p_base
from ....config import vrb

class Style:
    def __init__(self,

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
                 img_margin_top=0,
                 img_margin_bottom=0,
                 img_margin_right=0,
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
                /* DATEEDIT */
                QDateEdit {{
                background-color: rgba{bg};
                color: rgba{fg};
                selection-background-color: rgba{bg_selection};
                selection-color: rgba{fg_selection};
                }}
                QDateEdit:hover {{
                background-color: rgba{bg_hover};
                color: rgba{fg_hover};
                }}

                /* IMG CALENDRIER */
                QDateEdit::drop-down {{
                image: url({f"{img}{img_rgb}.svg"});
                width: {img_width}px;
                height: {img_height}px;
                margin-top: {img_margin_top}px;
                margin-bottom: {img_margin_bottom}px;
                margin-right: {img_margin_right}px;
                margin-left: {img_margin_left}px;
                }}
                QDateEdit::drop-down:hover {{
                image: url({f"{img_hover}{img_hover_rgb}.svg"});
                }}

                /* WIDGETS */
                QCalendarWidget QWidget {{
                alternate-background-color: rgba{bg_mois};
                color: rgb{fg_mois};
                }}

                /* TOOL BUTTON */
                QCalendarWidget QToolButton {{
                font-size: {font_size}px;
                background-color: rgba{bg_header};
                color: rgba{fg_header};
                }}
                QCalendarWidget QToolButton:hover {{
                background-color: rgba{bg_header_hover};
                color: rgba{fg_header_hover};
                }}

                /* FLECHE GAUCHE DROITE */
                QToolButton#qt_calendar_nextmonth  {{
                qproperty-icon: url({f"{img_right}{img_right_rgb}.svg"});
                icon-size: {font_size}px, {font_size}px;
                }}
                QToolButton#qt_calendar_prevmonth {{
                qproperty-icon: url({f"{img_left}{img_left_rgb}.svg"});
                icon-size: {font_size}px, {font_size}px;
                }}

                /* MENU DEROULANT */
                QCalendarWidget QMenu {{
                width: 150px;
                font-size: {font_size}px;
                font-family: {font};
                background-color: rgba{bg_header};
                color: rgba{fg_header};
                }}

                /* SPIN BOX */
                QCalendarWidget QSpinBox {{
                width: 60px;
                font-size: {font_size}px;
                font-family: {font};
                background-color: rgba{bg_header};
                color: rgba{fg_header};
                selection-background-color: rgba{bg_selection};
                selection-color: rgba{fg_selection};
                }}

                /* JOURS */
                QCalendarWidget QAbstractItemView {{
                font-size: {font_size}px;
                font-family: {font};
                font-weight: 30;
                outline: 0px;
                }}
                QCalendarWidget QAbstractItemView:enabled {{
                background-color: rgba{bg_item};
                color: rgba{fg_item};
                selection-background-color: rgba{fg_item};
                selection-color: rgba{bg_item};
                }}
                QCalendarWidget QWidget:item:hover, QCalendarWidget QWidget:item:selected {{
                background-color: rgba{bg_item_hover};
                color: rgba{fg_item_hover};
                border: {border_day_size}px {border_day_style} rgba{border_day_rgb};
                }}

                /* BARRE HAUT */
                QCalendarWidget QWidget#qt_calendar_navigationbar {{
                background-color: rgba{bg_header};
                }}

                /* BORDURES */
                .QDateEdit {{
                border-top: {border_top}px {border_style} rgba{border_rgb};
                border-bottom: {border_bottom}px {border_style} rgba{border_rgb};
                border-right: {border_right}px {border_style} rgba{border_rgb};
                border-left: {border_left}px {border_style} rgba{border_rgb};
                }}
                .QDateEdit:hover {{
                border-top: {border_top_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-bottom: {border_bottom_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-right: {border_right_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-left: {border_left_hover}px {border_style_hover} rgba{border_rgb_hover};
                }}
                
                /* RAYONS */
                .QDateEdit {{
                border-top-right-radius: {radius_top_right}px;
                border-top-left-radius: {radius_top_left}px;
                border-bottom-right-radius: {radius_bottom_right}px;
                border-bottom-left-radius: {radius_bottom_left}px;
                }}"""

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
        super().__init__(*wgs,
                         bg_gen=Rgb().tr(),
                         fg=Rgb().th3(),
                         bg_selection=Rgb().th3(),
                         fg_selection=Rgb().th1(),
    )
