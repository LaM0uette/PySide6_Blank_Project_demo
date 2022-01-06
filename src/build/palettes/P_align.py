from PySide6 import QtCore


class P_align:
    
    class c:
        align = QtCore.Qt.AlignCenter
        def c(self): return self.align | QtCore.Qt.AlignVCenter
        def t(self): return self.align | QtCore.Qt.AlignTop
        def b(self): return self.align | QtCore.Qt.AlignBottom
    class l:
        align = QtCore.Qt.AlignLeft
        def c(self): return self.align | QtCore.Qt.AlignVCenter
        def t(self): return self.align | QtCore.Qt.AlignTop
        def b(self): return self.align | QtCore.Qt.AlignBottom
    class r:
        align = QtCore.Qt.AlignRight
        def c(self): return self.align | QtCore.Qt.AlignVCenter
        def t(self): return self.align | QtCore.Qt.AlignTop
        def b(self): return self.align | QtCore.Qt.AlignBottom
