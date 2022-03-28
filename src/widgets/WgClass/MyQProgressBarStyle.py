from .MyQProgressBar import MyQProgressBar
from src.lib.globals import v_wg
from src.lib.palettes import *


class Style(MyQProgressBar):
    def __init__(
            self,
            widget,
            size_policy=v_wg.SIZE_POLICY,
            dim=v_wg.DIM_WG,
            font=v_wg.FONT,
            cursor=v_wg.CUR_ACTION,
            focus_policy=v_wg.FOCUS_POLICY,
            layout_direction=v_wg.LAYOUT_DIRECTION,

            value=DcValue.Base,
            align=DcAlign.Base,
            text_visible=True,
            progress_format=PaProgressFormat.VALUE,
    ):
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction,value,align,text_visible,progress_format)
