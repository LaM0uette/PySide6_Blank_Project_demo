from dataclasses import dataclass

from PySide6.QtWidgets import QAbstractSpinBox


@dataclass
class ButtonSymbols:

    NO_BUTTON = QAbstractSpinBox.NoButtons
    PLUS_MINUS = QAbstractSpinBox.PlusMinus
    UP_DOWN = QAbstractSpinBox.UpDownArrows
