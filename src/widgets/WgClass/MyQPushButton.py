from .MyQAbstractButton import MyQAbstractButton


class MyQPushButton(MyQAbstractButton):
    def __init__(
            self,
            widget,
            auto_default=False,
            default=False,
            flat=True,
    ):
        super().__init__(widget)

        widget.setAutoDefault(auto_default)
        widget.setDefault(default)
        widget.setFlat(flat)
