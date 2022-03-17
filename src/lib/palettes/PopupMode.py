from PySide6.QtWidgets import QToolButton


class PopupMode:

    def delayed_popup(self): return QToolButton.DelayedPopup
    def menu_button_popup(self): return QToolButton.MenuButtonPopup
    def instant_popup(self): return QToolButton.InstantPopup
