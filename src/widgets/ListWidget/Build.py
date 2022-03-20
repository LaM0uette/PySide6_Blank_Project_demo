from src.build.mods import Functions
from src.lib.palettes import *
from src.widgets import vb_wg


class Build:
    def __init__(
            self,
            *wgs,

            # Dimensions
            width=None,
            height=None,

            # Police
            font=vb_wg.FONT,
            font_size=vb_wg.FONT_SIZE,

            # Paramètres
            alternative_row_colors=False,
            drag_enabled=False,
            drag_drop_mode=vb_wg.DRAG_DROP_MODE,
            drop_action=vb_wg.DROP_ACTION,
            focus_policy=PaFocusPolicy.NO,
            flow=vb_wg.FLOW,
            frame_shape=vb_wg.FRAME_SHAPE,
            frame_shadow=vb_wg.FRAME_SHADOW,
            line_width=0,
            scroll_h=vb_wg.SCROLL_H,
            scroll_v=vb_wg.SCROLL_V,
            selection_behavior=vb_wg.SELECTION_BEHAVIOR,
            selection_mode=vb_wg.SELECTION_MODE,

            # Curseur
            cursor=vb_wg.CUR_VIEWPORT,

            # Couleurs BG
            bg=vb_wg.BG,
            bg_alternate=vb_wg.BG_ALTERNATE,
            bg_item=vb_wg.BG_ITEM,
            bg_item_hover=vb_wg.BG_ITEM_HOVER,
            bg_item_checked=vb_wg.BG_ITEM_CHECKED,
            bg_item_checked_hover=vb_wg.BG_ITEM_CHECKED_HOVER,
            # Couleurs FG
            fg=vb_wg.FG,
            fg_item=vb_wg.FG_ITEM,
            fg_item_hover=vb_wg.FG_ITEM_HOVER,
            fg_item_checked=vb_wg.FG_ITEM_CHECKED,
            fg_item_checked_hover=vb_wg.FG_ITEM_CHECKED_HOVER,

            # Bordures
            border=vb_wg.BORDER_WIDTH,
            border_style=vb_wg.BORDER_STYLE,
            border_rgb=vb_wg.BORDER_RGB,
            # Bordures hover
            border_hover=vb_wg.BORDER_WIDTH,
            border_hover_style=vb_wg.BORDER_STYLE,
            border_hover_rgb=vb_wg.BORDER_RGB,
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

            # PaScroll
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
        """
        *Border_Style: str() : dashed | dot-dash | dot-dot-dash | dotted | double | groove | inset | outset | ridge | solid | none \n
        *PaCur: list() : PaCur().%nomCurseur() \n
        *PaDim: int() : PaDim().%nomDim() \n
        *PaDragDropMode: QtWidgets.QAbstractItemView : PaDragDropMode().%nomDragMode \n
        *PaDropAction: QtCore.Qt : PaDropAction().%nomDropAction \n
        *PaFocusPolicy: QtCore.Qt : PaFocusPolicy().%nomFocus \n
        *PaFont: int() : PaFont().%nomFont() \n
        *PaFlow: QtWidgets.QListView : PaFlow().%nomFlow \n
        *PaFrameShape: QtWidgets.QFrame : PaFrameShape().%nomFrameForme \n
        *PaFrameShadow: QtWidgets.QFrame : PaFrameShadow().%nomFrameOmbre \n
        *RgbBox: tuple() : RgbBox().%nomCouleur() \n
        *PaSelectionBehavior: QtWidgets.QAbstractItemView : PaSelectionBehavior().%nomSelection \n
        *PaSelectionMode: QtWidgets.QAbstractItemView : PaSelectionMode().%nomSelection \n
        *Tuple: tuple() : (int(), int(), int(), int()) == (Top, Bottom, Right, Left) | (TopRight, TopLeft, BottomRight, BottomLeft) \n

        :param wgs: Widgets séparés par ","
        :param width: *PaDim
        :param height: *PaDim
        :param font: str()
        :param font_size: *PaFont
        :param alternative_row_colors: bool()
        :param drag_enabled: bool()
        :param drag_drop_mode: *PaDragDropMode
        :param drop_action: *PaDropAction
        :param focus_policy: *PaFocusPolicy
        :param flow: *PaFlow
        :param frame_shape: *PaFrameShape
        :param frame_shadow: *PaFrameShadow
        :param line_width: int()
        :param scroll_h: bool()
        :param scroll_v: bool()
        :param selection_behavior: *PaSelectionBehavior
        :param selection_mode: *PaSelectionMode
        :param cursor: *PaCur
        :param bg: *RgbBox
        :param bg_alternate: *RgbBox
        :param bg_item: *RgbBox
        :param bg_item_hover: *RgbBox
        :param bg_item_checked: *RgbBox
        :param bg_item_checked_hover: *RgbBox
        :param fg: *RgbBox
        :param fg_item: *RgbBox
        :param fg_item_hover: *RgbBox
        :param fg_item_checked: *RgbBox
        :param fg_item_checked_hover: *RgbBox
        :param border: *Tuple
        :param border_style: *Border_Style
        :param border_rgb: *RgbBox
        :param border_hover: *Tuple
        :param border_hover_style: *Border_Style
        :param border_hover_rgb: *RgbBox
        :param border_item: *Tuple
        :param border_item_style: *Border_Style
        :param border_item_rgb: *RgbBox
        :param border_item_hover: *Tuple
        :param border_item_hover_style: *Border_Style
        :param border_item_hover_rgb: *RgbBox
        :param border_item_checked: *Tuple
        :param border_item_checked_style: *Border_Style
        :param border_item_checked_rgb: *RgbBox
        :param border_item_checked_hover: *Tuple
        :param border_item_checked_hover_style: *Border_Style
        :param border_item_checked_hover_rgb: *RgbBox
        :param radius: *Tuple
        :param radius_item: *Tuple
        :param scroll_bg: *RgbBox
        :param scroll_width: *RgbBox
        :param scroll_height: *RgbBox
        :param scroll_handle_bg: *RgbBox
        :param scroll_handle_bg_hover: *RgbBox
        :param scroll_handle_fg: *RgbBox
        :param scroll_handle_fg_hover: *RgbBox
        :param scroll_handle_min_width: *PaDim
        :param scroll_handle_min_height: *PaDim
        """

        style = f"""
                /* LISTWIDGET */
                .QListWidget, .QListView {{
                background-color: rgba{bg};
                alternate-background-color: rgba{bg_alternate};
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
                border-top-right-radius: {radius_item[0]}px;
                border-top-left-radius: {radius_item[1]}px;
                border-bottom-right-radius: {radius_item[2]}px;
                border-bottom-left-radius: {radius_item[3]}px;
                }}
                .QListWidget::item:hover, .QListView::item:hover {{
                background-color: rgba{bg_item_hover};
                color: rgba{fg_item_hover};
                border-top: {border_item_hover[0]}px {border_item_hover_style} rgba{border_item_hover_rgb};
                border-bottom: {border_item_hover[1]}px {border_item_hover_style} rgba{border_item_hover_rgb};
                border-right: {border_item_hover[2]}px {border_item_hover_style} rgba{border_item_hover_rgb};
                border-left: {border_item_hover[3]}px {border_item_hover_style} rgba{border_item_hover_rgb};
                }}
                .QListWidget::item:selected, .QListView::item:selected {{
                background-color: rgba{bg_item_checked};
                color: rgba{fg_item_checked};
                border-top: {border_item_checked[0]}px {border_item_checked_style} rgba{border_item_checked_rgb};
                border-bottom: {border_item_checked[1]}px {border_item_checked_style} rgba{border_item_checked_rgb};
                border-right: {border_item_checked[2]}px {border_item_checked_style} rgba{border_item_checked_rgb};
                border-left: {border_item_checked[3]}px {border_item_checked_style} rgba{border_item_checked_rgb};
                }}
                .QListWidget::item:selected:hover, .QListView::item:selected:hover {{
                background-color: rgba{bg_item_checked_hover};
                color: rgba{fg_item_checked_hover};
                border-top: {border_item_checked_hover[0]}px {border_item_checked_hover_style} rgba{border_item_checked_hover_rgb};
                border-bottom: {border_item_checked_hover[1]}px {border_item_checked_hover_style} rgba{border_item_checked_hover_rgb};
                border-right: {border_item_checked_hover[2]}px {border_item_checked_hover_style} rgba{border_item_checked_hover_rgb};
                border-left: {border_item_checked_hover[3]}px {border_item_checked_hover_style} rgba{border_item_checked_hover_rgb};
                }}

                /* BORDURES */
                .QListWidget, .QListView {{
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}
                .QListWidget:hover, .QListView:hover {{
                border-top: {border_hover[0]}px {border_hover_style} rgba{border_hover_rgb};
                border-bottom: {border_hover[1]}px {border_hover_style} rgba{border_hover_rgb};
                border-right: {border_hover[2]}px {border_hover_style} rgba{border_hover_rgb};
                border-left: {border_hover[3]}px {border_hover_style} rgba{border_hover_rgb};
                }}

                /* RAYONS */
                .QListWidget, .QListView {{
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
            wg.setSelectionBehavior(selection_behavior)
            wg.setSelectionMode(selection_mode)

            # Curseur
            wg.setCursor(Functions().SET_CURSOR(cursor))
            wg.viewport().setCursor(Functions().SET_CURSOR(vb_wg.CUR_VIEW))

            # Style
            wg.setStyleSheet(style)
