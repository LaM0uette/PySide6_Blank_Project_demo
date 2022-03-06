from PySide6 import QtWidgets


class InsertPolicy:

    def cb_no_insert(self): return QtWidgets.QComboBox.NoInsert
    def cb_insert_top(self): return QtWidgets.QComboBox.InsertAtTop
    def cb_insert_bottom(self): return QtWidgets.QComboBox.InsertAtBottom
    def cb_insert_current(self): return QtWidgets.QComboBox.InsertAtCurrent
    def cb_insert_after_current(self): return QtWidgets.QComboBox.InsertAfterCurrent
    def cb_insert_before_current(self): return QtWidgets.QComboBox.InsertBeforeCurrent
    def cb_insert_alphabetically(self): return QtWidgets.QComboBox.InsertAlphabetically
