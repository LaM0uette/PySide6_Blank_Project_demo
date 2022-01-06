from .data.Dim import Dim

class P_dim(Dim):
    def __init__(self):
        super().__init__()

    class rtn:
        def __init__(self, w=None, h=None):
            self.w = w
            self.h = h

        def h(self):
            return {"w": self.w, "h": self.h}
        def h0(self):
            if self.w is not None: self.w *= P_dim().h0()
            if self.h is not None: self.h *= P_dim().h0()
            return {"w": self.w, "h": self.h}
        def h1(self):
            if self.w is not None: self.w *= P_dim().h1()
            if self.h is not None: self.h *= P_dim().h1()
            return {"w": self.w, "h": self.h}
        def h2(self):
            if self.w is not None: self.w *= P_dim().h2()
            if self.h is not None: self.h *= P_dim().h2()
            return {"w": self.w, "h": self.h}
        def h3(self):
            if self.w is not None: self.w *= P_dim().h3()
            if self.h is not None: self.h *= P_dim().h3()
            return {"w": self.w, "h": self.h}
        def h4(self):
            if self.w is not None: self.w *= P_dim().h4()
            if self.h is not None: self.h *= P_dim().h4()
            return {"w": self.w, "h": self.h}
        def h5(self):
            if self.w is not None: self.w *= P_dim().h5()
            if self.h is not None: self.h *= P_dim().h5()
            return {"w": self.w, "h": self.h}
        def h6(self):
            if self.w is not None: self.w *= P_dim().h6()
            if self.h is not None: self.h *= P_dim().h6()
            return {"w": self.w, "h": self.h}
        def h7(self):
            if self.w is not None: self.w *= P_dim().h7()
            if self.h is not None: self.h *= P_dim().h7()
            return {"w": self.w, "h": self.h}
        def h8(self):
            if self.w is not None: self.w *= P_dim().h8()
            if self.h is not None: self.h *= P_dim().h8()
            return {"w": self.w, "h": self.h}
        def h9(self):
            if self.w is not None: self.w *= P_dim().h9()
            if self.h is not None: self.h *= P_dim().h9()
            return {"w": self.w, "h": self.h}
        def h10(self):
            if self.w is not None: self.w *= P_dim().h10()
            if self.h is not None: self.h *= P_dim().h10()
            return {"w": self.w, "h": self.h}

    class all(rtn):
        def __init__(self):
            super().__init__()
    class aw(rtn):
        def __init__(self):
            super().__init__(w=None, h=1)
    class ah(rtn):
        def __init__(self):
            super().__init__(w=1, h=None)
    class carr(rtn):
        def __init__(self):
            super().__init__(w=1, h=1)
    class w_rect_1_4(rtn):
        def __init__(self):
            super().__init__(w=1.4, h=1)
    class h_rect_1_4(rtn):
        def __init__(self):
            super().__init__(w=1, h=1.4)
    class w_rect_2(rtn):
        def __init__(self):
            super().__init__(w=2, h=1)
    class h_rect_2(rtn):
        def __init__(self):
            super().__init__(w=1, h=2)
    class w_rect_3(rtn):
        def __init__(self):
            super().__init__(w=3, h=1)
    class h_rect_3(rtn):
        def __init__(self):
            super().__init__(w=1, h=3)
    class w_rect_4(rtn):
        def __init__(self):
            super().__init__(w=4, h=1)
    class h_rect_4(rtn):
        def __init__(self):
            super().__init__(w=1, h=4)
