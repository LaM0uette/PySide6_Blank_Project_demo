from src.build.mods import Functions
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

            # Paramètres
            edit=vb_wg.EDIT,
            curseur=vb_wg.CUR_MAIN,
            curseur_view=vb_wg.CUR_VIEW,

            # Couleurs BG
            bg=vb_wg.BG,
            bg_hover=vb_wg.BG_HOVER,
            bg_selection=vb_wg.BG_SELECTION,
            bg_item=vb_wg.BG_ITEM,
            bg_item_hover=vb_wg.BG_ITEM_HOVER,
            # Couleurs FG
            fg=vb_wg.FG,
            fg_hover=vb_wg.FG_HOVER,
            fg_selection=vb_wg.FG_SELECTION,
            fg_item=vb_wg.FG_ITEM,
            fg_item_hover=vb_wg.FG_ITEM_HOVER,

            # Images
            img=vb_wg.IMG_UNROLL,
            img_hover=vb_wg.IMG_UNROLL_HOVER,
            # Images RGB
            img_rgb=vb_wg.IMG_UNROLL_RGB,
            img_hover_rgb=vb_wg.IMG_UNROLL_HOVER_RGB,
            # Images DIM
            img_width=vb_wg.img_width,
            img_height=vb_wg.img_height,

            # Bordures
            border=vb_wg.BORDER_WIDTH,
            border_style=vb_wg.BORDER_STYLE,
            border_rgb=vb_wg.BORDER_RGB,
            # Bordures hover
            border_hover=vb_wg.BORDER_WIDTH,
            border_hover_style=vb_wg.BORDER_STYLE,
            border_hover_rgb=vb_wg.BORDER_RGB,

            # Rayons
            radius=vb_wg.RADIUS,

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
        """
        *Border_Style: str() : dashed | dot-dash | dot-dot-dash | dotted | double | groove | inset | outset | ridge | solid | none \n
        *Cur: list() : Cur().%nomCurseur() \n
        *Dim: int() : Dim().%nomDim() \n
        *Font: int() : Font().%nomFont() \n
        *Img: str() : Img().%nomImage() \n
        *Rgb: tuple() : Rgb().%nomCouleur() \n
        *Tuple: tuple() : (int(), int(), int(), int()) == (Top, Bottom, Right, Left) | (TopRight, TopLeft, BottomRight, BottomLeft) \n

        :param wgs: Widgets séparés par ","
        :param width: *Dim
        :param height: *Dim
        :param font: str()
        :param font_size: *Font
        :param edit: bool()
        :param curseur: *Cur
        :param curseur_view: *Cur
        :param bg: *Rgb
        :param bg_hover: *Rgb
        :param bg_selection: *Rgb
        :param bg_item: *Rgb
        :param bg_item_hover: *Rgb
        :param fg: *Rgb
        :param fg_hover: *Rgb
        :param fg_selection: *Rgb
        :param fg_item: *Rgb
        :param fg_item_hover: *Rgb
        :param img: *Img
        :param img_hover: *Img
        :param img_rgb: *Rgb
        :param img_hover_rgb:
        :param img_width: *Dim
        :param img_height: *Dim
        :param border: *Tuplev
        :param border_style: *Border_Style
        :param border_rgb: *Rgb
        :param border_hover: *Tuple
        :param border_hover_style: *Border_Style
        :param border_hover_rgb:
        :param radius: *Tuple
        :param scroll_bg: *Rgb
        :param scroll_width: *Dim
        :param scroll_height: *Dim
        :param scroll_handle_bg: *Rgb
        :param scroll_handle_bg_hover: *Rgb
        :param scroll_handle_fg: *Rgb
        :param scroll_handle_fg_hover: *Rgb
        :param scroll_handle_min_width: *Dim
        :param scroll_handle_min_height: *Dim
        """

        style = f"""
                /* COMBOBOX */
                QComboBox, QFontComboBox {{
                background-color: rgba{bg};
                color: rgba{fg};
                selection-background-color: rgba{bg_selection};
                selection-color: rgba{fg_selection};
                }}
                QComboBox:hover, QFontComboBox:hover {{
                background-color: rgba{bg_hover};
                color: rgba{fg_hover};
                }}

                /* BOUTON DE DEROULEMENT */
                QComboBox::drop-down, QFontComboBox::drop-down {{
                width: {height}px;
                border: none;
                }}

                /* IMAGE DU BOUTON DE DEROULEMENT */
                QComboBox::down-arrow, QFontComboBox::down-arrow {{
                image: url({f"{img}{img_rgb}.svg"});
                width: {img_width}px;
                height: {img_height}px;
                }}
                QComboBox::down-arrow:hover, QFontComboBox::down-arrow:hover {{
                image: url({f"{img_hover}{img_hover_rgb}.svg"});
                width: {img_width}px;
                height: {img_height}px;
                }}

                /* ELEMENTS DEROULEMENT */
                QComboBox QAbstractItemView::item, QFontComboBox QAbstractItemView::item {{
                background-color: rgba{bg_item};
                color: rgba{fg_item};
                }}
                QComboBox QAbstractItemView::item:hover, QFontComboBox QAbstractItemView::item:hover {{
                background-color: rgba{bg_item_hover};
                color: rgba{fg_item_hover};
                }}

                /* BORDURES */
                .QComboBox, .QFontComboBox {{
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}
                .QComboBox:hover, .QFontComboBox:hover {{
                border-top: {border_hover[0]}px {border_hover_style} rgba{border_hover_rgb};
                border-bottom: {border_hover[1]}px {border_hover_style} rgba{border_hover_rgb};
                border-right: {border_hover[2]}px {border_hover_style} rgba{border_hover_rgb};
                border-left: {border_hover[3]}px {border_hover_style} rgba{border_hover_rgb};
                }}

                /* RAYONS */
                .QComboBox, .QFontComboBox {{
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
            wg.setEditable(edit)
            if edit:
                Functions().SET_FONT(wg, font=font, font_size=font_size)
                wg.lineEdit().setFont(Functions().SET_FONT(wg, font=font, font_size=font_size))
                wg.lineEdit().setCursor(Functions().SET_CURSOR(vb_wg.CUR_LE()))

            # Curseur
            wg.setCursor(Functions().SET_CURSOR(curseur))
            wg.view().setCursor(Functions().SET_CURSOR(curseur_view))

            # Style
            wg.setStyleSheet(style)
