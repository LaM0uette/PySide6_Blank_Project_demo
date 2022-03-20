from .MyQAbstractButton import MyQAbstractButton


class MyQCheckBox(MyQAbstractButton):
    def __init__(
            self,
            widget,
            size_policy,
            dim,
            font,
            cursor,
            focus_policy,
            layout_direction,
            txt,
            ico,
            checkable,
            checked,
            auto_repeat,
            auto_exclusive,
            auto_repeat_delay,
            auto_repeat_interval,
            tristate,
    ):
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction,txt,ico,checkable,checked,auto_repeat,auto_exclusive,auto_repeat_delay,auto_repeat_interval)

        # Default
        widget.setTristate(tristate)
