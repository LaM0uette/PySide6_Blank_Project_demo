from .build import *


class In_classe:
    def __init__(self, ui):
        ### QFrame ###
        Frame.Menu_top(ui.fr_menu_top)
        Frame.Cadre_th2(ui.fr_main)
        ### /QFrame ###


        ### QLabel ###
        Label.H3(ui.lb_mt_nom)
        ### /QLabel ###

        Push_button.menu_top(ui.pb_mt_quitter).quitter()

