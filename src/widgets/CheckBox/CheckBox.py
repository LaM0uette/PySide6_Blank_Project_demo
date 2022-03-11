from src.lib.palettes import *
from src.widgets import vb_wg
from src.widgets.CheckBox.Build import Build


##################
##     BASE     ##
##################
class Base:
    def __init__(self, *wgs, margin=(0, 0, 0, (vb_wg.HEIGHT-(vb_wg.HEIGHT*StyleBase().x_ico()))/2)):
        self.wgs = wgs
        self.margin = margin

    def th(self):
        Build(
            *self.wgs,

            img_margin=self.margin,
        )
    def tr(self, bg=Rgb().tr(), fg=Rgb().th3()):
        Build(
            *self.wgs,

            bg=bg,
            bg_hover=bg,
            bg_checked=bg,
            bg_checked_hover=bg,
            bg_indeterminate=bg,
            bg_indeterminate_hover=bg,
            fg=fg,
            fg_checked=fg,
            fg_indeterminate=fg,
            fg_indeterminate_hover=Rgb().th2(),

            img_indeterminate_rgb="th3",
            img_indeterminate_hover_rgb="th2",
            img_margin=self.margin,
        )


##################
##     DEMO     ##
##################
class Demo:
    def __init__(self, *wgs):
        self.wgs = wgs
        
    def _rtn(
            self,
            
            auto_exclusive=True,
            triple_state=True,
            
            bg=Rgb().th3(),
            bg_hover=Rgb().th3(),
            bg_checked=Rgb().th1(),
            bg_checked_hover=Rgb().th1(),
            bg_indeterminate=Rgb().th2(),
            bg_indeterminate_hover=Rgb().th2(),
            
            fg=Rgb().th1(),
            fg_hover=Rgb().bn1(),
            fg_checked=Rgb().th3(),
            fg_checked_hover=Rgb().bn1(),
            fg_indeterminate=Rgb().th3(),
            fg_indeterminate_hover=Rgb().th1(),

            img_indeterminate_rgb="th3",
            img_indeterminate_hover_rgb="th1"
    ):
        Build(
            *self.wgs,
            
            auto_exclusive=auto_exclusive,
            triple_state=triple_state,
            
            bg=bg,
            bg_hover=bg_hover,
            bg_checked=bg_checked,
            bg_checked_hover=bg_checked_hover,
            bg_indeterminate=bg_indeterminate,
            bg_indeterminate_hover=bg_indeterminate_hover,
            
            fg=fg,
            fg_hover=fg_hover,
            fg_checked=fg_checked,
            fg_checked_hover=fg_checked_hover,
            fg_indeterminate=fg_indeterminate,
            fg_indeterminate_hover=fg_indeterminate_hover,

            img_margin=(0, 0, 0, (vb_wg.HEIGHT-(vb_wg.HEIGHT*StyleBase().x_ico()))/2),

            img_indeterminate_rgb=img_indeterminate_rgb,
            img_indeterminate_hover_rgb=img_indeterminate_hover_rgb
        )
        
    def th(self):
        self._rtn()
    def tr(self):
        self._rtn(
            bg=Rgb().tr(),
            bg_hover=Rgb().tr(),
            bg_checked=Rgb().tr(),
            bg_checked_hover=Rgb().tr(),
            bg_indeterminate=Rgb().tr(),
            bg_indeterminate_hover=Rgb().tr(),

            fg=Rgb().th3(),
            fg_checked=Rgb().th3(),
            fg_indeterminate=Rgb().th3(),
            fg_indeterminate_hover=Rgb().th2(),

            img_indeterminate_rgb="th3",
            img_indeterminate_hover_rgb="th2"
        )
