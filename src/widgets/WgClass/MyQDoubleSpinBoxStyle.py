from .MyQDoubleSpinBox import MyQDoubleSpinBox
from src.lib.globals import v_wg
from src.lib.palettes import *


class Style(MyQDoubleSpinBox):
    def __init__(
            self,
            widget,
            size_policy=v_wg.SIZE_POLICY,
            dim=v_wg.DIM_WG,
            font=v_wg.FONT,
            cursor=v_wg.CUR_ACTION,
            focus_policy=v_wg.FOCUS_POLICY,
            layout_direction=v_wg.LAYOUT_DIRECTION,

            wrapping=False,
            frame=False,
            align=DcAlign.Base,
            read_only=False,
            button_symbols=PaButtonSymbols.PLUS_MINUS,
            accelerated=True,

            suffix="",
            prefix="",
            decimals=2,
            value=v_wg.VALUE,
    ):
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction,wrapping,frame,align,read_only,button_symbols,accelerated,suffix,prefix,decimals,value)
