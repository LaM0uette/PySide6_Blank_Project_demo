from ....build import *
from ....build.widgets import VBase

class Style:
    def __init__(
            self,
            *wgs,
            width=VBase.WG_WIDTH,
            height=VBase.WG_HEIGHT,
            font=VBase.FONT,
            font_size=VBase.FONT_SIZE,
            height_separator=5,
            curseur=Cur().souris_main(),

            # Couleurs BG
            bg=VBase.BG,
            bg_hover=VBase.BG_HOVER,
            bg_item=VBase.BG_ITEM,
            bg_item_hover=VBase.BG_ITEM_HOVER,
            bg_item_checked=VBase.BG_ITEM_CHECKED,
            bg_item_checked_hover=VBase.BG_ITEM_CHECKED_HOVER,
            # Couleurs BG autres
            bg_separator=VBase.BG_SEPARATOR,
            # Couleurs FG
            fg=VBase.FG,
            fg_hover=VBase.FG_HOVER,
            fg_item=VBase.FG_ITEM,
            fg_item_hover=VBase.FG_ITEM_HOVER,
            fg_item_checked=VBase.FG_ITEM_CHECKED,
            fg_item_checked_hover=VBase.FG_ITEM_CHECKED_HOVER,

            # Positions WG
            margin_top=0,
            margin_bottom=0,
            margin_right=0,
            margin_left=0,
            padding_top=0,
            padding_bottom=0,
            padding_right=0,
            padding_left=0,

            # Bordures
            border=VBase.WG_BORDER_WIDTH,
            border_style=VBase.WG_BORDER_STYLE,
            border_rgb=VBase.WG_BORDER_RGB,
            # Bordures hover
            border_hover=VBase.WG_BORDER_WIDTH,
            border_hover_style=VBase.WG_BORDER_STYLE,
            border_hover_rgb=VBase.WG_BORDER_RGB,

            # Rayons
            radius=VBase.WG_RADIUS
    ):
        style = f"""
                /* MENU */
                QMenu {{
                background-color: rgba{bg};
                color: rgba{fg};
                }}
                QMenu:hover {{
                background-color: rgba{bg_hover};
                color: rgba{fg_hover};
                }}
                
                /* SEPARATEUR */
                QMenu::separator{{
                height: {height_separator}px;
                background-color: rgba{bg_separator};
                }}
                
                /* ITEM */
                QMenu::item {{
                background-color: rgb{bg_item};
                color: rgb{fg_item};
                margin-top={margin_top}px;
                margin-bottom={margin_bottom}px;
                margin-right={margin_right}px;
                margin-left={margin_left}px;
                padding-top={padding_top}px;
                padding-bottom={padding_bottom}px;
                padding-right={padding_right}px;
                padding-left={padding_left}px;
                }}
                QMenu::item:hover {{
                background-color: rgb{bg_item_hover};
                color: rgb{fg_item_hover};
                }}
                QMenu::item:selected {{
                background-color: rgb{bg_item_checked};
                color: rgb{fg_item_checked};
                }}
                QMenu::item:selected:hover {{
                background-color: rgb{bg_item_checked_hover};
                color: rgb{fg_item_checked_hover};
                }}
                
                /* BORDURES */
                .QMenu {{
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}
                .QMenu:hover {{
                border-top: {border_hover[0]}px {border_hover_style} rgba{border_hover_rgb};
                border-bottom: {border_hover[1]}px {border_hover_style} rgba{border_hover_rgb};
                border-right: {border_hover[2]}px {border_hover_style} rgba{border_hover_rgb};
                border-left: {border_hover[3]}px {border_hover_style} rgba{border_hover_rgb};
                }}
                
                /* RAYONS */
                .QCheckBox {{
                border-top-right-radius: {radius[0]}px;
                border-top-left-radius: {radius[1]}px;
                border-bottom-right-radius: {radius[2]}px;
                border-bottom-left-radius: {radius[3]}px;
                }}"""

        for wg in wgs:
            wg.setStyleSheet(style)

            Fct(wg=wg, w=width, h=height).DIM()
            wg.setFont(Fct(font=font, font_size=font_size).FONT())

            wg.setCursor(Fct(cur=curseur).CUR())


##################
##     BASE     ##
##################
class Main(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            img_margin_left=(VBase.WG_HEIGHT - (VBase.WG_HEIGHT * StyleBase().x_ico())) / 2,
        )
