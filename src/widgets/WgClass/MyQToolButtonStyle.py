from .MyQToolButton import MyQToolButton
from src.lib.globals import v_wg


class Style(MyQToolButton):
    def __init__(
            self,
            widget,
            size_policy_h=v_wg.SIZE_POLICY_V,
            size_policy_v=v_wg.SIZE_POLICY_H,
            fixed_width=v_wg.WG_WIDTH,
            fixed_height=v_wg.WG_HEIGHT,
            minimum_width=None,
            minimum_height=None,
            maximum_width=None,
            maximum_height=None,
            font=v_wg.FONT,
            cursor=v_wg.CUR_ACTION,
            focus_policy=v_wg.FOCUS_POLICY,
            layout_direction=v_wg.LAYOUT_DIRECTION,
            txt=v_wg.TXT,
            ico=None,
            ico_rgb="",
            ico_width=None,
            ico_height=None,
            checkable=False,
            checked=False,
            auto_repeat=False,
            auto_exclusive=False,
            auto_repeat_delay=v_wg.AUTO_REPEAT_DELAY,
            auto_repeat_interval=v_wg.AUTO_REPEAT_INTERVAL,
            popup_mode=v_wg.POPUP_MODE,
            tool_button_style=v_wg.TOOL_BUTTON_STYLE,
            auto_raise=False,
            arrow_type=v_wg.ARROW_TYPE,
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
        # Style
        super().__init__(widget, size_policy_h, size_policy_v, fixed_width, fixed_height, minimum_width, minimum_height, maximum_width, maximum_height, font, cursor, focus_policy, layout_direction, txt, ico, ico_rgb, ico_width, ico_height, checkable, checked, auto_repeat, auto_exclusive, auto_repeat_delay, auto_repeat_interval, popup_mode, tool_button_style, auto_raise, arrow_type)
        style = f"""
                /* BUTTON */
                QToolButton {{
                background-color: rgba{bg};
                color: rgba{fg};
                }}

                QToolButton:hover {{
                background-color: rgba{bg_hover};
                color: rgba{fg_hover};
                }}

                QToolButton:checked {{
                background-color: rgba{bg_checked};
                color: rgba{fg_checked};
                }}

                QToolButton:checked:hover {{
                background-color: rgba{bg_checked_hover};
                color: rgba{fg_checked_hover};
                }}

                QToolButton:pressed {{
                background-color: rgba{bg_pressed};
                color: rgba{fg_pressed};
                }}

                QToolButton:checked:pressed {{
                background-color: rgba{bg_checked_pressed};
                color: rgba{fg_checked_pressed};
                }}
                
                QToolButton::menu-indicator {{
                image: url({f"{img}{img_rgb}.svg"});
                subcontrol-position: right center;
                subcontrol-origin: padding;
                left: -2px;
                }}

                /* BORDURES */
                .QToolButton {{
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}
                .QToolButton:hover {{
                border-top: {border_hover[0]}px {border_hover_style} rgba{border_hover_rgb};
                border-bottom: {border_hover[1]}px {border_hover_style} rgba{border_hover_rgb};
                border-right: {border_hover[2]}px {border_hover_style} rgba{border_hover_rgb};
                border-left: {border_hover[3]}px {border_hover_style} rgba{border_hover_rgb};
                }}
                .QToolButton:checked {{
                border-top: {border_checked[0]}px {border_checked_style} rgba{border_checked_rgb};
                border-bottom: {border_checked[1]}px {border_checked_style} rgba{border_checked_rgb};
                border-right: {border_checked[2]}px {border_checked_style} rgba{border_checked_rgb};
                border-left: {border_checked[3]}px {border_checked_style} rgba{border_checked_rgb};
                }}
                .QToolButton:checked:hover {{
                border-top: {border_checked_hover[0]}px {border_checked_hover_style} rgba{border_checked_hover_rgb};
                border-bottom: {border_checked_hover[1]}px {border_checked_hover_style} rgba{border_checked_hover_rgb};
                border-right: {border_checked_hover[2]}px {border_checked_hover_style} rgba{border_checked_hover_rgb};
                border-left: {border_checked_hover[3]}px {border_checked_hover_style} rgba{border_checked_hover_rgb};
                }}

                /* RAYONS */
                .QToolButton {{
                border-top-right-radius: {radius[0]}px;
                border-top-left-radius: {radius[1]}px;
                border-bottom-right-radius: {radius[2]}px;
                border-bottom-left-radius: {radius[3]}px;
                }}"""
        widget.setStyleSheet(style)
