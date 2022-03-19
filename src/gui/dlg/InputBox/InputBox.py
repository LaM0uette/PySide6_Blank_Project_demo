from src import *
from src.gui.dlg.InputBox.InputDlg import InputDlg


class InputBox:
    WIDTH = 650

    @staticmethod
    def TXT(
            title="INPUT",
            msg="Tapez votre texte",
            ico=Img.INFO, ico_rgb="th3",
            txt_ok="Ok",
            txt_cancel="Annuler",
            width=650,
            height=250,
            opacity=1,
    ):
        input_dlg = InputDlg(
            title=title,
            msg=msg,
            ico=ico,
            ico_rgb=ico_rgb,
            txt_ok=txt_ok,
            txt_cancel=txt_cancel,
            width=width,
            height=height,
            opacity=opacity
        )
        input_dlg.exec()
        return input_dlg.input_txt or False
