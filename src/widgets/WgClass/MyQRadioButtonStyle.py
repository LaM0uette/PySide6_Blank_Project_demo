from .MyQAbstractButton import MyQAbstractButton
from src.lib.globals import v_wg
from src.lib.palettes import *


class Style(MyQAbstractButton):
    def __init__(
            self,
            widget,
            size_policy=v_wg.SIZE_POLICY,
            dim=v_wg.DIM_WG,
            font=v_wg.FONT,
            cursor=v_wg.CUR_ACTION,
            focus_policy=v_wg.FOCUS_POLICY,
            layout_direction=v_wg.LAYOUT_DIRECTION,
            txt=v_wg.TXT,
            ico=dc_ico.Base,
            checkable=True,
            checked=False,
            auto_repeat=False,
            auto_exclusive=True,
            auto_repeat_delay=v_wg.AUTO_REPEAT_DELAY,
            auto_repeat_interval=v_wg.AUTO_REPEAT_INTERVAL,
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
            spacing=10,
            img_uncheck=Img.CHECK0_ROND,
            img_uncheck_hover=Img.CHECK0_ROND,
            img_check=Img.CHECK2_ROND,
            img_check_hover=Img.CHECK2_ROND,
            img_uncheck_rgb=v_wg.IMG_UNCHECK_RGB,
            img_uncheck_hover_rgb=v_wg.IMG_UNCHECK_HOVER_RGB,
            img_check_rgb=v_wg.IMG_CHECK_RGB,
            img_check_hover_rgb=v_wg.IMG_CHECK_HOVER_RGB,
            img_width=15,
            img_height=15,
            img_margin=(0, 0, 0, 5),
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
        # Style
        super().__init__(widget, size_policy, dim, font, cursor, focus_policy, layout_direction, txt, ico, checkable, checked, auto_repeat, auto_exclusive, auto_repeat_delay, auto_repeat_interval)

        style = f"""
                /* CHECKBOX */
                QRadioButton {{
                background-color: rgba{bg};
                color: rgba{fg};
                spacing: {spacing}px;
                }}
                QRadioButton:hover {{
                background-color: rgba{bg_hover};
                color: rgba{fg_hover};
                }}
                QRadioButton:pressed {{
                background-color: rgba{bg_pressed};
                color: rgba{fg_pressed};
                }}
                QRadioButton:checked {{
                background-color: rgba{bg_checked};
                color: rgba{fg_checked};
                }}
                QRadioButton:checked:hover {{
                background-color: rgba{bg_checked_hover};
                color: rgba{fg_checked_hover};
                }}
                QRadioButton:checked:pressed {{
                background-color: rgba{bg_checked_pressed};
                color: rgba{fg_checked_pressed};
                }}

                /* IMG */
                QRadioButton::indicator {{
                margin-top: {img_margin[0]}px;
                margin-bottom: {img_margin[1]}px;
                margin-right: {img_margin[2]}px;
                margin-left: {img_margin[3]}px;
                width: {img_width}px;
                height: {img_height}px;
                }}
                QRadioButton::indicator:unchecked {{
                image: url({f"{img_uncheck}{img_uncheck_rgb}.svg"});
                }}
                QRadioButton::indicator:hover {{
                image: url({f"{img_uncheck_hover}{img_uncheck_hover_rgb}.svg"});
                }}
                QRadioButton::indicator:checked {{
                image: url({f"{img_check}{img_check_rgb}.svg"});
                }}
                QRadioButton::indicator:checked:hover {{
                image: url({f"{img_check_hover}{img_check_hover_rgb}.svg"});
                }}

                /* BORDURES */
                .QRadioButton {{
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}
                .QRadioButton:hover {{
                border-top: {border_hover[0]}px {border_hover_style} rgba{border_hover_rgb};
                border-bottom: {border_hover[1]}px {border_hover_style} rgba{border_hover_rgb};
                border-right: {border_hover[2]}px {border_hover_style} rgba{border_hover_rgb};
                border-left: {border_hover[3]}px {border_hover_style} rgba{border_hover_rgb};
                }}
                .QRadioButton:checked {{
                border-top: {border_checked[0]}px {border_checked_style} rgba{border_checked_rgb};
                border-bottom: {border_checked[1]}px {border_checked_style} rgba{border_checked_rgb};
                border-right: {border_checked[2]}px {border_checked_style} rgba{border_checked_rgb};
                border-left: {border_checked[3]}px {border_checked_style} rgba{border_checked_rgb};
                }}
                .QRadioButton:checked:hover {{
                border-top: {border_checked_hover[0]}px {border_checked_hover_style} rgba{border_checked_hover_rgb};
                border-bottom: {border_checked_hover[1]}px {border_checked_hover_style} rgba{border_checked_hover_rgb};
                border-right: {border_checked_hover[2]}px {border_checked_hover_style} rgba{border_checked_hover_rgb};
                border-left: {border_checked_hover[3]}px {border_checked_hover_style} rgba{border_checked_hover_rgb};
                }}

                /* RAYONS */
                .QRadioButton {{
                border-top-right-radius: {radius[0]}px;
                border-top-left-radius: {radius[1]}px;
                border-bottom-right-radius: {radius[2]}px;
                border-bottom-left-radius: {radius[3]}px;
                }}"""
        widget.setStyleSheet(style)
