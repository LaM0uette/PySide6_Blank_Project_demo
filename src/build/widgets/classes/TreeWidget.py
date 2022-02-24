from PySide6 import QtCore, QtWidgets

from ....build import *
from ....build.widgets import p_base

class Style:
    def __init__(
            self,
            *wgs,
            width=p_base.WIDTH,
            height=p_base.HEIGHT,
            font=p_base.FONT,
            font_size=p_base.FONT_SIZE,
            scroll_h=p_base.SCROLL_H,
            scroll_v=p_base.SCROLL_V,
            curseur=p_base.CUR,

            # Couleurs BG
            bg=p_base.BG,
            bg_item=p_base.BG_ITEM,
            bg_item_hover=p_base.BG_ITEM_HOVER,
            bg_item_checked=p_base.BG_ITEM_CHECKED,
            bg_item_checked_hover=p_base.BG_ITEM_CHECKED_HOVER,
            bg_header=Rgb().th2(),
            # Couleurs FG
            fg=p_base.FG,
            fg_item=p_base.FG_ITEM,
            fg_item_hover=p_base.FG_ITEM_HOVER,
            fg_item_checked=p_base.FG_ITEM_CHECKED,
            fg_item_checked_hover=p_base.FG_ITEM_CHECKED_HOVER,
            fg_header=Rgb().th1(),

            # Bordures
            border=p_base.WG_BORDER_WIDTH,
            border_style=p_base.WG_BORDER_STYLE,
            border_rgb=p_base.WG_BORDER_RGB,
            # Bordures hover
            border_hover=p_base.WG_BORDER_WIDTH,
            border_hover_style=p_base.WG_BORDER_STYLE,
            border_hover_rgb=p_base.WG_BORDER_RGB,
            # Bordures HD
            border_hd=p_base.WG_BORDER_WIDTH,
            border_hd_style=p_base.WG_BORDER_STYLE,
            border_hd_rgb=p_base.WG_BORDER_RGB,
            # Bordures item
            border_item_all=None,
            border_item_style=p_base.WG_BORDER_STYLE,
            border_item_rgb=p_base.WG_BORDER_RGB,
            border_item_top=p_base.WG_BORDER_WIDTH, border_item_bottom=p_base.WG_BORDER_WIDTH, border_item_right=p_base.WG_BORDER_WIDTH, border_item_left=p_base.WG_BORDER_WIDTH,
            # Bordures item hover
            border_item_all_hover=None,
            border_item_style_hover=p_base.WG_BORDER_STYLE,
            border_item_rgb_hover=p_base.WG_BORDER_RGB,
            border_item_top_hover=p_base.WG_BORDER_WIDTH, border_item_bottom_hover=p_base.WG_BORDER_WIDTH, border_item_right_hover=p_base.WG_BORDER_WIDTH, border_item_left_hover=p_base.WG_BORDER_WIDTH,
            # Bordures item checked
            border_item_all_checked=None,
            border_item_style_checked=p_base.WG_BORDER_STYLE,
            border_item_rgb_checked=p_base.WG_BORDER_RGB,
            border_item_top_checked=p_base.WG_BORDER_WIDTH, border_item_bottom_checked=p_base.WG_BORDER_WIDTH, border_item_right_checked=p_base.WG_BORDER_WIDTH, border_item_left_checked=p_base.WG_BORDER_WIDTH,
            # Bordures item checked hover
            border_item_all_checked_hover=None,
    ):
        style = f"""
                /* TREEWIDGET */
                QHeaderView::section {{
                background-color: rgba{bg_header};
                color: rgba{fg_header};
                border-top: {border_hd[0]}px {border_hd_style} rgba{border_hd_rgb};
                border-bottom: {border_hd[1]}px {border_hd_style} rgba{border_hd_rgb};
                border-right: {border_hd[2]}px {border_hd_style} rgba{border_hd_rgb};
                border-left: {border_hd[3]}px {border_hd_style} rgba{border_hd_rgb};
                }}
        
                QTreeWidget, QTreeView {{
                background-color: rgba{bg};
                color: rgba{fg};
                }}
        
                QTreeWidget::item, QTreeView::item {{
                background-color: rgba{bg_item};
                color: rgba{fg_item};
                border-top: {border_item_top}px {border_item_style} rgba{border_item_rgb};
                border-bottom: {border_item_bottom}px {border_item_style} rgba{border_item_rgb};
                border-right: {border_item_right}px {border_item_style} rgba{border_item_rgb};
                border-left: {border_item_left}px {border_item_style} rgba{border_item_rgb};
                }}
        
                QTreeWidget::item:hover, QTreeView::item:hover {{
                background-color: rgba{bg_item_hover};
                color: rgba{fg_item_hover};
                border-top: {border_item_top_hover}px {border_item_style_hover} rgba{border_item_rgb_hover};
                border-bottom: {border_item_bottom_hover}px {border_item_style_hover} rgba{border_item_rgb_hover};
                border-right: {border_item_right_hover}px {border_item_style_hover} rgba{border_item_rgb_hover};
                border-left: {border_item_left_hover}px {border_item_style_hover} rgba{border_item_rgb_hover};
                }}
        
                QTreeWidget::item:selected, QTreeView::item:selected {{
                background-color: rgba{bg_item_checked};
                color: rgba{fg_item_checked};
                border-top: {border_item_top_checked}px {border_item_style_checked} rgba{border_item_rgb_checked};
                border-bottom: {border_item_bottom_checked}px {border_item_style_checked} rgba{border_item_rgb_checked};
                border-right: {border_item_right_checked}px {border_item_style_checked} rgba{border_item_rgb_checked};
                border-left: {border_item_left_checked}px {border_item_style_checked} rgba{border_item_rgb_checked};
                }}
        
                QTreeWidget::item:selected:hover, QTreeView::item:selected:hover {{
                background-color: rgba{bg_item_checked_hover};
                color: rgba{fg_item_checked_hover};
                border-top: {border_item_top_checked_hover}px {border_item_style_checked_hover} rgba{border_item_rgb_checked_hover};
                border-bottom: {border_item_bottom_checked_hover}px {border_item_style_checked_hover} rgba{border_item_rgb_checked_hover};
                border-right: {border_item_right_checked_hover}px {border_item_style_checked_hover} rgba{border_item_rgb_checked_hover};
                border-left: {border_item_left_checked_hover}px {border_item_style_checked_hover} rgba{border_item_rgb_checked_hover};
                }}
        
                /* BORDURES */
                .QTreeWidget, .QTreeView {{
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}
                .QTreeWidget:hover, .QTreeView:hover {{
                border-top: {border_hover[0]}px {border_hover_style} rgba{border_hover_rgb};
                border-bottom: {border_hover[1]}px {border_hover_style} rgba{border_hover_rgb};
                border-right: {border_hover[2]}px {border_hover_style} rgba{border_hover_rgb};
                border-left: {border_hover[3]}px {border_hover_style} rgba{border_hover_rgb};
                }}
        """

        for wg in wgs:
            wg.setStyleSheet(style)

            Fct(wg=wg, w=width, h=height).DIM()
            wg.setFont(Fct(font=font, font_size=font_size).FONT())

            wg.setHorizontalScrollBarPolicy(scroll_h)
            wg.setVerticalScrollBarPolicy(scroll_v)

            wg.setFrameShape(QtWidgets.QFrame.NoFrame)

            wg.setCursor(Fct(cur=curseur).CUR())


