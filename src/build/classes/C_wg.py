from . import base

class C_wg:
    def __init__(self, **kwargs):

        self.kwargs = kwargs

        self.wg = self.kwargs.get("wg")

        attrs = self.kwargs.get("attrs")
        if attrs is None: return

        # Couleurs
        self.colors = attrs.get("colors")
        val = lambda v: self.colors.get(v) if self.colors.get(v) is not None else base.COLORS
        if self.colors is None: self.c1, self.c2, self.c3, self.bn = base.C1, base.C2, base.C3, base.C4
        else: self.c1, self.c2, self.c3, self.bn = val("c1"), val("c2"), val("c3"), val("bn")

        # Dimension
        self.dim = attrs.get("dim")
        if self.dim is None: self.dim = base.DIM

        # Images
        self.img = attrs.get("img")
        self.img_check = attrs.get("img_check")
            #th
        val = lambda v, v_th: attrs.get(v) if attrs.get(v) is not None else v_th
        self.th = val("th", base.TH)
        self.th_hover = val("th_hover", base.TH_HOVER)
        self.th_check = val("th_check", base.TH_CHECK)

        # Font
        self.font = attrs.get("font")
        if self.font is None: self.font = base.FONT

        # Radius
        self.rd = attrs.get("rd")
        val = lambda v: self.rd.get("px") if int(v) == 1 else base.PX
        if self.rd is None: self.rd = base.RD
        self.rd_mat = self.rd.get("mat")
        if self.rd_mat is None: self.rd_mat = base.RD_MAT
        self.r1, self.r2, self.r3, self.r4 = val(self.rd_mat[:1]), val(self.rd_mat[1:2]), val(self.rd_mat[2:3]), val(self.rd_mat[3:4])

        # Bordures
        self.bd = attrs.get("bd")

        if self.bd is None: self.bd = base.BD


        self.cur = attrs.get("cur")
        self.align = attrs.get("align")
        self.edit = attrs.get("edit")
        self.scroll = attrs.get("scroll")
        self.header = attrs.get("header")
        self.pb_sb = attrs.get("pb_sb")


    def STL_PB(self):
        self.wg.setStyleSheet(f"background-color: rgb{self.c1}")
