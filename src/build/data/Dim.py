from src.build.data.Data import Data

class Dim(Data):
    def __init__(self, grp="dimension"):
        super().__init__(grp)

    def h_mt(self): return self.GET_VAL("h9")
