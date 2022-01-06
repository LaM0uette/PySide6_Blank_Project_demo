from PySide6 import QtCore


class P_scroll:

    class rtn:
        def __init__(self, scroll):
            self.scroll = scroll

        def nd(self): return {"h": self.scroll, "v": QtCore.Qt.ScrollBarAsNeeded}
        def on(self): return {"h": self.scroll, "v": QtCore.Qt.ScrollBarAlwaysOn}
        def off(self): return {"h": self.scroll, "v": QtCore.Qt.ScrollBarAlwaysOff}


    class nd(rtn):
        def __init__(self):
            super().__init__(scroll=QtCore.Qt.ScrollBarAsNeeded)
    class on(rtn):
        def __init__(self):
            super().__init__(scroll=QtCore.Qt.ScrollBarAlwaysOn)
    class off(rtn):
        def __init__(self):
            super().__init__(scroll=QtCore.Qt.ScrollBarAlwaysOff)
