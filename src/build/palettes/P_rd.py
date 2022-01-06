# tl, tr, bl, br
class P_rd:

    class rtn:
        def __init__(self, mat):
            self.mat = mat

        def px_5(self): return {"mat": self.mat, "px": 5}
        def px_10(self): return {"mat": self.mat, "px": 10}
        def px_15(self): return {"mat": self.mat, "px": 15}
        def px_20(self): return {"mat": self.mat, "px": 20}
        def px_25(self): return {"mat": self.mat, "px": 25}
        def px_30(self): return {"mat": self.mat, "px": 30}


    class all(rtn):
        def __init__(self):
            super().__init__(mat="1111")
    class top_left(rtn):
        def __init__(self):
            super().__init__(mat="1000")
    class top_right(rtn):
        def __init__(self):
            super().__init__(mat="0100")
    class bottom_left(rtn):
        def __init__(self):
            super().__init__(mat="0010")
    class bottom_right(rtn):
        def __init__(self):
            super().__init__(mat="0001")

    class top(rtn):
        def __init__(self):
            super().__init__(mat="1100")
    class bottom(rtn):
        def __init__(self):
            super().__init__(mat="0011")
    class left(rtn):
        def __init__(self):
            super().__init__(mat="1010")
    class right(rtn):
        def __init__(self):
            super().__init__(mat="0101")
