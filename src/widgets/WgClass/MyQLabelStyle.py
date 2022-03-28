from .MyQLabel import MyQLabel
from src.lib.globals import v_wg
from ...lib.palettes import *


class Style(MyQLabel):
    def __init__(
            self,
            widget,
            size_policy=v_wg.SIZE_POLICY,
            dim=v_wg.DIM_WG,
            font=v_wg.FONT,
            cursor=v_wg.CUR_ACTION,
            focus_policy=v_wg.FOCUS_POLICY,
            layout_direction=v_wg.LAYOUT_DIRECTION,

            frame=v_wg.FRAME,

            text_format=PaTextFormat.PLAIN,
            pixmap=None,
            pixmap_rgb="",
            scaled_contents=True,
            align=DcAlign.Base,
            word_wrap=False,
            indent=0,
            open_external_link=False,
    ):
        super().__init__(widget, size_policy, dim, font, cursor, focus_policy, layout_direction, frame,text_format,pixmap,pixmap_rgb,scaled_contents,align,word_wrap,indent,open_external_link)
