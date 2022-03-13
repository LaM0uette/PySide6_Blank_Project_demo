from .MyQWidget import MyQWidget
from src.build.mods import Functions
from src.lib.globals import v_wg


class MyQAbstractButton(MyQWidget):
    def __init__(
            self,
            widget,
            txt=v_wg.TXT,
            ico=None,
            ico_rgb=None,
    ):
        super().__init__(widget)

        # Txt
        widget.setText(txt)

        # Ico
        if ico:
            widget.setIcon(Functions().SET_ICON(ico=ico, ico_rgb=ico_rgb))
            # widget.setIconSize(QtCore.QSize(dim, dim))
