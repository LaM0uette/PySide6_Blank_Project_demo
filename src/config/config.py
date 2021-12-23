import configparser

from . import vrb


### FICHIER CONFIG ______________
cfg = configparser.ConfigParser()
cfg.read(vrb.INI_CONFIG)

### infos _______________
nom = cfg["infos"]["nom"]
description = cfg["infos"]["description"]
version = float(cfg["infos"]["version"])
auteur = cfg["infos"]["auteur"]

### config ________________________
theme = cfg["config"]["theme"]
widht = int(cfg["config"]["widht"])
height = int(cfg["config"]["height"])
opacity = float(cfg["config"]["opacity"])
cur = cfg["config"]["cur"]

### var _____________________
auto_reload = True if cfg["var"]["autoreload"].lower() == "true" else False
auto_close = True if cfg["var"]["autoClose"].lower() == "true" else False
