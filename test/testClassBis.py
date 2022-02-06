class Demo:
    def __init__(self,
                 *args,
                 valeur=None,
                 couleurs = "bleu",
                 dimensions = 80,
                 police = 10
    ):
        self.args = args
        self.couleurs = couleurs
        self.dimensions = dimensions
        self.police = police

        try: self.couleurs = valeur.couleurs
        except: pass
        try: self.dimensions = valeur.dimensions
        except: pass
        try: self.police = valeur.police
        except: pass


        print(self.args, self.couleurs, self.dimensions, self.police)
        print(len(self.args))


class Test:
    couleurs = "orange"
    police = 20


lst = "f", "f", "r", "r", "r"
d = Demo(*lst, valeur=Test)
