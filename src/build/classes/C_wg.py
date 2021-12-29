from . import base

class C_wg:
    def __init__(self, **kwargs):

        self.kwargs = kwargs

        self.wg = self.kwargs.get("wg")

        attrs = self.kwargs.get("attrs")
        if attrs is None: return


        ### COULEURS
        self.colors_type = attrs.get("colors_type")
        if self.colors_type is None:
            self.colors_type = base.COLORS_TYPE

        self.colors = attrs.get("colors")

        val = lambda v: self.colors.get(v) if self.colors.get(v) is not None else base.COLORS
        if self.colors is None:
            self.c1, self.c2, self.c3, self.bn = base.C1, base.C2, base.C3, base.C4
        else:
            self.c1, self.c2, self.c3, self.bn = val("c1"), val("c2"), val("c3"), val("bn")


        ### DIMENSIONS
        self.dim = attrs.get("dim")
        if self.dim is None:
            self.dim = base.DIM

        self.x_ico = attrs.get("x_ico")
        if self.x_ico is None:
            self.x_ico = base.x_ico

        self.X_ICO = attrs.get("X_ICO")
        if self.X_ICO is None:
            self.X_ICO = base.X_ICO


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


        ### CURSOR
        self.cur = attrs.get("cur")
        if self.cur is None:
            self.cur = base.CUR


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


    def STL_PB(self):
        if self.colors_type == "th":
            self.wg.setStyleSheet(f"background-color: rgb{self.c1}")
        elif self.colors_type == "tr":
            self.wg.setStyleSheet(f"background-color: rgb{self.c3}")
