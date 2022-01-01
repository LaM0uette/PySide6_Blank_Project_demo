from PySide6 import QtCore, QtWidgets

from ..gui import *
from ..build import *
from ..config import *
from ..In_classe import In_classe


class Dlg(dlg_ui.Ui_Dlg, QtWidgets.QWidget):
    sgn_ok = QtCore.Signal(str)

    def __init__(self, titre="Information", **kwargs):
        super(Dlg, self).__init__()

        self.titre = titre
        self.kwargs = kwargs

        self.width = self.kwargs.get("w")
        if self.width is None:
            self.width = config.widht / 2

        self.height = self.kwargs.get("h")
        if self.height is None:
            self.height = config.height / 3

        self.opacity = self.kwargs.get("opacity")
        if self.opacity is None:
            self.opacity = 1

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowModality(QtCore.Qt.NonModal)
        self.setupUi(self)
        self.INIT()


    ### INITIALISATION
    def IN_BASE(self):
        ## Fenetre
        self.setWindowTitle(self.titre)
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)
        self.setWindowOpacity(self.opacity)
    def IN_CLASSE(self):
        In_classe(ui=self)

        # QLineEdit | QTextEdit | QPlainTextEdit
        try: pass
        except: pass
        finally: pass

        # QComboBox
        try: pass
        except: pass
        finally: pass

        # QDateEdit
        try: pass
        except: pass
        finally: pass

        # QFrame
        try: pass
        except: pass
        finally: pass

        # QLabel
        try: pass
        except: pass
        finally: pass

        # QListWidget
        try: pass
        except: pass
        finally: pass

        # QPushButton
        try: pass
        except: pass
        finally: pass

        # QCheckBox
        try: pass
        except: pass
        finally: pass

        # QRadioButton
        try: pass
        except: pass
        finally: pass

        # QProgressBar
        try: pass
        except: pass
        finally: pass

        # QScrollBoxArea
        try: pass
        except: pass
        finally: pass

        # QSpinBox | QDoubleSpinBox
        try: pass
        except: pass
        finally: pass

        # QTableWidget
        try: pass
        except: pass
        finally: pass

        # QToolBox
        try: pass
        except: pass
        finally: pass
    def IN_WG(self):
        # Base
        self.setCursor(Fct(cur="souris").CUR())
        self.setStyleSheet(f"background-color: rgb{P_rgb().th1()};")

        # Frame menu_top
        self.fr_menu_top.setFixedHeight(P_dim().h_mt())

        # Icone de l'app
        dim = P_dim().p_c_mt()
        Fct(wg=self.lb_mt_ico, w=dim.get("w"), h=dim.get("h")).DIM()
        # self.lb_mt_ico.setPixmap(QtGui.QPixmap(PXM))
        self.lb_mt_ico.setScaledContents(True)
        self.lb_mt_nom.setText(self.titre)
    def IN_WG_BASE(self):
        pass
    def IN_CONNECTIONS(self):
        ## Menu_top
        self.pb_mt_quitter.clicked.connect(lambda: self.close())

        #
        self.pushButton.clicked.connect(self.test)
    def IN_ACT(self):
        pass
    def INIT(self):
        self.IN_BASE()
        self.IN_CLASSE()
        self.IN_WG()
        self.IN_WG_BASE()
        self.IN_CONNECTIONS()
        self.IN_ACT()



    def test(self):
        self.sgn_ok.emit("ok")
