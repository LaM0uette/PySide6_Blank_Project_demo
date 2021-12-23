from PySide6 import QtCore, QtWidgets, QtGui

from . import vrb
from .build import cursor, functions
from .config import colors
from .dct_gen import dct_size, dct_img


### WG ________
class STYLE_WG:
    def __init__(self, **kwargs):
        from .dct_wg import dct_wg

        ### DEFINITION DU KWARGS ___________
        self.type_wg = kwargs.get("type_wg")
        self.wg_name = kwargs.get("wg_name")
        self.wg = kwargs.get("wg")


        ### CREATION DES CURSEURS
        self.dct_cur = {
            "agrandir": QtGui.QCursor(QtGui.QPixmap(cursor.cur_agrandir[0]), cursor.cur_agrandir[1], cursor.cur_agrandir[2]),
            "copier": QtGui.QCursor(QtGui.QPixmap(cursor.cur_copier[0]), cursor.cur_copier[1], cursor.cur_copier[2]),
            "crayon": QtGui.QCursor(QtGui.QPixmap(cursor.cur_crayon[0]), cursor.cur_crayon[1], cursor.cur_crayon[2]),
            "croix": QtGui.QCursor(QtGui.QPixmap(cursor.cur_croix[0]), cursor.cur_croix[1], cursor.cur_croix[2]),
            "fleche_nesw": QtGui.QCursor(QtGui.QPixmap(cursor.cur_fleche_nesw[0]), cursor.cur_fleche_nesw[1], cursor.cur_fleche_nesw[2]),
            "fleche_ns": QtGui.QCursor(QtGui.QPixmap(cursor.cur_fleche_ns[0]), cursor.cur_fleche_ns[1], cursor.cur_fleche_ns[2]),
            "fleche_nwse": QtGui.QCursor(QtGui.QPixmap(cursor.cur_fleche_nwse[0]), cursor.cur_fleche_nwse[1], cursor.cur_fleche_nwse[2]),
            "fleche_top": QtGui.QCursor(QtGui.QPixmap(cursor.cur_fleche_top[0]), cursor.cur_fleche_top[1], cursor.cur_fleche_top[2]),
            "fleche_tout": QtGui.QCursor(QtGui.QPixmap(cursor.cur_fleche_tout[0]), cursor.cur_fleche_tout[1], cursor.cur_fleche_tout[2]),
            "fleche_we": QtGui.QCursor(QtGui.QPixmap(cursor.cur_fleche_we[0]), cursor.cur_fleche_we[1], cursor.cur_fleche_we[2]),
            "IBeam": QtGui.QCursor(QtGui.QPixmap(cursor.cur_IBeam[0]), cursor.cur_IBeam[1], cursor.cur_IBeam[2]),
            "infos": QtGui.QCursor(QtGui.QPixmap(cursor.cur_infos[0]), cursor.cur_infos[1], cursor.cur_infos[2]),
            "main": QtGui.QCursor(QtGui.QPixmap(cursor.cur_main[0]), cursor.cur_main[1], cursor.cur_main[2]),
            "non": QtGui.QCursor(QtGui.QPixmap(cursor.cur_non[0]), cursor.cur_non[1], cursor.cur_non[2]),
            "retour": QtGui.QCursor(QtGui.QPixmap(cursor.cur_retour[0]), cursor.cur_retour[1], cursor.cur_retour[2]),
            "souris": QtGui.QCursor(QtGui.QPixmap(cursor.cur_souris[0]), cursor.cur_souris[1], cursor.cur_souris[2]),
            "souris_main": QtGui.QCursor(QtGui.QPixmap(cursor.cur_souris_main[0]), cursor.cur_souris_main[1], cursor.cur_souris_main[2]),
            "souris_non": QtGui.QCursor(QtGui.QPixmap(cursor.cur_souris_non[0]), cursor.cur_souris_non[1], cursor.cur_souris_non[2])
        }


        ### ARGUMENTS DE STYLE __________________________
        item = dct_wg.get(self.type_wg).get(self.wg_name)
        # Couleurs ___________________________________________________________________________________________________________________________
        self.colors = item.get("colors") if item.get("colors") is not None else {"type": None, "c1": None, "c2": None, "c3": None, "bn": None}
        self.colors_type = self.colors.get("type") if self.colors.get("type") is not None else "th"
        self.pal = self.colors.get("pal") if self.colors.get("pal") is not None else {"c1": None, "c2": None, "c3": None, "bn": None}
        self.c1 = self.pal.get("c1") if self.pal.get("c1") is not None else None
        self.c2 = self.pal.get("c2") if self.pal.get("c2") is not None else None
        self.c3 = self.pal.get("c3") if self.pal.get("c3") is not None else None
        self.bn = self.pal.get("bn") if self.pal.get("bn") is not None else None

        # Dimensions ________________________________________________________________________
        self.dim = item.get("dim") if item.get("dim") is not None else {"w": None, "h": None}
        #noinspection PyUnresolvedReferences
        self.dim_ico = self.dim.get("h") * dct_size.get("wg").get("x_ico") if self.dim.get("h") is not None else None

        # Images _________________
        self.img = item.get("img")
        self.img_check = item.get("img_check") if item.get("img_check") is not None else ""
        self.th = item.get("th") if item.get("th") is not None else "bn1"
        self.th_check = item.get("th_check") if item.get("th_check") is not None else "bn2"

        # Police ____________________________________________________________________
        self.font = item.get("font") if item.get("font") is not None else vrb.bs_font

        # Radius ______________________________________________________________________________
        self.rd = item.get("rd") if item.get("rd") is not None else {"mat": "1111", "px": None}
        self.rd_mat = self.rd.get("mat") if self.rd.get("mat") is not None else "1111"
        self.r1 = self.rd.get("px") if int(self.rd_mat[:1]) == 1 else None
        self.r2 = self.rd.get("px") if int(self.rd_mat[1:2]) == 1 else None
        self.r3 = self.rd.get("px") if int(self.rd_mat[2:3]) == 1 else None
        self.r4 = self.rd.get("px") if int(self.rd_mat[3:4]) == 1 else None

        # Bordures ____________________________________________________________________________
        self.bd = item.get("bd") if item.get("bd") is not None else {"mat": "1111", "px": None, "th": None}
        self.bd_mat = self.bd.get("mat") if self.bd.get("mat") is not None else "1111"
        self.bd_px = self.bd.get("px") if self.bd.get("px") is not None else dct_size.get('wg').get('bd')
        self.bd_th = self.bd.get("th") if self.bd.get("th") is not None else colors.bn1
        self.o1 = self.bd_th+(255, ) if int(self.bd_mat[:1]) == 1 else (0, 0, 0, 0)
        self.o2 = self.bd_th+(255, ) if int(self.bd_mat[1:2]) == 1 else (0, 0, 0, 0)
        self.o3 = self.bd_th+(255, ) if int(self.bd_mat[2:3]) == 1 else (0, 0, 0, 0)
        self.o4 = self.bd_th+(255, ) if int(self.bd_mat[3:4]) == 1 else (0, 0, 0, 0)

        # Curseur _
        self.cur = item.get("cur") if item.get("cur") is not None else "main"

        # Paramètres ______________________________________________________________________________________________________
        self.align = item.get("align") if item.get("align") is not None else QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter
        self.edit = item.get("edit") if item.get("edit") is not None else False
        self.scroll = item.get("scroll") if item.get("scroll") is not None else {"h": QtCore.Qt.ScrollBarAsNeeded, "v": QtCore.Qt.ScrollBarAsNeeded}
        self.header = item.get("header") if item.get("header") is not None else {"h": True, "v": True}
        self.pb_sb = item.get("pb_sb") if item.get("pb_sb") is not None else QtWidgets.QAbstractSpinBox.NoButtons

        ### LANCEMENT DES FONCTIONS ______
        dct_func_stl = {
            "cb": self.CB,
            "de": self.DE,
            "fr": self.FR,
            "lb": self.LB,
            "lw": self.LW,
            "pb": self.PB,
            "ckb": self.CKB,
            "rb": self.RB,
            "pg": self.PG,
            "sca": self.SCA,
            "sb": self.SB,
            "tb": self.TB,
            "tw": self.TW,
            "txt": self.TXT
        }
        dct_func_stl.get(self.type_wg)()

    def ALL(self):
        # Dimensions ___________________________________________________________
        try: functions.DIM(wg=self.wg, w=self.dim.get("w"), h=self.dim.get("h"))
        except: pass

        # Image ____________________________________________________________________________________________________
        if not self.type_wg in ("ckb", "rb"):
            try: functions.ICON(wg=self.wg, img=self.img + self.th, dim=self.dim_ico) if self.img is not None else False
            except: pass

        # Police ______________________________________
        try: self.wg.setFont(functions.FONT(self.font))
        except: pass

        # Curseur ________________________________________
        if not self.type_wg in ("fr", "lb", "pg", "sca"):
            try: self.wg.setCursor(self.dct_cur.get(self.cur))
            except: pass
            try: self.wg.view().setCursor(self.dct_cur.get("souris_main"))
            except: pass
            try: self.wg.viewport().setCursor(self.dct_cur.get(self.cur))
            except: pass
            try: self.wg.lineEdit().setCursor(self.dct_cur.get("IBeam"))
            except: pass
            try: self.wg.calendarWidget().setCursor(self.dct_cur.get("souris_main"))
            except: pass
        if self.type_wg in "sb" and self.colors_type == "tr":
            try: self.wg.lineEdit().setCursor(self.dct_cur.get("souris_main"))
            except: pass

        # Paramètres ________________________
        try: self.wg.setAlignment(self.align)
        except: pass
        try: self.wg.setEditable(self.edit)
        except: pass
        try: self.wg.setHorizontalScrollBarPolicy(self.scroll.get("h"))
        except: pass
        try: self.wg.setVerticalScrollBarPolicy(self.scroll.get("v"))
        except: pass
        try: self.wg.horizontalHeader().setVisible(self.header.get("h"))
        except: pass
        try: self.wg.verticalHeader().setVisible(self.header.get("v"))
        except: pass
        try: self.wg.setButtonSymbols(self.pb_sb)
        except: pass

    def CB(self):
        stl = {
            "th":
                "QComboBox {"
                f"background-color: rgb{self.c2};"
                f"color: rgb{self.c3};"
                f"font-size: {dct_size.get('police').get('h3')}px;"
                "font-weight: bold;"
                f"border-width: {dct_size.get('wg').get('bd')}px;"
                "border-style: solid;"
                f"border-color: rgba(0, 0, 0, 0) rgba(0, 0, 0, 0) rgb{self.c3} rgba(0, 0, 0, 0);"
                f"selection-background-color: rgb{self.c3};"
                f"selection-color: rgb{self.c1};"
                "}"

                "QComboBox::drop-down {"
                f"width: {dct_size.get('wg').get('h4')}px;"
                f"border: none;"
                "}"

                "QComboBox::down-arrow {"
                f"image: url({dct_img.get('flecheBottom') + 'bn1' + '.svg'});"
                f"width: {dct_size.get('wg').get('h4')}px;"
                "}"

                "QComboBox::down-arrow:hover {"
                f"image: url({dct_img.get('flecheBottom') + 'bn2' + '.svg'});"
                f"width: {dct_size.get('wg').get('h4')}px;"
                "}"

                "QComboBox QAbstractItemView::item {"
                f"background-color: rgb{self.c2};"
                f"color: rgb{self.c3};"
                f"border: none;"
                "}"

                "QComboBox QAbstractItemView::item:hover {"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.c2};"
                f"border: none;"
                "}"

                "QScrollBar::handle:vertical {"
                "min-height: 40px;"
                "}"
                "QScrollBar::handle:horizontal {"
                "min-width: 40px;"
                "}"
                "QScrollBar::handle {"
                f"background: rgb{self.c3};"
                "}"
                "QScrollBar::add-page, QScrollBar::sub-page {"
                f"background: rgb{self.c2};"
                f"border: rgb{self.c2};"
                "}"
        }
        self.wg.setStyleSheet(stl.get(self.colors_type)) if self.c1 is not None else False
        self.ALL()
    def DE(self):
        font_cal = dct_size.get('police').get('h3')
        stl = {
            "th":
                "QDateEdit::drop-down {"
                f"image: url({dct_img.get('calendrier') + '.svg'});"
                f"width: {dct_size.get('wg').get('h4')}px;"
                "}"

                "QDateEdit {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.c3};"
                "border: none;"
                f"selection-background-color: rgb{self.c3};"
                f"selection-color: rgb{self.c1};"
                "}"
                
                "QCalendarWidget QWidget {"
                f"alternate-background-color: rgb{self.c2};"
                f"color: rgb{self.c3};"
                "}"

                "QCalendarWidget QToolButton {"
                f"font-size: {font_cal}px;"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.c1};"
                "}"
                "QCalendarWidget QToolButton:hover {"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.bn};"
                "}"

                "QToolButton#qt_calendar_prevmonth {"
                f"qproperty-icon: url({dct_img.get('flecheGauche') + 'bn1' + '.svg'});"
                f"icon-size: {dct_size.get('wg').get('h4')}px, {dct_size.get('wg').get('h4')}px;"
                "}"
                "QToolButton#qt_calendar_nextmonth  {"
                f"qproperty-icon: url({dct_img.get('flecheDroite') + 'bn1' + '.svg'});"
                f"icon-size: {dct_size.get('wg').get('h4')}px, {dct_size.get('wg').get('h4')}px;"
                "}"

                "QCalendarWidget QMenu {"
                "width: 150px;"
                f"font-size: {font_cal}px;"
                "font-family: Berlin Sans FB Demi;"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.c1};"
                "}"
                
                "QCalendarWidget QMenu::item:selected {"
                "padding-left: 30px;"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.c1};"
                "}"

                "QCalendarWidget QSpinBox {"
                "width: 50px;"
                f"font-size: {font_cal}px;"
                "font-family: Berlin Sans FB Demi;"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.c1};"
                f"selection-background-color: rgb{self.c1};"
                f"selection-color: rgb{self.c3};"
                "}"

                "QCalendarWidget QAbstractItemView {"
                f"font-size: {font_cal}px;"
                "font-family: Berlin Sans FB Demi;"
                "font-weight: 30;"
                "outline: 0px;"
                "}"

                "QCalendarWidget QWidget:item:hover {"
                f"border: {dct_size.get('wg').get('bd')}px solid rgb{self.c3};"
                "}"

                "QCalendarWidget QAbstractItemView:enabled {"
                f"background-color: rgb{self.c2};"
                f"color: rgb{self.c3};"
                f"selection-background-color: rgb{self.c3};"
                f"selection-color: rgb{colors.bn2};"
                "}"

                "QCalendarWidget QWidget#qt_calendar_navigationbar {"
                f"background-color: rgb{self.c3};"
                "}"

                "QCalendarWidget QAbstractItemView:disabled {"
                f"color: rgb{self.c1};"
                "}"
        }
        self.wg.setStyleSheet(stl.get(self.colors_type)) if self.c1 is not None else False
        self.wg.setCalendarPopup(True)
        self.ALL()

        dateDuJour = vrb.date_now_format.split("_")
        QdateDuJour = QtCore.QDate(int(dateDuJour[2]), int(dateDuJour[1]), int(dateDuJour[0]))
        self.wg.setDateTime(QtCore.QDateTime(QdateDuJour, QtCore.QTime(0, 0, 0)))
        self.wg.setDate(QdateDuJour)

        self.wg.setFocusPolicy(QtCore.Qt.NoFocus)
    def FR(self):
        stl = {
            "th":
                ".QFrame {"
                f"background-color: rgb{self.c1};"
                "}",
            "bd":
                ".QFrame {"
                f"border-width: {self.bd_px}px;"
                "border-style: solid;"
                f"border-color: rgba{self.o1} rgba{self.o2} rgba{self.o3} rgba{self.o4};"
                "}"
        }
        self.wg.setStyleSheet(stl.get(self.colors_type)) if self.c1 is not None else False
        self.ALL()

        self.wg.setFrameShape(QtWidgets.QFrame.NoFrame)
    def LB(self):
        stl = {
            "th":
                "QLabel {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.c3};"
                "}",
            "tr":
                "QLabel {"
                f"color: rgb{self.c1};"
                "}"
        }
        self.wg.setStyleSheet(stl.get(self.colors_type)) if self.c1 is not None else False
        self.ALL()
    def LW(self):
        stl = {
            "th":
                "QListWidget {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.c3};"
                f"border: {dct_size.get('wg').get('bd')}px solid rgb{self.c3};"
                "}"
                "QListWidget::item:selected {"
                f"background-color: rgb{self.c2};"
                f"color: rgb{self.bn};"
                "}"
                "QListWidget::item:hover {"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.c1};"
                "}"
                "QListWidget::item:selected:hover {"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.bn};"
                "}"
                "QListWidget QScrollBar::handle:vertical {"
                "min-height: 40px;"
                "}"
                "QListWidget QScrollBar::handle:horizontal {"
                "min-width: 40px;"
                "}"
                "QListWidget QScrollBar::handle {"
                f"background-color: rgb{self.c3};"
                "}"
                "QListWidget QScrollBar::add-page, QScrollBar::sub-page {"
                f"background-color: rgb{self.c1};"
                f"border: rgb{self.c1};"
                "}"
        }
        self.wg.setStyleSheet(stl.get(self.colors_type)) if self.c1 is not None else False
        self.ALL()

        self.wg.setFrameShape(QtWidgets.QFrame.NoFrame)
    def PB(self):
        stl = {
            "txt":
                "QPushButton {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.c3};"
                f"border: {dct_size.get('wg').get('bd')}px solid rgb{self.c3};"
                "}"

                "QPushButton:hover {"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.c1};"
                f"border: {dct_size.get('wg').get('bd')}px solid rgb{self.c3};"
                "}"

                "QPushButton:pressed {"
                f"color: rgb{self.bn};"
                "}",
            "txt_inv":
                "QPushButton {"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.c1};"
                f"border: {dct_size.get('wg').get('bd')}px solid rgb{self.c3};"
                "}"

                "QPushButton:hover {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.c3};"
                f"border: {dct_size.get('wg').get('bd')}px solid rgb{self.c3};"
                "}"

                "QPushButton:pressed {"
                f"color: rgb{self.bn};"
                "}",
            "th":
                "QPushButton {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.c3};"
                "}"

                "QPushButton:hover {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.bn};"
                "}"

                "QPushButton:checked {"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.c1};"
                "}"

                "QPushButton:checked:hover {"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.bn};"
                "}"

                "QPushButton:flat {"
                "border: none;"
                "}",
            "tr":
                "QPushButton {"
                f"color: rgb{self.c3};"
                "}"

                "QPushButton:hover {"
                f"color: rgb{self.bn};"
                "}"

                "QPushButton:checked:hover {"
                f"color: rgb{self.bn};"
                "}"

                "QPushButton:flat {"
                "border: none;"
                "}",
            "zoom":
                "QPushButton {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.c3};"
                "}"

                "QPushButton:checked {"
                f"background-color: rgb{self.c3};"
                "}"

                "QPushButton:flat {"
                "border: none;"
                "}",
            "rd":
                "QPushButton {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.c3};"
                f"border-top-left-radius: {self.r1}px;"
                f"border-top-right-radius: {self.r2}px;"
                f"border-bottom-right-radius: {self.r4}px;"
                f"border-bottom-left-radius: {self.r3}px;"
                "}"

                "QPushButton:hover {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.bn};"
                "}"

                "QPushButton:checked {"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.c1};"
                "}"

                "QPushButton:checked:hover {"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.bn};"
                "}",
            "uni":
                "QPushButton {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.c1};"
                "}"
        
                "QPushButton:flat {"
                "border: none;"
                "}",
        }
        self.wg.setStyleSheet(stl.get(self.colors_type)) if self.c1 is not None else False
        self.ALL()

        self.wg.setFlat(True)
        self.wg.setFocusPolicy(QtCore.Qt.NoFocus)
        self.wg.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    def CKB(self):
        #noinspection PyUnresolvedReferences
        stl = {
            "th":
                "QCheckBox {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.c3};"
                "}"

                "QCheckBox:hover {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.bn};"
                "}"

                "QCheckBox:checked {"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.c1};"
                "}"

                "QCheckBox:checked:hover {"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.bn};"
                "}"

                "QCheckBox:flat {"
                "border: none;"
                "}"
                
                "QCheckBox::indicator {"
                f"margin-left: {(self.dim.get('h') - (self.dim.get('h') * dct_size.get('wg').get('x_ico')))/2}px;"
                f"width: {self.dim.get('h') * dct_size.get('wg').get('x_ico')}px;"
                f"height: {self.dim.get('h') * dct_size.get('wg').get('x_ico')}px"
                "}"

                "QCheckBox::indicator:unchecked {"
                f"image: url({self.img + self.th + '.svg'});"
                "}"

                "QCheckBox::indicator:disabled {"
                f"image: url({self.img + self.th + '.svg'});"
                "}"

                "QCheckBox::indicator:checked {"
                f"image: url({self.img_check + self.th_check + '.svg'});"
                "}",
            "tr":
                "QCheckBox {"
                f"color: rgb{self.c3};"
                "spacing: 10px;"
                "}"

                "QCheckBox:hover {"
                f"color: rgb{self.bn};"
                "}"

                "QCheckBox:checked:hover {"
                f"color: rgb{self.bn};"
                "}"

                "QCheckBox:flat {"
                "border: none;"
                "}"

                "QCheckBox::indicator {"
                f"margin-left: {(self.dim.get('h') - (self.dim.get('h') * dct_size.get('wg').get('x_ico')))/2}px;"
                f"width: {self.dim.get('h') * dct_size.get('wg').get('x_ico')}px;"
                f"height: {self.dim.get('h') * dct_size.get('wg').get('x_ico')}px"
                "}"

                "QCheckBox::indicator:unchecked {"
                f"image: url({self.img + self.th + '.svg'});"
                "}"

                "QCheckBox::indicator:disabled {"
                f"image: url({self.img + self.th + '.svg'});"
                "}"

                "QCheckBox::indicator:checked {"
                f"image: url({self.img_check + self.th_check + '.svg'});"
                "}",
            "rd":
                "QCheckBox {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.c3};"
                f"border-top-left-radius: {self.r1}px;"
                f"border-top-right-radius: {self.r2}px;"
                f"border-bottom-right-radius: {self.r4}px;"
                f"border-bottom-left-radius: {self.r3}px;"
                "}"

                "QCheckBox:hover {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.bn};"
                "}"

                "QCheckBox:checked {"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.c1};"
                "}"

                "QCheckBox:checked:hover {"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.bn};"
                "}"

                "QCheckBox::indicator {"
                f"margin-left: {(self.dim.get('h') - (self.dim.get('h') * dct_size.get('wg').get('x_ico')))/2}px;"
                f"width: {self.dim.get('h') * dct_size.get('wg').get('x_ico')}px;"
                f"height: {self.dim.get('h') * dct_size.get('wg').get('x_ico')}px"
                "}"

                "QCheckBox::indicator:unchecked {"
                f"image: url({self.img + self.th + '.svg'});"
                "}"

                "QCheckBox::indicator:disabled {"
                f"image: url({self.img + self.th + '.svg'});"
                "}"

                "QCheckBox::indicator:checked {"
                f"image: url({self.img_check + self.th_check + '.svg'});"
                "}"
        }
        self.wg.setStyleSheet(stl.get(self.colors_type)) if self.c1 is not None else False
        self.ALL()

        self.wg.setFocusPolicy(QtCore.Qt.NoFocus)
        self.wg.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    def RB(self):
        #noinspection PyUnresolvedReferences
        stl = {
            "th":
                "QRadioButton {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.c3};"
                "}"

                "QRadioButton:hover {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.bn};"
                "}"

                "QRadioButton:checked {"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.c1};"
                "}"

                "QRadioButton:checked:hover {"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.bn};"
                "}"

                "QRadioButton:flat {"
                "border: none;"
                "}"

                "QRadioButton::indicator {"
                f"margin-left: {(self.dim.get('h') - (self.dim.get('h') * dct_size.get('wg').get('x_ico')))/2}px;"
                f"width: {self.dim.get('h') * dct_size.get('wg').get('x_ico')}px;"
                f"height: {self.dim.get('h') * dct_size.get('wg').get('x_ico')}px"
                "}"

                "QRadioButton::indicator:unchecked {"
                f"image: url({self.img + self.th + '.svg'});"
                "}"

                "QRadioButton::indicator:disabled {"
                f"image: url({self.img + self.th + '.svg'});"
                "}"

                "QRadioButton::indicator:checked {"
                f"image: url({self.img_check + self.th_check + '.svg'});"
                "}",
            "tr":
                "QRadioButton {"
                f"color: rgb{self.c3};"
                "spacing: 10px;"
                "}"

                "QRadioButton:hover {"
                f"color: rgb{self.bn};"
                "}"

                "QRadioButton:checked:hover {"
                f"color: rgb{self.bn};"
                "}"

                "QRadioButton:flat {"
                "border: none;"
                "}"

                "QRadioButton::indicator {"
                f"margin-left: {(self.dim.get('h') - (self.dim.get('h') * dct_size.get('wg').get('x_ico')))/2}px;"
                f"width: {self.dim.get('h') * dct_size.get('wg').get('x_ico')}px;"
                f"height: {self.dim.get('h') * dct_size.get('wg').get('x_ico')}px"
                "}"

                "QRadioButton::indicator:unchecked {"
                f"image: url({self.img + self.th + '.svg'});"
                "}"
                
                "QRadioButton::indicator:disabled {"
                f"image: url({self.img + self.th + '.svg'});"
                "}"

                "QRadioButton::indicator:checked {"
                f"image: url({self.img_check + self.th_check + '.svg'});"
                "}",
            "rd":
                "QRadioButton {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.c3};"
                f"border-top-left-radius: {self.r1}px;"
                f"border-top-right-radius: {self.r2}px;"
                f"border-bottom-right-radius: {self.r4}px;"
                f"border-bottom-left-radius: {self.r3}px;"
                "}"

                "QRadioButton:hover {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.bn};"
                "}"

                "QRadioButton:checked {"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.c1};"
                "}"

                "QRadioButton:checked:hover {"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.bn};"
                "}"

                "QRadioButton::indicator {"
                f"margin-left: {(self.dim.get('h') - (self.dim.get('h') * dct_size.get('wg').get('x_ico')))/2}px;"
                f"width: {self.dim.get('h') * dct_size.get('wg').get('x_ico')}px;"
                f"height: {self.dim.get('h') * dct_size.get('wg').get('x_ico')}px"
                "}"

                "QRadioButton::indicator:unchecked {"
                f"image: url({self.img + self.th + '.svg'});"
                "}"

                "QRadioButton::indicator:disabled {"
                f"image: url({self.img + self.th + '.svg'});"
                "}"

                "QRadioButton::indicator:checked {"
                f"image: url({self.img_check + self.th_check + '.svg'});"
                "}"
        }
        self.wg.setStyleSheet(stl.get(self.colors_type)) if self.c1 is not None else False
        self.ALL()

        self.wg.setFocusPolicy(QtCore.Qt.NoFocus)
        self.wg.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    def PG(self):
        stl = {
            "th":
                "QProgressDialog {"
                f"background-color: rgb{self.c1};"
                "}"

                "QProgressBar {"
                f"border-left: {dct_size.get('wg').get('bd')} solid rgb{self.bn};"
                f"border-right: {dct_size.get('wg').get('bd')} solid rgb{self.bn};"
                f"padding-left: {dct_size.get('wg').get('bd') * 1.5}px;"
                f"padding-right: {dct_size.get('wg').get('bd') * 1.5}px;"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.bn};"
                "}"

                "QProgressBar::chunk {"
                f"background-color: rgb{self.c3};"
                "}"
        }
        self.wg.setStyleSheet(stl.get(self.colors_type)) if self.c1 is not None else False
        self.ALL()
    def SCA(self):
        stl = {
            "th":
                "QScrollArea QScrollBar {"
                f"background-color: rgb{self.c1};"
                "width: 20px;"
                "height: 20px;"
                "}"
                "QScrollArea QScrollBar::handle:vertical {"
                "min-height: 100px;"
                "}"
                "QScrollArea QScrollBar::handle:vertical {"
                "min-height: 100px;"
                "}"
                "QScrollArea QScrollBar::handle:horizontal {"
                "min-width: 100px;"
                "}"
                "QScrollArea QScrollBar::handle {"
                f"background-color: rgb{self.c3};"
                "}"
                "QScrollArea QScrollBar::add-page, QScrollArea QScrollBar::sub-page {"
                f"background-color: rgb{self.c1};"
                f"border: rgb{self.c1};"
                "}"
        }
        self.wg.setStyleSheet(stl.get(self.colors_type)) if self.c1 is not None else False
        self.ALL()

        self.wg.setFrameShape(QtWidgets.QFrame.NoFrame)
    def SB(self):
        stl = {
            "th":
                "QSpinBox, QDoubleSpinBox {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.c3};"
                f"selection-background-color: rgb{self.c3};"
                f"selection-color: rgb{self.c1};"
                "border: none;"
                "}",
            "tr":
                "QSpinBox, QDoubleSpinBox {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.c3};"
                f"selection-background-color: rgb{self.c1};"
                f"selection-color: rgb{self.c3};"
                "border: none;"
                "}"
        }
        self.wg.setStyleSheet(stl.get(self.colors_type)) if self.c1 is not None else False
        self.ALL()

        if self.colors_type == "tr":
            self.wg.setFocusPolicy(QtCore.Qt.NoFocus)
        self.wg.setFrame(QtWidgets.QFrame.NoFrame)
    def TB(self):
        stl = {
            "th":
                "QToolBox::tab {"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.c1};"
                "}"
                
                "QToolBox::tab:hover {"
                f"color: rgb{self.c2};"
                "}"
                
                "QToolBox::tab:selected {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.bn};"
                "}"
                "QScrollArea QScrollBar {"
                f"background-color: rgb{self.c1};"
                "width: 20px;"
                "height: 20px;"
                "}"
                "QScrollArea QScrollBar::handle:vertical {"
                "min-height: 100px;"
                "}"
                "QScrollArea QScrollBar::handle:vertical {"
                "min-height: 100px;"
                "}"
                "QScrollArea QScrollBar::handle:horizontal {"
                "min-width: 100px;"
                "}"
                "QScrollArea QScrollBar::handle {"
                f"background-color: rgb{self.c3};"
                "}"
                "QScrollArea QScrollBar::add-page, QScrollArea QScrollBar::sub-page {"
                f"background-color: rgb{self.c1};"
                f"border: rgb{self.c1};"
                "}",
            "bd":
                "QToolBox::tab {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.c3};"
                f"border-width: {dct_size.get('wg').get('bd')}px;"
                "border-style: solid;"
                f"border-color: rgba(0, 0, 0, 0) rgba(0, 0, 0, 0) rgb{self.c3} rgba(0, 0, 0, 0);"  # top > right > bottom > left
                "}"

                "QToolBox::tab:hover {"
                f"color: rgb{self.c2};"
                "}"

                "QToolBox::tab:selected {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.bn};"
                f"border-width: {dct_size.get('wg').get('bd')}px;"
                "border-style: solid;"
                f"border-color: rgba(0, 0, 0, 0) rgba(0, 0, 0, 0) rgb{self.bn} rgba(0, 0, 0, 0);"  # top > right > bottom > left
                "}"

                "QScrollArea QScrollBar {"
                f"background-color: rgb{self.c1};"
                "width: 20px;"
                "height: 20px;"
                "}"
                "QScrollArea QScrollBar::handle:vertical {"
                "min-height: 100px;"
                "}"
                "QScrollArea QScrollBar::handle:vertical {"
                "min-height: 100px;"
                "}"
                "QScrollArea QScrollBar::handle:horizontal {"
                "min-width: 100px;"
                "}"
                "QScrollArea QScrollBar::handle {"
                f"background-color: rgb{self.c3};"
                "}"
                "QScrollArea QScrollBar::add-page, QScrollArea QScrollBar::sub-page {"
                f"background-color: rgb{self.c1};"
                f"border: rgb{self.c1};"
                "}",
            "rd":
                "QToolBox::tab {"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.c1};"
                f"border-top-left-radius: {self.r1}px;"
                f"border-top-right-radius: {self.r2}px;"
                f"border-bottom-right-radius: {self.r4}px;"
                f"border-bottom-left-radius: {self.r3}px;"
                "}"
        
                "QToolBox::tab:hover {"
                f"color: rgb{self.c2};"
                "}"
        
                "QToolBox::tab:selected {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.bn};"
                "}"

                "QScrollArea QScrollBar {"
                f"background-color: rgb{self.c1};"
                "width: 20px;"
                "height: 20px;"
                "}"
                "QScrollArea QScrollBar::handle:vertical {"
                "min-height: 100px;"
                "}"
                "QScrollArea QScrollBar::handle:vertical {"
                "min-height: 100px;"
                "}"
                "QScrollArea QScrollBar::handle:horizontal {"
                "min-width: 100px;"
                "}"
                "QScrollArea QScrollBar::handle {"
                f"background-color: rgb{self.c3};"
                "}"
                "QScrollArea QScrollBar::add-page, QScrollArea QScrollBar::sub-page {"
                f"background-color: rgb{self.c1};"
                f"border: rgb{self.c1};"
                "}"
        }
        self.wg.setStyleSheet(stl.get(self.colors_type)) if self.c1 is not None else False
        self.ALL()
    def TW(self):
        stl1 = {
            "th":
                "QTableCornerButton::section {"
                f"background-color: rgb{self.c3};"
                "}"
                "QTableView {"
                f"gridline-color: rgb{self.c3};"
                f"color: rgb{self.c3};"
                f"border: {dct_size.get('wg').get('bd')}px solid rgb{self.c3};"
                "}"
                "QTableView::item:selected {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.c3};"
                "}"
                "QTableView::item:hover {"
                f"background-color: rgb{self.bn};"
                f"color: rgb{self.c3};"
                "}"
                "QTableView::item:selected:hover {"
                f"background-color: rgb{self.bn};"
                f"color: rgb{self.c3};"
                "}"

                "QTableView QScrollBar {"
                f"background-color: rgb{self.c3};"
                "width: 20px;"
                "height: 20px;"
                "}"
                "QTableView QScrollBar::handle:vertical {"
                "min-height: 100px;"
                "}"
                "QTableView QScrollBar::handle:vertical {"
                "min-height: 100px;"
                "}"
                "QTableView QScrollBar::handle:horizontal {"
                "min-width: 100px;"
                "}"
                "QTableView QScrollBar::handle {"
                f"background-color: rgb{self.c3};"
                "}"
                "QTableView QScrollBar::add-page, QScrollBar::sub-page {"
                f"background-color: rgb{self.c1};"
                f"border: rgb{self.c1};"
                "}"
        }
        stl2 = {
            "th":
                "QHeaderView::section {"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.c1};"
                "border-style: none;"
                "}"
                "QHeaderView::section:checked {"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.c1};"
                "}"
        }
        stl3 = {
            "th":
                "QHeaderView::section {"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.c1};"
                "border-style: none;"
                "}"
                "QHeaderView::section:checked {"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.c1};"
                "}"
        }
        self.wg.setStyleSheet(stl1.get(self.colors_type)) if self.c1 is not None else False
        self.wg.horizontalHeader().setStyleSheet(stl2.get(self.colors_type)) if self.c1 is not None else False
        self.wg.verticalHeader().setStyleSheet(stl3.get(self.colors_type)) if self.c1 is not None else False
        self.ALL()

        self.wg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.wg.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.wg.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
        self.wg.verticalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
    def TXT(self):
        stl = {
            "th":
                "QLineEdit, QPlainTextEdit, QTextEdit {"
                f"background-color: rgb{self.c1};"
                f"border: {dct_size.get('wg').get('bd')}px solid rgb{self.c3};"
                "}"
                
                "QScrollBar {"
                f"background-color: rgb{self.c1};"
                "width: 20px;"
                "height: 20px;"
                "}"
                "QScrollBar::handle:vertical {"
                "min-height: 100px;"
                "}"
                "QScrollBar::handle:vertical {"
                "min-height: 100px;"
                "}"
                "QScrollBar::handle:horizontal {"
                "min-width: 100px;"
                "}"
                "QScrollBar::handle {"
                f"background-color: rgb{self.c3};"
                "}"
                "QScrollBar::add-page, QScrollBar::sub-page {"
                f"background-color: rgb{self.c1};"
                f"border: rgb{self.c1};"
                "}",
            "bd":
                "QLineEdit, QPlainTextEdit, QTextEdit {"
                f"border-width: {dct_size.get('wg').get('bd')}px;"
                "border-style: solid;"
                f"border-color: rgba(0, 0, 0, 0) rgba(0, 0, 0, 0) rgb{self.c3} rgba(0, 0, 0, 0);"  # top > right > bottom > left
                f"selection-background-color: rgb{self.c3};"
                f"selection-color: rgb{self.c1};"
                "}"
                "QScrollBar {"
                f"background-color: rgb{self.c1};"
                "width: 20px;"
                "height: 20px;"
                "}"
                "QScrollBar::handle:vertical {"
                "min-height: 100px;"
                "}"
                "QScrollBar::handle:vertical {"
                "min-height: 100px;"
                "}"
                "QScrollBar::handle:horizontal {"
                "min-width: 100px;"
                "}"
                "QScrollBar::handle {"
                f"background-color: rgb{self.c3};"
                "}"
                "QScrollBar::add-page, QScrollBar::sub-page {"
                f"background-color: rgb{self.c1};"
                f"border: rgb{self.c1};"
                "}"
        }

        pl = QtGui.QPalette()
        pl.setColor(QtGui.QPalette.PlaceholderText, QtGui.QColor(*self.c2))
        pl.setColor(QtGui.QPalette.Text, QtGui.QColor(*self.c3))
        self.wg.setPalette(pl)

        self.wg.setStyleSheet(stl.get(self.colors_type)) if self.c1 is not None else False
        self.ALL()
