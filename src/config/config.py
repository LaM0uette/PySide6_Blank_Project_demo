import configparser


### FICHIER CONFIG ______________
cfg = configparser.ConfigParser()
cfg.read(filenames="cfg.ini", encoding="utf-8")

### infos _______________
nom = cfg["infos"]["nom"]
description = cfg["infos"]["description"]
version = float(cfg["infos"]["version"])
auteur = cfg["infos"]["auteur"]

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
