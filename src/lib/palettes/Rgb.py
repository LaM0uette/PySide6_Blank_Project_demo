import json

from src.config import config


class Rgb:

    @staticmethod
    def _get_rgb(val):
        with open(fr"src/theme/{config.theme}.json", "r") as fichier:
            js = json.load(fichier)
            return tuple(js[val])

    @staticmethod
    def _rgb_to_hex(rgb):
        return "#" + "%02x%02x%02x" % rgb

    TH1 = _get_rgb(val="th1") + (255, )
    TH2 = _get_rgb(val="th2") + (255, )
    TH3 = _get_rgb(val="th3") + (255, )
    BN1 = _get_rgb(val="bn1") + (255, )
    BN2 = _get_rgb(val="bn2") + (255, )
    TR = 0, 0, 0, 0

    HX_TH1 = _rgb_to_hex(_get_rgb(val="th1"))
    HX_TH2 = _rgb_to_hex(_get_rgb(val="th2"))
    HX_TH3 = _rgb_to_hex(_get_rgb(val="th3"))
    HX_BN1 = _rgb_to_hex(_get_rgb(val="bn1"))
    HX_BN2 = _rgb_to_hex(_get_rgb(val="bn2"))
