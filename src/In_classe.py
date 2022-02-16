from .build import *


class In_classe:
    def __init__(self, ui):
        ### QFrame ###
        Frame.Menu_top(ui.fr_menu_top)
        Frame.Cadre(ui.fr_main).th2()
        ### /QFrame ###


        ### QLabel ###
        Label.H3(ui.lb_mt_nom)
        ### /QLabel ###


        ### QPushButton ###
        Push_button.menu_top(ui.pb_mt_quitter).quitter()
        ### /QPushButton ###
