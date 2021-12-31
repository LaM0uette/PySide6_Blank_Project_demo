from PySide6 import QtCore, QtWidgets

from . import base
from . import Classe_wg
from ...build import *
from ...config import vrb


class C_wg:
    def __init__(self, **kwargs):

        self.kwargs = kwargs

        self.wg = self.kwargs.get("wg")

        attrs = self.kwargs.get("attrs")
        if attrs is None: return


        ### TYPE
        self.type = attrs.get("type")
        if self.type is None:
            self.type = base.TYPE

        ### COULEURS
        self.colors_type = attrs.get("colors_type")
        if self.colors_type is None:
            self.colors_type = base.COLORS_TYPE

        self.colors = attrs.get("colors")

        val = lambda v: self.colors.get(v) if self.colors.get(v) is not None else base.COLORS
        if self.colors is None:
            self.c1, self.c2, self.c3, self.bn1, self.bn2 = base.C1, base.C2, base.C3, base.BN1, base.BN2
        else:
            self.c1, self.c2, self.c3, self.bn1, self.bn2 = val("c1"), val("c2"), val("c3"), val("bn1"), val("bn2")


        ### DIMENSIONS
        self.dim = attrs.get("dim")
        if self.dim is None:
            self.dim = base.DIM
            self.dim_ico = 0
            self.DIM_ICO = 0
        else:
            try:
                self.dim_ico = self.dim.get("h") * P_style().x_ico()
                self.DIM_ICO = self.dim.get("h") * P_style().X_ICO()
            except: pass

        ### IMAGES
        self.img = attrs.get("img")
        self.img_check = attrs.get("img_check")

        val = lambda v, v_th: attrs.get(v) if attrs.get(v) is not None else v_th
        self.th = val("th", base.TH)
        self.th_hover = val("th_hover", base.TH_HOVER)
        self.th_check = val("th_check", base.TH_CHECK)


        ### FONT
        self.font = attrs.get("font")
        if self.font is None:
            self.font = base.FONT


        ### RADIUS
        self.rd = attrs.get("rd")
        if self.rd is None:
            self.rd = base.RD

        self.rd_mat = self.rd.get("mat")
        if self.rd_mat is None:
            self.rd_mat = base.RD_MAT

        val = lambda v: self.rd.get("px") if int(v) == 1 else base.RD_PX
        self.r1, self.r2, self.r3, self.r4 = val(self.rd_mat[:1]), val(self.rd_mat[1:2]), val(self.rd_mat[2:3]), val(self.rd_mat[3:4])


        ### BORDURES
        self.bd = attrs.get("bd")
        if self.bd is None:
            self.bd = base.BD

        self.bd_mat = self.bd.get("mat")
        if self.bd_mat is None:
            self.bd_mat = base.BD_MAT

        self.bd_px = self.bd.get("px")
        if self.bd_px is None:
            self.bd_px = base.BD_PX

        self.bd_th = self.bd.get("th")
        if self.bd_th is None:
            self.bd_th = base.BD_TH

        val = lambda v: self.bd_th + (255,) if int(v) == 1 else base.BD_RGBA
        self.o1, self.o2, self.o3, self.o4 = val(self.bd_mat[:1]), val(self.bd_mat[1:2]), val(self.bd_mat[2:3]), val(self.bd_mat[3:4])


        ### PARAMETRES
        self.align = attrs.get("align")
        if self.align is None:
            self.align = base.ALIGN

        self.edit = attrs.get("edit")
        if self.edit is None:
            self.edit = base.EDIT

        self.scroll = attrs.get("scroll")
        if self.scroll is None:
            self.scroll = base.SCROLL

        self.header = attrs.get("header")
        if self.header is None:
            self.header = base.HEADER

        self.pb_sb = attrs.get("pb_sb")
        if self.pb_sb is None:
            self.pb_sb = base.PB_SB


        ### CURSOR
        self.cur = attrs.get("cur")
        if self.cur is None:
            self.cur = base.CUR


        ### VAR
        wg_type = ""
        if isinstance(self.wg, QtWidgets.QComboBox): wg_type = "QComboBox"
        elif isinstance(self.wg, QtWidgets.QLabel): wg_type = "QLabel"
        elif isinstance(self.wg, QtWidgets.QPushButton): wg_type = "QPushButton"
        elif isinstance(self.wg, QtWidgets.QScrollArea): wg_type = "QScrollArea"

        bd = f"[class~='{wg_type}']" \
             "{" \
             f"border-width: {self.bd_px}px;" \
             "border-style: solid;" \
             f"border-color: rgba{self.o1} rgba{self.o2} rgba{self.o3} rgba{self.o4};" \
             "}"
        rd = f"[class~='{wg_type}']" \
             "{" \
             f"border-top-left-radius: {self.r1}px;" \
             f"border-top-right-radius: {self.r2}px;" \
             f"border-bottom-right-radius: {self.r4}px;" \
             f"border-bottom-left-radius: {self.r3}px;" \
             "}"
        flat = f"[class~='{wg_type}']:flat" \
               "{" \
               "border: none;" \
               "}"
        scroll = f"[class~='{wg_type}'] QScrollBar " \
                 "{" \
                 f"background-color: rgb{self.c1};" \
                 "width: 20px;" \
                 "height: 20px;" \
                 "}" \
                 f"[class~='{wg_type}'] ::handle:vertical" \
                 "{" \
                 "min-height: 100px;" \
                 "}" \
                 f"[class~='{wg_type}'] ::handle:vertical" \
                 "{" \
                 "min-height: 100px;" \
                 "}" \
                 f"[class~='{wg_type}'] ::handle:horizontal" \
                 "{" \
                 "min-width: 100px;" \
                 "}" \
                 f"[class~='{wg_type}']  QScrollBar::handle" \
                 "{" \
                 f"background-color: rgb{self.c3};" \
                 "}" \
                 f"[class~='{wg_type}']  QScrollBar::add-page, [class~='{wg_type}']  QScrollBar::sub-page" \
                 "{" \
                 f"background-color: rgb{self.c1};" \
                 f"border: rgb{self.c1};" \
                 "}"

        if self.bd.get("mat") == "0000":
            self.inc = rd
            self.inc_flat = rd + flat
        else:
            self.inc = rd + bd
            self.inc_flat = self.inc

        if wg_type in ("QComboBox", "QScrollArea"):
            self.inc += scroll
            self.inc_flat += scroll

    def STL_ALL(self, val=""):
        # Dimensions
        try: Fct(wg=self.wg, w=self.dim.get("w"), h=self.dim.get("h")).DIM()
        except: pass

        # Image
        if not val in ("ckb", "rb"):
            try: Fct(wg=self.wg, img=self.img + self.th, dim=self.dim_ico).ICON()
            except: pass

            # try: Fct(wg=self.wg, img=self.img + self.th).PIXMAP()
            # except: pass

        # Font
        try: self.wg.setFont(Fct(font_size=self.font).FONT())
        except: pass

        # Paramètres
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

        # Curseur
        if not val in ("fr", "lb", "pg", "sca"):
            try: self.wg.setCursor(Fct(cur=self.cur).CUR())
            except: pass
            try: self.wg.view().setCursor(Fct(cur="souris_main").CUR())
            except: pass
            try: self.wg.viewport().setCursor(Fct(cur=self.cur).CUR())
            except: pass
            try: self.wg.lineEdit().setCursor(Fct(cur="IBeam").CUR())
            except: pass
            try: self.wg.calendarWidget().setCursor(Fct(cur="souris_main").CUR())
            except: pass
        if val in "sb" and self.colors_type == "tr":
            try: self.wg.lineEdit().setCursor(Fct(cur="souris_main").CUR())
            except: pass

    def STL_CB(self):
        self.STL_ALL()

        stl = {
            "th":
                "QComboBox {"
                f"background-color: rgb{self.c2};"
                f"color: rgb{self.c3};"
                f"selection-background-color: rgb{self.c3};"
                f"selection-color: rgb{self.c1};"
                "padding: 1px 0px 1px 3px;" #############################
                "}"

                "QComboBox::drop-down {"
                f"width: {self.wg.height()}px;"
                f"border: none;"
                "}"

                "QComboBox::down-arrow {"
                f"image: url({P_img().fleche_bottom() + 'bn1' + '.svg'});"
                f"width: {self.dim_ico}px;"
                f"height: {self.dim_ico}px;"
                "}"

                "QComboBox::down-arrow:hover {"
                f"image: url({P_img().fleche_bottom() + 'bn2' + '.svg'});"
                f"width: {self.dim_ico}px;"
                f"height: {self.dim_ico}px;"
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

                f"{self.inc}",
            "tr":
                "QComboBox {"
                f"color: rgb{self.c3};"
                f"selection-background-color: rgb{self.c3};"
                f"selection-color: rgb{self.c1};"
                "padding: 1px 0px 1px 3px;" #############################
                "}"

                "QComboBox::drop-down {"
                f"width: {self.wg.height()}px;"
                f"border: none;"
                "}"

                "QComboBox::down-arrow {"
                f"image: url({P_img().fleche_bottom() + 'bn1' + '.svg'});"
                f"width: {self.dim_ico}px;"
                f"height: {self.dim_ico}px;"
                "}"

                "QComboBox::down-arrow:hover {"
                f"image: url({P_img().fleche_bottom() + 'bn2' + '.svg'});"
                f"width: {self.dim_ico}px;"
                f"height: {self.dim_ico}px;"
                "}"

                "QComboBox QAbstractItemView::item {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.c3};"
                f"border: none;"
                "}"

                "QComboBox QAbstractItemView::item:hover {"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.c1};"
                f"border: none;"
                "}"

                f"{self.inc}",

        }
        self.wg.setStyleSheet(stl.get(self.colors_type))
    def STL_DE(self):
        self.wg.setCalendarPopup(True)
        self.STL_ALL()

        font_cal = P_font().p()
        stl = {
            "th":
                "QDateEdit::drop-down {"
                f"image: url({P_img().calendrier() + '.svg'});"
                f"width: {self.dim_ico}px;"
                f"height: {self.dim_ico}px;" #
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
                f"color: rgb{self.bn1};"
                "}"

                "QToolButton#qt_calendar_prevmonth {"
                f"qproperty-icon: url({P_img().fleche_gauche() + 'bn1' + '.svg'});"
                f"icon-size: {self.dim_ico}px, {self.dim_ico}px;"
                "}"
                "QToolButton#qt_calendar_nextmonth  {"
                f"qproperty-icon: url({P_img().fleche_droite() + 'bn1' + '.svg'});"
                f"icon-size: {self.dim_ico}px, {self.dim_ico}px;"
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
                f"border: {P_style().bd()}px solid rgb{self.c3};"
                "}"

                "QCalendarWidget QAbstractItemView:enabled {"
                f"background-color: rgb{self.c2};"
                f"color: rgb{self.c3};"
                f"selection-background-color: rgb{self.c3};"
                f"selection-color: rgb{self.bn2};"
                "}"

                "QCalendarWidget QWidget#qt_calendar_navigationbar {"
                f"background-color: rgb{self.c3};"
                "}"

                "QCalendarWidget QAbstractItemView:disabled {"
                f"color: rgb{self.c1};"
                "}"
        }
        self.wg.setStyleSheet(stl.get(self.colors_type)) if self.c1 is not None else False

        dateDuJour = vrb.DATE_NOW_FORMAT.split("_")
        QdateDuJour = QtCore.QDate(int(dateDuJour[2]), int(dateDuJour[1]), int(dateDuJour[0]))
        self.wg.setDateTime(QtCore.QDateTime(QdateDuJour, QtCore.QTime(0, 0, 0)))
        self.wg.setDate(QdateDuJour)
        self.wg.setFocusPolicy(QtCore.Qt.NoFocus)
    def STL_LB(self):
        self.STL_ALL()

        stl = {
            "th":
                "QLabel {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.c3};"
                "}"
                
                f"{self.inc}",
            "tr":
                "QLabel {"
                f"color: rgb{self.c1};"
                "}"

                f"{self.inc}"
        }
        self.wg.setStyleSheet(stl.get(self.colors_type))
    def STL_PB(self):
        self.STL_ALL()

        stl = {
            "txt":
                "QPushButton {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.c3};"
                f"border: {P_style().bd()}px solid rgb{self.c3};"
                "}"
                
                "QPushButton:hover {"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.c1};"
                f"border: {P_style().bd()}px solid rgb{self.c3};"
                "}"
                
                "QPushButton:pressed {"
                f"color: rgb{self.bn1};"
                "}"
                
                f"{self.inc}",
            "txt_inv":
                "QPushButton {"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.c1};"
                f"border: {P_style().bd()}px solid rgb{self.c3};"
                "}"

                "QPushButton:hover {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.c3};"
                f"border: {P_style().bd()}px solid rgb{self.c3};"
                "}"

                "QPushButton:pressed {"
                f"color: rgb{self.bn1};"
                "}"
                
                f"{self.inc}",
            "th":
                "QPushButton {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.c3};"
                "}"

                "QPushButton:hover {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.bn1};"
                "}"

                "QPushButton:checked {"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.c1};"
                "}"

                "QPushButton:checked:hover {"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.bn1};"
                "}"
                
                "QPushButton:pressed {"
                f"color: rgb{self.bn2};"
                "}"
                
                "QPushButton:checked:pressed {"
                f"color: rgb{self.bn2};"
                "}"
                
                f"{self.inc_flat}",
            "tr":
                "QPushButton {"
                f"color: rgb{self.c3};"
                "}"

                "QPushButton:hover {"
                f"color: rgb{self.bn1};"
                "}"

                "QPushButton:checked:hover {"
                f"color: rgb{self.bn1};"
                "}"
                
                "QPushButton:pressed {"
                f"color: rgb{self.bn2};"
                "}"
                
                f"{self.inc_flat}",
            "zoom":
                "QPushButton {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.c3};"
                "}"

                "QPushButton:checked {"
                f"background-color: rgb{self.c3};"
                "}"
                
                f"{self.inc_flat}",
            "uni":
                "QPushButton {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.c1};"
                "}"
                
                f"{self.inc_flat}",
        }
        self.wg.setStyleSheet(stl.get(self.colors_type))

        self.wg.setFlat(True)
        self.wg.setFocusPolicy(QtCore.Qt.NoFocus)
        self.wg.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

        if self.type is None: return
        else: cls = Classe_wg.Classe_wg(wg=self.wg, dim_ico=self.dim_ico, DIM_ICO=self.DIM_ICO, img=self.img, img_check=self.img_check, th=self.th, th_hover=self.th_hover, th_check=self.th_check)

        if self.type == "check":
            self.wg.mousePressEvent = cls.MP_CHECK
        elif self.type == "ico":
            self.wg.enterEvent = cls.ENT_ICO
            self.wg.leaveEvent = cls.LVE_ICO
            self.wg.mousePressEvent = cls.MP_ICO
        elif self.type == "zoom":
            self.wg.enterEvent = cls.ENT_ZOOM
            self.wg.leaveEvent = cls.LVE_ZOOM
        else: return
    def STL_SCA(self):
        self.STL_ALL("sca")

        stl = {
            "th":
                ".QScrollArea .QWidget{"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.c3};"
                "}"
                
                f"{self.inc}"
        }
        self.wg.setStyleSheet(stl.get(self.colors_type))
        self.wg.setFrameShape(QtWidgets.QFrame.NoFrame)
