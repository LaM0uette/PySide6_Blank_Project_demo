from ....build import *
from ....build.widgets import p_base

class Style:
    def __init__(
            self,

            # Widgets
            *wgs,

            # Couleurs BG
            bg_gen=None,
            bg=p_base.BG,
            bg_hover=p_base.BG_HOVER,
            bg_selection=p_base.BG_SELECTION,
            bg_item=p_base.BG_ITEM,
            bg_item_hover=p_base.BG_ITEM_HOVER,

            # Couleurs FG
            fg_gen=None,
            fg=p_base.FG,
            fg_hover=p_base.FG_HOVER,
            fg_selection=p_base.FG_SELECTION,
            fg_item=p_base.BG_ITEM,
            fg_item_hover=p_base.BG_ITEM_HOVER,

            # Dimensions WG
            width=p_base.WG_WIDTH,
            height=p_base.WG_HEIGHT,

            # Police
            font=p_base.FONT,
            font_size=p_base.FONT_SIZE,

            img=p_base.IMG_DEROULANT,
            tm=p_base.IMG_RGB,
            img_hover=p_base.IMG_DEROULANT_HOVER,
            tm_hover=p_base.IMG_UNCHECK_HOVER_RGB,
            img_width=p_base.IMG_WIDTH,
            img_height=p_base.IMG_HEIGHT,

            bordure_width_top=p_base.WG_BORDER_WIDTH,
            bordure_width_bottom=p_base.WG_BORDER_WIDTH,
            bordure_width_right=p_base.WG_BORDER_WIDTH,
            bordure_width_left=p_base.WG_BORDER_WIDTH,
            bordure_style_top=p_base.WG_BORDER_STYLE,
            bordure_style_bottom=p_base.WG_BORDER_STYLE,
            bordure_style_right=p_base.WG_BORDER_STYLE,
            bordure_style_left=p_base.WG_BORDER_STYLE,
            bordure_couleur_top=p_base.WG_BORDER_RGB,
            bordure_couleur_bottom=p_base.WG_BORDER_RGB,
            bordure_couleur_right=p_base.WG_BORDER_RGB,
            bordure_couleur_left=p_base.WG_BORDER_RGB,
            rayon_top_left=p_base.WG_RADIUS,
            rayon_top_right=p_base.WG_RADIUS,
            rayon_bottom_right=p_base.WG_RADIUS,
            rayon_bottom_left=p_base.WG_RADIUS,
            scroll_bg=p_base.SCROLL_BG,
            scroll_handle_bg=p_base.SCROLL_HANDLE_BG,
            scroll_handle_fg=p_base.SCROLL_HANDLE_FG,
            scroll_width=p_base.SCROLL_WIDTH,
            scroll_height=p_base.SCROLL_HEIGHT,
            scroll_handle_min_width=p_base.SCROLL_HANDLE_MIN_WIDTH,
            scroll_handle_min_height=p_base.SCROLL_HANDLE_MIN_HEIGHT,
            edit=p_base.EDIT,
            curseur=p_base.CUR
    ):
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
                image: url({f"{img}{tm}.svg"});
                width: {img_width}px;
                height: {img_height}px;
                }}
                QComboBox::down-arrow:hover, QFontComboBox::down-arrow:hover {{
                image: url({f"{img_hover}{tm_hover}.svg"});
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
                border-top: {bordure_width_top}px {bordure_style_top} rgba{bordure_couleur_top};
                border-bottom: {bordure_width_bottom}px {bordure_style_bottom} rgba{bordure_couleur_bottom};
                border-right: {bordure_width_right}px {bordure_style_right} rgba{bordure_couleur_right};
                border-left: {bordure_width_left}px {bordure_style_left} rgba{bordure_couleur_left};
                }}

                /* RAYONS */
                .QComboBox, .QFontComboBox {{
                border-top-left-radius: {rayon_top_left}px;
                border-top-right-radius: {rayon_top_right}px;
                border-bottom-right-radius: {rayon_bottom_right}px;
                border-bottom-left-radius: {rayon_bottom_left}px;
                }}

                /* SCROLL */
                QComboBox QScrollBar, QFontComboBox QScrollBar {{
                background-color: rgb{scroll_bg};
                width: {scroll_width}px;
                height: {scroll_height}px;
                }}
                QComboBox::handle:horizontal, QFontComboBox::handle:horizontal {{
                min-width: {scroll_handle_min_width}px;
                }}
                QComboBox::handle:vertical, QFontComboBox::handle:vertical {{
                min-height: {scroll_handle_min_height}px;
                }}
                QComboBox QScrollBar::handle, QFontComboBox QScrollBar::handle {{
                background-color: rgb{scroll_handle_fg};
                }}

                QComboBox QScrollBar::add-page, QComboBox QScrollBar::sub-page, QFontComboBox QScrollBar::add-page, QFontComboBox QScrollBar::sub-page {{
                background-color: rgb{scroll_handle_bg};
                border: none;
                }}"""

        for wg in wgs:
            wg.setStyleSheet(style)

            Fct(wg=wg, w=width, h=height).DIM()
            wg.setFont(Fct(font=font, font_size=font_size).FONT())

            wg.setEditable(edit)

            wg.setCursor(Fct(cur=curseur).CUR())
            wg.view().setCursor(Fct(cur=P_cur().souris_main()).CUR())
            if edit:
                    wg.lineEdit().setFont(Fct(font_size=font_size).FONT())
                    wg.lineEdit().setCursor(Fct(cur=P_cur().IBeam()).CUR())


class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
           curseur=P_cur().main(),
           bordure_couleur_bottom=P_rgb().th2()+(255, ),
           bordure_width_bottom=P_style().bd()
    )
class Base_tr(Style):
    def __init__(self, *wgs):
        super().__init__(*wgs,
           bg=Rgb().tr(),
           bg_hover=Rgb().tr(),
           edit=True
    )
