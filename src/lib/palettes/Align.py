from PySide6 import QtCore


class Align:

    def center(self): return QtCore.Qt.AlignCenter
    def center_horizontal(self): return QtCore.Qt.AlignHCenter
    def center_vertical(self): return QtCore.Qt.AlignVCenter
    def top(self): return QtCore.Qt.AlignTop
    def bottom(self): return QtCore.Qt.AlignBottom
    def right(self): return QtCore.Qt.AlignRight
    def left(self): return QtCore.Qt.AlignLeft
