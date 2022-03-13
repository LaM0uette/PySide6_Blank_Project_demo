from src.build.mods import Functions
from src.lib.globals import v_wg
from src.lib.palettes import *


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
            font=v_wg.FONT,
            cursor=v_wg.CUR,
            focus_policy=v_wg.FOCUS_POLICY,
            layout_direction=v_wg.LAYOUT_DIRECTION,
    ):
        # SizePolicy
        widget.setSizePolicy(size_policy_h, size_policy_v)

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
