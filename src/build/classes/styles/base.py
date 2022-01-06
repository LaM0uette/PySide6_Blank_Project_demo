class Base:
    def __init__(self, *args, wg_type, **kwargs):

        self.wgs = args
        self.wg_type = wg_type
        self.args = kwargs

        for wg in self.wgs:
            print(wg, self.wg_type, self.args)
