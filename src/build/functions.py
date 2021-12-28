import glob
import os
import pathlib
import shutil

from PySide6 import QtGui

from . import *
from ..config import *


class Fct:
    def __init__(self, **kwargs):

        self.kwargs = kwargs

    def CUR(self):
        cur = self.kwargs.get("cur")
        if cur is None: cur = "souris"

        cursor = P_cur().RTN_CUR(cur)
        return QtGui.QCursor(QtGui.QPixmap(cursor[0]), cursor[1], cursor[2])
    def DIM(self):
        wg = self.kwargs.get("wg")
        if wg is None: return

        w, h = self.kwargs.get("w"), self.kwargs.get("h")

        wg.setFixedWidth(w) if w is not None else False
        wg.setFixedHeight(h) if h is not None else False
    def GEN_SVG(self):
        hx1, hx2, hx3, hx4, hxbn1, hxbn2 = P_rgb().hx_th1(), P_rgb().hx_th2(), P_rgb().hx_th3(), P_rgb().hx_th4(), P_rgb().hx_bn1(), P_rgb().hx_bn2()
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

        liens_img = os.listdir(vrb.DO_IMG)
        for lien_img in liens_img:
            lien = f"{vrb.DO_IMG}{lien_img}/"
            lien_tm = f"{lien}tm"

            os.makedirs(lien_tm) if not os.path.exists(lien_tm) else False

            for svg in glob.glob(f"{lien}*.svg"):
                if not "thc" in svg:
                    for rep in dct_rep_th.keys():
                        img_tm_svg = f"{pathlib.Path(svg).stem}{rep}.svg"
                        shutil.copyfile(svg, f"{lien_tm}/{img_tm_svg}")

                        for couleur in ls_couleurs:
                            svgMod = open(f"{lien_tm}/{img_tm_svg}", "r+")
                            data = svgMod.read()

                            data = data.replace(couleur["rgb_base"], couleur[dct_rep_th[rep]])
                            svgMod.seek(0)
                            svgMod.write(data)
                            svgMod.close()
                elif "thc" in svg:
                    shutil.copyfile(svg, f"{lien_tm}/{pathlib.Path(svg).stem[:-4]}.svg")
