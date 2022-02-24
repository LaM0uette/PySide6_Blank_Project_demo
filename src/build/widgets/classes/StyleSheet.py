from PySide6 import QtGui

from ....build import *
from ....build.widgets import p_base
from ....build.widgets.classes import Classe_pb


class StyleSheet:
    def __init__(
            self,

            # Couleurs BG
            bg_gen=None,
            bg=p_base.BG,
            bg_hover=p_base.BG_HOVER,
            bg_checked=p_base.BG_CHECKED,
            bg_checked_hover=p_base.BG_CHECKED_HOVER,
            bg_pressed=p_base.BG_PRESSED,
            bg_checked_pressed=p_base.BG_CHECKED_PRESSED,
            # Couleurs FG
            fg_gen=None,
            fg=p_base.FG,
            fg_hover=p_base.FG_HOVER,
            fg_checked=p_base.FG_CHECKED,
            fg_checked_hover=p_base.FG_CHECKED_HOVER,
            fg_pressed=p_base.FG_PRESSED,
            fg_checked_pressed=p_base.FG_CHECKED_PRESSED,

            # Images
            img_uncheck=p_base.IMG_UNCHECK,
            img_uncheck_hover=p_base.IMG_UNCHECK_HOVER,
            img_check=p_base.IMG_CHECK,
            img_check_hover=p_base.IMG_CHECK_HOVER,
            img=p_base.IMG_UNROLL,
            img_hover=p_base.IMG_UNROLL_HOVER,
            # Images RGB
            img_uncheck_rgb=p_base.IMG_UNCHECK_RGB,
            img_uncheck_hover_rgb=p_base.IMG_UNCHECK_HOVER_RGB,
            img_check_rgb=p_base.IMG_CHECK_RGB,
            img_check_hover_rgb=p_base.IMG_CHECK_HOVER_RGB,
            img_rgb=p_base.IMG_UNROLL_RGB,
            img_hover_rgb=p_base.IMG_UNROLL_HOVER_RGB,
            # Images DIM
            img_height=p_base.img_height,
            IMG_HEIGHT=p_base.IMG_HEIGHT,

            # Bordures
            border_all=None,
            border_style=p_base.WG_BORDER_STYLE,
            border_rgb=p_base.WG_BORDER_RGB,
            border_top=p_base.WG_BORDER_WIDTH, border_bottom=p_base.WG_BORDER_WIDTH, border_right=p_base.WG_BORDER_WIDTH, border_left=p_base.WG_BORDER_WIDTH,
            # Bordures hover
            border_all_hover=None,
            border_hover_style=p_base.WG_BORDER_STYLE,
            border_hover_rgb=p_base.WG_BORDER_RGB,
            border_hover_top=p_base.WG_BORDER_WIDTH, border_bottom_hover=p_base.WG_BORDER_WIDTH, border_right_hover=p_base.WG_BORDER_WIDTH, border_left_hover=p_base.WG_BORDER_WIDTH,
            # Bordures checked
            border_all_checked=None,
            border_checked_style=p_base.WG_BORDER_STYLE,
            border_checked_rgb=p_base.WG_BORDER_RGB,
            border_top_checked=p_base.WG_BORDER_WIDTH, border_bottom_checked=p_base.WG_BORDER_WIDTH, border_right_checked=p_base.WG_BORDER_WIDTH, border_left_checked=p_base.WG_BORDER_WIDTH,
            # Bordures checked hover
            border_all_checked_hover=None,
            border_checked_hover_style=p_base.WG_BORDER_STYLE,
            border_checked_hover_rgb=p_base.WG_BORDER_RGB,
            border_top_checked_hover=p_base.WG_BORDER_WIDTH, border_bottom_checked_hover=p_base.WG_BORDER_WIDTH, border_right_checked_hover=p_base.WG_BORDER_WIDTH, border_left_checked_hover=p_base.WG_BORDER_WIDTH,
    ):
        self.style = f"""
                QPushButton {{
                background-color: rgba{bg};
                color: rgba{fg};
                }}
        
                QPushButton:hover {{
                background-color: rgba{bg_hover};
                color: rgba{fg_hover};
                }}
        
                QPushButton:checked {{
                background-color: rgba{bg_checked};
                color: rgba{fg_checked};
                }}
        
                QPushButton:checked:hover {{
                background-color: rgba{bg_checked_hover};
                color: rgba{fg_checked_hover};
                }}
        
                QPushButton:pressed {{
                background-color: rgba{bg_pressed};
                color: rgba{fg_pressed};
                }}
        
                QPushButton:checked:pressed {{
                background-color: rgba{bg_checked_pressed};
                color: rgba{fg_checked_pressed};
                }}
        
                /* BORDURES */
                .QPushButton {{
                border-top: {border_top}px {border_style} rgba{border_rgb};
                border-bottom: {border_bottom}px {border_style} rgba{border_rgb};
                border-right: {border_right}px {border_style} rgba{border_rgb};
                border-left: {border_left}px {border_style} rgba{border_rgb};
                }}
                .QPushButton:hover {{
                border-top: {border_hover_top}px {border_hover_style} rgba{border_hover_rgb};
                border-bottom: {border_bottom_hover}px {border_hover_style} rgba{border_hover_rgb};
                border-right: {border_right_hover}px {border_hover_style} rgba{border_hover_rgb};
                border-left: {border_left_hover}px {border_hover_style} rgba{border_hover_rgb};
                }}
                .QPushButton:checked {{
                border-top: {border_top_checked}px {border_checked_style} rgba{border_checked_rgb};
                border-bottom: {border_bottom_checked}px {border_checked_style} rgba{border_checked_rgb};
                border-right: {border_right_checked}px {border_checked_style} rgba{border_checked_rgb};
                border-left: {border_left_checked}px {border_checked_style} rgba{border_checked_rgb};
                }}
                .QPushButton:checked:hover {{
                border-top: {border_top_checked_hover}px {border_checked_hover_style} rgba{border_checked_hover_rgb};
                border-bottom: {border_bottom_checked_hover}px {border_checked_hover_style} rgba{border_checked_hover_rgb};
                border-right: {border_right_checked_hover}px {border_checked_hover_style} rgba{border_checked_hover_rgb};
                border-left: {border_left_checked_hover}px {border_checked_hover_style} rgba{border_checked_hover_rgb};
                }}"""
        self.img_height = img_height
        self.IMG_HEIGHT = IMG_HEIGHT
        self.img = img
        self.img_hover = img_hover
        self.img_uncheck = img_uncheck
        self.img_uncheck_hover = img_uncheck_hover
        self.img_check = img_check
        self.img_check_hover = img_check_hover
        self.img_rgb = img_rgb
        self.img_hover_rgb = img_hover_rgb
        self.img_uncheck_rgb = img_uncheck_rgb
        self.img_uncheck_hover_rgb = img_uncheck_hover_rgb
        self.img_check_rgb = img_check_rgb
        self.img_check_hover_rgb = img_check_hover_rgb


    def get(self): return self.style
    def get_cls_pb(self, wg, wg_type):
        if wg_type is not None:
            if wg_type == "check":
                Fct(wg=wg, img=f"{self.img_uncheck}{self.img_uncheck_rgb}", dim=self.img_height).ICON()
            else:
                Fct(wg=wg, img=f"{self.img}{self.img_rgb}", dim=self.img_height).ICON()

            return Classe_pb.Classe_pb(
                wg=wg,
                dim_ico=self.img_height,
                DIM_ICO=self.IMG_HEIGHT,
                img=self.img,
                img_hover=self.img_hover,
                img_uncheck=self.img_uncheck,
                img_uncheck_hover=self.img_uncheck_hover,
                img_check=self.img_check,
                img_check_hover=self.img_check_hover,
                img_rgb=self.img_rgb,
                img_hover_rgb=self.img_hover_rgb,
                img_uncheck_rgb=self.img_uncheck_rgb,
                img_uncheck_hover_rgb=self.img_uncheck_hover_rgb,
                img_check_rgb=self.img_check_rgb,
                img_check_hover_rgb=self.img_check_hover_rgb,
            )

