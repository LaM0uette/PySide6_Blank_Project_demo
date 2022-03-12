class A:
    def __init__(
            self,
            width=1,
            height=None
    ):
        self.width = width
        self.height = height


class B(A):
    def __init__(self):
        super(B, self).__init__()

        print(self.width)



B()
