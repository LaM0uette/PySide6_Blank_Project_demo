from PySide6 import QtCore, QtWidgets, QtGui

from ... import rgb_ui
from .....build import *
from .....In_classe import In_classe


class Dlg_rgb(rgb_ui.Ui_Rgb, QtWidgets.QDialog):
    dragPos: QtCore.QPoint
    rep = False
    rgb = [0, 0, 0]

    def __init__(self,
                 titre,
                 rgb,
                 ico,
                 tm,
                 txt_pb_ok,
                 txt_pb_annuler,
                 width,
                 height,
                 opacity,
    ):
        super(Dlg_rgb, self).__init__()

        self.titre = titre
        self.rgb = rgb
        self.ico = ico
        self.tm = tm
        self.txt_pb_ok = txt_pb_ok
        self.txt_pb_annuler = txt_pb_annuler
        self.width = width
        self.height = height
        self.opacity = opacity

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setupUi(self)
        self.INIT()


    ### INITIALISATION
    def IN_BASE(self):
        ## Fenetre
        self.setWindowTitle(self.titre)
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)
        self.setWindowOpacity(self.opacity)
    def IN_CLASSE(self):
        def FRAME():
            Frame.base(self.fr_main).cadre_th3()
            Frame.menu_bottom_dlg(self.fr_rgb_bottom).th()
            Frame.base(self.fr_rgb_colors).radius()
        def LABEL():
            Label.h4(self.lb_rgb_red, self.lb_rgb_green, self.lb_rgb_blue).tr()
        def PUSH_BUTTON():
            Push_button.dlg_ok(self.pb_rgb_ok).txt()
            Push_button.dlg_nok(self.pb_rgb_annuler).txt_inv()
        def SLIDER():
            Slider.rgb(self.sd_rgb_red, self.sd_rgb_green, self.sd_rgb_blue).rond()
        def SPIN_BOX():
            Spin_box.rgb(self.sb_rgb_red, self.sb_rgb_green, self.sb_rgb_blue).bd_th3()


        def _func_try():
            err = f"[ {self.objectName()} ] ne fonctionne pas !"

            try: FRAME()
            except: print(f"FRAME{err}")

            try: LABEL()
            except: print(f"LABEL{err}")

            try: PUSH_BUTTON()
            except: print(f"PUSH_BUTTON{err}")

            try: SLIDER()
            except: print(f"SLIDER{err}")

            try: SPIN_BOX()
            except: print(f"SPIN_BOX{err}")
        _func_try()

        In_classe(ui=self)
    def IN_WG(self):
        # Base
        self.setCursor(Fct(cur=P_cur().souris()).CUR())
        self.setStyleSheet(f"background-color: rgb{P_rgb().th1()};")


        # Frame menu_top
        self.fr_menu_top.setFixedHeight(P_dim().h9())


        # Menu_top
        dim = P_dim().carr().h9()
        Fct(wg=self.lb_mt_ico, w=dim.get("w"), h=dim.get("h")).DIM()
        self.lb_mt_ico.setPixmap(QtGui.QPixmap(f"{self.ico}th3.svg"))
        self.lb_mt_ico.setScaledContents(True)
        self.lb_mt_nom.setText(self.titre)
        self.lb_mt_ico.setPixmap(QtGui.QPixmap(f"{self.ico}{self.tm}.svg"))
        self.lb_mt_ico.setScaledContents(True)


        # Message
        self.lb_rgb_red.setText("ROUGE")
        self.lb_rgb_green.setText("VERT")
        self.lb_rgb_blue.setText("BLEU")


        # pb ok
        self.pb_rgb_ok.setText(self.txt_pb_ok)
        self.pb_rgb_annuler.setText(self.txt_pb_annuler)
        self.pb_rgb_annuler.setDefault(True)
    def IN_CONNECTIONS(self):
        # Menu_top
        self.pb_mt_quitter.clicked.connect(lambda: self.close())

        # Slider
        self.sd_rgb_red.valueChanged.connect(lambda: self._set_sb_val())
        self.sd_rgb_green.valueChanged.connect(lambda: self._set_sb_val())
        self.sd_rgb_blue.valueChanged.connect(lambda: self._set_sb_val())
        # Spin box
        self.sb_rgb_red.valueChanged.connect(lambda: self._set_sd_val())
        self.sb_rgb_green.valueChanged.connect(lambda: self._set_sd_val())
        self.sb_rgb_blue.valueChanged.connect(lambda: self._set_sd_val())

        # pb ok
        self.pb_rgb_ok.clicked.connect(lambda: self.FCT_OK())
        self.pb_rgb_annuler.clicked.connect(lambda: self.close())
    def IN_WG_BASE(self):
        # Frame colors
        self.fr_rgb_colors.setFixedWidth(150)

        # slider / spin box
        self.sd_rgb_red.setValue(1)
        self.sd_rgb_red.setValue(0)

        self.sd_rgb_red.setValue(self.rgb[0])
        self.sd_rgb_green.setValue(self.rgb[1])
        self.sd_rgb_blue.setValue(self.rgb[2])
    def IN_ACT(self):
        pass
    def INIT(self):
        self.IN_BASE()
        self.IN_CLASSE()
        self.IN_WG()
        self.IN_CONNECTIONS()
        self.IN_WG_BASE()
        self.IN_ACT()


    ### ACTIONS
    def _set_sb_val(self):
        self.sb_rgb_red.setValue(self.sd_rgb_red.value())
        self.sb_rgb_green.setValue(self.sd_rgb_green.value())
        self.sb_rgb_blue.setValue(self.sd_rgb_blue.value())

        self._set_fr_color()
    def _set_sd_val(self):
        self.sd_rgb_red.setValue(self.sb_rgb_red.value())
        self.sd_rgb_green.setValue(self.sb_rgb_green.value())
        self.sd_rgb_blue.setValue(self.sb_rgb_blue.value())

        self._set_fr_color()
    def _set_fr_color(self):
        rgb = self.sd_rgb_red.value(), self.sd_rgb_green.value(), self.sd_rgb_blue.value()

        rgb_r = {"c1": (0, self.sd_rgb_green.value(), self.sd_rgb_blue.value()) + (255,),
                 "c2": (255, self.sd_rgb_green.value(), self.sd_rgb_blue.value()) + (255,)}

        rgb_g = {"c1": (self.sd_rgb_red.value(), 0, self.sd_rgb_blue.value()) + (255,),
                 "c2": (self.sd_rgb_red.value(), 255, self.sd_rgb_blue.value()) + (255,)}

        rgb_b = {"c1": (self.sd_rgb_red.value(), self.sd_rgb_green.value(), 0) + (255,),
                 "c2": (self.sd_rgb_red.value(), self.sd_rgb_green.value(), 255) + (255,)}

        Frame.base(self.fr_rgb_colors, colors={"c1": rgb}).radius()
        Slider.rgb(self.sd_rgb_red, gradient_colors=rgb_r).rgb()
        Slider.rgb(self.sd_rgb_green, gradient_colors=rgb_g).rgb()
        Slider.rgb(self.sd_rgb_blue, gradient_colors=rgb_b).rgb()


    ### FONCTIONS
    def FCT_OK(self):
        self.rep = True
        self.rgb = [self.sd_rgb_red.value(), self.sd_rgb_green.value(), self.sd_rgb_blue.value()]
        self.close()


    ### EVENT
    def mousePressEvent(self, event):
        cur = QtGui.QCursor()
        verifHeight = cur.pos().y() - self.pos().y()
        if event.buttons() == QtCore.Qt.LeftButton and verifHeight < P_dim().h9() and self.windowState() != QtCore.Qt.WindowMaximized:
            self.dragPos = event.globalPosition().toPoint()
            event.accept()
    def mouseMoveEvent(self, event):
        def act_move(event):
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
            self.dragPos = event.globalPosition().toPoint()
            event.accept()

        cur = QtGui.QCursor()
        height_verif = cur.pos().y() - self.pos().y()

        try:
            if event.buttons() == QtCore.Qt.LeftButton and height_verif < P_dim().h9() and self.windowState() != QtCore.Qt.WindowMaximized:
                act_move(event)
            if event.buttons() == QtCore.Qt.LeftButton and height_verif < P_dim().h9() and self.windowState() == QtCore.Qt.WindowMaximized:
                self.setWindowState(QtCore.Qt.WindowNoState)
                act_move(event)
        except AttributeError: pass
