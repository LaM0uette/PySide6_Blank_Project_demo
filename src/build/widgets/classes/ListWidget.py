from ....build import *
from ....build.widgets import p_base

class Style:
    def __init__(
            self,
            *wgs,
            width=p_base.WG_WIDTH,
            height=p_base.WG_HEIGHT,
            font=p_base.FONT,
            font_size=p_base.FONT_SIZE,
            scroll_h=p_base.SCROLL_H,
            scroll_v=p_base.SCROLL_V,
            curseur=P_cur().croix(),

            # Couleurs BG
            bg=p_base.BG,
            bg_item=p_base.BG_ITEM,
            bg_item_hover=p_base.BG_ITEM_HOVER,
            bg_item_checked=p_base.BG_ITEM_CHECKED,
            bg_item_checked_hover=p_base.BG_ITEM_CHECKED_HOVER,
            # Couleurs FG
            fg=p_base.FG,
            fg_item=p_base.FG_ITEM,
            fg_item_hover=p_base.FG_ITEM_HOVER,
            fg_item_checked=p_base.FG_ITEM_CHECKED,
            fg_item_checked_hover=p_base.FG_ITEM_CHECKED_HOVER,

            # Bordures
            border=p_base.WG_BORDER_WIDTH,
            border_style=p_base.WG_BORDER_STYLE,
            border_rgb=p_base.WG_BORDER_RGB,
            # Bordures hover
            border_hover=p_base.WG_BORDER_WIDTH,
            border_style_hover=p_base.WG_BORDER_STYLE,
            border_rgb_hover=p_base.WG_BORDER_RGB,
            # Bordures item
            border_item=p_base.WG_BORDER_WIDTH,
            border_item_style=p_base.WG_BORDER_STYLE,
            border_item_rgb=p_base.WG_BORDER_RGB,
            # Bordures item hover
            border_item_hover=p_base.WG_BORDER_WIDTH,
            border_item_style_hover=p_base.WG_BORDER_STYLE,
            border_item_rgb_hover=p_base.WG_BORDER_RGB,
            # Bordures item checked
            border_item_checked=p_base.WG_BORDER_WIDTH,
            border_item_style_checked=p_base.WG_BORDER_STYLE,
            border_item_rgb_checked=p_base.WG_BORDER_RGB,
            # Bordures item checked hover
            border_item_checked_hover=p_base.WG_BORDER_WIDTH,
            border_item_style_checked_hover=p_base.WG_BORDER_STYLE,
            border_item_rgb_checked_hover=p_base.WG_BORDER_RGB,

            # Rayons
            radius=p_base.WG_RADIUS,

            # Scroll
            scroll_bg=p_base.SCROLL_BG,
            scroll_width=p_base.SCROLL_WIDTH,
            scroll_height=p_base.SCROLL_HEIGHT,
            scroll_handle_bg=p_base.SCROLL_HANDLE_BG,
            scroll_handle_bg_hover=p_base.SCROLL_HANDLE_BG_HOVER,
            scroll_handle_fg=p_base.SCROLL_HANDLE_FG,
            scroll_handle_fg_hover=p_base.SCROLL_HANDLE_FG_HOVER,
            scroll_handle_min_width=p_base.SCROLL_HANDLE_MIN_WIDTH,
            scroll_handle_min_height=p_base.SCROLL_HANDLE_MIN_HEIGHT,
    ):
        style = f"""
                .QListWidget, .QListView {{
                background-color: rgba{bg};
                color: rgba{fg};
                }}
        
                /* ITEM */
                .QListWidget::item, .QListView::item {{
                background-color: rgba{bg_item};
                color: rgba{fg_item};
                border-top: {border_item[0]}px {border_item_style} rgba{border_item_rgb};
                border-bottom: {border_item[1]}px {border_item_style} rgba{border_item_rgb};
                border-right: {border_item[2]}px {border_item_style} rgba{border_item_rgb};
                border-left: {border_item[3]}px {border_item_style} rgba{border_item_rgb};
                }}
                .QListWidget::item:hover, .QListView::item:hover {{
                background-color: rgba{bg_item_hover};
                color: rgba{fg_item_hover};
                border-top: {border_item_hover[0]}px {border_item_style_hover} rgba{border_item_rgb_hover};
                border-bottom: {border_item_hover[1]}px {border_item_style_hover} rgba{border_item_rgb_hover};
                border-right: {border_item_hover[2]}px {border_item_style_hover} rgba{border_item_rgb_hover};
                border-left: {border_item_hover[3]}px {border_item_style_hover} rgba{border_item_rgb_hover};
                }}
                .QListWidget::item:selected, .QListView::item:selected {{
                background-color: rgba{bg_item_checked};
                color: rgba{fg_item_checked};
                border-top: {border_item_checked[0]}px {border_item_style_checked} rgba{border_item_rgb_checked};
                border-bottom: {border_item_checked[1]}px {border_item_style_checked} rgba{border_item_rgb_checked};
                border-right: {border_item_checked[2]}px {border_item_style_checked} rgba{border_item_rgb_checked};
                border-left: {border_item_checked[3]}px {border_item_style_checked} rgba{border_item_rgb_checked};
                }}
                .QListWidget::item:selected:hover, .QListView::item:selected:hover {{
                background-color: rgba{bg_item_checked_hover};
                color: rgba{fg_item_checked_hover};
                border-top: {border_item_checked_hover[0]}px {border_item_style_checked_hover} rgba{border_item_rgb_checked_hover};
                border-bottom: {border_item_checked_hover[1]}px {border_item_style_checked_hover} rgba{border_item_rgb_checked_hover};
                border-right: {border_item_checked_hover[2]}px {border_item_style_checked_hover} rgba{border_item_rgb_checked_hover};
                border-left: {border_item_checked_hover[3]}px {border_item_style_checked_hover} rgba{border_item_rgb_checked_hover};
                }}
        
                /* BORDURES */
                .QListWidget, .QListView {{
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}
                .QListWidget:hover, .QListView:hover {{
                border-top: {border_hover[0]}px {border_style_hover} rgba{border_rgb_hover};
                border-bottom: {border_hover[1]}px {border_style_hover} rgba{border_rgb_hover};
                border-right: {border_hover[2]}px {border_style_hover} rgba{border_rgb_hover};
                border-left: {border_hover[3]}px {border_style_hover} rgba{border_rgb_hover};
                }}
                
                .QListWidget, .QListView {{
                border-top-right-radius: {radius[0]}px;
                border-top-left-radius: {radius[1]}px;
                border-bottom-right-radius: {radius[2]}px;
                border-bottom-left-radius: {radius[3]}px;
                }}
                
                QScrollBar {{
                background-color: rgba{scroll_bg};
                width: {scroll_width}px;
                height: {scroll_height}px;
                }}
                QScrollBar::handle:horizontal {{
                min-width: {scroll_handle_min_width}px;
                }}
                QScrollBar::handle:vertical {{
                min-height: {scroll_handle_min_height}px;
                }}
                QScrollBar::handle {{
                background-color: rgba{scroll_handle_fg};
                }}
                QScrollBar::handle:hover {{
                background-color: rgba{scroll_handle_fg_hover};
                }}
                
                QScrollBar::add-page, QScrollBar::sub-page {{
                background-color: rgba{scroll_handle_bg};
                border: none;
                }}
                QScrollBar::add-page:hover, QScrollBar::sub-page:hover {{
                background-color: rgba{scroll_handle_bg_hover};
                border: none;
                }}"""

        for wg in wgs:
            wg.setStyleSheet(style)

            Fct(wg=wg, w=width, h=height).DIM()
            wg.setFont(Fct(font=font, font_size=font_size).FONT())

            wg.setHorizontalScrollBarPolicy(scroll_h)
            wg.setVerticalScrollBarPolicy(scroll_v)

            wg.setCursor(Fct(cur=curseur).CUR())
            wg.viewport().setCursor(Fct(cur=P_cur().souris_main()).CUR())


