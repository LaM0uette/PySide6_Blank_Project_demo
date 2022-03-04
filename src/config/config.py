import json
import os


### FICHIER CONFIG ______________
with open(f"{os.path.dirname(__file__)}\config.json", "r", encoding="utf-8") as fichier:
    cfg = json.load(fichier)

### infos _______________
nom = cfg["nom"]
description = cfg["description"]
version = cfg["version"]
auteur = cfg["auteur"]

### config ________________________
theme = cfg["config"]["theme"]
font = cfg["config"]["font"]
widht = cfg["config"]["widht"]
height = cfg["config"]["height"]
opacity = cfg["config"]["opacity"]
cur = cfg["config"]["cur"]

### var _____________________
debug = cfg["var"]["debug"]
resize = cfg["var"]["resize"]
auto_close = cfg["var"]["auto_close"]
toolbox_pin = cfg["var"]["toolbox_pin"]
