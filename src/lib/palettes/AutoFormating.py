from dataclasses import dataclass

from PySide6.QtWidgets import QTextEdit


@dataclass
class AutoFormating:

    NONE: QTextEdit = QTextEdit.AutoNone
    BULLET_LIST: QTextEdit = QTextEdit.AutoBulletList
    ALL: QTextEdit = QTextEdit.AutoAll
