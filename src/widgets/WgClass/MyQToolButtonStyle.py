from .MyQToolButton import MyQToolButton
from src.lib.globals import v_wg
from src.lib.palettes import *


class Style(MyQToolButton):
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
            ico=v_wg.ICO,
            checkable=False,
            checked=False,
            auto_actions=v_wg.AUTO_ACTIONS,

            popup_mode=v_wg.POPUP_MODE,
            tool_button_style=v_wg.TOOL_BUTTON_STYLE,
            auto_raise=False,
            arrow_type=v_wg.ARROW_TYPE,

            background=v_wg.BACKGROUND,
            foreground=v_wg.FOREGROUND,
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
        super().__init__(widget, size_policy, dim, font, cursor, focus_policy, layout_direction, txt, ico, checkable, checked, auto_actions, popup_mode, tool_button_style, auto_raise, arrow_type)
        style = f"""
                /* BUTTON */
                QToolButton {{
                background-color: rgba{background.base};
                color: rgba{foreground.base};
                }}
                QToolButton:hover {{
                background-color: rgba{background.hover};
                color: rgba{foreground.hover};
                }}
                QToolButton:checked {{
                background-color: rgba{background.checked};
                color: rgba{foreground.checked};
                }}
                QToolButton:checked:hover {{
                background-color: rgba{background.checked_hover};
                color: rgba{foreground.checked_hover};
                }}
                QToolButton:pressed {{
                background-color: rgba{background.pressed};
                color: rgba{foreground.pressed};
                }}
                QToolButton:checked:pressed {{
                background-color: rgba{background.checked_pressed};
                color: rgba{foreground.checked_pressed};
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
