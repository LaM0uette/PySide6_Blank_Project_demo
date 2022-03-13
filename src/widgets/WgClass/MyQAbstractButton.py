from .MyQWidget import MyQWidget
from src.lib.globals import v_wg


class MyQAbstractButton(MyQWidget):
    def __init__(
            self,
            widget,
            txt=v_wg.TXT,
    ):
        super().__init__(widget)

        widget.setText(txt)