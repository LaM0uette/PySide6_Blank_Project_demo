from .data.Data import Data

class P_police(Data):
    def __init__(self, grp="police"):
        super().__init__(grp)

    def titre(self): return self.GET_VAL("h1")
    def sous_titre(self): return self.GET_VAL("h2")
