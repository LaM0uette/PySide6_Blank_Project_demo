from ....build import *
from ....build.widgets import VBase

class Style:
    def __init__(
            self,
            *wgs,
            width=p_base.WG_WIDTH,
            height=p_base.WG_HEIGHT,
            font=p_base.FONT,
            font_size=p_base.FONT_SIZE,
            text_visible=p_base.TEXT_VISIBLE,
            align_horizontal=Align().h_center(),
            align_vertical=Align().v_center(),
            curseur=Cur().souris(),

            # Couleurs BG
            bg=p_base.BG,
            bg_chunk=p_base.BG_CHUNK,
            bg_chunk_hover=p_base.BG_CHUNK_HOVER,
            # Couleurs FG
            fg=p_base.FG,

            # Positions WG
            padding_top=0,
            padding_bottom=0,
            padding_right=0,
            padding_left=0,

            # Bordures
            border=p_base.WG_BORDER_WIDTH,
            border_style=p_base.WG_BORDER_STYLE,
            border_rgb=p_base.WG_BORDER_RGB,
            # Bordures hover
            border_hover=p_base.WG_BORDER_WIDTH,
            border_hover_style=p_base.WG_BORDER_STYLE,
            border_hover_rgb=p_base.WG_BORDER_RGB,

            # Rayons
            radius=p_base.WG_RADIUS,
            radius_chunk=p_base.WG_RADIUS
    ):
        style = f"""
                /* PROGRESSBAR */
                QProgressBar {{
                background-color: rgba{bg};
                color: rgba{fg};
                }}
        
                /* PROGRESS */
                QProgressBar::chunk {{
                background-color: rgba{bg_chunk};
                border-top-right-radius: {radius_chunk[0]}px;
                border-top-left-radius: {radius_chunk[1]}px;
                border-bottom-right-radius: {radius_chunk[2]}px;
                border-bottom-left-radius: {radius_chunk[3]}px;
                }}
                QProgressBar::chunk:hover {{
                background-color: rgba{bg_chunk_hover};
                }}
        
                /* BORDURES */
                .QProgressBar {{
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                padding-top={padding_top}px;
                padding-bottom={padding_bottom}px;
                padding-right={padding_right}px;
                padding-left={padding_left}px;
                }}
                .QProgressBar:hover {{
                border-top: {border_hover[0]}px {border_hover_style} rgba{border_hover_rgb};
                border-bottom: {border_hover[1]}px {border_hover_style} rgba{border_hover_rgb};
                border-right: {border_hover[2]}px {border_hover_style} rgba{border_hover_rgb};
                border-left: {border_hover[3]}px {border_hover_style} rgba{border_hover_rgb};
                }}
                
                /* RAYONS */
                .QProgressBar {{
                border-top-right-radius: {radius[0]}px;
                border-top-left-radius: {radius[1]}px;
                border-bottom-right-radius: {radius[2]}px;
                border-bottom-left-radius: {radius[3]}px;
                }}"""

        for wg in wgs:
            wg.setStyleSheet(style)

            Fct(wg=wg, w=width, h=height).DIM()
            wg.setFont(Fct(font=font, font_size=font_size).FONT())

            wg.setAlignment(align_horizontal | align_vertical)
            wg.setTextVisible(text_visible)

            wg.setCursor(Fct(cur=curseur).CUR())


##################
##     BASE     ##
##################
class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,

            border=((StyleBase().bd(), )*4),
            border_hover=((StyleBase().bd(), )*4),
            border_rgb=Rgb().th3(),
            border_hover_rgb=Rgb().th3(),
        )
class Base_tr(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            text_visible=False,

            bg=Rgb().tr(),

            border=((StyleBase().bd(), )*4),
            border_hover=((StyleBase().bd(), )*4),
            border_rgb=Rgb().th3(),
            border_hover_rgb=Rgb().th3(),
    )


##################
##     DEMO     ##
##################
class Demo_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,

            border=((StyleBase().bd(), )*4),
            border_hover=((StyleBase().bd(), )*4),
            border_rgb=Rgb().th3(),
            border_hover_rgb=Rgb().th3(),
            radius_chunk=(3, 0, 3, 0)
        )
class Demo_tr(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            text_visible=False,

            bg=Rgb().tr(),

            border=((StyleBase().bd(), )*4),
            border_hover=((StyleBase().bd(), )*4),
            border_rgb=Rgb().th3(),
            border_hover_rgb=Rgb().th3(),
            radius_chunk=(3, 0, 3, 0)
    )
