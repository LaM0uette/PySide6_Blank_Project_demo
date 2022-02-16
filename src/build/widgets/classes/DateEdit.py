from PySide6 import QtCore

from ....build import *
from ....build.widgets import p_base
from ....config import vrb

class Style:
    def __init__(self,

                 # Widgets
                 *wgs,

                 couleur_bg=p_base._COLORS_BG,
                 couleur_bg_hover=p_base._COLORS_BG_HOVER,
                 couleur_bg_selection=p_base.COLORS_BG_SELECTION,
                 couleur_bg_item=p_base.COLORS_BG_ITEM,
                 couleur_bg_item_hover=p_base.COLORS_BG_ITEM_HOVER,
                 couleur_bg_entete=p_base.COULEURS.get("c2") + (255,),
                 couleur_bg_entete_hover=p_base.COULEURS.get("c2") + (255,),
                 couleur_bg_mois=p_base.COULEURS.get("c2") + (255,),
                 couleur_fg=p_base._COLORS_FG,
                 couleur_fg_hover=p_base._COLORS_FG_HOVER,
                 couleur_fg_selection=p_base.COLORS_FG_SELECTION,
                 couleur_fg_item=p_base.COLORS_FG_ITEM,
                 couleur_fg_item_hover=p_base.COLORS_FG_ITEM_HOVER,
                 couleur_fg_entete=p_base.COULEURS.get("c1"),
                 couleur_fg_entete_hover=p_base.COULEURS.get("bn1"),
                 couleur_fg_mois=p_base.COULEURS.get("c1"),

                 # Dimensions WG
                 width=p_base.WG_WIDTH,
                 height=p_base.WG_HEIGHT,

                 # Police
                 font=p_base.FONT,
                 font_size=p_base.FONT_SIZE,

                 img=P_img().calendrier(),
                 tm="",
                 img_hover=P_img().calendrier(),
                 tm_hover="",
                 img_fleche_droite=p_base.IMG_DROITE,
                 tm_fleche_droite=p_base.TM_DROITE,
                 img_fleche_gauche=p_base.IMG_GAUCHE,
                 tm_fleche_gauche=p_base.TM_GAUCHE,
                 img_width=p_base.WG_HEIGHT,
                 img_height=p_base.WG_HEIGHT,
                 img_margin_top=0,
                 img_margin_bottom=0,
                 img_margin_right=0,
                 img_margin_left=0,

                 bordure_width_top=p_base.WG_BORDER_WIDTH,
                 bordure_width_bottom=p_base.WG_BORDER_WIDTH,
                 bordure_width_right=p_base.WG_BORDER_WIDTH,
                 bordure_width_left=p_base.WG_BORDER_WIDTH,
                 bordure_style_top=p_base.WG_BORDER_STYLE,
                 bordure_style_bottom=p_base.WG_BORDER_STYLE,
                 bordure_style_right=p_base.WG_BORDER_STYLE,
                 bordure_style_left=p_base.WG_BORDER_STYLE,
                 bordure_couleur_top=p_base.WG_BORDER_RGB,
                 bordure_couleur_bottom=p_base.WG_BORDER_RGB,
                 bordure_couleur_right=p_base.WG_BORDER_RGB,
                 bordure_couleur_left=p_base.WG_BORDER_RGB,
                 bordure_jours_taille=P_style().bd(),
                 bordure_jours_style="solid",
                 rayon_top_left=p_base.WG_RADIUS,
                 rayon_top_right=p_base.WG_RADIUS,
                 rayon_bottom_right=p_base.WG_RADIUS,
                 rayon_bottom_left=p_base.WG_RADIUS,

                 # Paramètres
                 align=p_base.ALIGN,

                 # Curseur
                 curseur=p_base.CUR
                 ):
        style = f"""
                /* DATEEDIT */
                QDateEdit {{
                background-color: rgba{couleur_bg};
                color: rgb{couleur_fg};
                selection-background-color: rgb{couleur_bg_selection};
                selection-color: rgb{couleur_fg_selection};
                }}
                QDateEdit:hover {{
                background-color: rgba{couleur_bg_hover};
                color: rgb{couleur_fg_hover};
                }}

                /* IMG CALENDRIER */
                QDateEdit::drop-down {{
                image: url({f"{img}{tm}.svg"});
                width: {img_width}px;
                height: {img_height}px;
                margin-top: {img_margin_top}px;
                margin-bottom: {img_margin_bottom}px;
                margin-right: {img_margin_right}px;
                margin-left: {img_margin_left}px;
                }}
                QDateEdit::drop-down:hover {{
                image: url({f"{img_hover}{tm_hover}.svg"});
                }}

                /* WIDGETS */
                QCalendarWidget QWidget {{
                alternate-background-color: rgba{couleur_bg_mois};
                color: rgb{couleur_fg_mois};
                }}

                /* TOOL BUTTON */
                QCalendarWidget QToolButton {{
                font-size: {font_size}px;
                background-color: rgba{couleur_bg_entete};
                color: rgb{couleur_fg_entete};
                }}
                QCalendarWidget QToolButton:hover {{
                background-color: rgba{couleur_bg_entete_hover};
                color: rgb{couleur_fg_entete_hover};
                }}

                /* FLECHE GAUCHE DROITE */
                QToolButton#qt_calendar_nextmonth  {{
                qproperty-icon: url({f"{img_fleche_droite}{tm_fleche_droite}.svg"});
                icon-size: {font_size}px, {font_size}px;
                }}
                QToolButton#qt_calendar_prevmonth {{
                qproperty-icon: url({f"{img_fleche_gauche}{tm_fleche_gauche}.svg"});
                icon-size: {font_size}px, {font_size}px;
                }}

                /* MENU DEROULANT */
                QCalendarWidget QMenu {{
                width: 150px;
                font-size: {font_size}px;
                font-family: {font};
                background-color: rgba{couleur_bg_entete};
                color: rgb{couleur_fg_entete};
                }}

                /* SPIN BOX */
                QCalendarWidget QSpinBox {{
                width: 60px;
                font-size: {font_size}px;
                font-family: {font};
                background-color: rgba{couleur_bg_entete};
                color: rgb{couleur_fg_entete};
                selection-background-color: rgb{couleur_bg_selection};
                selection-color: rgb{couleur_fg_selection};
                }}

                /* JOURS */
                QCalendarWidget QAbstractItemView {{
                font-size: {font_size}px;
                font-family: {font};
                font-weight: 30;
                outline: 0px;
                }}
                QCalendarWidget QAbstractItemView:enabled {{
                background-color: rgba{couleur_bg_item};
                color: rgb{couleur_fg_item};
                selection-background-color: rgb{couleur_fg_item};
                selection-color: rgb{couleur_bg_item};
                }}
                QCalendarWidget QWidget:item:hover, QCalendarWidget QWidget:item:selected {{
                background-color: rgba{couleur_bg_item_hover};
                color: rgb{couleur_fg_item_hover};
                border: {bordure_jours_taille}px {bordure_jours_style} rgb{couleur_fg_item_hover};
                }}

                /* BARRE HAUT */
                QCalendarWidget QWidget#qt_calendar_navigationbar {{
                background-color: rgba{couleur_bg_entete};
                }}

                /* BORDURES */
                .QDateEdit {{
                border-top: {bordure_width_top}px {bordure_style_top} rgba{bordure_couleur_top};
                border-bottom: {bordure_width_bottom}px {bordure_style_bottom} rgba{bordure_couleur_bottom};
                border-right: {bordure_width_right}px {bordure_style_right} rgba{bordure_couleur_right};
                border-left: {bordure_width_left}px {bordure_style_left} rgba{bordure_couleur_left};
                }}

                /* RAYONS */
                .QDateEdit {{
                border-top-left-radius: {rayon_top_left}px;
                border-top-right-radius: {rayon_top_right}px;
                border-bottom-right-radius: {rayon_bottom_right}px;
                border-bottom-left-radius: {rayon_bottom_left}px;
                }}"""

        for wg in wgs:
            wg.setStyleSheet(style)

            try:
                wg.setCalendarPopup(True)
                dateDuJour = vrb.DATE_NOW_FORMAT.split("_")
                QdateDuJour = QtCore.QDate(int(dateDuJour[2]), int(dateDuJour[1]), int(dateDuJour[0]))
                wg.setDateTime(QtCore.QDateTime(QdateDuJour, QtCore.QTime(0, 0, 0)))
                wg.setDate(QdateDuJour)
                wg.setFocusPolicy(QtCore.Qt.NoFocus)

                Fct(wg=wg, w=width, h=height).DIM()
                wg.setFont(Fct(font=font, font_size=font_size).FONT())

                wg.setAlignment(align)

                wg.setCursor(Fct(cur=curseur).CUR())
                wg.lineEdit().setCursor(Fct(cur=P_cur().IBeam()).CUR())
                wg.calendarWidget().setCursor(Fct(cur=P_cur().souris_main()).CUR())
            except: pass


class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs)
class Base_tr(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
           couleur_bg=(0, 0, 0, 0),
           couleur_bg_hover=(0, 0, 0, 0)
    )
