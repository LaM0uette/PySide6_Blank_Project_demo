from .styles import *


class rtn(Base):
    def __init__(self, *args, val=None):
        super().__init__(*args, wg_type="cb", val=val)


class test(rtn):
    def __init__(self, *args):
        super().__init__(*args, val="t")





"""
colors_type="th",
colors=P_rgb().p_th1(),
dim=P_dim().aw().h9(),
font=P_font().h4(),
rd=P_rd().%
bd=P_bd().bottom().th3(),
edit=True,
cur="souris_main")
"""