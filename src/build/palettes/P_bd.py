from .P_style import P_style
from .P_rgb import P_rgb


# top - right - bottom - left
class P_bd:

    class rtn:
        def __init__(self, mat, bd=P_style().bd()):
            self.mat = mat
            self.bd = bd

        def th1(self): return {"mat": self.mat, "px": self.bd, "th": P_rgb().th1()}
        def th2(self): return {"mat": self.mat, "px": self.bd, "th": P_rgb().th2()}
        def th3(self): return {"mat": self.mat, "px": self.bd, "th": P_rgb().th3()}
        def bn1(self): return {"mat": self.mat, "px": self.bd, "th": P_rgb().bn1()}
        def bn2(self): return {"mat": self.mat, "px": self.bd, "th": P_rgb().bn2()}


    class all(rtn):
        def __init__(self):
            super().__init__(mat="1111")
    class top(rtn):
        def __init__(self):
            super().__init__(mat="1000")
    class right(rtn):
        def __init__(self):
            super().__init__(mat="0100")
    class bottom(rtn):
        def __init__(self):
            super().__init__(mat="0010")
    class left(rtn):
        def __init__(self):
            super().__init__(mat="0001")

    class rl(rtn):
        def __init__(self):
            super().__init__(mat="0101")
    class trl(rtn):
        def __init__(self):
            super().__init__(mat="1101")
