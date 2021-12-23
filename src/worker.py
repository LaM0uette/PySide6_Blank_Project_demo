from PySide6 import QtCore


class worker_signals(QtCore.QObject):
    finished = QtCore.Signal()
    error = QtCore.Signal(tuple)
    result = QtCore.Signal(object)


class worker(QtCore.QRunnable):
    finished = QtCore.Signal()

    def __init__(self, func, *args, **kwargs):
        super(worker, self).__init__()

        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.signals = worker_signals()

    @QtCore.Slot()
    def run(self):
        self.func(*self.args, **self.kwargs)

        try: self.signals.finished.emit()
        except: pass
