from ....build import *


class wg:
    def __init__(self,
                 *args,
                 colors_type,
                 colors,
                 dim,
                 font,
                 bd,
                 rd,
                 edit,
                 cur
    ):
        self.wgs = args

        self.colors_type = colors_type
        self.colors = colors
        self.dim = dim
        self.font = font
        self.bd = bd
        self.rd = rd
        self.edit = edit
        self.cur = cur


        style_gen = f"""
        QComboBox {{
        color: rgb{self.colors.get("c3")};
        selection-background-color: rgb{self.colors.get("c3")};
        selection-color: rgb{self.colors.get("c1")};
        padding: 1px 0px 1px 3px;
        }}

        QComboBox::drop-down {{
        width: {self.dim.get("h")}px;
        border: none;
        }}

        QComboBox::down-arrow {{
        image: url({P_img().fleche_bottom() + "bn1" + ".svg"});
        width: {self.dim.get("h") * P_style().x_ico()}px;
        height: {self.dim.get("h") * P_style().x_ico()}px;
        }}

        QComboBox::down-arrow:hover {{
        image: url({P_img().fleche_bottom() + "bn2" + ".svg"});
        width: {self.dim.get("h") * P_style().x_ico()}px;
        height: {self.dim.get("h") * P_style().x_ico()}px;
        }}

        QComboBox QAbstractItemView::item {{
        background-color: rgb{self.colors.get("c1")};
        color: rgb{self.colors.get("c3")};
        border: none;
        }}

        QComboBox QAbstractItemView::item:hover {{
        background-color: rgb{self.colors.get("c3")};
        color: rgb{self.colors.get("c1")};
        border: none;
        }}"""
        style_type = {
            "th":
                f"""
                QComboBox {{
                background-color: rgb{self.colors.get("c2")};
                }}""",

            "tr":
                """
                QComboBox {
                background-color: rgba(0, 0, 0, 0);
                }"""
        }

        style = style_gen + style_type.get(self.colors_type)

        for wg in self.wgs:
            wg.setStyleSheet(style)

            Fct(wg=wg, w=self.dim.get("w"), h=self.dim.get("h")).DIM()
            wg.setFont(Fct(font_size=self.font).FONT())

            wg.setEditable(self.edit)

            wg.setCursor(Fct(cur=self.cur).CUR())
            wg.view().setCursor(Fct(cur=P_cur().souris_main()).CUR())
            if self.edit:
                wg.lineEdit().setCursor(Fct(cur=P_cur().IBeam()).CUR())
                wg.lineEdit().setFont(Fct(font_size=self.font).FONT())
