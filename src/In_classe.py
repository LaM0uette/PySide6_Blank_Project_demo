from .build import *


class In_classe:
    def __init__(self, ui):
        ### QFrame ###
        Frame.Menu_top(ui.fr_menu_top)
        # Frame.Cadre_th2(ui.fr_main)
        ### /QFrame ###

        def LABEL():
            Label.h3(ui.lb_mt_nom).tr()
        def PUSH_BUTTON():
            Push_button.menu_top(ui.pb_mt_quitter).quitter()


        def _func_try():
            err = "[ In_classe ] ne fonctionne pas !"

            try: LABEL()
            except: print(f"LABEL{err}")

            try: PUSH_BUTTON()
            except: print(f"PUSH_BUTTON{err}")

        _func_try()
