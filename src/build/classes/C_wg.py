class C_wg:
    def __init__(self, **kwargs):

        self.kwargs = kwargs

        self.wg = self.kwargs.get("wg")

        attrs = self.kwargs.get("attrs")
        if attrs is None: return

        # Couleurs
        self.colors = attrs.get("colors")
        val = lambda v: self.colors.get(v) if self.colors.get(v) is not None else None
        if self.colors is None: self.c1, self.c2, self.c3, self.bn = None, None, None, None
        else: self.c1, self.c2, self.c3, self.bn = val("c1"), val("c2"), val("c3"), val("bn")

        # Dimension
        self.dim = attrs.get("dim")
        if self.dim is None: self.dim = {"w": None, "h": None}

        # Images
        self.img = attrs.get("img")
        self.img_check = attrs.get("img_check")
        self.th = attrs.get("th")
        self.th_hover = attrs.get("th_hover")
        self.th_check = attrs.get("th_check")

        self.font = attrs.get("font")
        self.rd = attrs.get("rd")
        self.bd = attrs.get("bd")
        self.cur = attrs.get("cur")
        self.align = attrs.get("align")
        self.edit = attrs.get("edit")
        self.scroll = attrs.get("scroll")
        self.header = attrs.get("header")
        self.pb_sb = attrs.get("pb_sb")


    def STL_PB(self):
        self.wg.setStyleSheet(f"background-color: rgb{self.c1}")
