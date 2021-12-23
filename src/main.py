import sys

from PySide6 import QtCore, QtWidgets, QtGui

from .gui.main_ui import Ui_main


class main(Ui_main, QtWidgets.QWidget):
    def __init__(self):
        super(main, self).__init__()

        self.setupUi(self)
        self.INIT()


    def IN_BASE(self):
        pass
    def IN_CLASSE(self):
        pass
    def IN_WG(self):
        pass
    def IN_WG_BASE(self):
        pass
    def IN_CONNECTIONS(self):
        pass
    def IN_ACT(self):
        pass
    def INIT(self):
        self.IN_BASE()
        self.IN_CLASSE()
        self.IN_WG()
        self.IN_WG_BASE()
        self.IN_CONNECTIONS()
        self.IN_ACT()


app = QtWidgets.QApplication(sys.argv)
app.processEvents()

fen = main()
fen.show()

sys.exit(app.exec())
