from src.lib.globals import v_wg


class MyQWidget:
    def __init__(
            self,
            widget,
            size_policy_h=v_wg.SIZE_POLICY_H,
            size_policy_v=v_wg.SIZE_POLICY_V,
            fixed_width=None,
            fixed_height=None,
            minimum_width=None,
            minimum_height=None,
            maximum_width=None,
            maximum_height=None,
    ):

        widget.setSizePolicy(size_policy_h, size_policy_v)

        if fixed_width: widget.setFixedWidth(fixed_width)
        if fixed_height: widget.setFixedHeight(fixed_height)
        if minimum_width: widget.setMinimumWidth(minimum_width)
        if minimum_height: widget.setMinimumHeight(minimum_height)
        if maximum_width: widget.setMaximumWidth(maximum_width)
        if maximum_height: widget.setMaximumHeight(maximum_height)
