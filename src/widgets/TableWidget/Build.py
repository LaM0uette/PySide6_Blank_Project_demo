from PySide6 import QtCore, QtWidgets

from src.build.mods import Functions
from src.lib.palettes import *
from src.widgets import vb_wg


class Build:
    def __init__(
            self,
            *wgs,

            # Dimensions
            width=vb_wg.WIDTH,
            height=vb_wg.HEIGHT,

            # Police
            font=vb_wg.FONT,
            font_size=vb_wg.FONT_SIZE,
            font_size_hd=vb_wg.FONT_SIZE_HD,

            # Paramètres
            alternative_row_colors=False,
            drag_enabled=False,
            drag_drop_mode=vb_wg.DRAG_DROP_MODE,
            drop_action=vb_wg.DROP_ACTION,
            focus_policy=FocusPolicy().no_focus(),
            flow=vb_wg.FLOW,
            frame_shape=vb_wg.FRAME_SHAPE,
            frame_shadow=vb_wg.FRAME_SHADOW,
            line_width=0,
            scroll_h=vb_wg.SCROLL_H,
            scroll_v=vb_wg.SCROLL_V,
            header_h=vb_wg.HEADER_H,
            header_v=vb_wg.HEADER_V,
            selection_behavior=vb_wg.SELECTION_BEHAVIOR,
            selection_mode=vb_wg.SELECTION_MODE,

            # Curseur
            curseur=Cur().croix(),

            # Couleurs BG
            bg=vb_wg.BG,
            bg_item=vb_wg.BG_ITEM,
            bg_item_hover=vb_wg.BG_ITEM_HOVER,
            bg_item_checked=vb_wg.BG_ITEM_CHECKED,
            bg_item_checked_hover=vb_wg.BG_ITEM_CHECKED_HOVER,
            bg_corner=vb_wg.BG,
            bg_header=Rgb().th2(),
            bg_header_hover=Rgb().th2(),
            bg_header_checked=Rgb().th3(),
            bg_header_checked_hover=Rgb().th3(),
            # Couleurs FG
            fg=vb_wg.FG,
            fg_item=vb_wg.FG_ITEM,
            fg_item_hover=vb_wg.FG_ITEM_HOVER,
            fg_item_checked=vb_wg.FG_ITEM_CHECKED,
            fg_item_checked_hover=vb_wg.FG_ITEM_CHECKED_HOVER,
            fg_header=Rgb().th1(),
            fg_header_hover=Rgb().bn1(),
            fg_header_checked=Rgb().bn1(),
            fg_header_checked_hover=Rgb().bn2(),
            # couleurs autres
            gridline=vb_wg.GRIDLINE,

            # Bordures
            border=vb_wg.BORDER_WIDTH,
            border_style=vb_wg.BORDER_STYLE,
            border_rgb=vb_wg.BORDER_RGB,
            # Bordures hover
            border_hover=vb_wg.BORDER_WIDTH,
            border_hover_style=vb_wg.BORDER_STYLE,
            border_hover_rgb=vb_wg.BORDER_RGB,
            # Bordures HD
            border_hd=vb_wg.BORDER_WIDTH,
            border_hd_style=vb_wg.BORDER_STYLE,
            border_hd_rgb=vb_wg.BORDER_RGB,
            # Bordures HD hover
            border_hd_hover=vb_wg.BORDER_WIDTH,
            border_hd_hover_style=vb_wg.BORDER_STYLE,
            border_hd_hover_rgb=vb_wg.BORDER_RGB,
            # Bordures HD checked
            border_hd_checked=vb_wg.BORDER_WIDTH,
            border_hd_checked_style=vb_wg.BORDER_STYLE,
            border_hd_checked_rgb=vb_wg.BORDER_RGB,
            # Bordures HD checked hover
            border_hd_checked_hover=vb_wg.BORDER_WIDTH,
            border_hd_checked_hover_style=vb_wg.BORDER_STYLE,
            border_hd_checked_hover_rgb=vb_wg.BORDER_RGB,
            # Bordures item
            border_item=vb_wg.BORDER_WIDTH,
            border_item_style=vb_wg.BORDER_STYLE,
            border_item_rgb=vb_wg.BORDER_RGB,
            # Bordures item hover
            border_item_hover=vb_wg.BORDER_WIDTH,
            border_item_hover_style=vb_wg.BORDER_STYLE,
            border_item_hover_rgb=vb_wg.BORDER_RGB,
            # Bordures item checked
            border_item_checked=vb_wg.BORDER_WIDTH,
            border_item_checked_style=vb_wg.BORDER_STYLE,
            border_item_checked_rgb=vb_wg.BORDER_RGB,
            # Bordures item checked hover
            border_item_checked_hover=vb_wg.BORDER_WIDTH,
            border_item_checked_hover_style=vb_wg.BORDER_STYLE,
            border_item_checked_hover_rgb=vb_wg.BORDER_RGB,

            # Rayons
            radius=vb_wg.RADIUS,
            radius_item=vb_wg.RADIUS,
            radius_hd=vb_wg.RADIUS,

            # Scroll
            scroll_bg=vb_wg.SCROLL_BG,
            scroll_width=vb_wg.SCROLL_WIDTH,
            scroll_height=vb_wg.SCROLL_HEIGHT,
            scroll_handle_bg=vb_wg.SCROLL_HANDLE_BG,
            scroll_handle_bg_hover=vb_wg.SCROLL_HANDLE_BG_HOVER,
            scroll_handle_fg=vb_wg.SCROLL_HANDLE_FG,
            scroll_handle_fg_hover=vb_wg.SCROLL_HANDLE_FG_HOVER,
            scroll_handle_min_width=vb_wg.SCROLL_HANDLE_MIN_WIDTH,
            scroll_handle_min_height=vb_wg.SCROLL_HANDLE_MIN_HEIGHT,
    ):

        style = f"""
                /* CORNER */
                QTableCornerButton::section {{
                background-color: rgba{bg_corner};
                }}

                /* TABLE_WIDGET */
                QTableWidget, QTableView {{
                background-color: rgba{bg};
                gridline-color: rgba{gridline};
                color: rgba{fg};
                }}

                /* ITEM */
                QTableWidget::item, QTableView::item {{
                background-color: rgba{bg_item};
                color: rgba{fg_item};
                border-top: {border_item[0]}px {border_item_style} rgba{border_item_rgb};
                border-bottom: {border_item[1]}px {border_item_style} rgba{border_item_rgb};
                border-right: {border_item[2]}px {border_item_style} rgba{border_item_rgb};
                border-left: {border_item[3]}px {border_item_style} rgba{border_item_rgb};
                border-top-right-radius: {radius_item[0]}px;
                border-top-left-radius: {radius_item[1]}px;
                border-bottom-right-radius: {radius_item[2]}px;
                border-bottom-left-radius: {radius_item[3]}px;
                }}
                QTableWidget::item:hover, QTableView::item:hover {{
                background-color: rgba{bg_item_hover};
                color: rgba{fg_item_hover};
                border-top: {border_item_hover[0]}px {border_item_hover_style} rgba{border_item_hover_rgb};
                border-bottom: {border_item_hover[1]}px {border_item_hover_style} rgba{border_item_hover_rgb};
                border-right: {border_item_hover[2]}px {border_item_hover_style} rgba{border_item_hover_rgb};
                border-left: {border_item_hover[3]}px {border_item_hover_style} rgba{border_item_hover_rgb};
                }}
                QTableWidget::item:selected, QTableView::item:selected {{
                background-color: rgba{bg_item_checked};
                color: rgba{fg_item_checked};
                border-top: {border_item_checked[0]}px {border_item_checked_style} rgba{border_item_checked_rgb};
                border-bottom: {border_item_checked[1]}px {border_item_checked_style} rgba{border_item_checked_rgb};
                border-right: {border_item_checked[2]}px {border_item_checked_style} rgba{border_item_checked_rgb};
                border-left: {border_item_checked[3]}px {border_item_checked_style} rgba{border_item_checked_rgb};
                }}
                QTableWidget::item:selected:hover, QTableView::item:selected:hover {{
                background-color: rgba{bg_item_checked_hover};
                color: rgba{fg_item_checked_hover};
                border-top: {border_item_checked_hover[0]}px {border_item_checked_hover_style} rgba{border_item_checked_hover_rgb};
                border-bottom: {border_item_checked_hover[1]}px {border_item_checked_hover_style} rgba{border_item_checked_hover_rgb};
                border-right: {border_item_checked_hover[2]}px {border_item_checked_hover_style} rgba{border_item_checked_hover_rgb};
                border-left: {border_item_checked_hover[3]}px {border_item_checked_hover_style} rgba{border_item_checked_hover_rgb};
                }}

                /* BORDURES */
                .QTableWidget, .QTableView {{
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}
                .QTableWidget:hover, .QTableView:hover {{
                border-top: {border_hover[0]}px {border_hover_style} rgba{border_hover_rgb};
                border-bottom: {border_hover[1]}px {border_hover_style} rgba{border_hover_rgb};
                border-right: {border_hover[2]}px {border_hover_style} rgba{border_hover_rgb};
                border-left: {border_hover[3]}px {border_hover_style} rgba{border_hover_rgb};
                }}

                /* HEADER */
                QHeaderView::section {{
                background-color: rgba{bg_header};
                color: rgba{fg_header};
                border-top: {border_hd[0]}px {border_hd_style} rgba{border_hd_rgb};
                border-bottom: {border_hd[1]}px {border_hd_style} rgba{border_hd_rgb};
                border-right: {border_hd[2]}px {border_hd_style} rgba{border_hd_rgb};
                border-left: {border_hd[3]}px {border_hd_style} rgba{border_hd_rgb};
                border-top-right-radius: {radius_hd[0]}px;
                border-top-left-radius: {radius_hd[1]}px;
                border-bottom-right-radius: {radius_hd[2]}px;
                border-bottom-left-radius: {radius_hd[3]}px;
                }}
                QHeaderView::section:hover {{
                background-color: rgba{bg_header_hover};
                color: rgba{fg_header_hover};
                border-top: {border_hd_hover[0]}px {border_hd_hover_style} rgba{border_hd_hover_rgb};
                border-bottom: {border_hd_hover[1]}px {border_hd_hover_style} rgba{border_hd_hover_rgb};
                border-right: {border_hd_hover[2]}px {border_hd_hover_style} rgba{border_hd_hover_rgb};
                border-left: {border_hd_hover[3]}px {border_hd_hover_style} rgba{border_hd_hover_rgb};
                }}
                QHeaderView::section:checked {{
                background-color: rgba{bg_header_checked};
                color: rgba{fg_header_checked};
                border-top: {border_hd_checked[0]}px {border_hd_checked_style} rgba{border_hd_checked_rgb};
                border-bottom: {border_hd_checked[1]}px {border_hd_checked_style} rgba{border_hd_checked_rgb};
                border-right: {border_hd_checked[2]}px {border_hd_checked_style} rgba{border_hd_checked_rgb};
                border-left: {border_hd_checked[3]}px {border_hd_checked_style} rgba{border_hd_checked_rgb};
                }}
                QHeaderView::section:checked:hover {{
                background-color: rgba{bg_header_checked_hover};
                color: rgba{fg_header_checked_hover};
                border-top: {border_hd_checked_hover[0]}px {border_hd_checked_hover_style} rgba{border_hd_checked_hover_rgb};
                border-bottom: {border_hd_checked_hover[1]}px {border_hd_checked_hover_style} rgba{border_hd_checked_hover_rgb};
                border-right: {border_hd_checked_hover[2]}px {border_hd_checked_hover_style} rgba{border_hd_checked_hover_rgb};
                border-left: {border_hd_checked_hover[3]}px {border_hd_checked_hover_style} rgba{border_hd_checked_hover_rgb};
                }}

                /* RAYONS */
                .QTableWidget, .QTableView {{
                border-top-right-radius: {radius[0]}px;
                border-top-left-radius: {radius[1]}px;
                border-bottom-right-radius: {radius[2]}px;
                border-bottom-left-radius: {radius[3]}px;
                }}

                /* SCROLL */
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
            # Dimensions
            Functions().SET_DIM(wg, width=width, height=height)

            # Police
            Functions().SET_FONT(wg, font=font, font_size=font_size)
            wg.horizontalHeader().setFont(Functions().SET_FONT(wg, font=font, font_size=font_size_hd, rtn=True))
            wg.verticalHeader().setFont(Functions().SET_FONT(wg, font=font, font_size=font_size_hd, rtn=True))

            # Paramètres
            wg.setAlternatingRowColors(alternative_row_colors)
            wg.setDragEnabled(drag_enabled)
            wg.setDragDropMode(drag_drop_mode)
            wg.setDefaultDropAction(drop_action)
            wg.setFocusPolicy(focus_policy)
            wg.setFlow(flow)
            wg.setFrameShape(frame_shape)
            wg.setFrameShadow(frame_shadow)
            wg.setLineWidth(line_width)
            wg.setHorizontalScrollBarPolicy(scroll_h)
            wg.setVerticalScrollBarPolicy(scroll_v)
            wg.setHorizontalScrollBarPolicy(scroll_h)
            wg.setVerticalScrollBarPolicy(scroll_v)
            wg.horizontalHeader().setVisible(header_h)
            wg.verticalHeader().setVisible(header_v)
            wg.setSelectionBehavior(selection_behavior)
            wg.setSelectionMode(selection_mode)

            # Curseur
            wg.setCursor(Fct(cur=curseur).CUR())
            wg.viewport().setCursor(Fct(cur=curseur).CUR())

            # Style
            wg.setStyleSheet(style)
            wg.horizontalHeader().setStyleSheet(style)
            wg.verticalHeader().setStyleSheet(style)



            wg.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
            wg.verticalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
            wg.resizeColumnsToContents()
