from .build import *


class In_classe:
    def __init__(self, ui):
        def FRAME():
            Frame.base(ui.fr_main).cadre()
            Frame.base(ui.fr_body).tr()
            Frame.base(ui.fr_menu_top).menu_top()
            Frame.base(ui.fr_menu_bottom).menu_bot()


        def _func_try():
            try: FRAME()
            except: print("FRAME ne fonctionne pas !")

        _func_try()


        # QLabel
        with C_lb() as C_:
            C_.h3(ui.lb_mt_nom)


        with C_pb() as C_:
            C_.quitter(ui.pb_mt_quitter)

