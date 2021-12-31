from PySide6 import QtCore


class P_align:

    def c_c(self): return QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter
    def c_t(self): return QtCore.Qt.AlignCenter | QtCore.Qt.AlignTop
    def c_b(self): return QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom

    def l_c(self): return QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
    def l_t(self): return QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop
    def l_b(self): return QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom

    def r_c(self): return QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter
    def r_t(self): return QtCore.Qt.AlignRight | QtCore.Qt.AlignTop
    def r_b(self): return QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom
