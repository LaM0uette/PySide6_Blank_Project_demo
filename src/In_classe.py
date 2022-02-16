from .build import *


class In_classe:
    def __init__(self, ui):
        ### QFrame ###
        Frame.Menu_top(ui.fr_menu_top)
        Frame.Cadre(ui.fr_main).th2()
        ### /QFrame ###


        ### QLabel ###
        Label.Base_tr(ui.lb_mt_nom, font_size=P_font().h3())
        ### /QLabel ###


        ### QPushButton ###
        Push_button.menu_top(ui.pb_mt_quitter).quitter()
        ### /QPushButton ###
