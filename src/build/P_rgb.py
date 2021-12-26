from .data.Data import Data

class P_rgb(Data):
    def __init__(self):
        super().__init__()

    def th1(self): return self.TH("th1")
    def th2(self): return self.TH("th2")
    def th3(self): return self.TH("th3")
    def th4(self): return self.TH("th4")
    def bn1(self): return self.TH("bn1")
    def bn2(self): return self.TH("bn2")
