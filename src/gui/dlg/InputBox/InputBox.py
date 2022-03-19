import dataclasses
from functools import partial

from src import *
from src.gui.dlg.InputBox.InputDlg import InputDlg


@dataclasses.dataclass
class InputBox:

    @staticmethod
    def __rtn(width, height, opacity, title="INPUT", msg="Tapez votre texte", ico=Img.INFO, ico_rgb="th3", txt_ok="Ok", txt_cancel="Annuler"):
        input_dlg = InputDlg(
            width=width,
            height=height,
            opacity=opacity,
            title=title,
            msg=msg,
            ico=ico,
            ico_rgb=ico_rgb,
            txt_ok=txt_ok,
            txt_cancel=txt_cancel,
        )
        input_dlg.exec()
        return input_dlg.input_txt or False

    WIDTH: int = 650
    HEIGHT: int = 250
    OPACITY: float | int = 1

    TEXT = partial(__rtn, width=WIDTH, height=HEIGHT, opacity=OPACITY)
