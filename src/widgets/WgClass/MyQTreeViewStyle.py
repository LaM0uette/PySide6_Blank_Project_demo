from .MyQTreeView import MyQTreeView


class Style(MyQTreeView):
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

            scroll_policy,

            abstract_item_view,
            drag_drop,
            selection_mode,
            selection_behavior,

            uniform_row_height,
            items_expandable,
            sorting,
            animate,
            header_hidden,
    ):
        super().__init__(widget, size_policy, dim, font, cursor, focus_policy, layout_direction, frame, scroll_policy, abstract_item_view, drag_drop, selection_mode, selection_behavior, uniform_row_height,items_expandable,sorting,animate,header_hidden)


