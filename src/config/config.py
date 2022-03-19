import json
import os


class Config:
    def __init__(self):

        ### FICHIER CONFIG ###
        with open(f"{os.path.dirname(__file__)}\config.json", "r", encoding="utf-8") as fichier:
            cfg = json.load(fichier)

        ### infos ###
        self.nom = cfg["nom"]
        self.description = cfg["description"]
        self.version = cfg["version"]
        self.auteur = cfg["auteur"]

        ### config ###
        self.theme = cfg["config"]["theme"]
        self.font = cfg["config"]["font"]
        self.widht = cfg["config"]["widht"]
        self.height = cfg["config"]["height"]
        self.opacity = cfg["config"]["opacity"]
        self.cur = cfg["config"]["cur"]

        ### var ###
        self.debug = cfg["var"]["debug"]
        self.resize = cfg["var"]["resize"]
        self.auto_close = cfg["var"]["auto_close"]
        self.toolbox_pin = cfg["var"]["toolbox_pin"]
