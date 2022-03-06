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
            align_horizontal=Align().left(),
            align_vertical=Align().center_vertical(),
            focus_policy=vb_wg.FOCUS_POLICY,
            frame_shape=vb_wg.FRAME_SHAPE,
            frame_shadow=vb_wg.FRAME_SHADOW,
            line_width=0,
            open_external_link=False,
            text_format=vb_wg.TEXT_FORMAT,
            word_wrap=vb_wg.WORD_WRAP,

            # Curseur
            cursor=vb_wg.CUR,

            # Couleurs BG
            bg=vb_wg.BG,
            bg_hover=vb_wg.BG_HOVER,
            # Couleurs FG
            fg=vb_wg.FG,
            fg_hover=vb_wg.FG_HOVER,

            # Positions WG
            margin=(0,) * 4,
            padding=(0,) * 4,

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
                /* LABEL */
                .QLabel {{
                background-color: rgba{bg};
                color: rgba{fg};
                margin-top: {margin[0]}px;
                margin-bottom: {margin[1]}px;
                margin-right: {margin[2]}px;
                margin-left: {margin[3]}px;
                padding-top: {padding[0]}px;
                padding-bottom: {padding[1]}px;
                padding-right: {padding[2]}px;
                padding-left: {padding[3]}px;
                }}
                .QLabel:hover {{
                background-color: rgba{bg_hover};
                color: rgba{fg_hover};
                }}

                /* BORDURES */
                .QLabel {{
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}
                .QLabel:hover {{
                border-top: {border_hover[0]}px {border_hover_style} rgba{border_hover_rgb};
                border-bottom: {border_hover[1]}px {border_hover_style} rgba{border_hover_rgb};
                border-right: {border_hover[2]}px {border_hover_style} rgba{border_hover_rgb};
                border-left: {border_hover[3]}px {border_hover_style} rgba{border_hover_rgb};
                }}

                /* RAYONS */
                .QLabel {{
                border-top-right-radius: {radius[0]}px;
                border-top-left-radius: {radius[1]}px;
                border-bottom-right-radius: {radius[2]}px;
                border-bottom-left-radius: {radius[3]}px;
                }}"""
        for wg in wgs:
            # Dimensions
            Functions().SET_DIM(wg, width=width, height=height)

            # Police
            Functions().SET_FONT(wg, font=font, font_size=font_size)

            # Paramètres
            wg.setAlignment(align_horizontal | align_vertical)
            wg.setFocusPolicy(focus_policy)
            wg.setFrameShape(frame_shape)
            wg.setFrameShadow(frame_shadow)
            wg.setLineWidth(line_width)
            wg.setOpenExternalLinks(open_external_link)
            wg.setTextFormat(text_format)
            wg.setWordWrap(word_wrap)

            # Curseur
            wg.setCursor(Functions().SET_CURSOR(cursor))

            # Style
            wg.setStyleSheet(style)
