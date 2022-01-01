from PySide6 import QtCore, QtWidgets, QtGui

from ...build import *


class MB(QtWidgets.QMessageBox):
    def __init__(self, title, msg, ico):
        super(MB, self).__init__()

        self.setStyleSheet("QMessageBox {"
                           f"background-color: rgb{P_rgb().th1()};"
                           "}"

                           "QMessageBox QLabel {"
                           f"color: rgb{P_rgb().th1};"
                           "}"

                           "QMessageBox QPushButton {"
                           f"background-color: rgb{P_rgb().th3};"
                           f"color: rgb{P_rgb().th1};"
                           f"border: {P_style().bd()}px solid rgb{P_rgb().th1};"

                           f"font-size: {P_font().p()}px;"
                           "font-family: Berlin Sans FB Demi;"
                           "}"

                           "QMessageBox QPushButton:hover {"
                           f"background-color: rgb{P_rgb().th1};"
                           f"color: rgb{P_rgb().th3};"
                           f"border: {P_style().bd()}px solid rgb{P_rgb().th1};"
                           "}")
        self.setWindowTitle(title)
        self.setText(msg)
        self.setFont(Fct(font_size=P_font().p()).FONT())

        self.setWindowModality(QtCore.Qt.NonModal)
        self.setWindowIcon(QtGui.QIcon(ico))

        self.setCursor(Fct(cur="souris_main").CUR())
class MB_REPONSE(MB):
    def __init__(self, titre, msg, ico, msg_verif):
        super(MB_REPONSE, self).__init__(titre, msg, ico)

        self.addButton(self.Ok).setText(msg_verif)
        self.addButton(self.Cancel).setText("Annuler")
        self.setDefaultButton(QtWidgets.QMessageBox.Cancel)

        self.button(self.Ok).setFixedWidth(P_dim().h_h7())
        self.button(self.Ok).setFixedHeight(P_dim().h_h9())
        self.button(self.Cancel).setFixedWidth(P_dim().h_h7())
        self.button(self.Cancel).setFixedHeight(P_dim().h_h9())

        self.button(self.Ok).setCursor(Fct(cur="souris_main").CUR())
        self.button(self.Cancel).setCursor(Fct(cur="souris_main").CUR())
class MB_ALERTE(MB):
    def __init__(self, titre, msg, ico):
        super(MB_ALERTE, self).__init__(titre, msg, ico)

        self.addButton(self.Ok).setText("Ok")

        self.setDefaultButton(QtWidgets.QMessageBox.Ok)
        self.button(self.Ok).setFixedWidth(P_dim().h_h7())
        self.button(self.Ok).setFixedHeight(P_dim().h_h9())

        self.button(self.Ok).setCursor(Fct(cur="souris_main").CUR())
class MB_INFO(MB):
    def __init__(self, titre, msg, ico):
        super(MB_INFO, self).__init__(titre, msg, ico)

        self.addButton(self.Ok).setText("Ok")

        self.setDefaultButton(QtWidgets.QMessageBox.Ok)
        self.button(self.Ok).setFixedWidth(P_dim().h_h7())
        self.button(self.Ok).setFixedHeight(P_dim().h_h9())

        self.button(self.Ok).setCursor(Fct(cur="souris_main").CUR())
