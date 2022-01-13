from PySide6 import QtCore, QtWidgets, QtGui

from . import p_base
from .Push_button import Classe_wg
from ...build import *
from ...config import vrb


class C_wg:
    def __init__(self, **kwargs):  # sourcery no-metrics
        """
        type=str %,
        colors_type=str %,
        colors=P_rgb().%,
        dim=P_dim().%,
        x_ico=P_style().%,
        X_ICO=P_style().%,
        img=P_img().%,
        img_check=P_img().%,
        th=str %,
        th_hover=str %,
        th_check=str %,
        font=P_font().%,
        rd=P_rd().%,
        bd=P_bd().%,
        align=P_align().%,
        edit=Bool %,
        word_wrap=Bool %,
        scroll=P_scroll().%,
        header={"h": Bool %, "v": Bool %},
        pb_sb=P_pb_sb(). %,
        pb_side=""=str %,
        pad=float %,
        min=int | float %,
        max=int | float %,
        step=int | float %,
        cur=str %,
        """

        self.kwargs = kwargs

        self.wg = self.kwargs.get("wg")

        attrs = self.kwargs.get("attrs")
        if attrs is None: return


        ### TYPE
        self.type = attrs.get("type")
        if self.type is None:
            self.type = p_base.PB_TYPE

        ### COULEURS
        self.colors_type = attrs.get("colors_type")
        if self.colors_type is None:
            self.colors_type = p_base.COLORS_TYPE

        self.colors = attrs.get("colors")

        val = lambda v: self.colors.get(v) if self.colors.get(v) is not None else p_base.COLORS
        if self.colors is None:
            self.c1, self.c2, self.c3, self.bn1, self.bn2 = p_base.C1, p_base.C2, p_base.C3, p_base.BN1, p_base.BN2
        else:
            self.c1, self.c2, self.c3, self.bn1, self.bn2 = val("c1"), val("c2"), val("c3"), val("bn1"), val("bn2")


        ### DIMENSIONS
        self.dim = attrs.get("dim")
        if self.dim is None:
            self.dim = p_base.DIM
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
        self.th = val("th", p_base.TM)
        self.th_hover = val("th_hover", p_base.TM_HOVER)
        self.th_check = val("th_check", p_base.TM_CHECK)


        ### FONT
        self.font = attrs.get("font")
        if self.font is None:
            self.font = p_base.FONT


        ### RADIUS
        self.rd = attrs.get("rd")
        if self.rd is None:
            self.rd = p_base.RD

        self.rd_mat = self.rd.get("mat")
        if self.rd_mat is None:
            self.rd_mat = p_base.RD_MAT

        val = lambda v: self.rd.get("px") if int(v) == 1 else p_base.RD_PX
        self.r1, self.r2, self.r3, self.r4 = val(self.rd_mat[:1]), val(self.rd_mat[1:2]), val(self.rd_mat[2:3]), val(self.rd_mat[3:4])


        ### BORDURES
        self.bd = attrs.get("bd")
        if self.bd is None:
            self.bd = p_base.BD

        self.bd_mat = self.bd.get("mat")
        if self.bd_mat is None:
            self.bd_mat = p_base.BD_MAT

        self.bd_px = self.bd.get("px")
        if self.bd_px is None:
            self.bd_px = p_base.BD_PX

        self.bd_th = self.bd.get("th")
        if self.bd_th is None:
            self.bd_th = p_base.BD_TH

        val = lambda v: self.bd_th + (255,) if int(v) == 1 else p_base.BD_RGBA
        self.o1, self.o2, self.o3, self.o4 = val(self.bd_mat[:1]), val(self.bd_mat[1:2]), val(self.bd_mat[2:3]), val(self.bd_mat[3:4])


        ### PARAMETRES
        self.align = attrs.get("align")
        if self.align is None:
            self.align = p_base.ALIGN

        self.edit = attrs.get("edit")
        if self.edit is None:
            self.edit = p_base.EDIT

        self.word_wrap = attrs.get("word_wrap")
        if self.word_wrap is None:
            self.word_wrap = p_base.WORD_WRAP

        self.scroll = attrs.get("scroll")
        if self.scroll is None:
            self.scroll = p_base.SCROLL

        self.header = attrs.get("header")
        if self.header is None:
            self.header = p_base.HEADER

        self.pb_sb = attrs.get("pb_sb")
        if self.pb_sb is None:
            self.pb_sb = p_base.PB_SB

        self.pad = attrs.get("pad")
        if self.pad is None:
            self.pad = p_base.PAD
        elif self.pad == "bd":
            self.pad = P_style().bd()

        self.pb_side = attrs.get("pb_side")
        if self.pb_side is None:
            self.pb_side = p_base.PB_SIDE

        self.min = attrs.get("min")
        if self.min is None:
            self.min = p_base.VAL_MIN

        self.max = attrs.get("max")
        if self.max is None:
            self.max = p_base.VAL_MAX

        self.step = attrs.get("step")
        if self.step is None:
            self.step = p_base.STEP


            ### CURSOR
        self.cur = attrs.get("cur")
        if self.cur is None:
            self.cur = p_base.CUR


        ### VAR
        wg_type = ""
        if isinstance(self.wg, QtWidgets.QScrollArea): wg_type = "QScrollArea"
        elif isinstance(self.wg, QtWidgets.QTreeWidget): wg_type = "QTreeWidget"
        elif isinstance(self.wg, QtWidgets.QToolBox): wg_type = "QToolBox"

        elif isinstance(self.wg, QtWidgets.QFontComboBox): wg_type = "QFontComboBox"
        elif isinstance(self.wg, QtWidgets.QComboBox): wg_type = "QComboBox"
        elif isinstance(self.wg, QtWidgets.QDateEdit): wg_type = "QDateEdit"
        elif isinstance(self.wg, QtWidgets.QLabel): wg_type = "QLabel"
        elif isinstance(self.wg, QtWidgets.QListWidget): wg_type = "QListWidget"
        elif isinstance(self.wg, QtWidgets.QPushButton): wg_type = "QPushButton"
        elif isinstance(self.wg, QtWidgets.QCheckBox): wg_type = "QCheckBox"
        elif isinstance(self.wg, QtWidgets.QRadioButton): wg_type = "QRadioButton"
        elif isinstance(self.wg, QtWidgets.QProgressBar): wg_type = "QProgressBar"
        elif isinstance(self.wg, QtWidgets.QSlider): wg_type = "QSlider"
        elif isinstance(self.wg, QtWidgets.QSpinBox): wg_type = "QSpinBox"
        elif isinstance(self.wg, QtWidgets.QTableWidget): wg_type = "QTableWidget"
        elif isinstance(self.wg, QtWidgets.QLineEdit): wg_type = "QLineEdit"
        elif isinstance(self.wg, QtWidgets.QTextEdit): wg_type = "QTextEdit"
        elif isinstance(self.wg, QtWidgets.QPlainTextEdit): wg_type = "QPlainTextEdit"
        elif isinstance(self.wg, QtWidgets.QFrame): wg_type = "QFrame"


        # [class ~='{wg_type}']
        bd = f".{wg_type}#{self.wg.objectName()}" \
             "{" \
             f"border-width: {self.bd_px}px;" \
             "border-style: solid;" \
             f"border-color: rgba{self.o1} rgba{self.o2} rgba{self.o3} rgba{self.o4};" \
             f"padding: {self.pad}px;" \
             "}"
        rd = f".{wg_type}#{self.wg.objectName()}" \
             "{" \
             f"border-top-left-radius: {self.r1}px;" \
             f"border-top-right-radius: {self.r2}px;" \
             f"border-bottom-right-radius: {self.r4}px;" \
             f"border-bottom-left-radius: {self.r3}px;" \
             "}"
        flat = f".{wg_type}#{self.wg.objectName()}:flat" \
               "{" \
               "border: none;" \
               "}"
        scroll = f".{wg_type}#{self.wg.objectName()} QScrollBar " \
                 "{" \
                 f"background-color: rgb{self.c1};" \
                 "width: 20px;" \
                 "height: 20px;" \
                 "}" \
                 f".{wg_type}#{self.wg.objectName()} ::handle:vertical" \
                 "{" \
                 "min-height: 100px;" \
                 "}" \
                 f".{wg_type}#{self.wg.objectName()} ::handle:vertical" \
                 "{" \
                 "min-height: 100px;" \
                 "}" \
                 f".{wg_type}#{self.wg.objectName()} ::handle:horizontal" \
                 "{" \
                 "min-width: 100px;" \
                 "}" \
                 f".{wg_type}#{self.wg.objectName()}  QScrollBar::handle" \
                 "{" \
                 f"background-color: rgb{self.c3};" \
                 "}" \
                 f".{wg_type}#{self.wg.objectName()}  QScrollBar::add-page, .{wg_type}#{self.wg.objectName()} QScrollBar::sub-page" \
                 "{" \
                 f"background-color: rgb{self.c1};" \
                 f"border: rgb{self.c1};" \
                 "}"

        try:
            if self.pb_sb == QtWidgets.QAbstractSpinBox.ButtonSymbols.PlusMinus:
                pb_up = P_img().plus()
                pb_down = P_img().moins()
            elif self.pb_sb == QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows:
                pb_up = P_img().fleche_top()
                pb_down = P_img().fleche_bottom()
            else:
                pb_up = ""
                pb_down = ""

            dct_sb = {
                "lr":
                    "QSpinBox::up-button, QDoubleSpinBox::up-button  {"
                    "subcontrol-origin: margin;"
                    "subcontrol-position: center left;"
                    f"image: url({pb_up + 'th3.svg'});"
                    f"height: {self.dim_ico}px;"
                    f"width: {self.dim_ico}px;"
                    "}"
                    
                    "QSpinBox::down-button, QDoubleSpinBox::down-button  {"
                    "subcontrol-origin: margin;"
                    "subcontrol-position: center right;"
                    f"image: url({pb_down + 'th3.svg'});"
                    f"height: {self.dim_ico}px;"
                    f"width: {self.dim_ico}px;"
                    "}",
                "tb":
                    "QSpinBox::up-button, QDoubleSpinBox::up-button  {"
                    f"image: url({pb_up + 'th3.svg'});"
                    f"height: {self.dim.get('h') / 2}px;"
                    f"width: {self.dim.get('h') / 2}px;"
                    "}"
                    
                    "QSpinBox::down-button, QDoubleSpinBox::down-button  {"
                    f"image: url({pb_down + 'th3.svg'});"
                    f"height: {self.dim.get('h') / 2}px;"
                    f"width: {self.dim.get('h') / 2}px;"
                    "}",
            }
        except: dct_sb = {}

        if self.bd.get("mat") == "0000":
            self.inc = rd
            self.inc_flat = rd + flat
        else:
            self.inc = rd + bd
            self.inc_flat = self.inc
        if wg_type in {"QFontComboBox", "QComboBox", "QListWidget", "QScrollArea", "QTreeWidget", "QTableWidget", "QTextEdit", "QPlainTextEdit", "QToolBox"}:
            self.inc += scroll
            self.inc_flat += scroll
        if wg_type in {"QSpinBox"}:
            self.inc += dct_sb.get(self.pb_side)


    def STL_ALL(self, val=""):  # sourcery skip: extract-method
        # Dimensions
        try: Fct(wg=self.wg, w=self.dim.get("w"), h=self.dim.get("h")).DIM()
        except: pass

        # Image
        if val not in ("fr", "lw", "tw", "ck", "rb", "sca", "sb", "tb"):
            try: Fct(wg=self.wg, img=self.img + self.th, dim=self.dim_ico).ICON()
            except: pass

            # try: Fct(wg=self.wg, img=self.img + self.th).PIXMAP()
            # except: pass

        # Font
        if val not in ("fr", "sca"):
            try: self.wg.setFont(Fct(font_size=self.font).FONT())
            except: pass

        # Paramètres
        if val not in ("fr", "ck", "rb", "sca"):
            try: self.wg.setAlignment(self.align)
            except: pass
            try: self.wg.setEditable(self.edit)
            except: pass
            try: self.wg.setWordWrap(self.word_wrap)
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
        if val not in ("fr", "lb", "pg", "sca"):
            try: self.wg.setCursor(Fct(cur=self.cur).CUR())
            except: pass
            try: self.wg.view().setCursor(Fct(cur=P_cur().souris_main()).CUR())
            except: pass
            try: self.wg.viewport().setCursor(Fct(cur=self.cur).CUR())
            except: pass
            try: self.wg.lineEdit().setCursor(Fct(cur=P_cur().IBeam()).CUR())
            except: pass
            try: self.wg.calendarWidget().setCursor(Fct(cur=P_cur().souris_main()).CUR())
            except: pass
        if val in ("fr", "sb", "sca") and self.colors_type == "tr":
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
                f"background-color: rgba(0, 0, 0, 0);"
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
        self.wg.lineEdit().setFont(Fct(font_size=self.font).FONT())
    def STL_CK(self):
        self.STL_ALL("ck")

        stl = {
            "th":
                "QCheckBox {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.c3};"
                "}"

                "QCheckBox:hover {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.bn1};"
                "}"

                "QCheckBox:checked {"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.c1};"
                "}"

                "QCheckBox:checked:hover {"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.bn1};"
                "}"

                "QCheckBox:flat {"
                "border: none;"
                "}"

                "QCheckBox::indicator {"
                f"margin-left: {(self.dim.get('h') - (self.dim.get('h') * P_style().x_ico())) / 2}px;"
                f"width: {self.dim.get('h') * P_style().x_ico()}px;"
                f"height: {self.dim.get('h') * P_style().x_ico()}px"
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

                f"{self.inc}",
            "tr":
                "QCheckBox {"
                f"color: rgb{self.c3};"
                "spacing: 10px;"
                "}"

                "QCheckBox:hover {"
                f"color: rgb{self.bn1};"
                "}"

                "QCheckBox:checked:hover {"
                f"color: rgb{self.bn1};"
                "}"

                "QCheckBox:flat {"
                "border: none;"
                "}"

                "QCheckBox::indicator {"
                f"margin-left: {(self.dim.get('h') - (self.dim.get('h') * P_style().x_ico())) / 2}px;"
                f"width: {self.dim.get('h') * P_style().x_ico()}px;"
                f"height: {self.dim.get('h') * P_style().x_ico()}px"
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

                f"{self.inc}"
        }
        self.wg.setStyleSheet(stl.get(self.colors_type))
    def STL_DE(self):
        self.wg.setCalendarPopup(True)
        self.STL_ALL()

        font_cal = P_font().h4()
        stl = {
            "th":
                "QDateEdit::drop-down {"
                f"image: url({P_img().calendrier() + '.svg'});"
                f"width: {self.dim_ico}px;"
                f"height: {self.dim_ico}px;"
                f"margin-top: {(self.dim.get('h') - self.dim_ico)/2.5}px;"
                f"margin-right: {(self.dim.get('h') - self.dim_ico)/2.5}px;"
                "}"

                "QDateEdit {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.c3};"
                f"selection-background-color: rgb{self.c3};"
                f"selection-color: rgb{self.c1};"
                "border: none;"
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
                f"icon-size: {font_cal}px, {font_cal}px;"
                "}"
                "QToolButton#qt_calendar_nextmonth  {"
                f"qproperty-icon: url({P_img().fleche_droite() + 'bn1' + '.svg'});"
                f"icon-size: {font_cal}px, {font_cal}px;"
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

                f"{self.inc}",
            "tr":
                "QDateEdit::drop-down {"
                f"image: url({P_img().calendrier() + '.svg'});"
                f"width: {self.dim_ico}px;"
                f"height: {self.dim_ico}px;"
                f"margin-top: {(self.dim.get('h') - self.dim_ico) / 2.5}px;"
                f"margin-right: {(self.dim.get('h') - self.dim_ico) / 2.5}px;"
                "}"
        
                "QDateEdit {"
                f"background-color: rgba(0, 0, 0, 0);"
                f"color: rgb{self.c3};"
                f"selection-background-color: rgb{self.c3};"
                f"selection-color: rgb{self.c1};"
                "border: none;"
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
                f"icon-size: {font_cal}px, {font_cal}px;"
                "}"
                "QToolButton#qt_calendar_nextmonth  {"
                f"qproperty-icon: url({P_img().fleche_droite() + 'bn1' + '.svg'});"
                f"icon-size: {font_cal}px, {font_cal}px;"
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
        
                f"{self.inc}"
        }
        self.wg.setStyleSheet(stl.get(self.colors_type))

        dateDuJour = vrb.DATE_NOW_FORMAT.split("_")
        QdateDuJour = QtCore.QDate(int(dateDuJour[2]), int(dateDuJour[1]), int(dateDuJour[0]))
        self.wg.setDateTime(QtCore.QDateTime(QdateDuJour, QtCore.QTime(0, 0, 0)))
        self.wg.setDate(QdateDuJour)
        self.wg.setFocusPolicy(QtCore.Qt.NoFocus)
    def STL_FR(self):
        self.STL_ALL("fr")

        stl = {
            "th":
                f".QFrame#{self.wg.objectName()} "
                "{"
                f"background-color: rgb{self.c1};"
                "}"

                f"{self.inc}",
        }
        self.wg.setStyleSheet(stl.get(self.colors_type))
        self.wg.setFrameShape(QtWidgets.QFrame.NoFrame)
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
    def STL_LW(self):
        self.STL_ALL()

        stl = {
            "th":
                "QListWidget {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.c3};"
                f"border: {P_style().bd()}px solid rgb{self.c3};"
                "}"
                "QListWidget::item:selected {"
                f"background-color: rgb{self.c2};"
                f"color: rgb{self.bn1};"
                "}"
                "QListWidget::item:hover {"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.c1};"
                "}"
                "QListWidget::item:selected:hover {"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.bn1};"
                "}"

                f"{self.inc}"
        }
        self.wg.setStyleSheet(stl.get(self.colors_type))
        self.wg.setFrameShape(QtWidgets.QFrame.NoFrame)
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
        # self.wg.setFocusPolicy(QtCore.Qt.NoFocus)
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
    def STL_PG(self):
        self.STL_ALL()

        stl = {
            "th":
                "QProgressBar {"
                f"background-color: rgb{self.c1};"
                "}"

                "QProgressBar::chunk {"
                f"background-color: rgb{self.c3};"
                "}"

                f"{self.inc}"
        }
        self.wg.setStyleSheet(stl.get(self.colors_type))
    def STL_RB(self):
        self.STL_ALL("rb")

        stl = {
            "th":
                "QRadioButton {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.c3};"
                "}"

                "QRadioButton:hover {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.bn1};"
                "}"

                "QRadioButton:checked {"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.c1};"
                "}"

                "QRadioButton:checked:hover {"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.bn1};"
                "}"

                "QRadioButton:flat {"
                "border: none;"
                "}"

                "QRadioButton::indicator {"
                f"margin-left: {(self.dim.get('h') - (self.dim.get('h') * P_style().x_ico())) / 2}px;"
                f"width: {self.dim.get('h') * P_style().x_ico()}px;"
                f"height: {self.dim.get('h') * P_style().x_ico()}px"
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
                
                f"{self.inc}",
            "tr":
                "QRadioButton {"
                f"color: rgb{self.c3};"
                "spacing: 10px;"
                "}"

                "QRadioButton:hover {"
                f"color: rgb{self.bn1};"
                "}"

                "QRadioButton:checked:hover {"
                f"color: rgb{self.bn1};"
                "}"

                "QRadioButton:flat {"
                "border: none;"
                "}"

                "QRadioButton::indicator {"
                f"margin-left: {(self.dim.get('h') - (self.dim.get('h') * P_style().x_ico())) / 2}px;"
                f"width: {self.dim.get('h') * P_style().x_ico()}px;"
                f"height: {self.dim.get('h') * P_style().x_ico()}px"
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
                
                f"{self.inc}",
        }
        self.wg.setStyleSheet(stl.get(self.colors_type))
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
    def STL_SB(self):
        self.STL_ALL("sb")

        stl = {
            "th":
                "QSpinBox, QDoubleSpinBox {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.c3};"
                f"selection-background-color: rgb{self.c3};"
                f"selection-color: rgb{self.c1};"
                "}"

                f"{self.inc}",
            "tr":
                "QSpinBox, QDoubleSpinBox {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.c3};"
                f"selection-background-color: rgb{self.c1};"
                f"selection-color: rgb{self.c3};"
                "}"

                f"{self.inc}"
        }
        self.wg.setStyleSheet(stl.get(self.colors_type))

        self.wg.setMinimum(self.min)
        self.wg.setMaximum(self.max)
        self.wg.setSingleStep(self.step)

        if self.colors_type == "tr":
            self.wg.setFocusPolicy(QtCore.Qt.NoFocus)
        self.wg.setFrame(QtWidgets.QFrame.NoFrame)



    def STL_SD(self):
        self.STL_ALL()

        stl = {
            "th":
                "QSlider {"
                "margin: 0px"
                "}"
                
                "QSlider::groove:horizontal {"
                "border-radius: 5px;"
                "height: 20px;"
                "margin: 0px;"
                f"background-color: rgb{self.c2};"
                "}"
                
                "QSlider::groove:horizontal:hover {"
                f"background-color: rgb{self.c2};"
                "}"
                
                "QSlider::handle:horizontal {"
                "border: none;"
                "height: 20px;"
                "width: 20px;"
                "margin: -10px 0px;"
                "border-radius: 5px;"
                f"background-color: rgb{self.c3};"
                "}"
                
                "QSlider::handle:horizontal:hover {"
                f"background-color: rgb{self.bn1};"
                "}"
                "QSlider::handle:horizontal:pressed {"
                f"background-color: rgb{self.bn2};"
                "}"
                
                
                "QSlider::groove:vertical {"
                "border-radius: 5px;"
                "width: 20px;"
                "margin: 0px;"
                f"background-color: rgb{self.c2};"
                "}"
                
                "QSlider::groove:vertical:hover {"
                f"background-color: rgb{self.c2};"
                "}"
                
                "QSlider::handle:vertical {"
                "border: none;"
                "height: 20px;"
                "width: 20px;"
                "margin: 0px -10px;"
                "border-radius: 5px;"
                f"background-color: rgb{self.c3};"
                "}"
                
                "QSlider::handle:vertical:hover {"
                f"background-color: rgb{self.bn1};"
                "}"
                "QSlider::handle:vertical:pressed {"
                f"background-color: rgb{self.bn2};"
                "}"
                
                f"{self.inc}",
            "rond":
                "QSlider {"
                "margin: 0px"
                "}"
        
                "QSlider::groove:horizontal {"
                "border-radius: 10px;"
                "height: 20px;"
                "margin: 0px;"
                f"background-color: rgb{self.c2};"
                "}"
        
                "QSlider::groove:horizontal:hover {"
                f"background-color: rgb{self.c2};"
                "}"
        
                "QSlider::handle:horizontal {"
                "border: none;"
                "height: 5px;"
                "width: 14px;"
                "margin: -5px 0px;"
                "border-radius: 15px;"
                f"border: 8px solid rgb{self.c3};"
                "}"
                
                "QSlider::handle:horizontal:hover {"
                f"border: 8px solid rgb{self.bn1};"
                "}"
                "QSlider::handle:horizontal:pressed {"
                f"border: 8px solid rgb{self.bn2};"
                "}"
        
        
                "QSlider::groove:vertical {"
                "border-radius: 10px;"
                "width: 20px;"
                "margin: 0px;"
                f"background-color: rgb{self.c2};"
                "}"
        
                "QSlider::groove:vertical:hover {"
                f"background-color: rgb{self.c2};"
                "}"
        
                "QSlider::handle:vertical {"
                "border: none;"
                "height: 14px;"
                "width: 5px;"
                "margin: 0px -5px;"
                "border-radius: 15px;"
                f"border: 8px solid rgb{self.c3};"
                "}"
                
                "QSlider::handle:vertical:hover {"
                f"border: 8px solid rgb{self.bn1};"
                "}"
                "QSlider::handle:vertical:pressed {"
                f"border: 8px solid rgb{self.bn2};"
                "}"
        }
        self.wg.setStyleSheet(stl.get(self.colors_type))


    def STL_TW(self):
        self.STL_ALL()

        stl1 = {
            "th":
                "QTableCornerButton::section {"
                f"background-color: rgb{self.c3};"
                "}"
                "QTableView {"
                f"background-color: rgba(0, 0, 0, 0);"
                f"gridline-color: rgb{self.c3};"
                f"color: rgb{self.c3};"
                f"border: {P_style().bd()}px solid rgb{self.c3};"
                "}"
                "QTableView::item:selected {"
                f"background-color: rgb{self.c2};"
                f"color: rgb{self.c3};"
                "}"
                "QTableView::item:hover {"
                f"background-color: rgb{self.bn1};"
                f"color: rgb{self.c3};"
                "}"
                "QTableView::item:selected:hover {"
                f"background-color: rgb{self.bn1};"
                f"color: rgb{self.c3};"
                "}"

                f"{self.inc}"
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
        self.wg.setStyleSheet(stl1.get(self.colors_type))
        self.wg.horizontalHeader().setStyleSheet(stl2.get(self.colors_type))
        self.wg.verticalHeader().setStyleSheet(stl3.get(self.colors_type))

        self.wg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.wg.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.wg.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
        self.wg.verticalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
    def STL_TXT(self):
        self.STL_ALL()

        stl = {
            "th":
                "QLineEdit, QPlainTextEdit, QTextEdit {"
                f"background-color: rgb{self.c1};"
                "}"

                f"{self.inc}",
            "tr":
                "QLineEdit, QPlainTextEdit, QTextEdit {"
                f"background-color: rgba(0, 0, 0, 0);"
                "}"

                f"{self.inc}",
        }
        pl = QtGui.QPalette()
        pl.setColor(QtGui.QPalette.PlaceholderText, QtGui.QColor(*self.c2))
        pl.setColor(QtGui.QPalette.Text, QtGui.QColor(*self.c3))
        self.wg.setPalette(pl)

        self.wg.setStyleSheet(stl.get(self.colors_type))

    def STL_TRW(self):
        self.STL_ALL("trw")

        stl = {
            "th":
                "QHeaderView::section {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.c3};"
                "border: none"
                "}"
                 
                "QTreeView {"
                f"background-color: rgb{self.c1};"
                "}"
                
                "QTreeView::item {"
                f"background-color: rgb{self.c1};"
                f"color: rgb{self.c3};"
                "}"
                
                "QTreeView::item:hover {"
                f"color: rgb{self.bn1};"
                "}"
                
                "QTreeView::item:selected {"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.c1};"
                "}"
                
                "QTreeView::item:selected:hover {"
                f"background-color: rgb{self.c3};"
                f"color: rgb{self.bn1};"
                "}"

                f"{self.inc}",
            "tr":
                "QHeaderView::section {"
                "background-color: rgba(0, 0, 0, 0);"
                f"color: rgb{self.c3};"
                "border: none"
                "}"
        
                "QTreeView {"
                "background-color: rgba(0, 0, 0, 0);"
                "}"
        
                "QTreeView::item {"
                "background-color: rgba(0, 0, 0, 0);"
                f"color: rgb{self.c3};"
                "}"
        
                "QTreeView::item:hover {"
                "background-color: rgba(0, 0, 0, 0);"
                f"color: rgb{self.bn1};"
                "}"
        
                "QTreeView::item:selected {"
                "background-color: rgba(0, 0, 0, 0);"
                f"color: rgb{self.c2};"
                "}"
        
                "QTreeView::item:selected:hover {"
                "background-color: rgba(0, 0, 0, 0);"
                f"color: rgb{self.bn2};"
                "}"
        
                f"{self.inc}"
        }
        self.wg.setStyleSheet(stl.get(self.colors_type))
    def STL_TB(self):
        self.STL_ALL("tb")

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
                f"color: rgb{self.bn1};"
                "}"

                f"{self.inc}"
        }
        self.wg.setStyleSheet(stl.get(self.colors_type))


"""
background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));
"""


