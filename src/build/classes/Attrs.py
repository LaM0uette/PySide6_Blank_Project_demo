from . import p_base


class Attrs:
    def __init__(self,
                 bd=p_base.BD,
                 rd=p_base.RD
    ):

        self.bd = bd
        self.rd = rd

    def GET_BD(self):
        val = lambda v: self.bd.get("th") + (255,) if int(v) == 1 else p_base.BD_RGBA

        return {
            "o1": val(self.bd.get("mat")[:1]),
            "o2": val(self.bd.get("mat")[1:2]),
            "o3": val(self.bd.get("mat")[2:3]),
            "o4": val(self.bd.get("mat")[3:4]),
        }
    def GET_RD(self):
        val = lambda v: self.rd.get("px") if int(v) == 1 else p_base.RD_PX

        return {
            "r1": val(self.rd.get("mat")[:1]),
            "r2": val(self.rd.get("mat")[1:2]),
            "r3": val(self.rd.get("mat")[2:3]),
            "r4": val(self.rd.get("mat")[3:4]),
        }
