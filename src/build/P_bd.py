from .P_style import P_style
from .P_rgb import P_rgb


class P_bd:
    # top - right - bottom - left
    def bd1_bd_th1(self): return {"mat": "1111", "px": P_style().bd(), "th": P_rgb().th1()}
    def bd1_bd_th2(self): return {"mat": "1111", "px": P_style().bd(), "th": P_rgb().th2()}
    def bd1_bd_th3(self): return {"mat": "1111", "px": P_style().bd(), "th": P_rgb().th3()}
    def bd1_bd_th4(self): return {"mat": "1111", "px": P_style().bd(), "th": P_rgb().th4()}
    def bd1_bd_bn1(self): return {"mat": "1111", "px": P_style().bd(), "th": P_rgb().bn1()}
    def bd1_bd_bn2(self): return {"mat": "1111", "px": P_style().bd(), "th": P_rgb().bn2()}

    def bd0010_bd_th1(self): return {"mat": "0010", "px": P_style().bd(), "th": P_rgb().th1()}
    def bd0010_bd_th2(self): return {"mat": "0010", "px": P_style().bd(), "th": P_rgb().th2()}
    def bd0010_bd_th3(self): return {"mat": "0010", "px": P_style().bd(), "th": P_rgb().th3()}
    def bd0010_bd_bn1(self): return {"mat": "0010", "px": P_style().bd(), "th": P_rgb().bn1()}
    def bd0010_bd_bn2(self): return {"mat": "0010", "px": P_style().bd(), "th": P_rgb().bn2()}

    def bd0101_bd_bn1(self): return {"mat": "0101", "px": P_style().bd(), "th": P_rgb().bn1()}

    def bd1101_bd_bn1(self): return {"mat": "1101", "px": P_style().bd(), "th": P_rgb().bn1()}
