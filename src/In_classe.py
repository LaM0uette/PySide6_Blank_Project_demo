from .build import *


class In_classe:
    def __init__(self, ui):
        # QLineEdit | QTextEdit | QPlainTextEdit
        with C_le() as C_: pass

        # QComboBox
        with C_cb() as C_: pass

        # QDateEdit
        with C_de() as C_: pass

        # QFrame
        with C_fr() as C_:
            C_.main(ui.fr_main)
            C_.menu_top(ui.fr_menu_top)
            C_.body(ui.fr_body)
            C_.menu_bottom(ui.fr_menu_bottom)

        # QLabel
        with C_lb() as C_:
            C_.h3(ui.lb_mt_nom)

        # QListWidget
        with C_lw() as C_: pass

        # QPushButton
        with C_pb() as C_:
            C_.quitter(ui.pb_mt_quitter)

        # QCheckBox
        with C_cb() as C_: pass

        # QRadioButton
        with C_rb() as C_: pass

        # QProgressBar
        with C_pg() as C_: pass

        # QScrollBoxArea
        with C_sca() as C_: pass

        # QSpinBox | QDoubleSpinBox
        with C_sb() as C_: pass

        # QTableWidget
        with C_tw() as C_: pass

        # QToolBox
        with C_tb() as C_: pass
