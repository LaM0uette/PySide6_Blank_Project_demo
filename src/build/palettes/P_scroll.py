from PySide6 import QtCore


class P_scroll:

    def n_n(self): return {"h": QtCore.Qt.ScrollBarAsNeeded, "v": QtCore.Qt.ScrollBarAsNeeded}
    def n_on(self): return {"h": QtCore.Qt.ScrollBarAsNeeded, "v": QtCore.Qt.ScrollBarAlwaysOn}
    def n_of(self): return {"h": QtCore.Qt.ScrollBarAsNeeded, "v": QtCore.Qt.ScrollBarAlwaysOff}

    def on_n(self): return {"h": QtCore.Qt.ScrollBarAlwaysOn, "v": QtCore.Qt.ScrollBarAsNeeded}
    def on_on(self): return {"h": QtCore.Qt.ScrollBarAlwaysOn, "v": QtCore.Qt.ScrollBarAlwaysOn}
    def on_of(self): return {"h": QtCore.Qt.ScrollBarAlwaysOn, "v": QtCore.Qt.ScrollBarAlwaysOff}

    def of_n(self): return {"h": QtCore.Qt.ScrollBarAlwaysOff, "v": QtCore.Qt.ScrollBarAsNeeded}
    def of_on(self): return {"h": QtCore.Qt.ScrollBarAlwaysOff, "v": QtCore.Qt.ScrollBarAlwaysOn}
    def of_of(self): return {"h": QtCore.Qt.ScrollBarAlwaysOff, "v": QtCore.Qt.ScrollBarAlwaysOff}
