from dataclasses import dataclass

from PySide6.QtWidgets import QTextEdit


@dataclass
class AutoFormating:

    NONE = QTextEdit.AutoNone
    BULLET_LIST = QTextEdit.AutoBulletList
    ALL = QTextEdit.AutoAll
