import psutil

from src.config import *


if __name__ == "__main__":
    for proc in psutil.process_iter():
        pi = proc.as_dict(attrs=["pid", "name"])
        if pi["name"] == f"{config.nom}.exe":
            quit()


    from src.main import app