##################
##     BASE     ##
##################
class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            fg_item_checked=Rgb().bn1(),
        )
class Base_tr(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            bg=Rgb().tr(),
            bg_item=Rgb().tr(),
            bg_item_hover=Rgb().tr(),
            bg_item_checked=Rgb().tr(),
            bg_item_checked_hover=Rgb().tr(),
            fg_item=Rgb().th3(),
            fg_item_checked=Rgb().bn1(),
        )


##################
##     DEMO     ##
##################
class Demo_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            height=P_dim().h5(),

            fg_item_checked=Rgb().bn1(),
    )
class Demo_tr(Style):
    bd_item = (0, 0, 0, 2)

    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            height=P_dim().h5(),

            bg=Rgb().tr(),
            bg_item=Rgb().tr(),
            bg_item_hover=Rgb().tr(),
            bg_item_checked=Rgb().tr(),
            bg_item_checked_hover=Rgb().tr(),
            fg_item=Rgb().th3(),
            fg_item_checked=Rgb().bn1(),

            border_item=self.bd_item,
            border_item_hover=self.bd_item,
            border_item_checked=self.bd_item,
            border_item_checked_hover=self.bd_item,
            border_item_rgb=Rgb().th2(),
            border_item_rgb_hover=Rgb().th3(),
            border_item_rgb_checked=Rgb().bn1(),
            border_item_rgb_checked_hover=Rgb().bn1(),
    )
