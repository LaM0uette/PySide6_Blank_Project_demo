from src.config import config


class Cur:

    def CUR(self, img): return f"src/assets/cursor/{config.cur}/{img}.cur"
    def ANI(self, img): return f"src/assets/cursor/{config.cur}/{img}.ani"


    def agrandir(self): return [self.CUR("agrandir"), 9, 1]
    def copier(self): return [self.CUR("copier"), 9, 1]
    def crayon(self): return [self.CUR("crayon"), 1, 32]
    def croix(self): return [self.CUR("croix"), 16, 16]
    def fleche_nesw(self): return [self.CUR("fleche_nesw"), 16, 16]
    def fleche_ns(self): return [self.CUR("fleche_ns"), 16, 16]
    def fleche_nwse(self): return [self.CUR("fleche_nwse"), 16, 16]
    def fleche_top(self): return [self.CUR("fleche_top"), 16, 1]
    def fleche_tout(self): return [self.CUR("fleche_tout"), 16, 16]
    def fleche_we(self): return [self.CUR("fleche_we"), 16, 16]
    def IBeam(self): return [self.CUR("IBeam"), 16, 16]
    def infos(self): return [self.CUR("infos"), 9, 1]
    def main(self): return [self.CUR("main"), 9, 1]
    def non(self): return [self.CUR("non"), 16, 16]
    def retour(self): return [self.CUR("retour"), 9, 1]
    def souris(self): return [self.CUR("souris"), 9, 1]
    def souris_main(self): return [self.CUR("souris_main"), 9, 1]
    def souris_non(self): return [self.CUR("souris_non"), 9, 1]
    def wait(self): return [self.ANI("wait"), 16, 16]
