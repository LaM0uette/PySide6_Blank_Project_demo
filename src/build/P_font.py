from .data.Data import Data

class P_font(Data):
    def __init__(self, grp="font"):
        super().__init__(grp)

    def titre(self): return self.GET_VAL("h1")
    def sous_titre(self): return self.GET_VAL("h2")
    def p(self): return self.GET_VAL("h4")
