from PySide6.QtWidgets import QTextEdit
from dataclasses import dataclass


@dataclass
class AutoFormating:

    NONE: QTextEdit = QTextEdit.AutoNone
    BULLET_LIST: QTextEdit = QTextEdit.AutoBulletList
    ALL: QTextEdit = QTextEdit.AutoAll
