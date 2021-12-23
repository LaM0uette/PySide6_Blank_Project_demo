import datetime
import os


### BASES __
bs_font = 15


### VARIABLES GLOBALES __________
guid = str(os.getenv("USERNAME"))
date_now = datetime.datetime.now()
date_now_format = datetime.datetime.now().strftime("%d_%m_%Y")


### FLIENS FICHIERS _____________
ini_cfg = "src/config/config.ini"


### LIENS DOSSIERS ______________
lien_json = "src/config/themes/"
