from src.build.data.Dim import Dim

class P_dim(Dim):
    def __init__(self):
        super().__init__()

    def p_all(self): return {"w": None, "h": None}
    def p_aw_mt(self): return {"w": None, "h": self.h_mt()}
    def p_c_mt(self): return {"w": self.h_mt(), "h": self.h_mt()}
    def p_r_mt(self): return {"w": self.h_mt()*1.4, "h": self.h_mt()}

    def p_aw_h8(self): return {"w": None, "h": self.h_h8()}
    def p_aw_h9(self): return {"w": None, "h": self.h_h9()}

    def p_aw_demo(self): return {"w": None, "h": self.h_h8()}
