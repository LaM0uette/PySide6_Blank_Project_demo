from .build import *


class In_classe:
    def __init__(self, ui):
        def FRAME():
            Frame.base(ui.fr_main).cadre_th2()
            Frame.menu_top(ui.fr_menu_top).th()
        def LABEL():
            Label.h3(ui.lb_mt_nom).tr()
        def PUSH_BUTTON():
            Push_button.menu_top(ui.pb_mt_quitter).quitter()


        def _func_try():
            err = "[ In_classe ] ne fonctionne pas !"

            try: FRAME()
            except: print(f"FRAME{err}")

            try: LABEL()
            except: print(f"LABEL{err}")

            try: PUSH_BUTTON()
            except: print(f"PUSH_BUTTON{err}")

        _func_try()
