from .. import p_base
from ....build import *


class wg:
    def __init__(
            self,
            *wgs,
            couleur_bg=p_base.COULEUR_BG,
            couleur_bg_hover=p_base.COULEUR_BG_HOVER,
            couleur_bg_selection=p_base.COULEUR_BG_SELECTION,
            couleur_fg=p_base.COULEUR_FG,
            couleur_fg_hover=p_base.COULEUR_FG_HOVER,
            couleur_fg_selection=p_base.COULEUR_FG_SELECTION,
            couleur_bg_item=p_base.COULEUR_BG_ITEM,
            couleur_bg_item_hover=p_base.COULEUR_BG_ITEM_HOVER,
            couleur_fg_item=p_base.COULEUR_FG_ITEM,
            couleur_fg_item_hover=p_base.COULEUR_FG_ITEM_HOVER,
            wg_dim_width=p_base.DIM_WIDTH,
            wg_dim_height=p_base.DIM_HEIGHT,
            img=p_base.IMG_DEROULANT,
            tm=p_base.TM,
            img_hover=p_base.IMG_DEROULANT_HOVER,
            tm_hover=p_base.TM_HOVER,
            img_width=p_base.IMG_WIDTH,
            img_height=p_base.IMG_HEIGHT,
            bordure_width_top=p_base.BD_WIDTH,
            bordure_width_bottom=p_base.BD_WIDTH,
            bordure_width_right=p_base.BD_WIDTH,
            bordure_width_left=p_base.BD_WIDTH,
            bordure_style_top=p_base.BD_STYLE,
            bordure_style_bottom=p_base.BD_STYLE,
            bordure_style_right=p_base.BD_STYLE,
            bordure_style_left=p_base.BD_STYLE,
            bordure_couleur_top=p_base.BD_COULEUR,
            bordure_couleur_bottom=p_base.BD_COULEUR,
            bordure_couleur_right=p_base.BD_COULEUR,
            bordure_couleur_left=p_base.BD_COULEUR,
            rayon_top_left=p_base.RD_WG,
            rayon_top_right=p_base.RD_WG,
            rayon_bottom_right=p_base.RD_WG,
            rayon_bottom_left=p_base.RD_WG,
            police=p_base.FONT,
            police_taille=p_base.FONT_SIZE,
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
                border: none;
                }}

                /* BOUTON DE DEROULEMENT */
                QComboBox::drop-down, QFontComboBox::drop-down {{
                width: {wg_dim_height}px;
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
                background-color: rgb{couleur_bg_item};
                color: rgb{couleur_fg_item};
                }}
                QComboBox QAbstractItemView::item:hover, QFontComboBox QAbstractItemView::item:hover {{
                background-color: rgb{couleur_bg_item_hover};
                color: rgb{couleur_fg_item_hover};
                }}
                    
                /* BORDURES */
                .QCheckBox {{
                border-top: {bordure_width_top}px {bordure_style_top} rgba{bordure_couleur_top};
                border-bottom: {bordure_width_bottom}px {bordure_style_bottom} rgba{bordure_couleur_bottom};
                border-right: {bordure_width_right}px {bordure_style_right} rgba{bordure_couleur_right};
                border-left: {bordure_width_left}px {bordure_style_left} rgba{bordure_couleur_left};
                }}
                
                /* RAYONS */
                .QCheckBox {{
                border-top-left-radius: {rayon_top_left}px;
                border-top-right-radius: {rayon_top_right}px;
                border-bottom-right-radius: {rayon_bottom_right}px;
                border-bottom-left-radius: {rayon_bottom_left}px;
                }}

                
        """

        for wg in wgs:
            wg.setStyleSheet(style)

            try:
                Fct(wg=wg, w=wg_dim_width, h=wg_dim_height).DIM()
                wg.setFont(Fct(font=police, font_size=police_taille).FONT())

                wg.setEditable(edit)

                wg.setCursor(Fct(cur=curseur).CUR())
                wg.view().setCursor(Fct(cur=P_cur().souris_main()).CUR())
                if edit:
                    wg.lineEdit().setFont(Fct(font_size=police_taille).FONT())
                    wg.lineEdit().setCursor(Fct(cur=P_cur().IBeam()).CUR())
            except: pass
"""
/* SCROLL */
                QComboBox QScrollBar, QFontComboBox QScrollBar {{
                background-color: rgb{colors.get("c1")};
                width: 20px;
                height: 20px;
                }}
                QComboBox::handle:vertical, QFontComboBox::handle:vertical {{
                min-height: 100px;
                }}
                QComboBox::handle:vertical, QFontComboBox::handle:vertical {{
                min-height: 100px;
                }}
                QComboBox::handle:horizontal, QFontComboBox::handle:horizontal {{
                min-width: 100px;
                }}
                QComboBox QScrollBar::handle, QFontComboBox QScrollBar::handle {{
                background-color: rgb{colors.get("c3")};
                }}
                QComboBox QScrollBar::add-page, QComboBox QScrollBar::sub-page, QFontComboBox QScrollBar::add-page, QFontComboBox QScrollBar::sub-page {{
                background-color: rgb{colors.get("c1")};
                border: rgb{colors.get("c1")};
                }}

"""