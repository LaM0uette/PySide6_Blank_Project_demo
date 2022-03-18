from PySide6.QtCore import Qt


class ArrowType:

    @staticmethod
    def no(): return Qt.NoArrow

    @staticmethod
    def up(): return Qt.UpArrow

    @staticmethod
    def down(): return Qt.DownArrow

    @staticmethod
    def left(): return Qt.LeftArrow

    @staticmethod
    def right(): return Qt.RightArrow
