import json
import os

from src.config import vrb
from src.config import config

class Data:
    def __init__(self, grp=""):
        self.grp = grp

    def OPEN_JSON(self, fichier_json):
        with open(f"F:/Creative Cloud Files/01_PROJETS/01_PROG/01_PYTHON/PySide6_Blank_Project_demo/{fichier_json}.json", "r") as fichier:
            return json.load(fichier)
    def GET_VAL(self, val):
        js = self.OPEN_JSON(fichier_json=f"{vrb.DO_DATA}{self.grp}")
        return js.get(val)
    def TH(self, val):
        dt = self.OPEN_JSON(fichier_json=fr"{vrb.DO_THEME}{config.theme}")
        return tuple(dt[val])
    def TH_HEX(self, rgb):
        return "#" + "%02x%02x%02x" % rgb
