class Demo:
    def __init__(self,
                 valeur=None,
                 couleurs = "bleu",
                 dimensions = 70,
                 police = 10
    ):
        self.couleurs = couleurs
        self.dimensions = dimensions
        self.police = police

        try: self.couleurs = valeur.couleurs
        except: pass
        try: self.dimensions = valeur.dimensions
        except: pass
        try: self.police = valeur.police
        except: pass


        print(self.couleurs, self.dimensions, self.police)


class Test:
    couleurs = "rouge"
    police = 20

d = Demo(Test())
