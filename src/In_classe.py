from .build import *


class In_classe:
    def __init__(self, ui):

        self.CB(ui=ui)
        self.DE(ui=ui)
        self.FR(ui=ui)
        self.LB(ui=ui)
        self.LW(ui=ui)
        self.PB(ui=ui)
        self.SCA(ui=ui)

    def CB(self, ui):
        # Demo
        C_cb().demo_th(ui.cb_demo_th)
        C_cb().demo_tr(ui.cb_demo_tr)
    def DE(self, ui):
        # Demo
        C_de().demo_th(ui.de_demo_th)
        C_de().demo_tr(ui.de_demo_tr)
    def FR(self, ui):
        # Menu_top
        C_fr().menu_top(ui.fr_menu_top)

        # Demo
        C_fr().demo(ui.fr_cb, ui.fr_de, ui.fr_lw, ui.fr_pb, ui.fr_ck,
                    ui.fr_rb, ui.fr_pg, ui.fr_sb, ui.fr_tw, ui.fr_le,
                    ui.fr_te, ui.fr_pte)
    def LB(self, ui):
        # Titre app
        C_lb().h3_titre(ui.lb_mt_nom)

        # Demo
        C_lb().demo(ui.lb_cb_demo, ui.lb_de_demo, ui.lb_lw_demo, ui.lb_pb_demo, ui.lb_ck_demo,
                    ui.lb_rb_demo, ui.lb_pg_demo, ui.lb_sb_demo, ui.lb_tw_demo, ui.lb_le_demo,
                    ui.lb_te_demo, ui.lb_pte_demo)
    def LW(self, ui):
        # Demo
        C_lw().demo(ui.lw_demo)
    def PB(self, ui):
        # Menu_top
        C_pb().option(ui.pb_mt_option)
        C_pb().reduire(ui.pb_mt_reduire)
        C_pb().agrandir(ui.pb_mt_agrandir)
        C_pb().quitter(ui.pb_mt_quitter)

        # Demo
        C_pb().demo_txt(ui.pb_demo_txt)
        C_pb().demo_txt_inv(ui.pb_demo_txt_inv)
        C_pb().demo_th(ui.pb_demo_th)
        C_pb().demo_tr(ui.pb_demo_tr)
        C_pb().demo_ck(ui.pb_demo_ck)
        C_pb().demo_ck_ico(ui.pb_demo_ck_ico, ui.pb_demo_ico_ck)
        C_pb().demo_zoom(ui.pb_demo_zoom)
        C_pb().demo_rd(ui.pb_demo_rd)
        C_pb().demo_bd(ui.pb_demo_bd)
    def SCA(self, ui):
        # Demo
        C_sca().demo(ui.sca_main)
