from .data.Dim import Dim

class P_dim(Dim):
    def __init__(self):
        super().__init__()

    class rtn_w:
        def __init__(self, w=None):
            self.w = w

        def h0(self): return {"w": self.w, "h": P_dim().h_h0()}
        def h1(self): return {"w": self.w, "h": P_dim().h_h1()}
        def h2(self): return {"w": self.w, "h": P_dim().h_h2()}
        def h3(self): return {"w": self.w, "h": P_dim().h_h3()}
        def h4(self): return {"w": self.w, "h": P_dim().h_h4()}
        def h5(self): return {"w": self.w, "h": P_dim().h_h5()}
        def h6(self): return {"w": self.w, "h": P_dim().h_h6()}
        def h7(self): return {"w": self.w, "h": P_dim().h_h7()}
        def h8(self): return {"w": self.w, "h": P_dim().h_h8()}
        def h9(self): return {"w": self.w, "h": P_dim().h_h9()}
    class rtn_h:
        def __init__(self, h=None):
            self.h = h

        def h0(self): return {"w": P_dim().h_h0(), "h": self.h}
        def h1(self): return {"w": P_dim().h_h1(), "h": self.h}
        def h2(self): return {"w": P_dim().h_h2(), "h": self.h}
        def h3(self): return {"w": P_dim().h_h3(), "h": self.h}
        def h4(self): return {"w": P_dim().h_h4(), "h": self.h}
        def h5(self): return {"w": P_dim().h_h5(), "h": self.h}
        def h6(self): return {"w": P_dim().h_h6(), "h": self.h}
        def h7(self): return {"w": P_dim().h_h7(), "h": self.h}
        def h8(self): return {"w": P_dim().h_h8(), "h": self.h}
        def h9(self): return {"w": P_dim().h_h9(), "h": self.h}


    class aw(rtn_w):
        def __init__(self):
            super().__init__(w=None)
    class ah(rtn_h):
        def __init__(self):
            super().__init__(h=None)

    def p_all(self): return {"w": None, "h": None}
    def p_aw_mt(self): return {"w": None, "h": self.h_mt()}
    def p_aw_mb(self): return {"w": None, "h": self.h_mb()}

    def p_aw_mb_dlg_2(self): return {"w": None, "h": self.h_mb_dlg_2()}

    def p_c_mt(self): return {"w": self.h_mt(), "h": self.h_mt()}
    def p_c_mb(self): return {"w": self.h_mb(), "h": self.h_mb()}
    def p_r_mt(self): return {"w": self.h_mt()*1.4, "h": self.h_mt()}
    def p_r_mb(self): return {"w": self.h_mb()*1.4, "h": self.h_mb()}

    def p_r_mb_dlg(self): return {"w": self.h_h6(), "h": self.h_mb_dlg()}

    def p_c_h0(self): return {"w": self.h_h0(), "h": self.h_h0()}
    def p_c_h1(self): return {"w": self.h_h1(), "h": self.h_h1()}
    def p_c_h2(self): return {"w": self.h_h2(), "h": self.h_h2()}
    def p_c_h3(self): return {"w": self.h_h3(), "h": self.h_h3()}
    def p_c_h4(self): return {"w": self.h_h4(), "h": self.h_h4()}
    def p_c_h5(self): return {"w": self.h_h5(), "h": self.h_h5()}
    def p_c_h6(self): return {"w": self.h_h6(), "h": self.h_h6()}
    def p_c_h7(self): return {"w": self.h_h7(), "h": self.h_h7()}
    def p_c_h8(self): return {"w": self.h_h8(), "h": self.h_h8()}
    def p_c_h9(self): return {"w": self.h_h9(), "h": self.h_h9()}

    def p_h8_h9(self): return {"w": self.h_h8(), "h": self.h_h9()}

    def p_aw_demo(self): return {"w": None, "h": self.h_h8()}
    def p_h5_h8_demo(self): return {"w": self.h_h5(), "h": self.h_h8()}
    def p_list_demo(self): return {"w": None, "h": self.h_h5()}
