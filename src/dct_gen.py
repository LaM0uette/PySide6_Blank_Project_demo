### DOSSIERS SVG
lien_svg = {
    "divers": "src/assets/img/divers/",
    "main": "src/assets/img/main/",
    "ui": "src/assets/img/ui/"
}

### SIZES __
dct_size = {
    "police": {
        "h1": 30,
        "h2": 22,
        "h3": 16,
        "h4": 12
    },
    "wg": {
        # Bases ___
        "h-4": 500,
        "h-3": 400,
        "h-2": 300,
        "h-1": 200,
        "h0": 150,
        "h1": 100,
        "h2": 75,
        "h3": 50,
        "h4": 25,

        # Modifs de bases
        "bd": 2,
        "x_ico": 0.65,
        "X_ico": 0.80
    }
}
dct_dim = {
    # Menu top _____________________________
    "h_menu_top": dct_size.get("wg").get("h4"),

    # Demo ___________________________________
    "h_demo": dct_size.get("wg").get("h4")*1.4,
}


### IMAGES __________________________________
l_img_divers = lien_svg.get("divers") + "tm/"
l_img_main = lien_svg.get("main") + "tm/"
l_img_ui = lien_svg.get("ui") + "tm/"

dct_img = {
    # Divers _________________________________
    "calendrier": l_img_divers + "calendrier",

    # Main ___________________________
    "main": l_img_main + "main" + "_",

    # ui _______________________________
    "option": l_img_ui + "option" + "_",
    "reduire": l_img_ui + "reduire" + "_",
    "agrandir": l_img_ui + "agrandir" + "_",
    "quitter": l_img_ui + "quitter" + "_",
        #check
    "check": l_img_ui + "check" + "_",
    "valider": l_img_ui + "valider" + "_",
        #notif
    "alerte": l_img_ui + "alerte" + "_",
    "info": l_img_ui + "info" + "_",
        #fleches
    "flecheBottom": l_img_ui + "flecheBottom" + "_",
    "flecheDroite": l_img_ui + "flecheDroite" + "_",
    "flecheGauche": l_img_ui + "flecheGauche" + "_",
    "flecheTop": l_img_ui + "flecheTop" + "_"
}
