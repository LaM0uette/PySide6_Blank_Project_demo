from .rgb import rgb

class P_rgb(rgb):
    def __init__(self):
        super().__init__()

    def th1(self): return {"c1": rgb().th1(), "c2":rgb().th2(), "c3":rgb().th3(), "bn":rgb().bn1()}
    def th2(self): return {"c1":rgb().th2(), "c2":rgb().th1(), "c3":rgb().th4(), "bn":rgb().bn1()}
    def th3(self): return {"c1":rgb().th3(), "c2":rgb().th4(), "c3":rgb().th1(), "bn":rgb().bn1()}
    def th4(self): return {"c1":rgb().th4(), "c2":rgb().th3(), "c3":rgb().th2(), "bn":rgb().bn1()}
    def u1(self): return {"c1":rgb().th1()}
    def u2(self): return {"c1":rgb().th2()}
    def u3(self): return {"c1":rgb().th3()}
    def u4(self): return {"c1":rgb().th4()}

    def p_vert(self, fct=th1):
        th = fct(self)
        th.update({"c3": rgb().vert()})
        return th
