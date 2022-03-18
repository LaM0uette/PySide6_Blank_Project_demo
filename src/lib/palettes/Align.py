from PySide6.QtCore import Qt


class Align:

    @staticmethod
    def center(): return Qt.AlignCenter

    @staticmethod
    def center_horizontal(): return Qt.AlignHCenter

    @staticmethod
    def center_vertical(): return Qt.AlignVCenter

    @staticmethod
    def top(): return Qt.AlignTop

    @staticmethod
    def bottom(): return Qt.AlignBottom

    @staticmethod
    def right(): return Qt.AlignRight

    @staticmethod
    def left(): return Qt.AlignLeft
