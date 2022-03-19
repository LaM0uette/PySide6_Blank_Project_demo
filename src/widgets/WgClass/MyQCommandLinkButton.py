from .MyQPushButton import MyQPushButton


class MyQCommandLinkButton(MyQPushButton):
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
            ico_rgb,
            ico_width,
            ico_height,
            checkable,
            checked,
            auto_repeat,
            auto_exclusive,
            auto_repeat_delay,
            auto_repeat_interval,
            auto_default,
            default,
            flat,
            description
    ):

        # Default
        super().__init__(widget, size_policy, dim, font, cursor, focus_policy, layout_direction, txt, ico, ico_rgb, ico_width, ico_height, checkable, checked, auto_repeat, auto_exclusive, auto_repeat_delay, auto_repeat_interval, auto_default, default, flat)

        widget.setAutoDefault(auto_default)
        widget.setDefault(default)
        widget.setFlat(flat)
        if description: widget.setDescription(description)
