

class Img:

    def SVG(self, val, img): return f"src/assets/img/{val}/rgb/{img}"

    def calendrier(self): return self.SVG("divers", "calendrier")
    def main(self): return self.SVG("main", "main")
    def option(self): return self.SVG("ui", "option")
    def reduire(self): return self.SVG("ui", "reduire")
    def agrandir(self): return self.SVG("ui", "agrandir")
    def quitter(self): return self.SVG("ui", "quitter")
    def resize(self): return self.SVG("ui", "resize")
    def copier(self): return self.SVG("ui", "copier")
    def check(self): return self.SVG("ui", "check")
    def valider(self): return self.SVG("ui", "valider")
    def lock(self): return self.SVG("ui", "lock")
    def unlock(self): return self.SVG("ui", "unlock")
    def alerte(self): return self.SVG("ui", "alerte")
    def info(self): return self.SVG("ui", "info")
    def fleche_bottom(self): return self.SVG("ui", "fleche_bottom")
    def fleche_droite(self): return self.SVG("ui", "fleche_droite")
    def fleche_gauche(self): return self.SVG("ui", "fleche_gauche")
    def fleche_top(self): return self.SVG("ui", "fleche_top")
    def plus(self): return self.SVG("ui", "plus")
    def moins(self): return self.SVG("ui", "moins")