import cv2
import os
import time

from define import Define
from printer import Printer
from keyhandle import KeyHandler

class ImageProcessor:
    def __init__(self):
        pass

    def capture_image(self, ret, frame):
        if ret:
            self.save_image(frame, "Original")
        else:
            print("[Error] Image Capture Fail")
            
    def resize_and_grayscale(self, img):
        resized_img = cv2.resize(img, (Define.IMAGE_WIDTH, Define.IMAGE_HEIGHT))
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
        self.save_image(image, "gaussian_blur")
        return image
    
    def rotate_image(self, img):
        image = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        self.save_image(image, "rotated")
        return image
    
    def save_image(self, img, img_name):
        if not os.path.exists(os.path.dirname(Define.IMAGE_FOLDER_DIR)):
            os.makedirs(Define.IMAGE_FOLDER_DIR)
            
        if not img_name.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            img_name += '.jpg'
        
        image_path = os.path.join(Define.IMAGE_FOLDER_DIR, img_name)
        
        res = cv2.imwrite(image_path, img)
        if res:
            print(f"Save {img_name} image.")
        else:
            print(f"[Error] Failed to save {img_name} image.")

    def save_image_for_printing(self, img):
        if not os.path.exists(os.path.dirname(Define.IMAGE_FOLDER_DIR)):
            os.makedirs(Define.IMAGE_FOLDER_DIR)
            
        res = cv2.imwrite(Define.PRINTER_IMG_PATH, img)
        if res:
            print(f"Save image for printing.")
        else:
            print(f"[Error] Fail to save image for printing.")
        
    def show_image_to_print(self):
        if not os.path.exists(Define.PRINTER_IMG_PATH):
            return
        
        img = cv2.imread(Define.PRINTER_IMG_PATH)
        
        if img is None:
            print("[Error] Unable to load image file. Please check the file format.")
        
        while(True):
            cv2.imshow("Choose to print", img)
            # cv2.namedWindow("Webcam", cv2.WND_PROP_FULLSCREEN)
            # cv2.setWindowProperty("Webcam", 
            #                       cv2.WND_PROP_FULLSCREEN, 
            #                       cv2.WINDOW_FULLSCREEN)
            
            key = cv2.waitKey(1)
            
            if key == ord('q'):
                break
            elif key == ord('W'):
                Printer().print_image()
                break
            elif key == ord('R'):
                break
        
        cv2.destroyWindow("Choose to print")
        
    def concat_images(self, image1, image2, direction):
        if image1 is None or image2 is None:
            raise ValueError("No image file provided")
        
        # Match image type
        if image1.dtype != image2.dtype:
            image2 = image2.astype(image1.dtype)
            
        # Match image dimensions (make the number of color channels the same)
        if image1.ndim != image2.ndim:
            if image1.ndim == 2:  # 흑백 이미지
                image1 = cv2.cvtColor(image1, cv2.COLOR_GRAY2BGR)
            elif image2.ndim == 2:
                image2 = cv2.cvtColor(image2, cv2.COLOR_GRAY2BGR)

        if direction == 'h':
            if image1.shape[0] != image2.shape[0]:
                image2 = cv2.resize(image2, (image2.shape[1], image1.shape[0]))
            return cv2.hconcat([image1, image2])

        elif direction == 'v':
            if image1.shape[1] != image2.shape[1]:
                image2 = cv2.resize(image2, (image1.shape[1], image2.shape[0]))
            return cv2.vconcat([image1, image2])

        else:
            raise ValueError("The 'direction' argument must be 'h' or 'v'.")
   
    def process_image(self):
        img = cv2.imread(Define.CAPTURED_IMG_PATH)
        logo = cv2.imread(Define.LOGO_IMG_PATH)

        if img is None:
            print("[Error] Unable to load image.")
            return
        
        img = self.rotate_image(img)
        
        img = self.resize_and_grayscale(img)
        
        img = self.concat_images(logo, img, 'v')

        self.save_image_for_printing(img)
        
        