from .Dlg_msg import Dlg_msg


class Msg:

    def INFO(self):
        msg = Dlg_msg(msg="test")
        msg.exec()
