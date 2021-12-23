import configparser
import glob
import json
import os
import pathlib
import shutil

from PySide6 import QtCore, QtGui

from .. import classe_wg
from ..dct_gen import dct_img, lien_svg
from ..config import colors


### Dialog box
class DLG:
    def __init__(self, msg):

        self.msg = msg

    def VERIF_CHOIX(self, titre, msg_verif, ico=None):
        dlg = classe_wg.MB_REPONSE(titre=titre, msg=self.msg, ico=ico, msg_verif=msg_verif)
        return dlg.exec()
    def INFO(self):
        dlg = classe_wg.MB_INFO(titre="Erreur", msg=self.msg, ico=dct_img.get("info") + "th4")
        dlg.exec()
    def MSG_ERREUR(self):
        dlg = classe_wg.MB_ALERTE(titre="Erreur", msg=self.msg, ico=dct_img.get("alerte") + "th4")
        dlg.exec()


### FICHIERS
class JSON:
    def __init__(self, lien_json):

        self.lien_json = lien_json

    def OPEN(self):
        with open(os.path.abspath(self.lien_json), "r") as fichier:
            return json.load(fichier)
    def WRITE(self, data):
        with open(self.lien_json, 'w') as fichier:
            json.dump(data, fichier)
    def UPDATE(self, dct):
        with open(self.lien_json, "r+") as fichier:
            data = json.load(fichier)
            data.update(dct)
            fichier.seek(0)
            json.dump(data, fichier)
    def REMOVE(self, key):
        with open(self.lien_json, "r+") as fichier:
            data = json.load(fichier)
            data.pop(key)
            fichier.seek(0)
            json.dump(data, fichier)
class INI:
    def __init__(self, lien_ini):

        self.lien_ini = lien_ini

    def OPEN_INI(self):
        conf = configparser.ConfigParser()
        conf.read(self.lien_ini)
        return conf
    def WRITE_INI(self, ini):
        with open(self.lien_ini, "w") as configfile:
            ini.write(configfile)


### IMAGES
def GEN_SVG():
    hx1, hx2, hx3, hx4, hxbn1, hxbn2 = colors.hx_th1, colors.hx_th2, colors.hx_th3, colors.hx_th4, colors.hx_bn1, colors.hx_bn2
    ls_couleurs = [
        {"rgb_base": "#1D1D1B", "rgb_rep_th1": hx1, "rgb_rep_th2": hx2, "rgb_rep_th3": hx3, "rgb_rep_th4": hx4, "rgb_rep_bn1": hxbn1, "rgb_rep_bn2": hxbn2},
        {"rgb_base": "#3C3C3B", "rgb_rep_th1": hx2, "rgb_rep_th2": hx1, "rgb_rep_th3": hx1, "rgb_rep_th4": hx2, "rgb_rep_bn1": hx2, "rgb_rep_bn2": hx2},
        {"rgb_base": "#575756", "rgb_rep_th1": hx3, "rgb_rep_th2": hx3, "rgb_rep_th3": hx2, "rgb_rep_th4": hx3, "rgb_rep_bn1": hx3, "rgb_rep_bn2": hx3},
        {"rgb_base": "#F6F6F6", "rgb_rep_th1": hx4, "rgb_rep_th2": hx4, "rgb_rep_th3": hx4, "rgb_rep_th4": hx1, "rgb_rep_bn1": hx4, "rgb_rep_bn2": hx4},
        {"rgb_base": "#E30613", "rgb_rep_th1": hxbn1, "rgb_rep_th2": hxbn1, "rgb_rep_th3": hxbn1, "rgb_rep_th4": hxbn1, "rgb_rep_bn1": hx1, "rgb_rep_bn2": hxbn1},
        {"rgb_base": "#00983A", "rgb_rep_th1": hxbn2, "rgb_rep_th2": hxbn2, "rgb_rep_th3": hxbn2, "rgb_rep_th4": hxbn2, "rgb_rep_bn1": hxbn2, "rgb_rep_bn2": hx1}
    ]
    dct_rep_th = {
        "th1": "rgb_rep_th1",
        "th2": "rgb_rep_th2",
        "th3": "rgb_rep_th3",
        "th4": "rgb_rep_th4",
        "bn1": "rgb_rep_bn1",
        "bn2": "rgb_rep_bn2"
    }
    for lien in lien_svg:
        os.makedirs(lien_svg[lien] + "tm") if not os.path.exists(lien_svg[lien] + "tm") else False

        for svg in glob.glob(lien_svg[lien] + "*.svg"):
            if not "_thc" in svg:
                for rep in dct_rep_th.keys():
                    img_tm_svg = pathlib.Path(svg).stem + "_" + rep + ".svg"
                    shutil.copyfile(svg, lien_svg[lien] + "tm/" + img_tm_svg)

                    for couleur in ls_couleurs:
                        svgMod = open(lien_svg[lien] + "tm/" + img_tm_svg, "r+")
                        data = svgMod.read()

                        data = data.replace(couleur["rgb_base"], couleur[dct_rep_th[rep]])
                        svgMod.seek(0)
                        svgMod.write(data)
                        svgMod.close()
            elif "_thc" in svg:
                shutil.copyfile(svg, lien_svg[lien] + "tm/" + pathlib.Path(svg).stem[:-4] + ".svg")


### POLICE ________
def FONT(fontSize):
    ft = QtGui.QFont()
    ft.setFamily("Berlin Sans FB Demi")
    ft.setPointSize(fontSize)
    return ft


### WIDGETS ______
def DIM(wg, w, h):
    wg.setFixedWidth(w) if w is not None else False
    wg.setFixedHeight(h) if h is not None else False
def ICON(wg, img, dim):
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(img + ".svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
    wg.setIcon(icon) if dim is not None else False
    wg.setIconSize(QtCore.QSize(dim, dim)) if dim is not None else False
