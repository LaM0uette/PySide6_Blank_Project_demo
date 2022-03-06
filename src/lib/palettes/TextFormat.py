from PySide6.QtCore import Qt


class TextFormat:

    def plain_text(self): return Qt.PlainText
    def rich(self): return Qt.RichText
    def auto(self): return Qt.AutoText
    def markdown(self): return Qt.MarkdownText
