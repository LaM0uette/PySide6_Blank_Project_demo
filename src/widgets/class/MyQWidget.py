from src.lib.globals import v_wg


class MyQWidget:
    def __init__(
            self,
            widget,

            size_policy_h=v_wg.SIZE_POLICY_H,
            size_policy_v=v_wg.SIZE_POLICY_V,
    ):

        widget.setSizePolicy(size_policy_h, size_policy_v)
