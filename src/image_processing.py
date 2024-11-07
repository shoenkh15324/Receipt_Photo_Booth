import cv2
import os

from define import Define
from printer import Printer
from button import Button

class ImageProcessor:
    def __init__(self):
        pass

    def capture_image(self, ret, frame):
        if ret:
            self.save_image(frame, "Original")
        else:
            print("[Error] Image Capture Fail")
            
    def resize_and_grayscale(self, img):
        resized_img = cv2.resize(img, Define.IMAGE_SCALING_SIZE)
        grayscaled_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
        self.save_image(grayscaled_img, "resized and grayscaled")
        return grayscaled_img
    
    def normalizing(self, img):
        image = cv2.normalize(img, 
                              None, 
                              alpha = Define.IMAGE_NORMALIZE_ALPHA,
                              beta = Define.IMAGE_NORMALIZE_BETA, 
                              norm_type = cv2.NORM_MINMAX)
        self.save_image(image, "normalized")
        return image
    
    def adjust_contrast_and_brightness(self, img):
        image = cv2.convertScaleAbs(img, 
                                    alpha = Define.IMAGE_CONTRAST_ALPHA,
                                    beta = Define.IMAGE_BRIGHTNESS_BETA)
        self.save_image(image, "adjusted")
        return image
    
    # Binarization (black and white) processing
    def adaptive_binarization(self, img):
        image = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        self.save_image(image, "adaptive binarization")
        return image
    
    def binarization(self, img):
        _, image = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
        self.save_image(image, "binarization")
        return image
    
    def gaussian_blur(self, img):
        image = cv2.GaussianBlur(img, (5, 5), 0)
        return image
    
    def save_image(self, img, img_name):
        if not os.path.exists(os.path.dirname(Define.IMAGE_DIR)):
            os.makedirs(Define.IMAGE_DIR)
            
        # 확장자 추가 (예: .jpg)
        if not img_name.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            img_name += '.jpg'  # 기본값으로 .jpg 사용
        
        image_path = os.path.join(Define.IMAGE_DIR, img_name)
        
        res = cv2.imwrite(image_path, img)
        if res:
            print(f"Save {img_name} image.")
        else:
            print(f"[Error] Failed to save {img_name} image.")

    # Save 1-bit black and white image in PNG format
    def save_image_for_printing(self, img):
        if not os.path.exists(os.path.dirname(Define.IMAGE_DIR)):
            os.makedirs(Define.IMAGE_DIR)
            
        res = cv2.imwrite(Define.PRINTER_IMG_PATH, img)
        if res:
            print(f"Save image for printing.")
        else:
            print(f"[Error] Fail to save image for printing.")
        
    def log_image_size(self, img):
        # Get size of converted image
        height, width, _ = img.shape

        # Calculate the dimensions in inches
        width_inch = width / Define.PRINTER_DPI
        height_inch = height / Define.PRINTER_DPI

        # Convert to millimeters
        width_mm = width_inch * 25.4
        height_mm = height_inch * 25.4

        print(f"Original Size: {width}x{height} pixels")
        print(f"Converted Size: {width_mm:.2f}x{height_mm:.2f} mm at {Define.PRINTER_DPI} DPI")
        
    def show_image_to_print(self):
        if not os.path.exists(Define.PRINTER_IMG_PATH):
            return
        
        img = cv2.imread(Define.PRINTER_IMG_PATH)
        
        if img is None:
            print("[Error] Unable to load image file. Please check the file format.")
        
        while(True):
            cv2.imshow("Choose to print", img)
            keybaord = cv2.waitKey(1)
            button = Button.debounce_button()
            
            if keybaord == ord('q'):
                break
            
            if button == 'W':
                Printer.print_image()
            elif button == 'R':
                break
        
        cv2.destroyWindow("Choose to print")
   
    def process_image(self):
        img = cv2.imread(Define.CAPTURED_IMG_PATH)

        if img is None:
            print("[Error] Unable to load image.")
            return
        
        img = self.resize_and_grayscale(img)

        self.save_image_for_printing(img)