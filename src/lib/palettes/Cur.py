import json
import os

from src.config import config


class Cur:

    @staticmethod
    def _cursor(img, xy):
        return [f"src/assets/cursor/{config.cur}/{img}.cur", xy[0], xy[1]]

    with open(f"{os.path.dirname(f'src/assets/cursor/{config.cur}/_data.json')}/_data.json", "r", encoding="utf-8") as fichier:
        cur = json.load(fichier)

    _souris = cur["_souris"]
    _centre = cur["_centre"]
    _crayon = cur["_crayon"]
    _fleche_top = cur["_fleche_top"]

    AGRANDIR = _cursor("agrandir", _souris)
    COPIER = _cursor("copier", _souris)
    CRAYON = _cursor("crayon", _crayon)
    CROIX = _cursor("croix", _centre)
    FLECHE_NESW = _cursor("fleche_nesw", _centre)
    FLECHE_NS = _cursor("fleche_ns", _centre)
    FLECHE_NWSE = _cursor("fleche_nwse", _centre)
    FLECHE_TOP = _cursor("fleche_top", _fleche_top)
    FLECHE_MOVE = _cursor("fleche_move", _centre)
    FLECHE_WE = _cursor("fleche_we", _centre)
    IBEAM = _cursor("ibeam", _centre)
    INFOS = _cursor("infos", _souris)
    MAIN = _cursor("main", _souris)
    NON = _cursor("non", _centre)
    RETOUR = _cursor("retour", _souris)
    SOURIS = _cursor("souris", _souris)
    SOURIS_MAIN = _cursor("souris_main", _souris)
    SOURIS_NON = _cursor("souris_non", _souris)
