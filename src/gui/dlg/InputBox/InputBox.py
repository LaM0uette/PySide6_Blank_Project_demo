from functools import partial

from src import *
from src.gui.dlg.InputBox.InputDlg import InputDlg


class InputBox:

    @staticmethod
    def __rtn(width, height, opacity, title, msg, ico, ico_rgb, txt_ok, txt_cancel):
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


    __WIDTH, __HEIGHT, __OPACITY = 650, 250, 1

    TEXT = partial(
        __rtn,
        width=__WIDTH,
        height=__HEIGHT,
        opacity=__OPACITY,
        title="INPUT",
        msg="Tapez votre texte",
        ico=Img.INFO,
        ico_rgb="th3",
        txt_ok="Ok",
        txt_cancel="Annuler"
    )