##################
##     BASE     ##
##################
class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            style=StyleSheet(
            )
        )
class Base_tr(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            scroll_h=QtCore.Qt.ScrollBarAlwaysOff,
            scroll_v=QtCore.Qt.ScrollBarAlwaysOff,

            style=StyleSheet(
                bg_gen=Rgb().tr(),
                bg_item_gen=Rgb().tr(),
                fg_item=Rgb().th3(),
                fg_item_checked=Rgb().bn1(),
                border_item_gen_left=2,
                border_item_rgb=Rgb().th2(),
                border_item_rgb_hover=Rgb().th3(),
                border_item_rgb_checked=Rgb().bn1(),
                border_item_rgb_checked_hover=Rgb().bn1(),
            )
    )
class option(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            width=P_dim().h5(),
            scroll_h=QtCore.Qt.ScrollBarAlwaysOff,
            scroll_v=QtCore.Qt.ScrollBarAlwaysOff,

            style=StyleSheet(
                bg_gen=Rgb().tr(),
                bg_item_gen=Rgb().tr(),
                bg_header=Rgb().tr(),
                fg_item=Rgb().th3(),
                fg_item_checked=Rgb().bn1(),
                fg_header=Rgb().tr(),
                border_gen_right=2,
                border_gen_rgb=Rgb().th2(),
                border_item_gen_left=2,
                border_item_rgb=Rgb().th2(),
                border_item_rgb_hover=Rgb().th3(),
                border_item_rgb_checked=Rgb().bn1(),
                border_item_rgb_checked_hover=Rgb().bn1(),
            )
    )
