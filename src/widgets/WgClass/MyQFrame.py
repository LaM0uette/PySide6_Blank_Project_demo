from .MyQWidget import MyQWidget


class MyQAbstractButton(MyQWidget):
    def __init__(
            self,
            widget,
            size_policy,
            dim,
            font,
            cursor,
            focus_policy,
            layout_direction,

            frame_shape,
            frame_shadow,
            line_width,
    ):
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction)

        widget.setFrameShape(frame_shape)
        widget.setFrameShadow(frame_shadow)
        widget.setLineWidth(line_width)

        # if shadow: widget.setGraphicsEffect(shadow)
