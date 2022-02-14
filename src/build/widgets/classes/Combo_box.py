from ....build import *
from ....build.widgets import p_base

class Style:
    def __init__(
            self,
            *wgs,
            couleur_bg=p_base._COLORS_BG,
            couleur_bg_hover=p_base._COLORS_BG_HOVER,
            couleur_bg_selection=p_base.COLORS_BG_SELECTION,
            couleur_bg_item=p_base.COLORS_BG_ITEM,
            couleur_bg_item_hover=p_base.COLORS_BG_ITEM_HOVER,
            couleur_fg=p_base._COLORS_FG,
            couleur_fg_hover=p_base._COLORS_FG_HOVER,
            couleur_fg_selection=p_base.COLORS_FG_SELECTION,
            couleur_fg_item=p_base.COLORS_FG_ITEM,
            couleur_fg_item_hover=p_base.COLORS_FG_ITEM_HOVER,
            dim_width=p_base.WG_WIDTH,
            dim_height=p_base.WG_HEIGHT,
            img=p_base.IMG_DEROULANT,
            tm=p_base.IMG_RGB,
            img_hover=p_base.IMG_DEROULANT_HOVER,
            tm_hover=p_base.IMG_UNCHECK_HOVER_RGB,
            img_width=p_base.IMG_WIDTH,
            img_height=p_base.IMG_HEIGHT,
            police=p_base.FONT,
            police_taille=p_base.FONT_SIZE,
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
                background-color: rgba{couleur_bg};
                color: rgb{couleur_fg};
                selection-background-color: rgb{couleur_bg_selection};
                selection-color: rgb{couleur_fg_selection};
                border: none;
                }}
                QComboBox:hover, QFontComboBox:hover {{
                background-color: rgba{couleur_bg_hover};
                color: rgb{couleur_fg_hover};
                selection-background-color: rgb{couleur_bg_selection};
                selection-color: rgb{couleur_fg_selection};
                }}

                /* BOUTON DE DEROULEMENT */
                QComboBox::drop-down, QFontComboBox::drop-down {{
                width: {dim_height}px;
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
                background-color: rgba{couleur_bg_item};
                color: rgb{couleur_fg_item};
                }}
                QComboBox QAbstractItemView::item:hover, QFontComboBox QAbstractItemView::item:hover {{
                background-color: rgba{couleur_bg_item_hover};
                color: rgb{couleur_fg_item_hover};
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

            try:
                Fct(wg=wg, w=dim_width, h=dim_height).DIM()
                wg.setFont(Fct(font=police, font_size=police_taille).FONT())

                wg.setEditable(edit)

                wg.setCursor(Fct(cur=curseur).CUR())
                wg.view().setCursor(Fct(cur=P_cur().souris_main()).CUR())
                if edit:
                    wg.lineEdit().setFont(Fct(font_size=police_taille).FONT())
                    wg.lineEdit().setCursor(Fct(cur=P_cur().IBeam()).CUR())
            except: pass


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
           couleur_bg=(0, 0, 0, 0),
           couleur_bg_hover=(0, 0, 0, 0),
           edit=True
    )
