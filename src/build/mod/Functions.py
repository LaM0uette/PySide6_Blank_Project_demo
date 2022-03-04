

class Functions:

    def SET_DIM(self, *args, width=None, height=None):
        for wg in args:
            if width is not None: wg.setFixedWidth(width)
            if height is not None: wg.setFixedHeight(height)
