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

            abstract_item_view,
    ):
        super().__init__(widget, size_policy, dim, font, cursor, focus_policy, layout_direction, frame, scroll_policy)

        widget.setAutoScroll(abstract_item_view.auto_scroll)
        widget.setAutoScrollMargin(abstract_item_view.auto_scroll_margin)
        widget.setTabKeyNavigation(abstract_item_view.tab_navigation)
        widget.setDragEnabled(abstract_item_view.drag_drop.drag_enabled)
        widget.setDragDropMode(abstract_item_view.drag_drop.drag_drop_mode)
        widget.setDefaultDropAction(abstract_item_view.drag_drop.drop_action)
        widget.setAlternatingRowColors(abstract_item_view.alternative_row_colors)
        widget.setSelectionMode(abstract_item_view.selection_mode)
        widget.setSelectionBehavior(abstract_item_view.selection_behavior)
