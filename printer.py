import os
import subprocess
from define import Define

class Printer:
    def __init__(self):
        pass

    def printImage():
        os.system(f"lp {Define.PRINTER_IMG_PATH}")