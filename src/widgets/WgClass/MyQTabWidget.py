from .MyQWidget import MyQWidget


class MyQTabWidget(MyQWidget):
    def __init__(
            self,
            widget,
            size_policy,
            dim,
            font,
            cursor,
            focus_policy,
            layout_direction,

            frame,
    ):
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction)
