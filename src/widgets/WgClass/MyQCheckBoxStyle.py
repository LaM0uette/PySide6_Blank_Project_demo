from .MyQCheckBox import MyQCheckBox
from src.lib.globals import v_wg


class Style(MyQCheckBox):
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
            checkable=True,
            checked=False,
            auto_actions=v_wg.AUTO_ACTIONS_EXCLUSIVE,

            tristate=False,

            background=v_wg.BACKGROUND,
            foreground=v_wg.FOREGROUND,
            spacing=10,
            img=v_wg.IMG,
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
            border_indeterminate=v_wg.BORDER_WIDTH,
            border_indeterminate_style=v_wg.BORDER_STYLE,
            border_indeterminate_rgb=v_wg.BORDER_RGB,
            border_indeterminate_hover=v_wg.BORDER_WIDTH,
            border_indeterminate_hover_style=v_wg.BORDER_STYLE,
            border_indeterminate_hover_rgb=v_wg.BORDER_RGB,
            radius=v_wg.RADIUS
    ):
        # Style
        super().__init__(widget, size_policy, dim, font, cursor, focus_policy, layout_direction, txt, ico, checkable, checked, auto_actions, tristate)

        style = f"""
                /* CHECKBOX */
                QCheckBox {{
                background-color: rgba{background.base};
                color: rgba{foreground.base};
                spacing: {spacing}px;
                }}
                QCheckBox:hover {{
                background-color: rgba{background.hover};
                color: rgba{foreground.hover};
                }}
                QCheckBox:indeterminate {{
                background-color: rgba{background.indeterminate};
                color: rgba{foreground.indeterminate};
                }}
                QCheckBox:indeterminate:hover {{
                background-color: rgba{background.indeterminate_hover};
                color: rgba{foreground.indeterminate_hover};
                }}
                QCheckBox:checked {{
                background-color: rgba{background.checked};
                color: rgba{foreground.checked};
                }}
                QCheckBox:checked:hover {{
                background-color: rgba{background.checked_hover};
                color: rgba{foreground.checked_hover};
                }}
                QCheckBox:pressed {{
                background-color: rgba{background.pressed};
                color: rgba{foreground.pressed};
                }}
                QCheckBox:checked:pressed {{
                background-color: rgba{background.checked_pressed};
                color: rgba{foreground.checked_pressed};
                }}
                QCheckBox:indeterminate:pressed {{
                background-color: rgba{background.indeterminate_pressed};
                color: rgba{foreground.indeterminate_pressed};
                }}

                /* IMG */
                QCheckBox::indicator {{
                margin-top: {img.margin[0]}px;
                margin-bottom: {img.margin[1]}px;
                margin-right: {img.margin[2]}px;
                margin-left: {img.margin[3]}px;
                width: {img.width}px;
                height: {img.height}px;
                }}
                QCheckBox::indicator:unchecked {{
                image: url({f"{img.uncheck}{img.uncheck_rgb}.svg"});
                }}
                QCheckBox::indicator:hover {{
                image: url({f"{img.uncheck_hover}{img.uncheck_hover_rgb}.svg"});
                }}
                QCheckBox::indicator:checked {{
                image: url({f"{img.check}{img.check_rgb}.svg"});
                }}
                QCheckBox::indicator:checked:hover {{
                image: url({f"{img.check_hover}{img.check_hover_rgb}.svg"});
                }}
                QCheckBox::indicator::indeterminate {{
                image: url({f"{img.indeterminate}{img.indeterminate_rgb}.svg"});
                }}
                QCheckBox::indicator::indeterminate:hover {{
                image: url({f"{img.indeterminate_hover}{img.indeterminate_hover_rgb}.svg"});
                }}

                /* BORDURES */
                .QCheckBox {{
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}
                .QCheckBox:hover {{
                border-top: {border_hover[0]}px {border_hover_style} rgba{border_hover_rgb};
                border-bottom: {border_hover[1]}px {border_hover_style} rgba{border_hover_rgb};
                border-right: {border_hover[2]}px {border_hover_style} rgba{border_hover_rgb};
                border-left: {border_hover[3]}px {border_hover_style} rgba{border_hover_rgb};
                }}
                .QCheckBox:checked {{
                border-top: {border_checked[0]}px {border_checked_style} rgba{border_checked_rgb};
                border-bottom: {border_checked[1]}px {border_checked_style} rgba{border_checked_rgb};
                border-right: {border_checked[2]}px {border_checked_style} rgba{border_checked_rgb};
                border-left: {border_checked[3]}px {border_checked_style} rgba{border_checked_rgb};
                }}
                .QCheckBox:checked:hover {{
                border-top: {border_checked_hover[0]}px {border_checked_hover_style} rgba{border_checked_hover_rgb};
                border-bottom: {border_checked_hover[1]}px {border_checked_hover_style} rgba{border_checked_hover_rgb};
                border-right: {border_checked_hover[2]}px {border_checked_hover_style} rgba{border_checked_hover_rgb};
                border-left: {border_checked_hover[3]}px {border_checked_hover_style} rgba{border_checked_hover_rgb};
                }}
                .QCheckBox:indeterminate {{
                border-top: {border_indeterminate[0]}px {border_indeterminate_style} rgba{border_indeterminate_rgb};
                border-bottom: {border_indeterminate[1]}px {border_indeterminate_style} rgba{border_indeterminate_rgb};
                border-right: {border_indeterminate[2]}px {border_indeterminate_style} rgba{border_indeterminate_rgb};
                border-left: {border_indeterminate[3]}px {border_indeterminate_style} rgba{border_indeterminate_rgb};
                }}
                .QCheckBox:indeterminate:hover {{
                border-top: {border_indeterminate_hover[0]}px {border_indeterminate_hover_style} rgba{border_indeterminate_hover_rgb};
                border-bottom: {border_indeterminate_hover[1]}px {border_indeterminate_hover_style} rgba{border_indeterminate_hover_rgb};
                border-right: {border_indeterminate_hover[2]}px {border_indeterminate_hover_style} rgba{border_indeterminate_hover_rgb};
                border-left: {border_indeterminate_hover[3]}px {border_indeterminate_hover_style} rgba{border_indeterminate_hover_rgb};
                }}

                /* RAYONS */
                .QCheckBox {{
                border-top-right-radius: {radius[0]}px;
                border-top-left-radius: {radius[1]}px;
                border-bottom-right-radius: {radius[2]}px;
                border-bottom-left-radius: {radius[3]}px;
                }}"""
        widget.setStyleSheet(style)
