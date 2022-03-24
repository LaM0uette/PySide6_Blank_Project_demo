from .MyQFrame import MyQFrame
from src.build.mods import Functions


class MyQAbstractScrollArea(MyQFrame):
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

            scroll_h_policy,
            scroll_v_policy,
            size_adjust_policy,
    ):
        super().__init__(widget, size_policy, dim, font, cursor, focus_policy, layout_direction, frame)

        widget.setHorizontalScrollBarPolicy(scroll_h_policy)
        widget.setVerticalScrollBarPolicy(scroll_v_policy)
        widget.setSizeAdjustPolicy(size_adjust_policy)
