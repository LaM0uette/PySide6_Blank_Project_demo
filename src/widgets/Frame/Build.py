from src.build.mods import Functions
from src.lib.palettes import *
from src.widgets import vb_wg, vb_app


class Build:
    def __init__(
            self,
            *wgs,

            # Dimensions
            width=vb_app.WIDTH,
            height=vb_app.HEIGHT,

            # Paramètres
            shadow=None,
            curseur=Cur().souris(),

            # Couleurs BG
            bg=vb_wg.BG,

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
    ):
        style = f"""
                /* FRAME */
                .QFrame {{
                background-color: rgba{bg};
                }}

                /* BORDURES */
                .QFrame {{
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}
                .QFrame:hover {{
                border-top: {border_hover[0]}px {border_hover_style} rgba{border_hover_rgb};
                border-bottom: {border_hover[1]}px {border_hover_style} rgba{border_hover_rgb};
                border-right: {border_hover[2]}px {border_hover_style} rgba{border_hover_rgb};
                border-left: {border_hover[3]}px {border_hover_style} rgba{border_hover_rgb};
                }}

                /* RAYONS */
                .QFrame {{
                border-top-right-radius: {radius[0]}px;
                border-top-left-radius: {radius[1]}px;
                border-bottom-right-radius: {radius[2]}px;
                border-bottom-left-radius: {radius[3]}px;
                }}"""

        for wg in wgs:
            # Dimensions
            Functions().SET_DIM(wg, width=width, height=height)

            # Paramètres
            if shadow is not None:
                wg.setGraphicsEffect(shadow)

            # Curseur
            wg.setCursor(Functions().SET_CURSOR(curseur))

            # Style
            wg.setStyleSheet(style)
