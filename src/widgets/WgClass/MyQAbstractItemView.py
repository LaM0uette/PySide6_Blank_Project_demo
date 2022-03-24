from .MyQAbstractScrollArea import MyQAbstractScrollArea


class MyQAbstractItemView(MyQAbstractScrollArea):
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

            auto_scroll,
            auto_scroll_margin,
            tab_navigation,
            drag_enabled,
            drag_drop_mode,
            drop_action,
            alternative_row_colors,
            selection_mode,
            selection_behavior,
    ):
        super().__init__(widget, size_policy, dim, font, cursor, focus_policy, layout_direction, frame, scroll_policy)

        widget.setAutoScroll(auto_scroll)
        widget.setAutoScrollMargin(auto_scroll_margin)
        widget.setTabKeyNavigation(tab_navigation)
        widget.setDragEnabled(drag_enabled)
        widget.setDragDropMode(drag_drop_mode)
        widget.setDefaultDropAction(drop_action)
        widget.setAlternatingRowColors(alternative_row_colors)
        widget.setSelectionMode(selection_mode)
        widget.setSelectionBehavior(selection_behavior)
