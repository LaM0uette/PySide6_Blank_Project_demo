from .Data import Data

class Dim(Data):
    def __init__(self, grp="dimension"):
        super().__init__(grp)

    def h_mt(self): return self.GET_VAL("h9")
    def h_mb(self): return self.GET_VAL("h9")/1.4

    def h_mb_dlg(self): return self.GET_VAL("h9")
    def h_mb_dlg_2(self): return self.GET_VAL("h9")+2

    def h_h0(self): return self.GET_VAL("h0")
    def h_h1(self): return self.GET_VAL("h1")
    def h_h2(self): return self.GET_VAL("h2")
    def h_h3(self): return self.GET_VAL("h3")
    def h_h4(self): return self.GET_VAL("h4")
    def h_h5(self): return self.GET_VAL("h5")
    def h_h6(self): return self.GET_VAL("h6")
    def h_h7(self): return self.GET_VAL("h7")
    def h_h8(self): return self.GET_VAL("h8")
    def h_h9(self): return self.GET_VAL("h9")
