import os
import time

import psutil


if __name__ == "__main__":
    for proc in psutil.process_iter():
        pi = proc.as_dict(attrs=['pid', 'name'])
        if pi["name"] == config.nom + ".exe":
            quit()

    os.startfile(os.path.abspath("src/scripts/convert_ui.bat"))
    time.sleep(0.4)

    from src.main import app
