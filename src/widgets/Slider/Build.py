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

            # Paramètres
            value_min=vb_wg.VALUE_MIN,
            value_max=vb_wg.VALUE_MAX,
            value_step=vb_wg.VALUE_STEP,
            page_step=vb_wg.PAGE_STEP,
            tick_position=vb_wg.TICK_POSITION,

            # Curseur
            cursor=vb_wg.CUR,
            
            # Couleurs BG
            bg=vb_wg.BG,
            bg_groove=vb_wg.BG_GROOVE,
            bg_groove_2=None,
            bg_groove_hover=vb_wg.BG_GROOVE_HOVER,
            bg_groove_hover_2=None,
            bg_groove_pressed=vb_wg.BG_GROOVE_PRESSED,
            bg_groove_pressed_2=None,
            bg_handle=vb_wg.BG_HANDLE,
            bg_handle_hover=vb_wg.BG_HANDLE_HOVER,
            bg_handle_pressed=vb_wg.BG_HANDLE_PRESSED,
            gradient=((0,) * 4),
            
            # Dimensions WG
            width_groove=Dim().h9(),
            height_groove=Dim().h9(),
            width_handle_h=Dim().h9(),
            height_handle_h=Dim().h9(),
            width_handle_v=Dim().h9(),
            height_handle_v=Dim().h9(),
            
            # Positions WG
            margin_handle_h=(0,) * 4,
            margin_handle_v=(0,) * 4,
            
            # Bordures
            border=vb_wg.BORDER_WIDTH,
            border_style=vb_wg.BORDER_STYLE,
            border_rgb=vb_wg.BORDER_RGB,
            # Bordures hover
            border_hover=vb_wg.BORDER_WIDTH,
            border_hover_style=vb_wg.BORDER_STYLE,
            border_hover_rgb=vb_wg.BORDER_RGB,
            # Bordures slider h
            border_handle_h=vb_wg.BORDER_WIDTH,
            border_handle_h_style=vb_wg.BORDER_STYLE,
            border_handle_h_rgb=vb_wg.BORDER_RGB,
            # Bordures slider v
            border_handle_v=vb_wg.BORDER_WIDTH,
            border_handle_v_style=vb_wg.BORDER_STYLE,
            border_handle_v_rgb=vb_wg.BORDER_RGB,

            # Rayons
            radius=vb_wg.RADIUS,
            radius_groove_h=vb_wg.RADIUS,
            radius_groove_v=vb_wg.RADIUS,
            radius_handle_h=vb_wg.RADIUS,
            radius_handle_v=vb_wg.RADIUS,
    ):

        style = f"""
                /* SLIDER  */
                QSlider {{
                background-color: rgba{bg};
                }}

                /* BARRE_H */
                QSlider::groove:horizontal {{
                background-color: qlineargradient(spread:pad, x1:{gradient[0]}, y1:{gradient[1]}, x2:{gradient[2]}, y2:{gradient[3]}, stop:0 rgba{bg_groove}, stop:1 rgba{bg_groove_2});
                height: {height_groove}px;
                border-top-right-radius: {radius_groove_h[0]}px;
                border-top-left-radius: {radius_groove_h[1]}px;
                border-bottom-right-radius: {radius_groove_h[2]}px;
                border-bottom-left-radius: {radius_groove_h[3]}px;
                }}
                QSlider::groove:horizontal:hover {{
                background-color: qlineargradient(spread:pad, x1:{gradient[0]}, y1:{gradient[1]}, x2:{gradient[2]}, y2:{gradient[3]}, stop:0 rgba{bg_groove_hover}, stop:1 rgba{bg_groove_hover_2});
                }}
                QSlider::groove:horizontal:pressed {{
                background-color: qlineargradient(spread:pad, x1:{gradient[0]}, y1:{gradient[1]}, x2:{gradient[2]}, y2:{gradient[3]}, stop:0 rgba{bg_groove_pressed}, stop:1 rgba{bg_groove_pressed_2});
                }}

                /* CURSEUR_H */
                QSlider::handle:horizontal {{
                background-color: rgba{bg_handle};
                width: {width_handle_h}px;
                height: {height_handle_h}px;
                border-top-right-radius: {radius_handle_h[0]}px;
                border-top-left-radius: {radius_handle_h[1]}px;
                border-bottom-right-radius: {radius_handle_h[2]}px;
                border-bottom-left-radius: {radius_handle_h[3]}px;
                margin-top: {margin_handle_h[0]}px;
                margin-bottom: {margin_handle_h[1]}px;
                margin-right: {margin_handle_h[2]}px;
                margin-left: {margin_handle_h[3]}px;
                border-top: {border_handle_h[0]}px {border_handle_h_style} rgba{border_handle_h_rgb};
                border-bottom: {border_handle_h[1]}px {border_handle_h_style} rgba{border_handle_h_rgb};
                border-right: {border_handle_h[2]}px {border_handle_h_style} rgba{border_handle_h_rgb};
                border-left: {border_handle_h[3]}px {border_handle_h_style} rgba{border_handle_h_rgb};
                }}
                QSlider::handle:horizontal:hover {{
                background-color: rgba{bg_handle_hover};
                }}
                QSlider::handle:horizontal:pressed {{
                background-color: rgba{bg_handle_pressed};
                }}

                /* BARRE_V */
                QSlider::groove:vertical {{
                background-color: qlineargradient(spread:pad, x1:{gradient[0]}, y1:{gradient[1]}, x2:{gradient[2]}, y2:{gradient[3]}, stop:0 rgba{bg_groove}, stop:1 rgba{bg_groove_2});
                width: {width_groove}px;
                border-top-right-radius: {radius_groove_v[0]}px;
                border-top-left-radius: {radius_groove_v[1]}px;
                border-bottom-right-radius: {radius_groove_v[2]}px;
                border-bottom-left-radius: {radius_groove_v[3]}px;
                }}
                QSlider::groove:vertical:hover {{
                background-color: qlineargradient(spread:pad, x1:{gradient[0]}, y1:{gradient[1]}, x2:{gradient[2]}, y2:{gradient[3]}, stop:0 rgba{bg_groove_hover}, stop:1 rgba{bg_groove_hover_2});
                }}
                QSlider::groove:vertical:pressed {{
                background-color: qlineargradient(spread:pad, x1:{gradient[0]}, y1:{gradient[1]}, x2:{gradient[2]}, y2:{gradient[3]}, stop:0 rgba{bg_groove_pressed}, stop:1 rgba{bg_groove_pressed_2});
                }}

                /* CURSEUR_V */
                QSlider::handle:vertical {{
                background-color: rgba{bg_handle};
                width: {width_handle_v}px;
                height: {height_handle_v}px;
                border-top-right-radius: {radius_handle_v[0]}px;
                border-top-left-radius: {radius_handle_v[1]}px;
                border-bottom-right-radius: {radius_handle_v[2]}px;
                border-bottom-left-radius: {radius_handle_v[3]}px;
                margin-top: {margin_handle_v[0]}px;
                margin-bottom: {margin_handle_v[1]}px;
                margin-right: {margin_handle_v[2]}px;
                margin-left: {margin_handle_v[3]}px;
                border-top: {border_handle_v[0]}px {border_handle_v_style} rgba{border_handle_v_rgb};
                border-bottom: {border_handle_v[1]}px {border_handle_v_style} rgba{border_handle_v_rgb};
                border-right: {border_handle_v[2]}px {border_handle_v_style} rgba{border_handle_v_rgb};
                border-left: {border_handle_v[3]}px {border_handle_v_style} rgba{border_handle_v_rgb};
                }}
                QSlider::handle:vertical:hover {{
                background-color: rgba{bg_handle_hover};
                }}
                QSlider::handle:vertical:pressed {{
                background-color: rgba{bg_handle_pressed};
                }}

                /* BORDURES */
                .QSlider {{
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}
                .QSlider:hover {{
                border-top: {border_hover[0]}px {border_hover_style} rgba{border_hover_rgb};
                border-bottom: {border_hover[1]}px {border_hover_style} rgba{border_hover_rgb};
                border-right: {border_hover[2]}px {border_hover_style} rgba{border_hover_rgb};
                border-left: {border_hover[3]}px {border_hover_style} rgba{border_hover_rgb};
                }}

                /* RAYONS */
                .QSlider {{
                border-top-right-radius: {radius[0]}px;
                border-top-left-radius: {radius[1]}px;
                border-bottom-right-radius: {radius[2]}px;
                border-bottom-left-radius: {radius[3]}px;
                }}"""
        for wg in wgs:
            # Dimensions
            Functions().SET_DIM(wg, width=width, height=height)

            # Paramètres
            wg.setMinimum(value_min)
            wg.setMaximum(value_max)
            wg.setSingleStep(value_step)
            wg.setPageStep(page_step)
            wg.setTickPosition(tick_position)

            # Curseur
            wg.setCursor(Functions().SET_CURSOR(cursor))

            # Style
            wg.setStyleSheet(style)
