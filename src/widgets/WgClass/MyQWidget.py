from src.build.mods import Functions


class MyQWidget:
    def __init__(
            self,
            widget,
            size_policy,
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
    ):
        print(size_policy.horizontal, size_policy.vertical)
        # SizePolicy
        widget.setSizePolicy(size_policy.horizontal, size_policy.vertical)

        # Dimmensions
        if fixed_width: widget.setFixedWidth(fixed_width)
        if fixed_height: widget.setFixedHeight(fixed_height)
        if minimum_width: widget.setMinimumWidth(minimum_width)
        if minimum_height: widget.setMinimumHeight(minimum_height)
        if maximum_width: widget.setMaximumWidth(maximum_width)
        if maximum_height: widget.setMaximumHeight(maximum_height)

        # Font
        widget.setFont(font)

        # Curseur
        widget.setCursor(Functions().SET_CURSOR(cursor))

        # FocusPolicy
        widget.setFocusPolicy(focus_policy)

        # LayoutDirection
        widget.setLayoutDirection(layout_direction)
