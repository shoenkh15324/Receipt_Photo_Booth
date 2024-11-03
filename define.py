import os

class Define:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # Directory path of the current file
    IMAGE_DIR = os.path.join(BASE_DIR, "image")
    CAPTURED_IMG_PATH = os.path.join(IMAGE_DIR, "Original.jpg")
    PRINTER_IMG_PATH = os.path.join(IMAGE_DIR, "Printer_image.png")

    IMAGE_SCALING_SIZE = (500, 375)
    IMAGE_CONTRAST_ALPHA = 2.0 # Contrast (1.0 is no change)
    IMAGE_BRIGHTNESS_BETA = 50 # Brightness (0 is no change)

    PRINTER_DPI = 180