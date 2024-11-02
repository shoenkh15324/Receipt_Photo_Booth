import cv2
from define import Define
from printer import Printer

class ImageProcessing:
    def __init__(self):
        # Ensure the directory exists
        # os.makedirs(CAPTURED_IMG_PATH, exist_ok=True)
        pass

    def capture(self, ret, frame):
        if ret:
            cv2.imwrite(Define.CAPTURED_IMG_PATH, frame) # 640x480 pixels, jpeg
            print("Image Capture Success")
        else:
            print("Error: Image Capture Fail")

    def convertCapturedImageToPrinterImg(self):
    # Load the image
        img = cv2.imread(Define.CAPTURED_IMG_PATH)

        if img is None:
            print("Error: Unable to load image.")
            return
        
        # Scaling img size
        resized_img = cv2.resize(img, Define.IMAGE_SCALING_SIZE)

        # Grayscaling
        image_gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

        # Get the original dimensions
        height, width, _ = resized_img.shape

        # Image Normalize
        #image_nomalized = cv2.normalize(image_gray, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

        # Contrast
        #image_contrast = cv2.convertScaleAbs(image_gray, alpha = Define.IMAGE_CONTRAST_ALPHA)

        image_binary = cv2.adaptiveThreshold(image_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

        # Calculate the dimensions in inches
        width_inch = width / Define.PRINTER_DPI
        height_inch = height / Define.PRINTER_DPI

        # Convert to millimeters
        width_mm = width_inch * 25.4
        height_mm = height_inch * 25.4

        print(f"Original Size: {width}x{height} pixels")
        print(f"Converted Size: {width_mm:.2f}x{height_mm:.2f} mm at {Define.PRINTER_DPI} DPI")

        cv2.imwrite(Define.PRINTER_IMG_PATH, image_binary)

        # Print image
        Printer.printImage()
    
        # If you want to set DPI in the output image, you'll need a library like PIL (Pillow)
        # from PIL import Image
        # img_pil = Image.open(PRINTER_IMG_PATH)
        # img_pil.save(PRINTER_IMG_PATH, dpi=(PRINTER_DPI, PRINTER_DPI))


