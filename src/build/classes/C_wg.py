class C_wg:
    def __init__(self, **kwargs):

        self.kwargs = kwargs

    def STL_PB(self):
        self.kwargs.get("wg").setStyleSheet(f"background-color: rgb{self.kwargs.get('s')}")