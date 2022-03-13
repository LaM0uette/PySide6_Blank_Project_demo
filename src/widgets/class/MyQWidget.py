


class MyQWidget:
    def __init__(
            self,
            widget,

            size_policy_h,
            size_policy_v,
    ):

        widget.setSizePolicy(size_policy_h, size_policy_v)
