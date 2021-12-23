import os
import time

import psutil

from src.build import functions
from src.config import config


if __name__ == "__main__":
    for proc in psutil.process_iter():
        pi = proc.as_dict(attrs=['pid', 'name'])
        if pi["name"] == config.nom + ".exe":
            quit()

    if config.auto_reload:
        os.startfile(os.path.abspath("src/scripts/convert_ui.bat"))
        time.sleep(0.4)

        functions.GEN_SVG()

    from src.main import app
