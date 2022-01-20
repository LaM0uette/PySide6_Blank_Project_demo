from .wg import wg
from .. import p_base
from ....build import *


class rtn:
    def __init__(self,
                 *wgs,
                 pb_type=p_base.PB_TYPE,
                 colors_type=p_base.COLORS_TYPE,
                 colors=p_base.COLORS,
                 x_ico=P_style().x_ico(),
                 X_ICO=P_style().X_ICO(),
                 dim=p_base.DIM,
                 img=None,
                 img_check=None,
                 tm=p_base.TM,
                 tm_hover=p_base.TM_HOVER,
                 tm_check=p_base.TM_CHECK,
                 font=p_base.FONT,
                 bd=p_base.BD,
                 rd=p_base.RD,
                 cur=p_base.CUR
                 ):
        self.wgs = wgs

        self.pb_type = pb_type
        self.colors_type = colors_type
        self.colors = colors
        self.x_ico = x_ico
        self.X_ICO = X_ICO
        self.dim = dim
        self.img = img
        self.img_check = img_check
        self.tm = tm
        self.tm_hover = tm_hover
        self.tm_check = tm_check
        self.font = font
        self.bd = bd
        self.rd = rd
        self.cur = cur

    def rtn(self):
        wg(
            *self.wgs,
            pb_type=self.pb_type,
            colors_type=self.colors_type,
            colors=self.colors,
            x_ico=self.x_ico,
            X_ICO=self.X_ICO,
            dim=self.dim,
            img=self.img,
            img_check=self.img_check,
            tm=self.tm,
            tm_hover=self.tm_hover,
            tm_check=self.tm_check,
            font=self.font,
            bd=self.bd,
            rd=self.rd,
            cur=self.cur,
        )

    def txt(self):
        self.colors_type = "txt"
        self.rtn()
    def txt_inv(self):
        self.colors_type = "txt_inv"
        self.rtn()
    def th(self):
        self.colors_type = "th"
        self.rtn()
    def tr(self):
        self.colors_type = "tr"
        self.rtn()
    def zoom(self):
        self.colors_type = "zoom"
        self.rtn()
    def uni(self):
        self.colors_type = "uni"
        self.rtn()

    def option(self):
        self.img = P_img().option()
        self.tm = "th2"
        self.tr()
    def reduire(self):
        self.img = P_img().reduire()
        self.tm = "bn1"
        self.tr()
    def agrandir(self):
        self.img = P_img().agrandir()
        self.tm = "th3"
        self.tr()
    def quitter(self):
        self.img = P_img().quitter()
        self.tm = "bn2"
        self.tr()

    def copier(self, tm="bn1"):
        self.pb_type="zoom"
        self.img = P_img().copier()
        self.tm = tm
        self.zoom()
    def lock(self):
        self.img = P_img().lock()
        self.tm = "bn1"
        self.tr()

    def zoom_calendrier(self):
        self.img = P_img().calendrier()
        self.zoom()

    def plein(self):
        self.dim = P_dim().aw().h5()
        self.th()
    def plein_th1(self):
        self.colors=P_rgb().p_th1()
        self.bd = P_bd().all().th2()
        self.plein()
    def plein_th2(self):
        self.colors=P_rgb().p_th2()
        self.plein()
    def plein_th3(self):
        self.colors=P_rgb().p_th3()
        self.plein()
    def plein_bn1(self):
        self.colors=P_rgb().p_bn1()
        self.plein()
    def plein_bn2(self):
        self.colors=P_rgb().p_bn2()
        self.plein()

    def demo_rd(self):
        self.rd = P_rd().all().px_5()
        self.th()
    def demo_bd(self):
        self.bd = P_bd().all().bn1()
        self.th()


class base_txt(rtn):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                         colors=P_rgb().p_th1(),
                         dim=P_dim().aw().h9(),
                         font=P_font().h4(),
                         cur=P_cur().main(),
        )
class base(rtn):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                         colors=P_rgb().p_th3(),
                         dim=P_dim().aw().h9(),
                         font=P_font().h4(),
                         cur=P_cur().main(),
        )
class menu_top(rtn):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                         pb_type="zoom",
                         colors=P_rgb().p_th3(),
                         dim=P_dim().w_rect_1_4().h9(),
                         font=P_font().h4(),
                         cur=P_cur().souris_main(),
        )
class ck_ico(rtn):
    def __init__(self, *wgs,
                 img=P_img().check(),
                 img_check=P_img().valider(),
                 tm="th2",
                 tm_check="th3",
                 ):
        super().__init__(*wgs,
                         pb_type="check",
                         colors=P_rgb().p_th3(),
                         dim=P_dim().aw().h9(),
                         img=img,
                         img_check=img_check,
                         tm=tm,
                         tm_check=tm_check,
                         font=P_font().h4(),
                         cur=P_cur().main(),
        )
class zoom(rtn):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                         pb_type="zoom",
                         colors=P_rgb().p_th3(),
                         dim=P_dim().aw().h9(),
                         img=P_img().main(),
                         font=P_font().h4(),
                         cur=P_cur().main(),
        )

class dlg_ok(rtn):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                         colors=P_rgb().p_vert_th2(),
                         dim=P_dim().ah().h6(),
                         font=P_font().h4(),
                         cur=P_cur().souris_main(),
        )
class dlg_nok(rtn):
    def __init__(self, *wgs):
        super().__init__(*wgs,
                         colors=P_rgb().p_rouge_th2(),
                         dim=P_dim().ah().h6(),
                         font=P_font().h4(),
                         cur=P_cur().souris_main(),
        )

class rgb(rtn):
    def __init__(self, *wgs,
                 colors=P_rgb().p_th3(),
                 dim=P_dim().aw().h9()):
        super().__init__(*wgs,
                         colors=colors,
                         dim=dim,
                         font=P_font().h4(),
                         cur=P_cur().main(),
        )
