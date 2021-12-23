"""
_TITRE: Définition des widgets

_DESC: Chaque widget dois être renseigné ici. on peut définir tous ses champs à la main ou lui assigner une classe.

A0: "lb": {"label": classe_du_label}}
    _ex: "lb": {"label": lb.get("h1_tr1")}}
"""

from . import dct_classe_wg

def DCT_SET(val):
    return dct_classe_wg.dct_classe.get(val)
cb = DCT_SET(val="cb")
de = DCT_SET(val="de")
fr = DCT_SET(val="fr")
lb = DCT_SET(val="lb")
lw = DCT_SET(val="lw")
pb = DCT_SET(val="pb")
ckb = DCT_SET(val="ckb")
rb = DCT_SET(val="rb")
pg = DCT_SET(val="pg")
sca = DCT_SET(val="sca")
sb = DCT_SET(val="sb")
tb = DCT_SET(val="tb")
tw = DCT_SET(val="tw")
txt = DCT_SET(val="txt")


dct_wg = {
    # Widgets
    "txt": {
        # Option _
        "le_nom_theme": txt.get("option_line"),
    },
    "cb": {
        # Options ____________________
        "cb_choix_theme": cb.get("option"),
    },
    "de": {},
    "fr": {
        # Menu Top _________________________
        "fr_menu_top": fr.get("aw_menu_top"),

        # Options ____________________________
        "fr_opt_theme": fr.get("tb"),
        "fr_opt_affichages": fr.get("tb")
    },
    "lb": {
        # Menu Top _______________________
        "lb_mt_version": lb.get("version"),
        "lb_mt_nom": lb.get("nom_app"),

        # Option __________________________
        "lb_choix_theme": lb.get("option"),
        "lb_nom_theme": lb.get("option"),
        "lb_th1": lb.get("option"),
        "lb_th2": lb.get("option"),
        "lb_th3": lb.get("option"),
        "lb_th4": lb.get("option"),
        "lb_bn1": lb.get("option"),
        "lb_bn2": lb.get("option"),
        "lb_opacity": lb.get("option"),
        "lb_opacity_titre": lb.get("option_titre"),
        "lb_auto_reload": lb.get("option"),
        "lb_parametre_titre": lb.get("option_titre"),
        "lb_auto_close": lb.get("option"),
    },
    "lw": {},
    "pb": {
        # Menu Top ________________________
        "pb_mt_option": pb.get("mt_option"),
        "pb_mt_reduire": pb.get("mt_reduire"),
        "pb_mt_agrandir": pb.get("mt_agrandir"),
        "pb_mt_quitter": pb.get("mt_quitter"),

        # Option ___________________________
        "pb_creer_theme": pb.get("option_txt"),
        "pb_modif_theme": pb.get("option_txt"),
        "pb_supp_theme": pb.get("annuler"),
        "pb_appliquer": pb.get("appliquer"),
        "pb_ok": pb.get("valider"),
        "pb_th1": pb.get("uni"),
        "pb_th2": pb.get("uni"),
        "pb_th3": pb.get("uni"),
        "pb_th4": pb.get("uni"),
        "pb_bn1": pb.get("uni"),
        "pb_bn2": pb.get("uni"),
    },
    "ckb": {
        # Option
        "ckb_auto_reload": ckb.get("option"),
        "ckb_auto_close": ckb.get("option"),
    },
    "rb": {},
    "pg": {},
    "sca": {},
    "sb": {
        # Option
        "sp_opacity": sb.get("option"),
    },
    "tw": {},

    # Boites
    "tb": {
        "tb_option": tb.get("option")
    }
}
