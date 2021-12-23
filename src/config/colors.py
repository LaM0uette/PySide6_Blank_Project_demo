import json
import os

from ..config import config
from .. import vrb


### COULEURS ______________________________________________________________________
def RGB_TO_HEX(rgb):
    return "#" + "%02x%02x%02x" % rgb

# Themes
with open(os.path.abspath(vrb.lien_json + f"{config.theme}.json"), "r") as fichier:
    data = json.load(fichier)

    th1 = tuple(data["th1"])
    th2 = tuple(data["th2"])
    th3 = tuple(data["th3"])
    th4 = tuple(data["th4"])
    bn1 = tuple(data["bn1"])
    bn2 = tuple(data["bn2"])

    hx_th1 = RGB_TO_HEX(th1)
    hx_th2 = RGB_TO_HEX(th2)
    hx_th3 = RGB_TO_HEX(th3)
    hx_th4 = RGB_TO_HEX(th4)
    hx_bn1 = RGB_TO_HEX(bn1)
    hx_bn2 = RGB_TO_HEX(bn2)

# Uniques
vert = (78, 194, 58)
rouge = (199, 60, 90)
