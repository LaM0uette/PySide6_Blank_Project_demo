from .MyQPushButton import MyQPushButton
from .ClassePb import ClassePb
from src.build.mods import Functions
from src.lib.globals import v_wg
from src.lib.palettes import *


class Style(MyQPushButton):
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
            cursor=v_wg.CUR,
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
            auto_default=False,
            default=False,
            flat=True,
            pb_type=None,
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
        super().__init__(widget,size_policy_h,size_policy_v,fixed_width,fixed_height,minimum_width,minimum_height,maximum_width,maximum_height,font,cursor,focus_policy,layout_direction,txt,ico,ico_rgb,ico_width,ico_height,checkable,checked,auto_repeat,auto_exclusive,auto_repeat_delay,auto_repeat_interval,auto_default,default,flat)

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

        # Classes PB
        cls = ClassePb(
            widget=widget,
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
                widget.setIcon(Functions().SET_ICON(ico=img_uncheck, rgb=img_uncheck_rgb))
            else:
                widget.setIcon(Functions().SET_ICON(ico=img, rgb=img_rgb))

            if not img_height: img_height = widget.height() * StyleBase().x_ico()
            widget.setIconSize(Functions().SET_ICON_DIM(width=img_height, height=img_height))

        if pb_type == "check":
            widget.enterEvent = cls.ENT_CHECK
            widget.leaveEvent = cls.LVE_CHECK
            widget.mousePressEvent = cls.MP_CHECK
        elif pb_type == "ico":
            widget.enterEvent = cls.ENT_ICO
            widget.leaveEvent = cls.LVE_ICO
            widget.mousePressEvent = cls.MP_ICO
        elif pb_type == "zoom":
            widget.enterEvent = cls.ENT_ZOOM
            widget.leaveEvent = cls.LVE_ZOOM
