from dataclasses import dataclass

from PySide6.QtCore import Qt


@dataclass
class Align:

    CENTER = Qt.AlignCenter
    CENTER_HORIZONTAL = Qt.AlignHCenter
    CENTER_VERTICAL = Qt.AlignVCenter
    TOP = Qt.AlignTop
    BOTTOM = Qt.AlignBottom
    RIGHT = Qt.AlignRight
    LEFT = Qt.AlignLeft
