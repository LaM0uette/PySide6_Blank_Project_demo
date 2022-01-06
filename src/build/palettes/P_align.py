from PySide6 import QtCore


class P_align:

    class rtn:
        def __init__(self, align):
            self.align = align

        def c(self): return self.align | QtCore.Qt.AlignVCenter
        def t(self): return self.align | QtCore.Qt.AlignTop
        def b(self): return self.align | QtCore.Qt.AlignBottom


    class c(rtn):
        def __init__(self):
            super().__init__(align=QtCore.Qt.AlignCenter)
    class l(rtn):
        def __init__(self):
            super().__init__(align=QtCore.Qt.AlignLeft)
    class r(rtn):
        def __init__(self):
            super().__init__(align=QtCore.Qt.AlignRight)
