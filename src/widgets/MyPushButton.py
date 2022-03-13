from .WgClass.MyQPushButton import MyQPushButton
from src.lib.palettes import *
from src.lib.globals import v_wg


##################
##     BASE     ##
##################
class Base(MyQPushButton):
    def __init__(
            self,
            widget,

            bg=v_wg.BG,
            bg_hover=v_wg.BG_HOVER,
            bg_checked=v_wg.BG_CHECKED,
            bg_checked_hover=v_wg.BG_CHECKED_HOVER,
            bg_pressed=v_wg.BG_PRESSED,
            bg_checked_pressed=v_wg.BG_CHECKED_PRESSED,

            fg=v_wg.FG,
            fg_hover=v_wg.FG_HOVER,
            fg_checked=v_wg.FG_CHECKED,
            fg_checked_hover=v_wg.FG_CHECKED_HOVER,
            fg_pressed=v_wg.FG_PRESSED,
            fg_checked_pressed=v_wg.FG_CHECKED_PRESSED,

            img_uncheck=v_wg.IMG_UNCHECK,
            img_uncheck_hover=v_wg.IMG_UNCHECK_HOVER,
            img_check=v_wg.IMG_CHECK,
            img_check_hover=v_wg.IMG_CHECK_HOVER,
            img=v_wg.IMG_UNROLL,
            img_hover=v_wg.IMG_UNROLL_HOVER,

            img_uncheck_rgb=v_wg.IMG_UNCHECK_RGB,
            img_uncheck_hover_rgb=v_wg.IMG_UNCHECK_HOVER_RGB,
            img_check_rgb=v_wg.IMG_CHECK_RGB,
            img_check_hover_rgb=v_wg.IMG_CHECK_HOVER_RGB,
            img_rgb=v_wg.IMG_UNROLL_RGB,
            img_hover_rgb=v_wg.IMG_UNROLL_HOVER_RGB,

            img_height=None,
            IMG_HEIGHT=None,

            border=v_wg.BORDER_WIDTH,
            border_style=v_wg.BORDER_STYLE,
            border_rgb=v_wg.BORDER_RGB,

            border_hover=v_wg.BORDER_WIDTH,
            border_hover_style=v_wg.BORDER_STYLE,
            border_hover_rgb=v_wg.BORDER_RGB,

            border_checked=v_wg.BORDER_WIDTH,
            border_checked_style=v_wg.BORDER_STYLE,
            border_checked_rgb=v_wg.BORDER_RGB,

            border_checked_hover=v_wg.BORDER_WIDTH,
            border_checked_hover_style=v_wg.BORDER_STYLE,
            border_checked_hover_rgb=v_wg.BORDER_RGB,

            radius=v_wg.RADIUS
    ):
        super().__init__(widget)

        # Style
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
        widget.setStyleSheet(style)


class Transparent(Base):
    def __init__(self, widget):
        super().__init__(
            widget,
            bg=Rgb().tr(),
            bg_hover=Rgb().tr(),
            bg_checked=Rgb().tr(),
            bg_checked_hover=Rgb().tr(),
            bg_pressed=Rgb().tr(),
            bg_checked_pressed=Rgb().tr(),
            fg=Rgb().th3(),
            fg_checked=Rgb().bn1(),
        )
