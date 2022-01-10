from PySide6 import QtCore

from ..Attrs import Attrs
from ....build import *
from ....config import vrb


class wg:
    def __init__(self,
                 *wgs,
                 colors_type,
                 colors,
                 dim,
                 font,
                 bd,
                 rd,
                 align,
                 cur
    ):
        bds = Attrs(bd=bd).GET_BD()
        rds = Attrs(rd=rd).GET_RD()

        ft = P_font().h4()
        style_gen = f"""
        /* IMG CALENDRIER */
        QDateEdit::drop-down {{
        image: url({P_img().calendrier() + '.svg'});
        width: {dim.get("h") * P_style().x_ico()}px;
        height: {dim.get("h") * P_style().x_ico()}px;
        margin-top: {(dim.get('h') - dim.get("h") * P_style().x_ico()) / 2.5}px;
        margin-right: {(dim.get('h') - dim.get("h") * P_style().x_ico()) / 2.5}px;
        }}
        
        /* DATEEDIT */
        QDateEdit {{
        color: rgb{colors.get("c3")};
        selection-background-color: rgb{colors.get("c3")};
        selection-color: rgb{colors.get("c1")};
        border: none;
        }}
        
        /*  */
        QCalendarWidget QWidget {{
        alternate-background-color: rgb{colors.get("c2")};
        color: rgb{colors.get("c3")};
        }}

        /*  */
        QCalendarWidget QToolButton {{
        font-size: {ft}px;
        background-color: rgb{colors.get("c3")};
        color: rgb{colors.get("c1")};
        }}
        QCalendarWidget QToolButton:hover {{
        background-color: rgb{colors.get("c3")};
        color: rgb{colors.get("bn1")};
        }}

        /*  */
        QToolButton#qt_calendar_prevmonth {{
        qproperty-icon: url({P_img().fleche_gauche() + 'bn1' + '.svg'});
        icon-size: {ft}px, {ft}px;
        }}
        QToolButton#qt_calendar_nextmonth  {{
        qproperty-icon: url({P_img().fleche_droite() + 'bn1' + '.svg'});
        icon-size: {ft}px, {ft}px;
        }}

        /*  */
        QCalendarWidget QMenu {{
        width: 150px;
        font-size: {ft}px;
        font-family: Berlin Sans FB Demi;
        background-color: rgb{colors.get("c3")};
        color: rgb{colors.get("c1")};
        }}

        /*  */
        QCalendarWidget QMenu::item:selected {{
        padding-left: 30px;
        background-color: rgb{colors.get("c3")};
        color: rgb{colors.get("c1")};
        }}

        /*  */
        QCalendarWidget QSpinBox {{
        width: 50px;
        font-size: {ft}px;
        font-family: Berlin Sans FB Demi;
        background-color: rgb{colors.get("c3")};
        color: rgb{colors.get("c1")};
        selection-background-color: rgb{colors.get("c1")};
        selection-color: rgb{colors.get("c3")};
        }}

        /*  */
        QCalendarWidget QAbstractItemView {{
        font-size: {ft}px;
        font-family: Berlin Sans FB Demi;
        font-weight: 30;
        outline: 0px;
        }}

        /*  */
        QCalendarWidget QWidget:item:hover {{
        border: {P_style().bd()}px solid rgb{colors.get("c3")};
        }}

        /*  */
        QCalendarWidget QAbstractItemView:enabled {{
        background-color: rgb{colors.get("c2")};
        color: rgb{colors.get("c3")};
        selection-background-color: rgb{colors.get("c3")};
        selection-color: rgb{colors.get("bn2")};
        }}

        /*  */
        QCalendarWidget QWidget#qt_calendar_navigationbar {{
        background-color: rgb{colors.get("c3")};
        }}

        /*  */
        QCalendarWidget QAbstractItemView:disabled {{
        color: rgb{colors.get("c1")};
        }}
        

        /* BORDURES */
        QCalendarWidget {{
        border-width: {P_style().bd()}px;
        border-style: solid;
        border-color: rgba{bds.get("o1")} rgba{bds.get("o2")} rgba{bds.get("o3")} rgba{bds.get("o4")};
        padding: {P_style().bd()}px;
        }}
        
        /* RAYONS */
        QCalendarWidget {{
        border-top-left-radius: {rds.get("r1")}px;
        border-top-right-radius: {rds.get("r2")}px;
        border-bottom-right-radius: {rds.get("r4")}px;
        border-bottom-left-radius: {rds.get("r3")}px;
        }}
"""
        style_type = {
            "th": f"""
            QDateEdit {{
            background-color: rgb{colors.get("c1")};
            }}""",
            "tr": """
            QDateEdit {
            background-color: rgba(0, 0, 0, 0);
            }"""
        }


        style = style_gen + style_type.get(colors_type)
        for wg in wgs:
            wg.setStyleSheet(style)

            try:
                wg.setCalendarPopup(True)
                dateDuJour = vrb.DATE_NOW_FORMAT.split("_")
                QdateDuJour = QtCore.QDate(int(dateDuJour[2]), int(dateDuJour[1]), int(dateDuJour[0]))
                wg.setDateTime(QtCore.QDateTime(QdateDuJour, QtCore.QTime(0, 0, 0)))
                wg.setDate(QdateDuJour)
                wg.setFocusPolicy(QtCore.Qt.NoFocus)

                Fct(wg=wg, w=dim.get("w"), h=dim.get("h")).DIM()
                wg.setFont(Fct(font_size=font).FONT())

                wg.setAlignment(align)

                wg.setCursor(Fct(cur=cur).CUR())
                wg.lineEdit().setCursor(Fct(cur=P_cur().IBeam()).CUR())
                wg.calendarWidget().setCursor(Fct(cur=P_cur().souris_main()).CUR())
            except: pass
