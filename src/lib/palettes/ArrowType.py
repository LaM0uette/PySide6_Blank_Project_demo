from dataclasses import dataclass

from PySide6.QtCore import Qt


@dataclass
class ArrowType:

    NO = Qt.NoArrow
    UP = Qt.UpArrow
    DOWN = Qt.DownArrow
    LEFT = Qt.LeftArrow
    RIGHT = Qt.RightArrow
