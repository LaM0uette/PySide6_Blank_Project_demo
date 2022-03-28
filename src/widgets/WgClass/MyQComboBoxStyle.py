from .MyQComboBox import MyQComboBox
from src.lib.globals import v_wg
from src.lib.palettes import *


class Style(MyQComboBox):
    def __init__(
            self,
            widget,
            size_policy=v_wg.SIZE_POLICY,
            dim=v_wg.DIM_WG,
            font=v_wg.FONT,
            cursor=v_wg.CUR_ACTION,
            focus_policy=v_wg.FOCUS_POLICY,
            layout_direction=v_wg.LAYOUT_DIRECTION,

            editable=True,
            max_visible_items=10,
            insert_policy=PaInsertPolicy.NO,
            set_frame=False,
    ):
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction,editable,max_visible_items,insert_policy,set_frame)
