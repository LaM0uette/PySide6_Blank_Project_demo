from .MyQLineEdit import MyQLineEdit
from src.lib.globals import v_wg
from src.lib.palettes import *


class Style(MyQLineEdit):
    def __init__(
            self,
            widget,
            size_policy=v_wg.SIZE_POLICY,
            dim=v_wg.DIM_WG,
            font=v_wg.FONT,
            cursor=v_wg.CUR_ACTION,
            focus_policy=PaFocusPolicy.STRONG,
            layout_direction=v_wg.LAYOUT_DIRECTION,

            input_mask=PaInputMask.NO,
            max_length=32767,
            frame=False,
            echo_mode=PaEchoMode.NORMAL,
            align=DcAlign.Base,
            drag_enabled=False,
            read_only=False,
            clear_button=False,
    ):
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction,input_mask,max_length,frame,echo_mode,align,drag_enabled,read_only,clear_button)
