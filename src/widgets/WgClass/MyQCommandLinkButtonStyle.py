from .MyQCommandLinkButton import MyQCommandLinkButton
from src.lib.globals import v_wg


class Style(MyQCommandLinkButton):
    def __init__(
            self,
            widget,
            size_policy=v_wg.SIZE_POLICY,
            dim=v_wg.DIM,
            font=v_wg.FONT,
            cursor=v_wg.CUR_ACTION,
            focus_policy=v_wg.FOCUS_POLICY,
            layout_direction=v_wg.LAYOUT_DIRECTION,

            txt=v_wg.TXT,
            ico=v_wg.ICO,
            checkable=False,
            checked=False,
            auto_actions=v_wg.AUTO_ACTIONS,

            auto_default=False,
            default=False,
            flat=True,
            description=None,

            background=v_wg.BACKGROUND,
            foreground=v_wg.FOREGROUND,
            spacing=10,
            img=v_wg.IMG,
            border=v_wg.BORDER,
    ):
        # Style
        super().__init__(widget, size_policy, dim, font, cursor, focus_policy, layout_direction, txt, ico, checkable, checked, auto_actions, auto_default, default, flat, description)

        style = f"""
                /* MyCommandLinkButton */
                QCommandLinkButton {{
                background-color: rgba{background.base};
                color: rgba{foreground.base};
                spacing: {spacing}px;
                }}
                QCommandLinkButton:hover {{
                background-color: rgba{background.hover};
                color: rgba{foreground.hover};
                }}
                QCommandLinkButton:checked {{
                background-color: rgba{background.checked};
                color: rgba{foreground.checked};
                }}
                QCommandLinkButton:checked:hover {{
                background-color: rgba{background.checked_hover};
                color: rgba{foreground.checked_hover};
                }}
                QCommandLinkButton:pressed {{
                background-color: rgba{background.pressed};
                color: rgba{foreground.pressed};
                }}
                QCommandLinkButton:checked:pressed {{
                background-color: rgba{background.checked_pressed};
                color: rgba{foreground.checked_pressed};
                }}

                /* IMG */
                QCommandLinkButton::indicator {{
                margin-top: {img.margin[0]}px;
                margin-bottom: {img.margin[1]}px;
                margin-right: {img.margin[2]}px;
                margin-left: {img.margin[3]}px;
                width: {img.width}px;
                height: {img.height}px;
                }}
                QCommandLinkButton::indicator:unchecked {{
                image: url({f"{img.uncheck}{img.uncheck_rgb}.svg"});
                }}
                QCommandLinkButton::indicator:hover {{
                image: url({f"{img.uncheck_hover}{img.uncheck_hover_rgb}.svg"});
                }}
                QCommandLinkButton::indicator:checked {{
                image: url({f"{img.check}{img.check_rgb}.svg"});
                }}
                QCommandLinkButton::indicator:checked:hover {{
                image: url({f"{img.check_hover}{img.check_hover_rgb}.svg"});
                }}

                /* BORDURES */
                .QCommandLinkButton {{
                border-top: {border.base[0]}px {border.base_style} rgba{border.base_rgb};
                border-bottom: {border.base[1]}px {border.base_style} rgba{border.base_rgb};
                border-right: {border.base[2]}px {border.base_style} rgba{border.base_rgb};
                border-left: {border.base[3]}px {border.base_style} rgba{border.base_rgb};
                }}
                .QCommandLinkButton:hover {{
                border-top: {border.hover[0]}px {border.hover_style} rgba{border.hover_rgb};
                border-bottom: {border.hover[1]}px {border.hover_style} rgba{border.hover_rgb};
                border-right: {border.hover[2]}px {border.hover_style} rgba{border.hover_rgb};
                border-left: {border.hover[3]}px {border.hover_style} rgba{border.hover_rgb};
                }}
                .QCommandLinkButton:checked {{
                border-top: {border.checked[0]}px {border.checked_style} rgba{border.checked_rgb};
                border-bottom: {border.checked[1]}px {border.checked_style} rgba{border.checked_rgb};
                border-right: {border.checked[2]}px {border.checked_style} rgba{border.checked_rgb};
                border-left: {border.checked[3]}px {border.checked_style} rgba{border.checked_rgb};
                }}
                .QCommandLinkButton:checked:hover {{
                border-top: {border.checked_hover[0]}px {border.checked_hover_style} rgba{border.checked_hover_rgb};
                border-bottom: {border.checked_hover[1]}px {border.checked_hover_style} rgba{border.checked_hover_rgb};
                border-right: {border.checked_hover[2]}px {border.checked_hover_style} rgba{border.checked_hover_rgb};
                border-left: {border.checked_hover[3]}px {border.checked_hover_style} rgba{border.checked_hover_rgb};
                }}

                /* RAYONS */
                .QCommandLinkButton {{
                border-top-right-radius: {border.radius[0]}px;
                border-top-left-radius: {border.radius[1]}px;
                border-bottom-right-radius: {border.radius[2]}px;
                border-bottom-left-radius: {border.radius[3]}px;
                }}"""
        widget.setStyleSheet(style)
