from src.build.mods import Functions


class MyQWidget:
    def __init__(
            self,
            widget,
            size_policy,
            dim,
            font,
            cursor,
            focus_policy,
            layout_direction,
    ):
        # SizePolicy
        widget.setSizePolicy(size_policy.horizontal, size_policy.vertical)

        # Dimmensions
        if dim.minimum_width: widget.setMinimumWidth(dim.minimum_width)
        if dim.minimum_height: widget.setMinimumHeight(dim.minimum_height)
        if dim.maximum_width: widget.setMaximumWidth(dim.maximum_width)
        if dim.maximum_height: widget.setMaximumHeight(dim.maximum_height)

        # Font
        widget.setFont(font)

        # Curseur
        widget.setCursor(Functions().SET_CURSOR(cursor))

        # FocusPolicy
        widget.setFocusPolicy(focus_policy)

        # LayoutDirection
        widget.setLayoutDirection(layout_direction)
