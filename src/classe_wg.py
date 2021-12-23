from PySide6 import QtCore, QtWidgets, QtGui

from .build import cursor, functions
from .config import colors
from .dct_gen import dct_size
from .dct_wg import dct_wg

pb = dct_wg.get("pb")
police = dct_size.get("police")
wg = dct_size.get("wg")


### QPushButton
class PB_CHECK(QtWidgets.QPushButton):
    def __init__(self, texte):
        super(PB_CHECK, self).__init__(texte)

    def mousePressEvent(self, event):
        if event.buttons() and QtCore.Qt.LeftButton:
            if self.isChecked() and self.isEnabled():
                self.setChecked(False)
                nom_pb = pb.get(self.objectName())
                functions.ICON(wg=self, img=nom_pb.get("img") + nom_pb.get("th"), dim=nom_pb.get("dim").get("h") * wg.get("x_ico"))
            elif not self.isChecked() and self.isEnabled():
                self.setChecked(True)
                nom_pb = pb.get(self.objectName())
                functions.ICON(wg=self, img=nom_pb.get("img_check") + nom_pb.get("th"), dim=nom_pb.get("dim").get("h") * wg.get("x_ico"))
class PB_ICO(QtWidgets.QPushButton):
    def __init__(self, texte):
        super(PB_ICO, self).__init__(texte)

    def enterEvent(self, event: QtGui.QEnterEvent) -> None:
        if not self.isChecked() and self.isEnabled():
            nom_pb = pb.get(self.objectName())
            functions.ICON(wg=self, img=nom_pb.get("img") + nom_pb.get("th_hover"), dim=nom_pb.get("dim").get("h") * wg.get("x_ico"))
    def leaveEvent(self, event: QtGui.QEnterEvent) -> None:
        if not self.isChecked() and self.isEnabled():
            nom_pb = pb.get(self.objectName())
            functions.ICON(wg=self, img=nom_pb.get("img") + nom_pb.get("th"), dim=nom_pb.get("dim").get("h") * wg.get("x_ico"))
    def mousePressEvent(self, event):
        if event.buttons() and QtCore.Qt.LeftButton:
            nom_pb = pb.get(self.objectName())
            if self.isChecked() and self.isEnabled():
                self.setChecked(False)
                functions.ICON(wg=self, img=nom_pb.get("img") + nom_pb.get("th"), dim=nom_pb.get("dim").get("h") * wg.get("x_ico"))
            elif not self.isChecked() and self.isEnabled() and nom_pb.get("th_check") is not None:
                self.setChecked(True)
                functions.ICON(wg=self, img=nom_pb.get("img") + nom_pb.get("th_check"), dim=nom_pb.get("dim").get("h") * wg.get("x_ico"))
class PB_ZOOM(QtWidgets.QPushButton):
    def enterEvent(self, event: QtGui.QEnterEvent) -> None:
        if self.isEnabled():
            nom_pb = pb.get(self.objectName())
            dim = nom_pb.get("dim").get("h") * wg.get("X_ico")
            self.setIconSize(QtCore.QSize(dim, dim))
    def leaveEvent(self, event: QtGui.QEnterEvent) -> None:
        if not self.isChecked() and self.isEnabled():
            nom_pb = pb.get(self.objectName())
            dim = nom_pb.get("dim").get("h") * wg.get("x_ico")
            self.setIconSize(QtCore.QSize(dim, dim))


### QMessageBox ________________
class MB(QtWidgets.QMessageBox):
    def __init__(self, title, msg, ico):
        super(MB, self).__init__()

        self.setStyleSheet("QMessageBox {"
                           f"background-color: rgb{colors.th2};"
                           "}"

                           "QMessageBox QLabel {"
                           f"color: rgb{colors.th4};"
                           "}"

                           "QMessageBox QPushButton {"
                           f"background-color: rgb{colors.th2};"
                           f"color: rgb{colors.th4};"
                           f"border: {wg.get('bd')}px solid rgb{colors.th4};"

                           f"font-size: {police.get('h3')}px;"
                           "font-family: Berlin Sans FB Demi;"
                           "}"

                           "QMessageBox QPushButton:hover {"
                           f"background-color: rgb{colors.th4};"
                           f"color: rgb{colors.th2};"
                           f"border: {wg.get('bd')}px solid rgb{colors.th4};"
                           "}")
        self.setWindowTitle(title)
        self.setText(msg)
        self.setFont(functions.FONT(police.get("h3")))

        self.setWindowModality(QtCore.Qt.NonModal)
        self.setWindowIcon(QtGui.QIcon(ico))

        self.setCursor(QtGui.QCursor(QtGui.QPixmap(cursor.cur_souris[0]), cursor.cur_souris[1], cursor.cur_souris[2]))
class MB_REPONSE(MB):
    def __init__(self, titre, msg, ico, msg_verif):
        super(MB_REPONSE, self).__init__(titre, msg, ico)

        self.addButton(self.Ok).setText(msg_verif)
        self.addButton(self.Cancel).setText("Annuler")
        self.setDefaultButton(QtWidgets.QMessageBox.Cancel)

        self.button(self.Ok).setFixedWidth(wg.get("h1"))
        self.button(self.Ok).setFixedHeight(wg.get("h4"))
        self.button(self.Cancel).setFixedWidth(wg.get("h1"))
        self.button(self.Cancel).setFixedHeight(wg.get("h4"))

        self.button(self.Ok).setCursor(QtGui.QCursor(QtGui.QPixmap(cursor.cur_souris[0]), cursor.cur_souris[1], cursor.cur_souris[2]))
        self.button(self.Cancel).setCursor(QtGui.QCursor(QtGui.QPixmap(cursor.cur_souris[0]), cursor.cur_souris[1], cursor.cur_souris[2]))
class MB_ALERTE(MB):
    def __init__(self, titre, msg, ico):
        super(MB_ALERTE, self).__init__(titre, msg, ico)

        self.addButton(self.Ok).setText("Ok")

        self.setDefaultButton(QtWidgets.QMessageBox.Ok)
        self.button(self.Ok).setFixedWidth(wg.get("h1"))
        self.button(self.Ok).setFixedHeight(wg.get("h4"))

        self.button(self.Ok).setCursor(QtGui.QCursor(QtGui.QPixmap(cursor.cur_souris[0]), cursor.cur_souris[1], cursor.cur_souris[2]))
class MB_INFO(MB):
    def __init__(self, titre, msg, ico):
        super(MB_INFO, self).__init__(titre, msg, ico)

        self.addButton(self.Ok).setText("Ok")

        self.setDefaultButton(QtWidgets.QMessageBox.Ok)
        self.button(self.Ok).setFixedWidth(wg.get("h1"))
        self.button(self.Ok).setFixedHeight(wg.get("h4"))

        self.button(self.Ok).setCursor(QtGui.QCursor(QtGui.QPixmap(cursor.cur_souris[0]), cursor.cur_souris[1], cursor.cur_souris[2]))
