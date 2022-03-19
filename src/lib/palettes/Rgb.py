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




    def get_rgb(self, val):
        with open(fr"src/theme/{config.theme}.json", "r") as fichier:
            js = json.load(fichier)
            return tuple(js[val])
    def get_rgba(self, val):
        return self.get_rgb(val=val) + (255,)
    def rgb_to_hex(self, rgb):
        return "#" + "%02x%02x%02x" % rgb

    def th1(self): return self.get_rgba("th1")
    def th2(self): return self.get_rgba("th2")
    def th3(self): return self.get_rgba("th3")
    def bn1(self): return self.get_rgba("bn1")
    def bn2(self): return self.get_rgba("bn2")
    def tr(self): return 0, 0, 0, 0

    def hx_th1(self): return self.rgb_to_hex(self.get_rgb("th1"))
    def hx_th2(self): return self.rgb_to_hex(self.get_rgb("th2"))
    def hx_th3(self): return self.rgb_to_hex(self.get_rgb("th3"))
    def hx_bn1(self): return self.rgb_to_hex(self.get_rgb("bn1"))
    def hx_bn2(self): return self.rgb_to_hex(self.get_rgb("bn2"))
