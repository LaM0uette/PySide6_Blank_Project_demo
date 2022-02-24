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
            font=p_base.FONT,
            font_size=p_base.FONT_SIZE,
            align_horizontal=Align().h_center(),
            align_vertical=Align().v_center(),
            curseur=Cur().souris_main(),

            # Couleurs BG
            bg=p_base.BG,
            bg_hover=p_base.BG_HOVER,
            bg_selection=p_base.BG_SELECTION,
            bg_item=p_base.BG_ITEM,
            bg_item_hover=p_base.BG_ITEM_HOVER,
            bg_header=Rgb().th2(),
            bg_header_hover=Rgb().th2(),
            bg_mois=Rgb().th2(),
            # Couleurs FG
            fg=p_base.FG,
            fg_hover=p_base.FG_HOVER,
            fg_selection=p_base.FG_SELECTION,
            fg_item=p_base.FG_ITEM,
            fg_item_hover=p_base.FG_ITEM_HOVER,
            fg_header=Rgb().th1(),
            fg_header_hover=Rgb().bn1(),
            fg_mois=Rgb().th1(),

            # Images
            img=p_base.IMG_UNROLL,
            img_hover=p_base.IMG_UNROLL_HOVER,
            img_right=p_base.IMG_RIGHT,
            img_left=p_base.IMG_LEFT,
            # Images RGB
            img_rgb=p_base.IMG_UNROLL_RGB,
            img_hover_rgb=p_base.IMG_UNROLL_HOVER_RGB,
            img_right_rgb=p_base.IMG_RIGHT_RGB,
            img_left_rgb=p_base.IMG_LEFT_RGB,
            # Images DIM
            img_width=p_base.img_width,
            img_height=p_base.img_height,
            # Images positions
            img_margin_top=0,
            img_margin_bottom=0,
            img_margin_right=0,
            img_margin_left=0,

            # Bordures
            border=p_base.WG_BORDER_WIDTH,
            border_style=p_base.WG_BORDER_STYLE,
            border_rgb=p_base.WG_BORDER_RGB,
            # Bordures hover
            border_hover=p_base.WG_BORDER_WIDTH,
            border_hover_style=p_base.WG_BORDER_STYLE,
            border_hover_rgb=p_base.WG_BORDER_RGB,

            # Bordures jours
            border_day_size=P_style().bd(),
            border_day_style=p_base.WG_BORDER_STYLE,
            border_day_rgb=p_base.FG_ITEM_HOVER,

            # Rayons
            radius=p_base.WG_RADIUS,
    ):
        style = f"""
                /* WIDGET */
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
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}
                .QDateEdit:hover {{
                border-top: {border_hover[0]}px {border_hover_style} rgba{border_hover_rgb};
                border-bottom: {border_hover[1]}px {border_hover_style} rgba{border_hover_rgb};
                border-right: {border_hover[2]}px {border_hover_style} rgba{border_hover_rgb};
                border-left: {border_hover[3]}px {border_hover_style} rgba{border_hover_rgb};
                }}
                
                /* RAYONS */
                .QDateEdit {{
                border-top-right-radius: {radius[0]}px;
                border-top-left-radius: {radius[1]}px;
                border-bottom-right-radius: {radius[2]}px;
                border-bottom-left-radius: {radius[3]}px;
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
            wg.lineEdit().setCursor(Fct(cur=Cur().IBeam()).CUR())
            wg.calendarWidget().setCursor(Fct(cur=Cur().souris_main()).CUR())


##################
##     BASE     ##
##################
class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            img=P_img().calendrier(),
            img_hover=P_img().calendrier(),
            img_rgb="",
            img_hover_rgb="",
            img_margin_top=(p_base.WG_HEIGHT - p_base.IMG_HEIGHT) / 2,
            img_margin_right=(p_base.WG_HEIGHT - p_base.IMG_HEIGHT) / 2,
        )
class Base_tr(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            bg=Rgb().tr(),
            bg_hover=Rgb().tr(),
            fg=Rgb().th3(),
            bg_selection=Rgb().th3(),
            fg_selection=Rgb().th1(),
            img=P_img().calendrier(),
            img_hover=P_img().calendrier(),
            img_rgb="",
            img_hover_rgb="",
            img_margin_top=(p_base.WG_HEIGHT - p_base.IMG_HEIGHT) / 2,
            img_margin_right=(p_base.WG_HEIGHT - p_base.IMG_HEIGHT) / 2,
    )
