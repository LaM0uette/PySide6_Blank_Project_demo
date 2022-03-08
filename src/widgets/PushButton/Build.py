from PySide6 import QtWidgets

from src.build.mods import Functions
from src.widgets import vb_wg
from src.widgets.PushButton.ClassePb import ClassePb


class Build:
    def __init__(
            self,
            *wgs,

            # Dimensions
            width=vb_wg.WIDTH,
            height=vb_wg.HEIGHT,

            # Police
            font=vb_wg.FONT,
            font_size=vb_wg.FONT_SIZE,

            # Paramètres
            pb_type=None,

            # Curseur
            cursor=vb_wg.CUR,

            # Couleurs BG
            bg=vb_wg.BG,
            bg_hover=vb_wg.BG_HOVER,
            bg_checked=vb_wg.BG_CHECKED,
            bg_checked_hover=vb_wg.BG_CHECKED_HOVER,
            bg_pressed=vb_wg.BG_PRESSED,
            bg_checked_pressed=vb_wg.BG_CHECKED_PRESSED,
            # Couleurs FG
            fg=vb_wg.FG,
            fg_hover=vb_wg.FG_HOVER,
            fg_checked=vb_wg.FG_CHECKED,
            fg_checked_hover=vb_wg.FG_CHECKED_HOVER,
            fg_pressed=vb_wg.FG_PRESSED,
            fg_checked_pressed=vb_wg.FG_CHECKED_PRESSED,

            # Images
            img_uncheck=vb_wg.IMG_UNCHECK,
            img_uncheck_hover=vb_wg.IMG_UNCHECK_HOVER,
            img_check=vb_wg.IMG_CHECK,
            img_check_hover=vb_wg.IMG_CHECK_HOVER,
            img=vb_wg.IMG_UNROLL,
            img_hover=vb_wg.IMG_UNROLL_HOVER,
            # Images RGB
            img_uncheck_rgb=vb_wg.IMG_UNCHECK_RGB,
            img_uncheck_hover_rgb=vb_wg.IMG_UNCHECK_HOVER_RGB,
            img_check_rgb=vb_wg.IMG_CHECK_RGB,
            img_check_hover_rgb=vb_wg.IMG_CHECK_HOVER_RGB,
            img_rgb=vb_wg.IMG_UNROLL_RGB,
            img_hover_rgb=vb_wg.IMG_UNROLL_HOVER_RGB,
            # Images DIM
            img_height=vb_wg.img_height,
            IMG_HEIGHT=vb_wg.IMG_HEIGHT,

            # Bordures
            border=vb_wg.BORDER_WIDTH,
            border_style=vb_wg.BORDER_STYLE,
            border_rgb=vb_wg.BORDER_RGB,
            # Bordures hover
            border_hover=vb_wg.BORDER_WIDTH,
            border_hover_style=vb_wg.BORDER_STYLE,
            border_hover_rgb=vb_wg.BORDER_RGB,
            # Bordures checked
            border_checked=vb_wg.BORDER_WIDTH,
            border_checked_style=vb_wg.BORDER_STYLE,
            border_checked_rgb=vb_wg.BORDER_RGB,
            # Bordures checked hover
            border_checked_hover=vb_wg.BORDER_WIDTH,
            border_checked_hover_style=vb_wg.BORDER_STYLE,
            border_checked_hover_rgb=vb_wg.BORDER_RGB,

            # Rayons
            radius=vb_wg.RADIUS
    ):
        
        style = f"""
                /* BUTTON */
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
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}
                .QPushButton:hover {{
                border-top: {border_hover[0]}px {border_hover_style} rgba{border_hover_rgb};
                border-bottom: {border_hover[1]}px {border_hover_style} rgba{border_hover_rgb};
                border-right: {border_hover[2]}px {border_hover_style} rgba{border_hover_rgb};
                border-left: {border_hover[3]}px {border_hover_style} rgba{border_hover_rgb};
                }}
                .QPushButton:checked {{
                border-top: {border_checked[0]}px {border_checked_style} rgba{border_checked_rgb};
                border-bottom: {border_checked[1]}px {border_checked_style} rgba{border_checked_rgb};
                border-right: {border_checked[2]}px {border_checked_style} rgba{border_checked_rgb};
                border-left: {border_checked[3]}px {border_checked_style} rgba{border_checked_rgb};
                }}
                .QPushButton:checked:hover {{
                border-top: {border_checked_hover[0]}px {border_checked_hover_style} rgba{border_checked_hover_rgb};
                border-bottom: {border_checked_hover[1]}px {border_checked_hover_style} rgba{border_checked_hover_rgb};
                border-right: {border_checked_hover[2]}px {border_checked_hover_style} rgba{border_checked_hover_rgb};
                border-left: {border_checked_hover[3]}px {border_checked_hover_style} rgba{border_checked_hover_rgb};
                }}

                /* RAYONS */
                .QPushButton {{
                border-top-right-radius: {radius[0]}px;
                border-top-left-radius: {radius[1]}px;
                border-bottom-right-radius: {radius[2]}px;
                border-bottom-left-radius: {radius[3]}px;
                }}"""
        for wg in wgs:
            # Dimensions
            Functions().SET_DIM(wg, width=width, height=height)

            # Police
            Functions().SET_FONT(wg, font=font, font_size=font_size)

            # Paramètres
            wg.setFlat(True)
            wg.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

            # Curseur
            wg.setCursor(Functions().SET_CURSOR(cursor))

            # Style
            wg.setStyleSheet(style)

            cls = ClassePb(
                wg=wg,
                dim_ico=img_height,
                DIM_ICO=IMG_HEIGHT,
                img=img,
                img_hover=img_hover,
                img_uncheck=img_uncheck,
                img_uncheck_hover=img_uncheck_hover,
                img_check=img_check,
                img_check_hover=img_check_hover,
                img_rgb=img_rgb,
                img_hover_rgb=img_hover_rgb,
                img_uncheck_rgb=img_uncheck_rgb,
                img_uncheck_hover_rgb=img_uncheck_hover_rgb,
                img_check_rgb=img_check_rgb,
                img_check_hover_rgb=img_check_hover_rgb,
            )

            if pb_type is not None:
                if pb_type == "check":
                    Functions().SET_ICON(wg=wg, img=f"{img_uncheck}{img_uncheck_rgb}", dim=img_height)
                else:
                    Functions().SET_ICON(wg=wg, img=f"{img}{img_rgb}", dim=img_height)

            if pb_type == "check":
                wg.enterEvent = cls.ENT_CHECK
                wg.leaveEvent = cls.LVE_CHECK
                wg.mousePressEvent = cls.MP_CHECK
            elif pb_type == "ico":
                wg.enterEvent = cls.ENT_ICO
                wg.leaveEvent = cls.LVE_ICO
                wg.mousePressEvent = cls.MP_ICO
            elif pb_type == "zoom":
                wg.enterEvent = cls.ENT_ZOOM
                wg.leaveEvent = cls.LVE_ZOOM
