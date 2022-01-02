from src.build.data.Dim import Dim

class P_dim(Dim):
    def __init__(self):
        super().__init__()

    def p_all(self): return {"w": None, "h": None}
    def p_aw_mt(self): return {"w": None, "h": self.h_mt()}
    def p_aw_mb(self): return {"w": None, "h": self.h_mb()}

    def p_aw_mb_10(self): return {"w": None, "h": self.h_mb_10()}

    def p_c_mt(self): return {"w": self.h_mt(), "h": self.h_mt()}
    def p_r_mt(self): return {"w": self.h_mt()*1.4, "h": self.h_mt()}
    def p_r_mb(self): return {"w": self.h_mb()*4, "h": self.h_mb()}

    def p_aw_h0(self): return {"w": None, "h": self.h_h0()}
    def p_aw_h1(self): return {"w": None, "h": self.h_h1()}
    def p_aw_h2(self): return {"w": None, "h": self.h_h2()}
    def p_aw_h3(self): return {"w": None, "h": self.h_h3()}
    def p_aw_h4(self): return {"w": None, "h": self.h_h4()}
    def p_aw_h5(self): return {"w": None, "h": self.h_h5()}
    def p_aw_h6(self): return {"w": None, "h": self.h_h6()}
    def p_aw_h7(self): return {"w": None, "h": self.h_h7()}
    def p_aw_h8(self): return {"w": None, "h": self.h_h8()}
    def p_aw_h9(self): return {"w": None, "h": self.h_h9()}

    def p_aw_demo(self): return {"w": None, "h": self.h_h8()}
    def p_h5_h8_demo(self): return {"w": self.h_h5(), "h": self.h_h8()}
    def p_list_demo(self): return {"w": None, "h": self.h_h5()}
