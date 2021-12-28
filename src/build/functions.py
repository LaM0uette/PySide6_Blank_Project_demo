from . import P_cur

class Functions:
    def __init__(self, **kwargs):

        self.kwargs = kwargs

    def CUR(self):
        cur = lambda val: P_cur().RTN_CUR(val)
        return QtGui.QCursor(QtGui.QPixmap(cur(val)[0]), cur(val)[1], cur(val)[2])