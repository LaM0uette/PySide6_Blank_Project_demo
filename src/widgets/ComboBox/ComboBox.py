from src.lib.palettes import *
from src.widgets.ComboBox.Build import Build


##################
##     BASE     ##
##################
class Base:
    def __init__(self, *wgs):
        self.wgs = wgs

    def th(self):
        Build(
            *self.wgs,
        )
    def tr(self):
        Build(
            *self.wgs,
            edit=True,
            curseur=Cur().souris_main(),

            bg=Rgb().tr(),
            bg_hover=Rgb().tr(),
            fg=Rgb().th3(),
            bg_selection=Rgb().th3(),
            fg_selection=Rgb().th1(),
        )
