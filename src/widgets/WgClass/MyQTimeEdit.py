from PySide6 import QtCore

from .MyQAbstractSpinBox import MyQAbstractSpinBox


class MyQTimeEdit(MyQAbstractSpinBox):
    def __init__(
            self,
            widget,
            size_policy,
            dim,
            font,
            cursor,
            focus_policy,
            layout_direction,

            wrapping,
            frame,
            align,
            read_only,
            button_symbols,
            accelerated,

            date_time,
    ):
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction,wrapping,frame,align,read_only,button_symbols,accelerated)

        widget.setDateTime(QtCore.QDateTime(QtCore.QDate(*date_time.date), QtCore.QTime(*date_time.time)))
