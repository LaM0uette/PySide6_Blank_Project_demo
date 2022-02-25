from ....build import *
from ....build.widgets import VBase

class Style:
    def __init__(
            self,
            *wgs,
            width=VBase.WIDTH,
            height=VBase.HEIGHT,
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
            margin=((0, )*4),
            padding=((0, )*4),

            # Bordures
            border=VBase.WG_BORDER_WIDTH,
            border_style=VBase.WG_BORDER_STYLE,
            border_rgb=VBase.WG_BORDER_RGB,

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
                margin-top={margin[0]}px;
                margin-bottom={margin[1]}px;
                margin-right={margin[2]}px;
                margin-left={margin[3]}px;
                padding-top={padding[0]}px;
                padding-bottom={padding[1]}px;
                padding-right={padding[2]}px;
                padding-left={padding[3]}px;
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

            border=((StyleBase().bd(), )*4),
            border_rgb=Rgb().th2(),
        )
