from PySide6 import QtWidgets, QtGui


class Shadow:

    def ombre_portee(self, wg):
        shadow = QtWidgets.QGraphicsDropShadowEffect(wg)
        shadow.setBlurRadius(12)
        shadow.setColor(QtGui.QColor(0, 0, 0, 130))
        shadow.setOffset(0, 0)
        return shadow
