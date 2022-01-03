from .data.Rgb import Rgb

class P_rgb(Rgb):
    def __init__(self):
        super().__init__()

    def p_th1(self): return {"c1": Rgb().th1(), "c2": Rgb().th2(), "c3": Rgb().th3(), "bn1": Rgb().bn1(), "bn2": Rgb().bn2()}
    def p_th2(self): return {"c1": Rgb().th2(), "c2": Rgb().th3(), "c3": Rgb().th1(), "bn1": Rgb().bn1(), "bn2": Rgb().bn2()}
    def p_th3(self): return {"c1": Rgb().th3(), "c2": Rgb().th1(), "c3": Rgb().th2(), "bn1": Rgb().bn1(), "bn2": Rgb().bn2()}
    def p_u1(self): return {"c1": Rgb().th1()}
    def p_u2(self): return {"c1": Rgb().th2()}
    def p_u3(self): return {"c1": Rgb().th3()}

    def p_vert_th1(self):
        p = self.p_th1()
        p["c3"] = Rgb().vert()
        return p
    def p_vert_th2(self):
        p = self.p_th2()
        p["c3"] = Rgb().vert()
        return p

    def p_rouge_th1(self):
        p = self.p_th1()
        p["c3"] = Rgb().rouge()
        return p
    def p_rouge_th2(self):
        p = self.p_th2()
        p["c3"] = Rgb().rouge()
        return p
