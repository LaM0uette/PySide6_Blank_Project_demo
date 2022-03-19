from .MyQWidget import MyQWidget
from src.build.mods import Functions


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
            txt,
            ico,
            ico_rgb,
            ico_width,
            ico_height,
            checkable,
            checked,
            auto_repeat,
            auto_exclusive,
            auto_repeat_delay,
            auto_repeat_interval
    ):
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction)

        # Txt
        if txt: widget.setText(txt)

        # Ico
        if ico:
            widget.setIcon(Functions().SET_ICON(ico=ico, rgb=ico_rgb))

            if not ico_width: ico_width = widget.height()
            if not ico_height: ico_height = widget.height()
            widget.setIconSize(Functions().SET_ICON_DIM(width=ico_width, height=ico_height))

        # Actions
        widget.setCheckable(checkable)
        widget.setChecked(checked)
        widget.setAutoRepeat(auto_repeat)
        widget.setAutoExclusive(auto_exclusive)
        widget.setAutoRepeatDelay(auto_repeat_delay)
        widget.setAutoRepeatDelay(auto_repeat_interval)
