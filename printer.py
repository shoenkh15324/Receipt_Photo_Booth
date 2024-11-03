import os
import subprocess
import platform

from define import Define

class Printer:
    def __init__(self):
        pass

    def print_image(self):
        current_os = platform.system()
        
        if current_os == "Linux":
            os.system(f"lp {Define.PRINTER_IMG_PATH}")
        elif current_os == "Windows":
            subprocess.run(["print", Define.PRINTER_IMG_PATH], shell=True)
        else:
            raise NotImplementedError("[Error] Printing is not supported on this operating system.")
