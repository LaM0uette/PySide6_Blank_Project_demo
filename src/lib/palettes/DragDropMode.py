from PySide6.QtWidgets import QAbstractItemView


class DragDropMode:

    NO = QAbstractItemView.NoDragDrop
    DRAG_ONLY = QAbstractItemView.DragOnly
    DROP_ONLY = QAbstractItemView.DropOnly
    DRAG_AND_DROP = QAbstractItemView.DragDrop
    INTERNAL_MOVE = QAbstractItemView.InternalMove
