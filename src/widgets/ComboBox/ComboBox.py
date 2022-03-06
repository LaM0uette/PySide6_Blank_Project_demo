from src.build.mods import Functions
from src.widgets import vb_wg


##################
##     BASE     ##
##################
class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            curseur=Cur().main(),
    )
class Base_tr(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            edit=True,
            bg=Rgb().tr(),
            bg_hover=Rgb().tr(),
            fg=Rgb().th3(),
            bg_selection=Rgb().th3(),
            fg_selection=Rgb().th1(),
    )
