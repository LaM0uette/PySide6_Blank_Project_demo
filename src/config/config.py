import json
import os


### FICHIER CONFIG ______________
with open(os.path.relpath("src/config/config.json"), "r", encoding="utf-8") as fichier:
    cfg = json.load(fichier)

### infos _______________
nom = cfg["nom"]
description = cfg["description"]
version = float(cfg["version"])
auteur = cfg["auteur"]

### config ________________________
theme = cfg["config"]["theme"]
font = cfg["config"]["font"]
widht = int(cfg["config"]["widht"])
height = int(cfg["config"]["height"])
opacity = float(cfg["config"]["opacity"])
cur = cfg["config"]["cur"]

### var _____________________
debug = cfg["var"]["debug"].lower() == "true"
resize = cfg["var"]["resize"].lower() == "true"
autoClose = cfg["var"]["autoClose"].lower() == "true"
toolBoxPin = cfg["var"]["toolBoxPin"].lower() == "true"
