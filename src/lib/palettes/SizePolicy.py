from PySide6.QtWidgets import QSizePolicy


class SizePolicy:

    def fixed(self): return QSizePolicy.Fixed
    def minimum(self): return QSizePolicy.Minimum
    def maximum(self): return QSizePolicy.Maximum
    def prefered(self): return QSizePolicy.Preferred
    def minimum_expanding(self): return QSizePolicy.MinimumExpanding
    def expanding(self): return QSizePolicy.Expanding
    def ignored(self): return QSizePolicy.Ignored
