from src.build.data.Rgb import Rgb

class P_rgb(Rgb):
    def __init__(self):
        super().__init__()

    def th1(self): return {"c1": Rgb().th1(), "c2": Rgb().th2(), "c3": Rgb().th3(), "bn": Rgb().bn1()}
    def th2(self): return {"c1": Rgb().th2(), "c2": Rgb().th1(), "c3": Rgb().th4(), "bn": Rgb().bn1()}
    def th3(self): return {"c1": Rgb().th3(), "c2": Rgb().th4(), "c3": Rgb().th1(), "bn": Rgb().bn1()}
    def th4(self): return {"c1": Rgb().th4(), "c2": Rgb().th3(), "c3": Rgb().th2(), "bn": Rgb().bn1()}
    def u1(self): return {"c1": Rgb().th1()}
    def u2(self): return {"c1": Rgb().th2()}
    def u3(self): return {"c1": Rgb().th3()}
    def u4(self): return {"c1": Rgb().th4()}

    def vert_th1(self): return {"c1": Rgb().th1(), "c2": Rgb().th2(), "c3": Rgb().vert(), "bn": Rgb().bn1()}
    def rouge_th1(self): return {"c1": Rgb().th1(), "c2": Rgb().th2(), "c3": Rgb().rouge(), "bn": Rgb().bn1()}
