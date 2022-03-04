from PySide6.QtWidgets import QAbstractSpinBox


class SpinButton:

    def no_button(self): return QAbstractSpinBox.NoButtons
    def plus_minus(self): return QAbstractSpinBox.PlusMinus
    def up_down(self): return QAbstractSpinBox.UpDownArrows
