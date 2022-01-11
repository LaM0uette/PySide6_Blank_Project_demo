from .build import *


class In_classe:
    def __init__(self, ui):
        def FRAME():
            Frame.base(ui.fr_main).cadre_th2()
            Frame.menu_top(ui.fr_menu_top).th()


        def _func_try():
            err = "[ In_classe ] ne fonctionne pas !"

            try: FRAME()
            except: print(f"FRAME{err}")

        _func_try()


        # QLabel
        with C_lb() as C_:
            C_.h3(ui.lb_mt_nom)


        with C_pb() as C_:
            C_.quitter(ui.pb_mt_quitter)

