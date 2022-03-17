from .MyQAbstractButton import MyQAbstractButton


class MyQCheckBox(MyQAbstractButton):
    def __init__(
            self,
            widget,
            size_policy_h,
            size_policy_v,
            fixed_width,
            fixed_height,
            minimum_width,
            minimum_height,
            maximum_width,
            maximum_height,
            font,
            cursor,
            focus_policy,
            layout_direction,
            txt,
            ico,
            ico_rgb,
            ico_width,
            ico_height,
            checkable,
            checked,
            auto_repeat,
            auto_exclusive,
            auto_repeat_delay,
            auto_repeat_interval,
            tristate,
    ):
        super().__init__(widget,size_policy_h,size_policy_v,fixed_width,fixed_height,minimum_width,minimum_height,maximum_width,maximum_height,font,cursor,focus_policy,layout_direction,txt,ico,ico_rgb,ico_width,ico_height,checkable,checked,auto_repeat,auto_exclusive,auto_repeat_delay,auto_repeat_interval)

        # Default
        widget.setTristate(tristate)
