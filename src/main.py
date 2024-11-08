import cv2
import os

from define import Define
from image_processing import ImageProcessor
from serial_communication import SerialCommunicator

def check_image_file_exist():
    if not os.path.exists(os.path.dirname(Define.IMAGE_FOLDER_DIR)):
        os.makedirs(Define.IMAGE_FOLDER_DIR)

def init():
    check_image_file_exist()
    SerialCommunicator().connect()
    
def main():
    webcam = cv2.VideoCapture(0)
    cv2.namedWindow("Webcam", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Webcam", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    if not webcam.isOpened():
        print("Error: Webcam Open Failed")
        exit()

    while True:
        ret, frame = webcam.read()
        key = cv2.waitKey(1)

        if not ret:
            print("Error: Could not read frame")
            exit()

        frame = cv2.flip(frame, 1)

        cv2.imshow('Webcam', frame)
        
        key = cv2.waitKey(1)

        if key == ord('q'): # Quit
            break
        elif key == ord('w'): # Capture, Image process, Print
            ImageProcessor().capture_image(ret, frame)
            ImageProcessor().process_image()
            ImageProcessor().show_image_to_print()
            
    webcam.release()
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    init()
    main()
