from PySide6.QtCore import Qt


class ToolButtonStyle:

    def icon_only(self): return Qt.ToolButtonIconOnly
    def text_only(self): return Qt.ToolButtonTextOnly
    def text_beside_icon(self): return Qt.ToolButtonTextBesideIcon
    def text_under_icon(self): return Qt.ToolButtonTextUnderIcon
    def follow_style(self): return Qt.ToolButtonFollowStyle
