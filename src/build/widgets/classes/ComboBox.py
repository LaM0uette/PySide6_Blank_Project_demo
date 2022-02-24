from .StyleSheet import StyleSheet
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
            edit=p_base.EDIT,
            curseur=P_cur().souris_main(),

            # Couleurs BG
            bg=p_base.BG,
            bg_hover=p_base.BG_HOVER,
            bg_selection=p_base.BG_SELECTION,
            bg_item=p_base.BG_ITEM,
            bg_item_hover=p_base.BG_ITEM_HOVER,
            # Couleurs FG
            fg=p_base.FG,
            fg_hover=p_base.FG_HOVER,
            fg_selection=p_base.FG_SELECTION,
            fg_item=p_base.FG_ITEM,
            fg_item_hover=p_base.FG_ITEM_HOVER,

            # Images
            img=p_base.IMG_UNROLL,
            img_hover=p_base.IMG_UNROLL_HOVER,
            # Images RGB
            img_rgb=p_base.IMG_UNROLL_RGB,
            img_hover_rgb=p_base.IMG_UNROLL_HOVER_RGB,
            # Images DIM
            img_width=p_base.img_width,
            img_height=p_base.img_height,

            # Bordures
            border_style=p_base.WG_BORDER_STYLE,
            border_rgb=p_base.WG_BORDER_RGB,
            border_top=p_base.WG_BORDER_WIDTH, border_bottom=p_base.WG_BORDER_WIDTH, border_right=p_base.WG_BORDER_WIDTH, border_left=p_base.WG_BORDER_WIDTH,
            # Bordures hover
            border_style_hover=p_base.WG_BORDER_STYLE,
            border_rgb_hover=p_base.WG_BORDER_RGB,
            border_top_hover=p_base.WG_BORDER_WIDTH, border_bottom_hover=p_base.WG_BORDER_WIDTH, border_right_hover=p_base.WG_BORDER_WIDTH, border_left_hover=p_base.WG_BORDER_WIDTH,

    ):
        style = f"""
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
                border-top: {border_top}px {border_style} rgba{border_rgb};
                border-bottom: {border_bottom}px {border_style} rgba{border_rgb};
                border-right: {border_right}px {border_style} rgba{border_rgb};
                border-left: {border_left}px {border_style} rgba{border_rgb};
                }}
                .QComboBox:hover, .QFontComboBox:hover {{
                border-top: {border_top_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-bottom: {border_bottom_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-right: {border_right_hover}px {border_style_hover} rgba{border_rgb_hover};
                border-left: {border_left_hover}px {border_style_hover} rgba{border_rgb_hover};
                }}
        """

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
        super().__init__(
            *wgs,
            curseur=P_cur().main(),
            style=StyleSheet(
            )
    )
class Base_tr(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            edit=True,
            style=StyleSheet(
                bg_gen=Rgb().tr(),
                fg=Rgb().th3(),
                bg_selection=Rgb().th3(),
                fg_selection=Rgb().th1(),
            )
    )
