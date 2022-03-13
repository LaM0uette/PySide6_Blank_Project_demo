from .MyQWidget import MyQWidget
from src.build.mods import Functions
from src.lib.globals import v_wg


class MyQAbstractButton(MyQWidget):
    def __init__(
            self,
            widget,
            txt=v_wg.TXT,
            ico=None,
            ico_rgb="",
            ico_width=None,
            ico_height=None,
            checkable = False,
            checked = False,
            auto_repeat = False,
            auto_exclusive = False,
            auto_repeat_delay = v_wg.REPEAT_DELAY,
            auto_repeat_interval = v_wg.REPEAT_INTERVAL,
    ):
        super().__init__(widget)

        # Txt
        widget.setText(txt)

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
