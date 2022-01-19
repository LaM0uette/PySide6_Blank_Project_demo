import os
import time

import psutil

from src.config import *


if __name__ == "__main__":
    for proc in psutil.process_iter():
        pi = proc.as_dict(attrs=["pid", "name"])
        if pi["name"] == f"{config.nom}.exe":
            quit()

    if config.auto_reload:
        os.startfile(os.path.abspath(f"{vrb.DO_SCRIPT}convert_ui.bat"))
        time.sleep(1)

        from src.build import *

        Fct().GEN_SVG()
        time.sleep(0.5)

    from src.main import app
