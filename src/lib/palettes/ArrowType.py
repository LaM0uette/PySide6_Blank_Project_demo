from dataclasses import dataclass

from PySide6.QtCore import Qt


@dataclass
class ArrowType:
    NO: Qt = Qt.NoArrow
    UP: Qt = Qt.UpArrow
    DOWN: Qt = Qt.DownArrow
    LEFT: Qt = Qt.LeftArrow
    RIGHT: Qt = Qt.RightArrow
