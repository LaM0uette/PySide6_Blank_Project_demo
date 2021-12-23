import json

from ..config import vrb


class Data:
    def __init__(self, grp):
        self.grp = grp

    def OPEN_JSON(self, fichier_json):
        with open(f"{fichier_json}.json", "r") as fichier:
            return json.load(fichier)
    def GET_VAL(self, val):
        js = self.OPEN_JSON(fichier_json=f"{vrb.DO_JS_DATA}{self.grp}")
        return js.get(val)


class Police(Data):
    def __init__(self, grp="police"):
        super().__init__(grp)

    def titre(self): return self.GET_VAL("h1")
    def sous_titre(self): return self.GET_VAL("h2")
class Widg(Data):
    def __init__(self, grp="wg"):
        super().__init__(grp)

    def bd(self): return self.GET_VAL("bd")
    def x_ico(self): return self.GET_VAL("x_ico")
    def X_ICO(self): return self.GET_VAL("X_ICO")

class Dim(Data):
    def __init__(self, grp="dimension"):
        super().__init__(grp)

    def h_mt(self): return self.GET_VAL("h9")
class Pal(Dim):
    def __init__(self):
        super().__init__()

    def p_all(self): return {"w": None, "h": None}
    def p_aw_mt(self): return {"w": None, "h": self.h_mt()}
    def p_c_mt(self): return {"w": self.h_mt(), "h": self.h_mt()}
    def p_r_mt(self): return {"w": self.h_mt()*1.4, "h": self.h_mt()}
