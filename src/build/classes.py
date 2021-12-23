import json

from ..config import vrb


class Data:
    def __init__(self, grp):
        self.grp = grp

    def OPEN_JSON(self, fichier_json):
        with open(f"{fichier_json}.json", "r") as fichier:
            return json.load(fichier)
    def GET(self, val):
        js = self.OPEN_JSON(fichier_json=f"{vrb.DO_JS_DATA}{self.grp}")
        return js.get(val)


    def GET_CLS(self, val):
        return {
            "h_menu_top": self.GET("h9"),
        }.get(val)
