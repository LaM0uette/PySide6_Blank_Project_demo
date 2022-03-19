class Img:

    @staticmethod
    def _svg(val, img):
        return f"src/assets/img/{val}/rgb/{img}"

    CALENDRIER = _svg("divers", "calendrier")
    MAIN = _svg("main", "main")
    OPTION = _svg("ui", "option")
    REDUIRE = _svg("ui", "reduire")
    AGRANDIR = _svg("ui", "agrandir")
    QUITTER = _svg("ui", "quitter")
    RESIZE = _svg("ui", "resize")
    COPIER = _svg("ui", "copier")
    CHECK0 = _svg("ui", "check0")
    CHECK1 = _svg("ui", "check1")
    CHECK2 = _svg("ui", "check2")
    CHECK0_ROND = _svg("ui", "check0_rond")
    CHECK1_ROND = _svg("ui", "check1_rond")
    CHECK2_ROND = _svg("ui", "check2_rond")
    LOCK = _svg("ui", "lock")
    UNLOCK = _svg("ui", "unlock")
    ALERTE = _svg("ui", "alerte")
    INFO = _svg("ui", "info")
    FLECHE_TOP = _svg("ui", "fleche_top")
    FLECHE_BOTTOM = _svg("ui", "fleche_bottom")
    FLECHE_RIGHT = _svg("ui", "fleche_droite")
    FLECHE_LEFT = _svg("ui", "fleche_gauche")
    PLUS = _svg("ui", "plus")
    MOINS = _svg("ui", "moins")
