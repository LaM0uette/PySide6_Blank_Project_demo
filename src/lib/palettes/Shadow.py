from functools import partial

from PySide6 import QtWidgets, QtGui


class Shadow:

    @staticmethod
    def _get_shadow(wg, blur_radius: int, rgba: tuple, offset: list):
        shadow = QtWidgets.QGraphicsDropShadowEffect(wg)
        shadow.setBlurRadius(blur_radius)
        shadow.setColor(QtGui.QColor(*rgba))
        shadow.setOffset(offset[0], offset[1])
        return shadow

    GLOW = partial(_get_shadow, blur_radius=8, rgba=(0, 0, 0, 255), offset=[0, 0])
    PRESPECTIVE = partial(_get_shadow, blur_radius=6, rgba=(0, 0, 0, 150), offset=[3, 3])
    OMBRE_PORTEE = partial(_get_shadow, blur_radius=12, rgba=(0, 0, 0, 150), offset=[0, 0])

    def ombre_portee(self, wg):
        shadow = QtWidgets.QGraphicsDropShadowEffect(wg)
        shadow.setBlurRadius(12)
        shadow.setColor(QtGui.QColor(*self.rgb, 150))
        shadow.setOffset(0, 0)
        return shadow
