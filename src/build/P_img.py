from ..config import vrb

class P_img:

    def SVG(self, val, img): return f"{vrb.DO_IMG}{val}/tm/{img}"

    def calendrier(self): return self.SVG("divers", "calendrier")
