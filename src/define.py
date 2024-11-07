import os

class Define:
    CURR_DIR = os.path.dirname(os.path.abspath(__file__))
    ROOT_DIR = os.path.join(CURR_DIR, "..")
    IMAGE_FOLDER_DIR = os.path.join(ROOT_DIR, "image")
    CAPTURED_IMG_PATH = os.path.join(IMAGE_FOLDER_DIR, "Original.jpg")
    PRINTER_IMG_PATH = os.path.join(IMAGE_FOLDER_DIR, "Printer_image.png")

    IMAGE_SCALING_SIZE = (500, 375)
    IMAGE_CONTRAST_ALPHA = 0.1 # Contrast (1.0 is no change)
    IMAGE_BRIGHTNESS_BETA = 30 # Brightness (0 is no change)
    IMAGE_NORMALIZE_ALPHA = 0
    IMAGE_NORMALIZE_BETA = 255

    PRINTER_DPI = 180
    
    SERIAL_COMM_BAUDRATE = 9600
    SERIAL_COMM_TIMEOUT = 1.5
    
    BUTTON_DEBOUNCE_TIME = 0.2 # sec
